# Zeta Wear · Lab de agentes — «El becario infinito»

**GOEI 2026/27 · UIE.** Vuestro equipo ha «contratado» un agente de IA que
programa. Vosotros no picáis código: **encargáis, auditáis y decidís si se
firma**. Nada se mergea sin validarlo por muestreo: recalculad a mano unas
referencias antes de firmar.

## Qué hay aquí

- `datos/` — el catálogo Zeta Wear (20 SKU) y la serie diaria de Fast&City.
  Datos sintéticos del curso.
- `encargos/01..05` — los cinco encargos, listos para copiar como Issues.
- `CHECKLIST_AUDITORIA.md` — la lista que se pasa a CADA pull request.
- `tests/` + CI — guardarraíles automáticos (se ejecutan solos en cada PR).
  Que el CI esté verde NO significa que el resultado sea correcto: significa
  que tiene la forma correcta. La verdad-terreno la ponéis vosotros
  recalculando una muestra a mano.
- `planB/` — si vuestro agente no está disponible, hay un PR congelado para
  auditar sin conexión.

## Reglas del lab

1. Un encargo = un Issue = un PR. No se mezclan.
2. El plan que proponga el agente **se lee y se corrige antes de aprobarlo**.
3. Ningún merge sin: checklist pasada + muestreo recalculado a mano +
   comentario de review escrito en el PR (será evaluado).
4. Si el agente usa un dato que no existe en este repo, se rechaza el PR y
   se documenta — detectarlo puntúa.

La guía paso a paso completa: `GUIA_EQUIPO.md`.
