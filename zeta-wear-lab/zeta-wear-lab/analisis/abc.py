import csv
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, "datos", "ex2_sku_master.csv")
    output_dir = os.path.join(base_dir, "resultados")
    output_path = os.path.join(output_dir, "abc.csv")

    items = []
    with open(input_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sku = row["sku"]
            price = float(row["price"])
            cost = float(row["cost"])
            demand = float(row["annual_demand"])
            margen_anual = demand * (price - cost)
            items.append({
                "sku": sku,
                "margen_anual": margen_anual
            })

    # Ordenar de mayor a menor margen anual
    items.sort(key=lambda x: x["margen_anual"], reverse=True)

    total_margen = sum(item["margen_anual"] for item in items)

    acumulado = 0.0
    for item in items:
        acumulado += item["margen_anual"]
        pct_acumulado = (acumulado / total_margen) * 100.0
        item["pct_acumulado"] = pct_acumulado

        # Cortes: A hasta el 80% acumulado, B hasta el 95%, C el resto
        # Nota: Asignación basada en si el porcentaje acumulado previo o actual está dentro del umbral,
        # o si el pct_acumulado individual no supera el umbral excepto para el elemento que cruza.
        # En la práctica estándar de ABC: si el pct_acumulado <= 80 -> A, si <= 95 -> B, else C.
        # Ajustamos para evitar saltar la categoría A si el primer ítem ya supera 80% (no es el caso aquí)
        # o cuando el corte se define por el pct_acumulado.
        if pct_acumulado <= 80.0:
            clase = "A"
        elif pct_acumulado <= 95.0:
            clase = "B"
        else:
            clase = "C"

        # En el caso de que un elemento supere ligeramente el 80% pero sea de los primeros,
        # se verifica si el anterior estaba por debajo de 80. Por ejemplo, en el análisis previo,
        # ZW-DEN-002 llegó a 79.15% (A) y ZW-ACC-004 llegó a 81.59% (B).
        item["clase_abc"] = clase

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["sku", "margen_anual", "pct_acumulado", "clase_abc"])
        writer.writeheader()
        for item in items:
            writer.writerow({
                "sku": item["sku"],
                "margen_anual": f"{item['margen_anual']:.2f}",
                "pct_acumulado": f"{item['pct_acumulado']:.2f}",
                "clase_abc": item["clase_abc"]
            })

if __name__ == "__main__":
    main()
