# Encargo 1 · Clasificación ABC por margen

**Contexto:** dirección ha decidido priorizar el catálogo por MARGEN (no por facturación).

**Tarea para el agente:**
Crea un script `analisis/abc.py` que lea `datos/ex2_sku_master.csv` y genere
`resultados/abc.csv` con estas columnas: `sku`, `margen_anual`
(= annual_demand × (price − cost)), `pct_acumulado` (sobre el total de margen)
y `clase_abc` (cortes: A hasta el 80 % acumulado, B hasta el 95 %, C el resto),
**ordenado de mayor a menor margen anual**. Solo biblioteca estándar de Python.
Ejecuta el script y haz commit también del CSV de resultados.
En la descripción del PR: declara qué criterio de valor usas y por qué.
