import csv
import math
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, "datos", "ex2_monthly_sales.csv")
    output_dir = os.path.join(base_dir, "resultados")
    output_path = os.path.join(output_dir, "xyz.csv")

    items = []
    with open(input_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sku = row["sku"]
            sales = [float(row[k]) for k in row.keys() if k != "sku"]
            n = len(sales)
            media_mensual = sum(sales) / n

            # Desviación típica muestral (ddof=1)
            varianza = sum((x - media_mensual) ** 2 for x in sales) / (n - 1)
            desv_tipica = math.sqrt(varianza)

            cv = desv_tipica / media_mensual if media_mensual != 0 else 0.0

            if cv <= 0.25:
                clase_xyz = "X"
            elif cv <= 0.5:
                clase_xyz = "Y"
            else:
                clase_xyz = "Z"

            items.append({
                "sku": sku,
                "media_mensual": media_mensual,
                "desv_tipica": desv_tipica,
                "cv": cv,
                "clase_xyz": clase_xyz
            })

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["sku", "media_mensual", "desv_tipica", "cv", "clase_xyz"])
        writer.writeheader()
        for item in items:
            writer.writerow({
                "sku": item["sku"],
                "media_mensual": f"{item['media_mensual']:.2f}",
                "desv_tipica": f"{item['desv_tipica']:.2f}",
                "cv": f"{item['cv']:.4f}",
                "clase_xyz": item["clase_xyz"]
            })

if __name__ == "__main__":
    main()
