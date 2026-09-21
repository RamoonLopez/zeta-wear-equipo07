# Lab de agentes «El becario infinito» — Guía del equipo, paso a paso

**GOEI 2026/27 · UIE · Equipos de 3–4.** Vuestro equipo ha contratado un
becario que programa rápido, redacta mejor que vosotros, no se cansa… y a
veces se inventa las cosas. Vuestro trabajo en este lab NO es programar: es
**encargar bien, auditar de verdad y decidir si se firma**. Exactamente lo
que hará de vosotros el mercado.

**La regla de oro:** ningún pull request se mergea sin pasar el
`CHECKLIST_AUDITORIA.md` y sin una **verificación por muestreo hecha por
vosotros**: elegid 2–3 referencias y recalculad sus números a mano o en una
celda de hoja de cálculo. Si el agente y vuestra muestra no cuadran, alguien
se equivoca — y hay que averiguar quién antes de firmar.

---

## Paso 0 · Cuentas (10' — y una gestión que conviene hacer YA)

1. **GitHub**: una cuenta por miembro del equipo (github.com, gratis).
2. **GitHub Education** (muy recomendado, tarda unos días en aprobarse:
   solicitadlo hoy aunque el lab sea otro día): education.github.com →
   *Student Developer Pack*, con el correo de la universidad. Incluye
   **Copilot Pro gratis para estudiantes**, que es una de las opciones de
   agente del paso 2.
3. **Google**: una cuenta por equipo (vale una personal) para Jules y Gemini.
4. **Vercel**: la crearéis en el encargo 5 con el botón «Continue with
   GitHub» — no hace falta nada más.

## Paso 1 · Vuestro repo (10')

1. Abrid el repo plantilla del curso (URL en el campus) → botón verde
   **«Use this template» → «Create a new repository»**.
2. Propietario: la cuenta de un miembro · Nombre: `zeta-wear-equipoNN` ·
   Visibilidad: **Public** (los agentes gratuitos y Vercel lo necesitan).
3. En el repo nuevo: *Settings → Collaborators* → añadid al resto del equipo.
4. Comprobad que en la pestaña *Actions* está el workflow «guardarrailes»:
   es el CI que se ejecutará solo en cada PR.

## Paso 2 · Elegid vuestro agente (10')

Cualquiera de los tres vale para todo el lab. Si uno se queda sin cuota,
cambiad a otro — los encargos son los mismos.

**Opción A — Jules (Google), la recomendada.** jules.google.com → entrar con
la cuenta Google del equipo → «Connect to GitHub» → instalad la app dándole
acceso SOLO a vuestro repo → seleccionad el repo. Plan gratuito: 15 tareas al
día y 3 simultáneas. Trabaja en una máquina virtual, propone un plan, y
cuando termina **abre un pull request** en vuestro repo.

**Opción B — Copilot coding agent (si ya tenéis GitHub Education).** En
vuestro repo, abrid el Issue del encargo y **asignádselo a Copilot** (en
*Assignees*). Copilot trabaja en segundo plano y abre el PR él solo.

**Opción C — Gemini CLI (todo en vuestro portátil).** Requiere Node 20+:
`npm install -g @google/gemini-cli`, después `gemini` dentro del clon del
repo y entrad con la cuenta Google (gratis, 1.000 peticiones/día). Aquí el
agente edita en local: pedidle que trabaje en una rama, revisad con
`git diff`, y el PR lo abrís vosotros. Es la opción con más control — y más
trabajo manual.

**Para todos los equipos (2', obligatorio):** instalad la app **Gemini Code
Assist** de GitHub (github.com/apps/gemini-code-assist, gratis) en vuestro
repo. Revisa automáticamente cada PR y deja comentarios. Spoiler: NO
sustituye vuestra auditoría — al final del lab compararéis qué cazó ella y
qué cazasteis vosotros.

## Paso 3 · El ciclo de trabajo (así se hace CADA encargo)

1. **Issue**: en GitHub → *Issues → New issue* → copiad tal cual el texto de
   `encargos/NN-*.md` (título incluido).
2. **Encargo al agente**: pegadle el texto del issue y añadid siempre esta
   frase: *«Trabaja en una rama nueva y abre un pull request. No toques
   nada fuera de lo que pide el encargo.»*
3. **El plan**: Jules (y Copilot) proponen un plan antes de tocar código.
   **Leedlo.** ¿Va a usar los datos correctos? ¿El criterio que pedís? Si
   algo chirría, corregidlo ANTES de aprobar el plan. Aprobar planes sin
   leer es firmar cheques en blanco.
4. **Mientras trabaja** (5–15 min): preparad la auditoría — checklist abierta
   y vuestra muestra elegida: apuntad ya las 2–3 referencias que vais a
   recalcular a mano y qué esperáis ver (¿tiene pinta de Pareto? ¿cuántas
   referencias en A, más o menos?).
5. **Auditar el PR**: pestaña *Files changed*. Pegad el
   `CHECKLIST_AUDITORIA.md` como comentario y marcadlo punto a punto.
   Mirad el CI (verde = forma correcta, NO verdad) y la review automática de
   Gemini Code Assist. Comentad **en las líneas concretas** del código.
6. **Decidir**: *Review changes* → **Request changes** (con argumentos: el
   agente corregirá y actualizará el PR) o **Approve** + merge. Rechazar
   bien documentado puntúa igual que aprobar bien documentado.

## Paso 4 · Los encargos, en orden

| # | Encargo | Aviso |
|---|---|---|
| 1 | ABC por margen (`encargos/01`) | Antes de mergear: recalculad a mano el margen de 2–3 referencias |
| 2 | XYZ (`encargos/02`) | El punto 3 del checklist, con especial cariño |
| 3 | Matriz + políticas (`encargos/03`) | Cruzad a mano la celda de vuestras referencias de muestra |
| 4 | KPIs para el comité (`encargos/04`) | Pasad el checklist ENTERO antes de opinar. Entero. |
| 5 | El escaparate (`encargos/05`) | Ver paso 5 |

Los encargos 1→3 son secuenciales (cada uno usa el resultado del anterior:
mergead antes de encargar el siguiente). El 4 y el 5 pueden ir en paralelo.

## Paso 5 · Vercel: de repo a producto con URL (15')

Cuando el PR del encargo 5 esté mergeado:

1. vercel.com → **Continue with GitHub** (plan Hobby, gratis).
2. **Add New… → Project** → *Import* vuestro repo.
3. Framework Preset: **Other** · sin build command · Deploy.
4. En ~1 minuto tenéis URL pública (`zeta-wear-equipoNN.vercel.app`).
   Abridla en el móvil: ¿se ve la matriz? ¿el clic funciona? ¿los avisos
   AZ/AY dicen lo mismo que vuestro `clasificacion.csv`?
5. Bonus: desde ahora, **cada merge redespliega solo**. Eso también es
   la sesión de hoy: integración continua de verdad.

## Paso 6 · El memo final (con Gemini como redactor auditado)

1. En gemini.google.com, pegad vuestro `clasificacion.csv` **ya validado** y
   pedid: *«Redacta un memo de 5 líneas al director de operaciones: qué 5
   referencias merecen más atención de gestión y por qué, citando la celda
   de la matriz y una cifra en euros de estos datos. Solo con estos datos.»*
2. **Auditad el borrador**: ¿cita alguna cifra que NO esté en vuestros
   resultados? ¿algún "benchmark del sector" de la nada? Corregidlo.
3. Versión final en `resultados/memo.md` (podéis subirla desde el editor web
   de GitHub) con la URL de Vercel al pie y los nombres del equipo.

## Qué se entrega y qué se evalúa

**Entrega (URL del repo en la tarea del campus):** los PRs con vuestras
reviews visibles, `resultados/` completo, `resultados/memo.md` y la URL de
Vercel.

**Se evalúa vuestra AUDITORÍA, no el código del agente:** calidad de los
issues, reviews con comentarios técnicos en líneas concretas, decisiones
merge/reject argumentadas, el memo (celda + cifra, sin datos inventados) y
la comparación final: ¿qué cazasteis vosotros que la IA revisora no vio?

## Si algo falla

- **Cuota del agente agotada / servicio caído** → cambiad de opción del menú
  del paso 2, o haced la auditoría del PR congelado: `planB/REVISION_SIN_AGENTE.md`.
- **El agente dice que le faltan datos** → bien por él. ¿Seguro que el dato
  existe en el repo? Esa respuesta también se documenta en el PR.
- **CI en rojo** → pestaña *Actions*, leed el log: dice exactamente qué
  estructura esperaba.
- **Vercel enseña el README en vez del dashboard** → falta `index.html` en
  la raíz del repo.
- **El dashboard no carga el CSV** → el fetch debe usar ruta relativa
  (`resultados/clasificacion.csv`, sin barra inicial).
- **Cualquier otra duda** → preguntad al profesor, en clase o por el foro
  del campus. Preguntar pronto es más barato que mergear mal.
