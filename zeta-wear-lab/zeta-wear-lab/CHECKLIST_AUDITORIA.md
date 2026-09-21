# Checklist de auditoría — se pasa a CADA pull request

Copiad esta lista como comentario del PR y marcadla. Un «no» = Request changes.

## Datos y criterio
- [ ] ¿Todos los datos que usa **existen en este repo**? (ni inventados ni "típicos del sector")
- [ ] ¿El criterio de valor está **declarado** (margen/facturación/coste) y es el que pedía el encargo?
- [ ] ¿El CV está calculado sobre la serie **mensual** (no la diaria)?
- [ ] Si limpió o excluyó filas, ¿lo **declara**? (limpiar sin declarar = rechazo)

## Cálculo
- [ ] ¿El orden es por **valor total**, no por cantidad ni precio unitario?
- [ ] ¿El % acumulado termina en 100 (±0,1)?
- [ ] ¿Los cortes A/B/C son 80/95 y las clases XYZ usan 0,25/0,5?

## Verificación por muestreo (vuestra verdad-terreno)
- [ ] Elegid 2–3 referencias y recalculad SU margen a mano (demanda × (precio − coste)): ¿coincide con el CSV del PR?
- [ ] Recalculad el CV de UNA referencia con sus 12 meses (media y desviación, a mano o en una celda de hoja de cálculo): ¿sale la misma clase?
- [ ] ¿El reparto tiene forma de Pareto (pocas referencias concentran ~80 % del valor)? Si sale media clase en A, algo está mal ordenado.
- [ ] Las fronterizas (cv o % acumulado rozando un corte): ¿a qué lado caen, y el PR lo justifica?

## Forma
- [ ] ¿El PR explica QUÉ hizo y POR QUÉ, o solo pega código?
- [ ] ¿El CI está en verde? (recordad: verde = forma correcta, no verdad)
- [ ] Veredicto escrito: APROBAR / PEDIR CAMBIOS + argumento en 2 líneas
