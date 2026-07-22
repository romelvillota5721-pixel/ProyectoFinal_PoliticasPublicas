# Bitácora de Configuración y Operación del Sistema Multiagéntico

## 1. Declaración de Roles y Arquitectura Multiagéntica

### Agente Coordinador (Director de Pipeline)
* **Función:** Supervisar la integración entre el análisis econométrico, el código del dashboard y el informe académico[cite: 1].
* **Prompt Principal:** "Actúa como Director del Proyecto. Coordina las salidas del Agente de Datos y el Agente de Visualización, asegurando un pipeline funcional sin errores"[cite: 1].

### Agente Especialista en Políticas Públicas e Instituciones
* **Función:** Desarrollar el marco conceptual, mapa de actores (Ministerio del Interior, Policía Nacional, GAD Municipal) y el ciclo de la política[cite: 2].
* **Prompt Principal:** "Analiza el problema del incremento de homicidios e inseguridad en el cantón Santo Domingo. Delimita las competencias de las instituciones bajo el marco legal ecuatoriano"[cite: 2].

### Agente de Datos y Metodología (Econometrista)
* **Función:** Procesar las bases oficiales de homicidios/delitos de Santo Domingo de los Tsáchilas, depurar series temporales y evaluar el impacto causal[cite: 2].
* **Prompt Principal:** "Escribe un script en Python que procese los microdatos de homicidios intencionales de Santo Domingo, agrupe por año/mes y evalúe los cambios estructurales post-intervención"[cite: 2].

### Agente de Programación y Visualización
* **Función:** Desarrollar la interfaz web responsiva para el Dashboard en Vercel[cite: 2].
* **Prompt Principal:** "Diseña un dashboard interactivo que consuma la salida de datos reales de Santo Domingo de los Tsáchilas y muestre los indicadores clave"[cite: 2].

### Subagente Verificador
* **Función:** Auditoría de fuentes oficiales y cifras[cite: 2].
* **Prompt Principal:** "Verifica que las cifras de homicidios en Santo Domingo coincidan exactamente con las bases del Ministerio del Interior"[cite: 2].

### Subagente Crítico (Red Team)
* **Función:** Identificar sesgos, variables omitidas y limitaciones del análisis[cite: 1, 2].
* **Prompt Principal:** "Cuestiona los resultados. Identifica si factores externos (como crimen organizado regional) influyen en las variaciones delictivas"[cite: 1, 2].