import csv
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    abc_path = os.path.join(base_dir, "resultados", "abc.csv")
    xyz_path = os.path.join(base_dir, "resultados", "xyz.csv")
    clasificacion_path = os.path.join(base_dir, "resultados", "clasificacion.csv")
    politicas_path = os.path.join(base_dir, "resultados", "politicas.md")

    abc_dict = {}
    with open(abc_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            abc_dict[row["sku"]] = row["clase_abc"]

    xyz_dict = {}
    with open(xyz_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            xyz_dict[row["sku"]] = {
                "cv": row["cv"],
                "clase_xyz": row["clase_xyz"]
            }

    clasificacion = []
    celdas_ocupadas = set()

    for sku, clase_abc in abc_dict.items():
        xyz_data = xyz_dict[sku]
        clase_xyz = xyz_data["clase_xyz"]
        cv = xyz_data["cv"]
        celda = f"{clase_abc}{clase_xyz}"
        celdas_ocupadas.add(celda)

        clasificacion.append({
            "sku": sku,
            "clase_abc": clase_abc,
            "cv": cv,
            "clase_xyz": clase_xyz,
            "celda": celda
        })

    # Guardar clasificacion.csv
    with open(clasificacion_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["sku", "clase_abc", "cv", "clase_xyz", "celda"])
        writer.writeheader()
        for row in clasificacion:
            writer.writerow(row)

    # Definición de políticas por celda ocupada
    politicas_def = {
        "AX": "Alta rentabilidad y demanda muy estable. Reaprovisionamiento automático contínuo con stock de seguridad mínimo.",
        "AY": "Alta rentabilidad y demanda moderadamente variable. Revisión periódica estrecha y stock de seguridad moderado.",
        "AZ": "Alta rentabilidad pero demanda altamente impredecible. Gestión bajo pedido o revisión frecuente con stock de colchón alto para evitar roturas.",
        "BX": "Rentabilidad media y demanda estable. Automatización de pedidos por punto de reorden con stock de seguridad estándar.",
        "BY": "Rentabilidad media y demanda variable. Revisión periódica mensual ajustando pronósticos de demanda.",
        "BZ": "Rentabilidad media y demanda muy variable. Compra bajo pedido o lote mínimo estricto, reduciendo riesgo de obsolescencia.",
        "CX": "Baja rentabilidad y demanda estable. Compras agrupadas o lotes grandes para minimizar costes de gestión.",
        "CY": "Baja rentabilidad y demanda variable. Revisión puntual y compras bajo demanda o consumo.",
        "CZ": "Baja rentabilidad y demanda impredecible. Evaluar eliminación del catálogo o mantener exclusivamente bajo pedido estricto."
    }

    # Generar politicas.md
    with open(politicas_path, mode="w", encoding="utf-8") as f:
        f.write("# Políticas de Gestión de Inventario por Celda ABC-XYZ\n\n")
        f.write("A continuación se detallan las políticas de gestión asociadas a las celdas ocupadas de la matriz:\n\n")
        for celda in sorted(celdas_ocupadas):
            politica = politicas_def.get(celda, "Revisión periódica adaptada a las características de margen y variabilidad.")
            f.write(f"### Celda {celda}\n")
            f.write(f"- {politica}\n\n")

if __name__ == "__main__":
    main()
