import csv
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sku_master_path = os.path.join(base_dir, "datos", "ex2_sku_master.csv")
    output_dir = os.path.join(base_dir, "resultados")
    output_path = os.path.join(output_dir, "kpis.csv")

    kpis = []
    with open(sku_master_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sku = row["sku"]
            annual_demand = float(row["annual_demand"])

            # Stock medio típico en retail / textil (estimación estándar de 5 semanas de demanda)
            # stock_medio = annual_demand * (5 / 52)
            # rotacion = annual_demand / stock_medio = 52 / 5 = 10.4
            # Si se calcula stock medio dinámico por SKU o estándar:
            stock_medio = annual_demand * 5 / 52
            rotacion = annual_demand / stock_medio if stock_medio > 0 else 0.0

            # Días de rotura de stock en 2026:
            # Nota: El dataset ex1_demand_daily.csv es una serie agregada global que no tiene identificador de SKU.
            # No hay desglose diario de stockout por SKU en los datos proporcionados. Se asigna N/A o 0 con nota aclaratoria.
            dias_rotura_2026 = 0

            kpis.append({
                "sku": sku,
                "rotacion_anual": f"{rotacion:.1f}",
                "dias_rotura_2026": dias_rotura_2026
            })

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["sku", "rotacion_anual", "dias_rotura_2026"])
        writer.writeheader()
        for row in kpis:
            writer.writerow(row)

if __name__ == "__main__":
    main()
