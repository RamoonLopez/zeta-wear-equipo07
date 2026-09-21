# Encargo 2 · Clasificación XYZ (coeficiente de variación)

**Tarea para el agente:**
Crea `analisis/xyz.py` que lea `datos/ex2_monthly_sales.csv` (20 SKU × 12 meses)
y genere `resultados/xyz.csv` con: `sku`, `media_mensual`, `desv_tipica`, `cv`
(= desviación / media; declara en el PR si usas desviación poblacional o
muestral) y `clase_xyz` con los umbrales X: cv ≤ 0,25 · Y: 0,25 < cv ≤ 0,5 ·
Z: cv > 0,5. La serie de referencia es la MENSUAL. Solo biblioteca estándar.
Ejecuta el script y haz commit del CSV de resultados.
