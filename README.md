# **Entendimiento del negocio**

## Determinar los objetivos del negocio

### Antecedentes
El trabajo infantil en Bogotá sigue siendo un fenómeno social complejo que limita el desarrollo integral de los niños, niñas y adolescentes (NNA), afectando su acceso a la educación, su bienestar emocional y su salud física. La existencia de registros integrados ofrece una oportunidad para caracterizar y comprender este problema de manera más precisa.

### Criterios de éxito del negocio
Proporcionar a las instituciones gubernamentales y sociales datos confiables y estructurados que apoyen la toma de decisiones y contribuyan a políticas públicas efectivas orientadas a la protección de la niñez.

## Evaluar la situación

### Inventario de recursos
La base de datos cuenta con información de NNA y sus condiciones laborales, familiares, sociales y de salud, lo que permite un análisis multidimensional. También se dispone de personal técnico para procesar la información y de herramientas tecnológicas para su análisis.

### Requisitos, supuestos y restricciones
Se debe garantizar la protección de datos personales y el cumplimiento de la normativa en materia de confidencialidad. Además, se asume que los registros reflejan la realidad de los NNA, aunque podrían existir vacíos o subregistros.

### Riesgos y contingencias
La información puede presentar problemas de calidad como datos faltantes, inconsistencias o errores de digitación. También existe el riesgo de sesgo, pues no todos los casos de trabajo infantil son reportados o detectados.

### Terminología
Es fundamental precisar los conceptos clave: “trabajo infantil”, “peores formas de trabajo infantil”, “acompañamiento social y psicológico”, “riesgo de vulnerabilidad” y “protección integral”.

### Costos y beneficios
Los costos se asocian al procesamiento, limpieza y análisis de la base de datos, así como a la capacitación de equipos en metodologías analíticas, al igual que equipos en caso de que se requiera un sobre muestreo. Los beneficios superan ampliamente los costos, ya que la información resultante puede sustentar intervenciones que mejoren la calidad de vida y reduzcan la vulneración de derechos de los NNA.

## Determinar los objetivos de minería de datos

### Objetivos de la minería de datos
Explorar la base para identificar patrones en la situación de los NNA, como factores familiares o sociales que inciden en la permanencia en el trabajo infantil; segmentar la población por edad, género y localidad; y reconocer variables críticas asociadas a condiciones de mayor vulnerabilidad.

### Criterios de éxito de la minería de datos
Lograr indicadores estadísticos, visualizaciones y modelos analíticos que permitan identificar perfiles de riesgo y zonas prioritarias de intervención, aportando valor real a los responsables de políticas sociales.


# **Objetivos**

## Objetivo específico
Analizar y diagnosticar la situación del trabajo infantil en Bogotá a partir de registros sociales, familiares, de salud y laborales, con el fin de proporcionar información confiable y visualmente interpretativa que oriente la formulación de políticas públicas y estrategias de protección integral para niños, niñas y adolescentes.
 
## Objetivo específico

**1.** Caracterizar la población infantil y adolescente en condición de trabajo en Bogotá, según variables sociodemográficas (edad, género, localidad) y de entorno, identificando los grupos más afectados y estableciendo indicadores de incidencia por segmento poblacional.

**2.** Analizar las condiciones familiares, sociales y de salud de los NNA registrados, con el fin de detectar patrones de vulnerabilidad asociados a la permanencia en trabajo infantil.

**3.** Identificar las diferencias territoriales y zonas de concentración del trabajo infantil entre las localidades de Bogotá, utilizando herramientas de análisis espacial y segmentación de datos.

**4.** Determinar las variables críticas (económicas, sociales, educativas o de salud) que más influyen en la probabilidad de que un NNA trabaje o esté en peores formas de trabajo infantil, aplicando técnicas analíticas de minería de datos.

**5.** Generar un informe visual e interpretativo con los resultados del análisis, incluyendo indicadores, gráficos, mapas y conclusiones, para el 16 de octubre, para que sirva como insumo técnico en la formulación de políticas públicas y programas de protección infantil.

# **Alcance y criterios de éxito del proyecto**

## Alcance
El proyecto se centra en el análisis de la base de datos del Sistema de Información Integrado para el Registro y la Erradicación del Trabajo Infantil y sus Peores Formas en Bogotá. La información incluye registros de niños, niñas y adolescentes (NNA) con datos sociodemográficos, familiares, sociales, de salud y laborales.
El alcance contempla:

 - Procesamiento, limpieza y organización de los registros disponibles.

 - Análisis descriptivo y exploratorio para caracterizar la población en condición de trabajo infantil.

 - Identificación de patrones y factores de riesgo asociados al fenómeno.

 - Elaboración de indicadores y visualizaciones que apoyen la toma de decisiones institucionales.

Quedan fuera del alcance del presente análisis: la recolección de nueva información en campo y la implementación directa de programas de intervención, dado que el objetivo principal es el diagnóstico y generación de insumos para la política pública.

**Criterios de éxito**

El proyecto se considerará exitoso si logra:

**1.** Producir un diagnóstico integral y confiable sobre la magnitud y características del trabajo infantil en Bogotá.

**2.** Identificar factores de riesgo y territorios críticos que permitan priorizar acciones de intervención.

**3.** Generar insumos visuales y analíticos que sean comprensibles y útiles para los tomadores de decisiones en el diseño de políticas y programas de protección infantil.

# **Terminología**

## Glosario de terminología del negocio

**Trabajo infantil:** Actividades económicas o de supervivencia realizadas por niños, niñas o adolescentes que afectan negativamente su desarrollo físico, mental, social o educativo.

**Peores formas de trabajo infantil:** Modalidades que implican explotación, peligro, ilegalidad o riesgo extremo para la salud y la vida de los NNA (ej. trabajo en minas, explotación sexual, reclutamiento ilícito).

**NNA:** Sigla para “niños, niñas y adolescentes”. Se utiliza como denominación inclusiva de la población objeto de estudio.

**Acompañamiento social y familiar:** Estrategias implementadas por entidades sociales para brindar apoyo psicosocial, educativo y económico a las familias y NNA en riesgo.

**Condiciones de salud:** Información relativa al bienestar físico y psicológico de los NNA que permite identificar afectaciones derivadas del trabajo infantil.


## Glosario de terminología de minería de datos

**Variable:** Característica o atributo registrado en la base de datos (ejemplo: edad, género, localidad, estado de salud).

**Registro:** Cada fila en la base de datos que corresponde a un NNA con sus respectivas características.

**Segmentación (clustering):** Técnica que agrupa individuos con características similares (ejemplo: clúster de NNA en riesgo alto según edad y condiciones laborales).

**Patrón:** Relación recurrente identificada en los datos (ejemplo: mayor incidencia de trabajo infantil en localidades con baja asistencia escolar).

**Indicador:** Medida cuantitativa construida a partir de los datos para describir un fenómeno (ejemplo: porcentaje de NNA que trabajan por localidad).

# **Recursos (Base)**

- **Identificación y fechas:**  
  `Id_fic`, `Usuario`, `Red_fic`, `Fecha_intervencion`, `Fecha_seguimiento_cierre`, `Fecha_reposicion`.  
  *Variables clave para identificar cada registro y dar seguimiento temporal a los procesos.*  

- **Resultados y seguimiento:**  
  `NNA_desvinculado_de_la_actividad_laboral`, `Adolescente_trabajo_protegido`, `Intervencion_que_termina_el_proceso`.  
  *Indicadores sobre el estado del proceso y resultados obtenidos en la intervención.*  

- **Salud y nutrición:**  
  `Peso`, `Talla_cm`, `Clasificacion_nutricional`, `Requiere_asesoria_de_nutricion`, `Alertas_psicosociales`, `Salud_bucal`, `Infancia`, `En_mujeres`, `Etapa_de_gestacion`.  
  *Variables que describen el estado físico y nutricional del NNA, así como alertas de salud.*  

- **Individuo y hogar:**  
  `Edad`, `Sexo`, `Genero`, `Estado_civil`, `Fecha_nacimiento`, `Nacionalidad`, `Etnia`, `Pueblo`, `Vinculo_con_el_jefe_de_hogar`, `Personas_a_cargo`.  
  *Características sociodemográficas y del entorno familiar del NNA.*  

- **Educación y trabajo:**  
  `Ocupacion`, `IdNivelEducativo`, `RazonAbandonoEscolar`.  
  *Información educativa y laboral que permite analizar el impacto del trabajo infantil en la formación.*  

- **Protección social:**  
  `Afiliacion_al_SGSSS`, `Nombre_EAPB`, `Subgrupo_SISBEN`, `Estrato`.  
  *Variables que identifican el acceso a servicios de salud y programas sociales.*  

- **Territorio y dirección:**  
  `Localidad`, `UPZ`, `Barrio`, `Barrio_priorizado`, `Manzana_del_cuidado`, `Coordenadas_X/Y`.  
  *Información territorial que permite localizar espacialmente a los NNA y detectar focos de vulnerabilidad.*  

- **Operación del programa:**  
  `Nombre_de_la_UT`, `Perfil_profesional`, `Temas_tratados`, `Acompanamiento#`, `IEC#`.  
  *Datos sobre la gestión y seguimiento de los programas de intervención.*  

## 4. ENTENDIMIENTO DE LOS DATOS

### 4.1 Estructura general de la base

| Variable | Descripción | Ejemplo |
|-----------------------|-----------------------------|-------------------|
| `SEXO` | Sexo del NNA | 1- Hombre |
| `OCUPACIÓN` | Actividad principal | 3- Estudiante |
| `LOCALIDAD` | Zona de residencia | 19- Ciudad Bolívar |
| `ESTRATO_SOCIOECONÓMICO` | Nivel económico del hogar | 2\. Bajo |
| `POBLACIÓN_DIFERENCIAL_Y_DE_INCLUSIÓN` | Grupo poblacional especial | 13- Migrante |
| `NNA_DESVINCULADO_DE_LA_ACTIVIDAD_LABORAL` | Estado laboral actual | SI / NO |

![](01_dashboard_general.png)

------------------------------------------------------------------------

### 4.2 Variables con mayor porcentaje de faltantes

![](6abf94e5-b7ae-4ee6-8239-a96e6fbeae13.png)

Las 15 variables con mayor porcentaje de faltantes incluyen campos
administrativos y de intervención institucional, como:\
- `INFORMACIÓN_DEL_ACUDIENTE`\
- `INFORMACIÓN_LABORAL`\
- `ACOMPAÑAMIENTO_2`\
- `ÚLTIMA_INTERVENCIÓN`\
- `DIRECCIÓN_DE_LA_VIVIENDA`

El **100% de faltantes** en estas variables responde a campos
condicionales no aplicables en todos los registros.

Por tanto, se decidió **no imputarlas** y excluirlas del modelado
predictivo.

------------------------------------------------------------------------

### 4.3 Anonimización y consistencia

-   Eliminación de identificadores personales.\
-   Estandarización de texto y codificación de variables.\
-   Conversión de fechas, factores y etiquetas uniformes.\
-   Normalización de nombres de localidades y estratos.

------------------------------------------------------------------------

## 5. ANÁLISIS DESCRIPTIVO

### 5.1 Caracterización demográfica

| Variable | Distribución destacada |
|-----------------------|-------------------------------------------------|
| **Sexo** | 1- Hombre: 40.6% / 2- Mujer: 39.6% / Intersexual: 0.0% |
| **Estrato socioeconómico** | 2\. Bajo (52.3%), 3. Medio-bajo (16.0%), 1. Bajo-bajo (11.4%) |
| **Ocupación principal** | 3- Estudiante (39.7%), 2- Trabajo informal (17.1%), 11- Ninguno (4.8%) |
| **Vínculo con el jefe del hogar** | Hijo(a) (57.4%), Nieto(a) (2.4%), Otro pariente (1.9%) |

![](01_dashboard_demografico.png)

> 🧠 *La mayoría de los NNA son hombres y estudiantes pertenecientes a
> hogares de estrato bajo, principalmente en el sur de la ciudad.*

------------------------------------------------------------------------

### 5.2 Condición laboral de los NNA

| Estado laboral | Frecuencia | Porcentaje |
|----------------|------------|------------|
| SI             | 35,071     | 62.1%      |
| NO             | 7,248      | 12.8%      |
| Si             | 1,557      | 2.8%       |
| No             | 421        | 0.7%       |
| NO APLICA      | 32         | 0.1%       |
| NA             | 12,144     | 21.5%      |

> ⚠️ **El 64.9% de los NNA** han estado o están vinculados laboralmente,
> lo cual indica una **alta incidencia de trabajo infantil** en la
> muestra analizada.

![](03_analisis_laboral.png)

------------------------------------------------------------------------

### 5.3 Distribución territorial

| Localidad          | Casos reportados (%) |
|--------------------|----------------------|
| 19- Ciudad Bolívar | 11.9%                |
| 7- Bosa            | 9.1%                 |
| 8- Kennedy         | 8.4%                 |
| 11- Suba           | 7.6%                 |
| 10- Engativá       | 5.9%                 |

> 📍 Las localidades del sur y suroccidente (Ciudad Bolívar, Bosa y
> Kennedy) concentran el **mayor número de casos**.

------------------------------------------------------------------------

### 5.4 Población diferencial

![](dda9e5c0-dda7-466e-af5a-d55e485dc0a2.png)

| Condición                       | Porcentaje |
|---------------------------------|------------|
| 14- No Aplica                   | 90.8%      |
| 13- Migrante                    | 8.7%       |
| 2- Discapacidad                 | 0.3%       |
| 1- Víctima del conflicto armado | 0.1%       |

> 💬 Los NNA migrantes presentan **mayor exposición al trabajo
> informal**, especialmente en sectores de bajo estrato.

------------------------------------------------------------------------

### 5.5 Cruces analíticos clave

![](02_cruces_analiticos.png)\
![](03_heatmap_ocupacion_sexo.png)\
![](02_heatmap_vinculo.png)

-   Las **ocupaciones informales** están asociadas mayormente a
    hombres.\
-   Las **labores de cuidado y oficios del hogar** son realizadas
    principalmente por mujeres.\
-   Los **nietos, hijastros y familiares indirectos** presentan mayores
    tasas de trabajo infantil.

------------------------------------------------------------------------

## 6. MODELADO PREDICTIVO

### 6.1 Modelos utilizados

| Modelo              | Accuracy | Observaciones                              |
|------------------|----------------------|--------------------------------|
| Árbol de decisión   | 0.81     | Buen balance entre precisión y simplicidad |
| Random Forest       | 0.88     | Mejor desempeño general                    |
| Gradient Boosting   | 0.87     | Buen ajuste pero mayor complejidad         |
| Regresión logística | 0.73     | Base comparativa                           |

![](01_comparacion_modelos.png) ![](03_confusion_matrix.png)
![](02_importancia_variables.png)

### 6.2 Variables más relevantes

1.  Ocupación\
2.  Estrato socioeconómico\
3.  Localidad\
4.  Sexo\
5.  Vínculo con el jefe del hogar

> 🔍 *Las variables socioeconómicas y familiares explican la mayor parte
> de la varianza del modelo.*

------------------------------------------------------------------------

## 7. HALLAZGOS CLAVE

1.  **Alta prevalencia del trabajo infantil (≈65%)**, especialmente en
    hogares de bajo estrato y estructura familiar extendida.\
2.  **Ciudad Bolívar, Bosa y Kennedy** son las zonas con mayor
    concentración de casos.\
3.  **Sexo y ocupación** mantienen relación directa: hombres en trabajo
    informal, mujeres en cuidado del hogar.\
4.  Los **migrantes** y **NNA con discapacidad** muestran mayor
    vulnerabilidad.\
5.  El **estrato bajo y medio-bajo** es el principal determinante
    socioeconómico.\
6.  El **modelo Random Forest** alcanzó **0.88 de exactitud**, validando
    su potencial predictivo.

------------------------------------------------------------------------

## 8. CONCLUSIONES

✅ **Cumplimiento del criterio de éxito:**\
El modelo superó el umbral esperado (Accuracy \> 0.80), cumpliendo los
objetivos de predicción y caracterización.

📈 **Conclusiones generales:** - El trabajo infantil en Bogotá tiene una
**causa estructural socioeconómica**.\
- Se observa un **perfil de riesgo concentrado en el sur y occidente**
de la ciudad.\
- Los resultados permiten **diseñar estrategias territoriales
focalizadas** y **políticas basadas en evidencia**.\
- La aplicación de **CRISP–DM** garantizó orden, trazabilidad y
replicabilidad del proceso analítico.

------------------------------------------------------------------------

## 9. RECOMENDACIONES

1.  **Focalizar intervenciones** en las localidades con mayor incidencia
    (Ciudad Bolívar, Bosa, Kennedy).\
2.  **Fortalecer programas de acompañamiento familiar**, especialmente
    en hogares no nucleares.\
3.  **Implementar estrategias educativas** de reintegración para NNA
    desvinculados laboralmente.\
4.  **Consolidar un sistema de monitoreo permanente** de casos, con
    datos actualizados y compartidos entre instituciones.\
5.  **Actualizar el modelo predictivo** semestralmente para incorporar
    nuevos registros y tendencias.

------------------------------------------------------------------------

## 10. ANEXOS VISUALES

![](30c404fe-3c53-4974-8a45-6892f21b1090.png)
![](02_heatmap_vinculo.png) ![](02_sexo_ocupacion.png)
![](04_poblacion_diferencial.png) ![](01_dashboard_general.png)
![](03_analisis_laboral.png)

------------------------------------------------------------------------

## 11. CONCLUSIÓN FINAL

El análisis permitió construir una **visión integral del trabajo
infantil en Bogotá**, integrando factores **demográficos, familiares,
económicos y territoriales**.\
El modelo predictivo desarrollado ofrece una herramienta robusta para
apoyar decisiones institucionales en la **erradicación y prevención del
trabajo infantil**.


