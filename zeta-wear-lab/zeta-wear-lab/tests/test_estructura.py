"""Guardarrailes estructurales. Verde = forma correcta, NO verdad-terreno.
La validacion de fondo la hace el equipo contra su matriz de cartas."""
import csv, os, pytest

RES = os.path.join(os.path.dirname(__file__), "..", "resultados")
DAT = os.path.join(os.path.dirname(__file__), "..", "datos")

def leer(nombre, carpeta=RES):
    ruta = os.path.join(carpeta, nombre)
    if not os.path.exists(ruta):
        pytest.skip(f"{nombre} aun no existe (encargo pendiente)")
    with open(ruta, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def test_dataset_integro():
    filas = leer("ex2_sku_master.csv", DAT)
    assert len(filas) == 20, "el catalogo debe tener 20 SKU"

def test_abc_estructura():
    filas = leer("abc.csv")
    assert len(filas) == 20, "abc.csv debe tener los 20 SKU"
    margenes = [float(f["margen_anual"]) for f in filas]
    assert margenes == sorted(margenes, reverse=True), "debe ir ordenado de mayor a menor margen"
    assert abs(float(filas[-1]["pct_acumulado"]) - 100.0) < 0.1, "el % acumulado debe terminar en 100"
    assert set(f["clase_abc"] for f in filas) <= {"A", "B", "C"}

def test_xyz_estructura():
    filas = leer("xyz.csv")
    assert len(filas) == 20
    for f in filas:
        cv = float(f["cv"])
        assert cv >= 0
        esperada = "X" if cv <= 0.25 else ("Y" if cv <= 0.5 else "Z")
        assert f["clase_xyz"] == esperada, f"{f['sku']}: cv={cv} no cuadra con clase {f['clase_xyz']}"

def test_clasificacion_estructura():
    filas = leer("clasificacion.csv")
    assert len(filas) == 20
    for f in filas:
        assert f["celda"] == f["clase_abc"] + f["clase_xyz"], f"{f['sku']}: celda mal formada"
