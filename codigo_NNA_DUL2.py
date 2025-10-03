# -- coding: utf-8 --
import argparse
import hashlib
import json
import os
from typing import List, Dict, Any

import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# CONFIGURACIÓN - ADAPTADO A NNA
# =============================================================================

DROP_COLS = [
    "NUMERO DOCUMENTO",
    "1ER. NOMBRE", "2DO. NOMBRE", "1ER. APELLIDO", "2DO. APELLIDO",
    "Nombre y apellidos Completos",
    "DIRECCION DE LA VIVIENDA", "BARRIO", "NOMBRE DEL LUGAR",
    "COORDENADA X", "COORDENADA Y"
]

HASH_COLS = ["NUMERO DOCUMENTO"]

GROUPS = {
    "identificacion": [
        "TIPO IDENTIFICACION", "SEXO", "GENERO", "ESTADO CIVIL"
    ],
    "educacion": [
        "NIVEL EDUCATIVO", "ESTUDIA", "GRADO", "CURSO DE VIDA"
    ],
    "hogar": [
        "VINCULO CON EL JEFE DE HOGAR", "NUMERO DE MIEMBROS DEL HOGAR",
        "CATEGORIA DEL ESTRATO SOCIOECONOMICO"
    ],
    "territorio": [
        "BARRIO", "NOMBRE DEL LUGAR", "DIRECCION DE LA VIVIENDA",
        "COORDENADA X", "COORDENADA Y"
    ],
    "salud": [
        "EPS", "AFILIACION A ADRES", "CATEGORIA DE LA DISCAPACIDAD",
        "RECIBE ATENCION EN SALUD"
    ]
}

CROSSES = {
    "sexo_x_educacion": ["SEXO", "NIVEL EDUCATIVO"],
    "genero_x_estado_civil": ["GENERO", "ESTADO CIVIL"],
    "hogar_x_afiliacion": ["NUMERO DE MIEMBROS DEL HOGAR", "AFILIACION A ADRES"]
}

# =============================================================================
# UTILIDADES
# =============================================================================

def load_excel(path: str, sheet: int = 0) -> pd.DataFrame:
    """Carga un archivo Excel (.xlsx)."""
    return pd.read_excel(path, sheet_name=sheet)

def hash_value(value: Any) -> str:
    """Genera hash SHA-256 para anonimizar datos."""
    if pd.isna(value):
        return None
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza inicial: eliminar columnas sensibles y aplicar hash."""
    df = df.copy()

    # Eliminar columnas sensibles
    for col in DROP_COLS:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    # Encriptar columnas
    for col in HASH_COLS:
        if col in df.columns:
            df[col] = df[col].apply(hash_value)

    return df

# =============================================================================
# PERFILAMIENTO
# =============================================================================

def generate_dictionary(df: pd.DataFrame, outdir: str):
    """Generar diccionario de datos básico."""
    dictionary = []
    for col in df.columns:
        dictionary.append({
            "variable": col,
            "tipo": str(df[col].dtype),
            "valores_unicos": df[col].nunique(),
            "nulos": int(df[col].isna().sum())
        })

    out_path = os.path.join(outdir, "data_dictionary.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, indent=4, ensure_ascii=False)
    print(f"✅ Diccionario de datos guardado en {out_path}")

def profile_data(df: pd.DataFrame, outdir: str):
    """Perfilamiento: resumen general y estadísticas."""
    summary = {
        "filas": len(df),
        "columnas": len(df.columns),
        "columnas": list(df.columns),
        "nulos_totales": int(df.isna().sum().sum())
    }

    out_path = os.path.join(outdir, "profile_summary.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)
    print(f"✅ Perfilamiento guardado en {out_path}")

# =============================================================================
# GRÁFICOS
# =============================================================================

def plot_categorical(df: pd.DataFrame, col: str, outdir: str):
    """Genera gráfico de barras para variables categóricas."""
    if col not in df.columns:
        return
    plt.figure(figsize=(6, 4))
    df[col].value_counts(dropna=False).plot(kind="bar")
    plt.title(f"Distribución de {col}")
    plt.tight_layout()
    out_path = os.path.join(outdir, f"{col}_bar.png")
    plt.savefig(out_path)
    plt.close()
    print(f"📊 Gráfico guardado: {out_path}")

def plot_cross(df: pd.DataFrame, cols: List[str], outdir: str):
    """Cruces entre variables categóricas."""
    if not all(c in df.columns for c in cols):
        return
    ct = pd.crosstab(df[cols[0]], df[cols[1]])
    ct.plot(kind="bar", stacked=True, figsize=(6, 4))
    plt.title(f"Cruce: {cols[0]} vs {cols[1]}")
    plt.tight_layout()
    out_path = os.path.join(outdir, f"{cols[0]}vs{cols[1]}.png")
    plt.savefig(out_path)
    plt.close()
    print(f"📊 Cruce guardado: {out_path}")

# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Perfilamiento base NNA.xlsx")
    parser.add_argument('--input', type=str, required=True, help='Ruta al archivo Excel de entrada')
    parser.add_argument('--sep', type=str, default='auto', help='Separador de columnas (no usado en Excel, solo para compatibilidad)')
    parser.add_argument('--sheet', type=str, default='BD', help='Índice o nombre de la hoja de Excel (por defecto: BD)')
    parser.add_argument('--outdir', type=str, default='reports_nna', help='Directorio salida')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    # Cargar base
    # Convertir sheet a int si es posible
    try:
        sheet_val = int(args.sheet)
    except (ValueError, TypeError):
        sheet_val = args.sheet
    df = load_excel(args.input, sheet=sheet_val)
    print(f"📂 Base cargada con {df.shape[0]} filas y {df.shape[1]} columnas.")

    # Gráficos de columnas específicas
    columnas_graficas = [
        'ESTRATO', 'OCUPACIÓN', 'CATEGORÍAS DE LA DISCAPACIDAD', 'LOCALIDAD',
        'TEMA TRATADOS', 'ALERTAS PSICOSOCIALES', 'CLASIFICACIÓN NUTRICIONAL',
        'REQUIERE ASESORÍA DE NUTRICIÓN',
        'INTERVENCIÓN DE NIÑO, NIÑA O ADOLESCENTE QUE TERMINA EL PROCESO',
        'NNA DESVINCULADO DE LA ACTIVIDAD LABORAL'
    ]
    for col in columnas_graficas:
        if col in df.columns:
            plot_categorical(df, col, args.outdir)

    # Cruces relevantes entre variables
    cruces = [
        ('ESTRATO', 'OCUPACIÓN'),
        ('ESTRATO', 'LOCALIDAD'),
        ('OCUPACIÓN', 'CATEGORÍAS DE LA DISCAPACIDAD'),
        ('CLASIFICACIÓN NUTRICIONAL', 'REQUIERE ASESORÍA DE NUTRICIÓN'),
        ('ALERTAS PSICOSOCIALES', 'TEMA TRATADOS'),
        ('INTERVENCIÓN DE NIÑO, NIÑA O ADOLESCENTE QUE TERMINA EL PROCESO', 'NNA DESVINCULADO DE LA ACTIVIDAD LABORAL'),
        # Puedes agregar más cruces relevantes aquí
    ]
    for col1, col2 in cruces:
        if col1 in df.columns and col2 in df.columns:
            plot_cross(df, [col1, col2], args.outdir)
    parser = argparse.ArgumentParser(description="Perfilamiento base NNA.xlsx")
    parser.add_argument('--input', type=str, required=True, help='Ruta al archivo Excel de entrada')
    parser.add_argument('--sep', type=str, default='auto', help='Separador de columnas (no usado en Excel, solo para compatibilidad)')
    parser.add_argument('--sheet', type=str, default='BD', help='Índice o nombre de la hoja de Excel (por defecto: BD)')
    parser.add_argument('--outdir', type=str, default='reports_nna', help='Directorio salida')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    # Cargar base
    # Convertir sheet a int si es posible
    try:
        sheet_val = int(args.sheet)
    except (ValueError, TypeError):
        sheet_val = args.sheet
    df = load_excel(args.input, sheet=sheet_val)
    print(f"📂 Base cargada con {df.shape[0]} filas y {df.shape[1]} columnas.")

    # Limpiar
    df_clean = clean_data(df)

    # Perfilamiento
    generate_dictionary(df_clean, args.outdir)
    profile_data(df_clean, args.outdir)

    # Gráficos básicos
    for group, cols in GROUPS.items():
        for col in cols:
            if col in df_clean.columns:
                plot_categorical(df_clean, col, args.outdir)

    # Cruces
    for name, cols in CROSSES.items():
        plot_cross(df_clean, cols, args.outdir)

    print("🎯 Análisis terminado.")

if __name__ == "__main__":
    main()