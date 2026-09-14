---
name: variaciones-estaticos-meta
description: Hace VARIACIONES de un estático de Meta que ya existe, en vez de crear uno desde cero. Dirección pasa la pieza de referencia y la skill devuelve variaciones claras del MISMO formato y el MISMO ángulo, cambiando todo lo demás — fondo, foto, composición, redacción. Skill INDEPENDIENTE: tiene sus propios parámetros, audits, referencias visuales, plantillas y copys, copiados de `estaticos-meta` pero separados, para que las dos evolucionen sin pisarse. ⛔ La IA RECREA una persona real que se le adjunta, NUNCA inventa una cara ni un escenario de cero: siempre hay una imagen real debajo (material del cliente o stock gratuito). ⛔ NO se usa ante FATIGA de un anuncio: cuando la frecuencia 7d pasa de 3,0 lo que entra es un CONCEPTO DISTINTO y eso lo hace `estaticos-meta` — más variaciones del mismo ángulo cuentan como una sola apuesta y no abren público nuevo. Usar cuando Dirección diga "haz variaciones de este estático", "más versiones de este ad", "varía este creativo", o pase una pieza que RINDE y pida otras con el mismo ángulo. MODO RÁPIDO: Dirección puede pasar el brief, la guía y las piezas a variar en orden; se validan con `preparar_tanda.py`, la preproducción y la auditoría van en agentes aparte, cada variación en su pestaña, y a Drive solo se entra al final con `cerrar_tanda.py`.
---

# Variaciones de un estático que ya funciona

Esto **no crea conceptos nuevos**: coge una pieza que ya existe y saca versiones distintas del
**mismo ángulo**. Para crear desde cero está `estaticos-meta`; si Dirección no pasa una pieza de
referencia, esta skill **no aplica**.

## Cuándo se usa esta skill — y cuándo NO (Consejo, 11-09-2026)

> ⛔ **NO se usa ante FATIGA.** Antes esta skill decía ser «lo que pide `gestion-cuenta-meta` cuando un
> anuncio muere por fatiga». **Era falso y contradecía la doctrina de la casa.** Ante fatiga —frecuencia
> 7d > 3,0 con CTR cayendo y CPL subiendo— lo que entra es **un CONCEPTO DISTINTO**, otro ángulo u otro
> formato, y eso lo hace `estaticos-meta`. El ángulo agotó su bolsillo de audiencia: **más variaciones
> del mismo ángulo no abren público nuevo** — Meta las agrupa y cuentan como **una sola apuesta**
> (`../gestion-cuenta-meta/references/parametros-campana.md` §9 y §9-bis).

**Se usa en DOS casos, y en ninguno más — y OJO, porque producen cosas DISTINTAS.** Antes los dos
caían en el mismo flujo (3 variaciones cambiándolo todo), que es justo lo que el caso B desautoriza:

| | **A · Dirección lo pide** | **B · La pieza NUNCA funcionó** |
|---|---|---|
| **Señal** | te lo pide y ya | CTR único **< 0,6 %**, o **3× el CPL objetivo con cero leads**, **sin haber funcionado nunca** |
| **Autoridad** | `../funnel/SKILL.md` (tabla de disparadores): «a petición de Dirección y **solo sobre una pieza que rinde**» | `../gestion-cuenta-meta/references/parametros-campana.md` **§9-bis** (07-09-2026) |
| **Qué pieza se varía** | **la que pasa Dirección** | ⚠️ **NO la que falló: el GANADOR histórico de la cuenta.** La pieza que falló es solo la señal que dispara |
| **Cuántas salen** | **3** | **1** (2 como mucho) |
| **Qué cambia** | foto + composición + estructura del titular + reparto del texto (§«Lo que SÍ cambia») | **UN SOLO elemento: el titular O la foto. No los dos** |
| **Prueba de los 200 px** | **sí**, obligatoria: si no se distinguen, se rehace | **NO aplica.** Aquí parecerse al ganador es el objetivo, no el defecto. Se comprueba lo contrario: que **no** se haya ido de territorio |
| **Checks V** | los cinco (V-1 a V-5) | **V-2 (ángulo) y V-3 (imagen real) sí; V-1, V-4 y V-5 NO** — están escritos para la tanda de 3 |

**Por qué «un solo elemento» en el caso B y no tres variaciones cambiándolo todo.** El dato de la casa
—iterar sobre un ganador acierta ~25 % frente al ~10 % de un concepto nuevo
(`../gestion-cuenta-meta/SKILL.md` §6)— está medido sobre la **iteración mínima**. Cambiarlo todo menos
el ángulo se parece más a un concepto nuevo disfrazado: te comes el coste de producir tres piezas y la
tasa de acierto del concepto nuevo, sin la ventaja de abrir público.

**Y en el caso A, tres variaciones NO son tres apuestas.** Comparten ángulo, así que para Meta son
**una sola** (`parametros-campana.md §9`). Eso significa dos cosas prácticas: (1) las tres ocupan huecos
del conjunto (**3-5 anuncios activos**, `../gestion-cuenta-meta/SKILL.md §4`) comprando una sola
decisión, así que **no se suben las tres a la vez si eso deja el conjunto sin conceptos distintos** —lo
decide `armar-campana-meta`, no esta skill—; y (2) la diferencia de CPL entre las tres hermanas en un
presupuesto pequeño es **varianza, no señal**: no se declara ganadora a una sobre otra sin el volumen que
pide la puerta de datos (3× TCPL).

**Comprobación antes de producir, en los DOS casos:** mirar la **frecuencia 7d real** de la pieza que se
va a variar.
- **Cómo se mira:** con el MCP de Meta en solo lectura (`ads_get_ad_entities` / las herramientas
  `ads_insights_*`), o pidiéndole el dato a `gestion-cuenta-meta`, que es la skill que lee la cuenta.
- **Si está por encima de 3,0 en prospección (o 5,0 en retargeting):** esta skill **no es la
  herramienta** —el ángulo agotó su bolsillo— y se manda a `estaticos-meta` a por un concepto nuevo.
- **Si el dato no se puede obtener** (la pieza ya no corre, la cuenta no responde, Dirección la pasó sin
  contexto): **no se para la tanda**. Se produce, se anota «frecuencia no disponible» en el specs y se
  dice en el resumen final. Lo que no se hace es inventarse el número.
- **Si Dirección lo pide sabiendo que está fatigada:** se hace —es su decisión— y se le dice en el resumen
  que la pieza madre estaba fatigada y que esto no abre público nuevo.

## Esta skill es INDEPENDIENTE

Tiene **sus propios** parámetros, audits, referencias visuales, plantillas y copys. No lee nada de
`estaticos-meta`: las dos se pueden tocar por separado sin pisarse.

Lo único compartido es `fundamentos-copy` —Ogilvy, Schwartz, el panel y el compliance de Meta—,
que es la base común de todas las skills de la casa y va instalada al lado.

| Qué | Dónde |
|---|---|
| Los 9 formatos y su spec visual (+ la §10 «Tres pasos», que está **fuera** de la secuencia) | `references/formatos-visual-spec.md` |
| **Parámetros de COPY (fuente única)** | `references/parametros-copy.md` |
| Audit de copy por formato | `references/audit-copy-por-formato.md` |
| Audit visual y severidades | `references/audit-playbook-b2b.md` · `references/audit-rules.json` |
| Auto-QC (§0 juicio de DC + §G checklist visual) | `references/calidad-y-autoqc.md` |
| Zonas seguras y reglas técnicas | `references/reglas-tecnicas-y-copy.md` |
| Anti-patrones y compliance | `../fundamentos-copy/references/lo-que-no-funciona.md` |
| Ogilvy, Schwartz, titulares, panel | `../fundamentos-copy/references/` |
| Referencias visuales reales (94 piezas) | `references/refs/` |
| Plantillas de montaje y render | `templates/` |
| Medir safe zones | `scripts/zonas_seguras.py` |
| Errores ya cometidos | `references/errores-y-aprendizajes.md` |
| Qué convierte de verdad (ranking por leads y CPL) | `references/estaticos-ganadores.md` — **se abre al leer la pieza de referencia**: si la original es de un ángulo que ya rinde, ahí está el dato |
| Arquetipos B2B (⚠️ **consulta, no doctrina**) | `references/informe-b2b-100-reglas.md` · `references/informe-b2b-enciclopedia.md` — **no se ejecuta nada de ahí**; solo el catálogo de arquetipos, y solo si el cliente es B2B de verdad |

⚠️ **Los references son la copia AL DÍA de los de `estaticos-meta`** (sincronizada el 11-09-2026),
con un aviso arriba que dice lo único que cambia: allí son 9 piezas nuevas, aquí 3 variaciones de una
que ya existe. **El motor es el MISMO** —se genera con el GPT adjuntándole la imagen real, bajo
«recrear sí, inventar no»—, así que `references/prompts-gpt.md`, `references/produccion-render.md` y `references/chrome-rapido.md`
**SÍ se usan aquí**: son el manual del motor.
> Antes este bloque decía que esos tres «no se usan» y que la pieza se montaba solo con las
> plantillas HTML. Era inviable: entonces **solo había plantilla de 2 de los 9 formatos**, así que 7 de
> cada 9 variaciones no se podían entregar. Con el GPT se entregan los 9, y las plantillas quedan como
> plan B igual que en la skill hermana — **hoy ya cubren los 9 formatos** (ver §3).

**Qué se lee en cada fase** (no se leen todos de golpe):

| Fase | Qué abrir |
|---|---|
| 1 · leer la pieza | `references/formatos-visual-spec.md` (identificar el formato) |
| 2 · material | el manifiesto de `preparar_tanda.py` y la preproducción (§MODO RÁPIDO). Drive solo si no se pasó nada (`--drive`) |
| 3 · generar | `references/prompts-gpt.md` (recipe y CAMBIOS-tipo) · `references/chrome-rapido.md` (manejar Chrome) · `references/reglas-tecnicas-y-copy.md` · la ficha del formato en `references/formatos-visual-spec.md` |
| 4 · auditar | **`references/parametros-copy.md`** (los números de copy) · `references/calidad-y-autoqc.md` (§0 + §G + los checks V) · `references/audit-copy-por-formato.md` · `references/audit-rules.json` · **`../fundamentos-copy/references/lo-que-no-funciona.md`** (compliance: Atributos Personales es la causa nº 1 de desaprobación, y las categorías especiales — vivienda y crédito — afectan a media cartera) · **`../fundamentos-copy/references/ogilvy-reglas-reales.md`** (los 16 checks O1-O16) · `../fundamentos-copy/references/panel-expertos.md` |
| siempre | `references/errores-y-aprendizajes.md` **antes de empezar**, y se le añade una entrada cada vez que Dirección corrija algo |

## ⚡ MODO RÁPIDO — el recorrido por defecto (consejo + Dirección, 13-09-2026)

Dirección: *«si le paso el brief, la guía y los estáticos a variar en orden, que no entre a Drive al
principio: solo al final, a subir»*. Conclusión del consejo, que manda sobre cómo se ejecuta todo lo de
abajo: **un solo agente (tú) es el dueño de Chrome**; todo lo que no necesita navegador sale del hilo y
corre a la vez en agentes **sin herramientas de Chrome** (`~/.claude/agents/`); Drive solo al final; y
cada tanda se cronometra. Scripts en `~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/` (`EC/`).

| Momento | Qué se hace |
|---|---|
| **T0 · 1 llamada** | `python3 EC/preparar_tanda.py "<C>" --modo variaciones --variar <pieza1> <pieza2>… [--logo …] [--guia …] [--brief …] [--desde …]` — las piezas a variar quedan en `Insumos/variar/01_…`, `02_…` **en el orden en que Dirección las pasó**. Exit 1 (falta la pieza, el brief o el logo) = no se abre Chrome. Sin material y con `Insumos/` vacío → `--drive` |
| **T0 · a la vez, en segundo plano** | Agente **`preproduccion-estaticos`** en modo `variaciones`: la **ficha «PIEZA DE REFERENCIA»** de cada pieza, claims permitidos con cita, paleta/tipos, compliance → `Insumos/preproduccion_Tanda<N>.md`. Agente **`auditor-estaticos`** con el ARRANQUE. Si hace falta stock para alguna variación, **`casting-estaticos`** |
| **T0 · a la vez, tú** | Frecuencia 7d de las piezas madre (MCP de Meta, solo lectura) · cuenta de ChatGPT + Mensaje 1 en **una pestaña por variación** (`references/chrome-rapido.md` §6) |
| **T1** | Llega la preproducción: si una ficha dice `ÁNGULO DUDOSO`, esa es la única pregunta a Dirección y **solo esa pieza espera**; las demás siguen. Mensaje 2 en cada pestaña |
| **Por imagen** | Esperar y descargar en una llamada (`chrome-rapido.md` §5), **con el nombre `Madre<m>_VAR<v>_<formato>_<angulo>_v<ronda>_<ratio>.png`** (§5 «Naming del fichero») → `recoger_png.py … --pieza Madre<m>_VAR<v> --ronda <k> --skill variaciones-estaticos-meta` → mirada rápida tuya (cara inventada, formato o ángulo cambiado, logo roto) → `SendMessage` al auditor **y a la vez** pides el 9:16 de esa variación. Si el 1:1 vuelve con `CAMBIOS`, el 9:16 en curso se tira y se pega el `CAMBIOS_PARA_GPT` del auditor |
| **Cierre de variación** | Los dos ratios en `PASA` → `SendMessage` pidiendo `PANEL` y la **prueba de los 200 px** con las hermanas ya aprobadas → línea en `PROGRESO` |
| **Final · en segundo plano** | `python3 EC/cerrar_tanda.py "<C>" --tanda N` con `run_in_background` (número de tanda definitivo contra Drive, sube solo las piezas registradas de ESTA tanda y en su última versión —las viejas no se resuben—, avisa si a una variación le falta el 1:1 o el 9:16, specs, verificación, logo) · `python3 EC/cronometro_tanda.py "<C>" N resumen` |

- El auditor se lanza **una vez** (`Agent`, `subagent_type: "auditor-estaticos"`, en segundo plano) y cada
  imagen va por **`SendMessage` al mismo agente**: así recuerda la madre y las hermanas, que es lo que
  exige la prueba de los 200 px y los checks V. Su última línea es `VEREDICTO <X> · <fichero>`.
- ⛔ **Lo que no se adelanta nunca:** dar por buena, renombrar sin `_PEND` o subir una variación sin
  veredicto entero y panel. Si el auditor no responde, se relanza con el ARRANQUE y mientras tanto se
  audita tú esa pieza, entera.
- Marcas de tiempo a mano: `python3 EC/cronometro_tanda.py "<C>" N marca gpt_envio|cambios --pieza Madre<m>_VAR<v>`.

## ⛔ RECREAR SÍ, INVENTAR NO (Dirección, 11-09-2026 · precisado el 11-09 tras la auditoría)

La regla empezó siendo «nada de IA para personas ni fondos» y **así estaba mal planteada**: la tanda
normal de `estaticos-meta` genera las 9 piezas con el GPT recreando una persona real que le
adjuntamos, y si una cara generada fuera inaceptable, lo sería también allí. La regla, en su forma
buena, es la misma para las dos skills:

| | |
|---|---|
| ✅ **RECREAR** | El GPT puede redibujar una **persona real que le adjuntamos** —material del cliente o una foto de stock que hemos elegido— manteniendo su rostro, pelo, gafas y edad. Detrás de esa cara hay una persona de verdad y una escena de verdad |
| ✅ **TRATAR** | Recortar, extender un fondo liso, limpiar un elemento que molesta, reencuadrar |
| ⛔ **INVENTAR** | Una cara que no existe, una persona «de ejemplo», un equipo de gente generado de cero. Si el GPT devuelve una cara que no se parece a la referencia, **ha inventado una persona → REGENERATE re-adjuntando la foto** |
| ⛔ **GENERAR EL ESCENARIO DE CERO** | Un fondo, un local, una obra o un producto que no existe en ningún sitio. El fondo sale de una imagen real (del cliente o de stock) y el GPT lo recompone, no lo imagina |

**La frontera, en una frase: tiene que haber una imagen real debajo.** Sin foto adjunta no se genera:
el condicionamiento visual **no se arrastra entre turnos**, así que la foto se re-adjunta en CADA
mensaje (1:1, 9:16 y cada CAMBIOS) o el modelo inventa una cara — es el fallo real que dio origen a
la regla.

**Orden de dónde sale esa imagen real** (no cambia):

| Orden | De dónde sale la imagen |
|---|---|
| **1º** | **Material del cliente**: su Drive, sus fotos, su obra, su producto, su equipo, su local |
| **2º** | **Capturas hechas ahora**: su web, su panel, su ficha de Google, sus reseñas |
| **3º** | **Pedírselo a Dirección** — casi siempre hay material que no nos han dado. Se pide en el resumen, **sin parar la tanda** (ver §2) |
| **4º** | **Stock gratuito real** (foto de verdad, con su licencia): Pexels, Unsplash, Pixabay. Se anota **fuente e id** de cada foto |

La razón no es estética: una cara **inventada** en un anuncio de un negocio real es un problema de
credibilidad y, en algunos mercados, de compliance. Y se nota. Una cara **recreada a partir de una
persona real** es el flujo normal de la casa y pasa el audit (`references/calidad-y-autoqc.md §0`).

> ⚠️ **Límite legal que la skill NO resuelve y hay que tener presente:** Pexels, Unsplash y Pixabay
> **no dan derechos para sugerir que la persona de la foto respalda el servicio.** Un Testimonio con
> cara de stock, nombre y cita es justo eso. Mientras la cita sea provisional y lleve `[REEMPLAZAR]`
> quemado en el PNG la pieza no se publica, así que no llega a pasar — pero **una pieza con cara de
> stock y testimonio no sale a campaña sin cara y autorización del cliente real.**

## Lo que NO cambia entre variaciones

Es lo que hace que sea una variación y no otro anuncio:

- **El ÁNGULO.** El dolor, el miedo o la promesa con la que entra. Si cambia el ángulo, ya no es
  una variación: es una pieza nueva y va por `estaticos-meta`.
- **El FORMATO.** Si la referencia es Review+Claim, todas son Review+Claim. Si es Antes/Después,
  todas Antes/Después.
  > ⚠️ **«Testimonio» NO es uno de los 9 formatos, aunque sea la pieza que más produce la casa** — y la
  > ficha-contrato de §1 (más abajo) obliga a poner uno de los 9. Tabla de equivalencias, porque si no la ficha-contrato
  > no se puede rellenar justo con la pieza más común:
  >
  > | Lo que se dice a diario | Formato real de los 9 |
  > |---|---|
  > | **Testimonio** (cita + cara + nombre + ★) | **3 · Review+Claim** — manda la voz del cliente |
  > | **Testimonio de cifra** («+1000 ya han…») | **8 · Prueba social (Stat Drop)** — manda el número |
  > | **Antes/Después**, X vs ✓ | **2 · Antes/Después** |
  > | **Editorial / Advertorial** | **1 · Artículo/Noticia** |
  > | **3 pasos / «cómo funciona»** | **fuera de los 9** → se resuelve dentro de **4 · Característica→Beneficio** con sus 3 checks redactados como pasos (`references/formatos-visual-spec.md §10`) |
  >
  > La plantilla se llama `templates/testimonio.html` por historia: es la del formato **3 · Review+Claim**.
- **El avatar** al que le habla.
- **La promesa** y el **CTA**.

## Lo que SÍ cambia, y tiene que cambiar de verdad

Una variación que solo cambia dos palabras no sirve: Meta la lee como la misma pieza y no abre
público nuevo.

| | Cómo cambia |
|---|---|
| **Fondo / foto** | **distinto SIEMPRE**. Nunca dos variaciones con la misma imagen |
| **Composición** | dónde va el texto, el peso visual, el encuadre |
| **Titular** | misma idea, **otra estructura**: si la original es pregunta, esta afirma; si es cifra, esta es consecuencia; si es negación, esta es promesa. **No vale cambiar sinónimos** |
| **Prueba** | otro testimonio, otra cifra u otro detalle real. **Si no hay más pruebas reales, se repite la misma**: nunca se inventa una para variar |
| **Paleta** | dentro de la marca: cambia **qué elemento lleva el acento** (titular / CTA / fondo), no los colores de la marca |

**La prueba para saber si una variación vale:** ponlas juntas a **200 px de ancho** y mira 2
segundos. Si a ese tamaño no distingues cuál es cuál, **no es una variación**: se rehace. Es
subjetiva a propósito —no hay métrica para esto—, pero se hace **siempre y con las tres juntas**,
no de memoria.

## Flujo

### 1. Leer la pieza de referencia

**Qué acepta como referencia**, por orden de preferencia:
1. El **PNG o JPG** del estático (lo ideal: se ve todo).
2. Una **captura de pantalla** del anuncio.
3. El **enlace a la carpeta del Drive** donde está.
4. El **enlace de la Biblioteca de Anuncios de Meta**.

Si lo que llega no permite leer el titular y ver la imagen, **se pide otra vez**. No se trabaja
sobre una referencia que no se ve.

**Antes de nada se rellena esta ficha**, que es el contrato de lo intocable:

```
PIEZA DE REFERENCIA
  Cliente:
  Formato (1 de los 9 — ver la tabla de equivalencias de abajo):
  Ángulo (el dolor/miedo/promesa con el que entra):
  Avatar (a quién le habla):
  Promesa:
  CTA:
  Prueba que usa (testimonio / cifra / antes-después / ninguna):
  Imagen que usa (qué se ve):
  ¿Rinde? (CPL y leads, si se saben):
  → Y con ese dato se DECIDE: sin rendimiento conocido, ¿por qué esta pieza y no otra?
```

**Si el ángulo no queda claro, se pregunta a Dirección — y esta es la ÚNICA pregunta que hace esta skill.**
No se deduce: una variación con otro ángulo ensucia el test y no se nota hasta que los números no
cuadran. Todo lo demás va solo: la auditoría es interna, no se narra pieza por pieza ni se piden
aprobaciones (`references/calidad-y-autoqc.md §F`). La otra compuerta humana del funnel es activar la
campaña, y eso es de otra skill.

**PARA QUÉ SE PIDE EL RENDIMIENTO (y por qué antes sobraba).** La ficha recogía «¿Rinde? (CPL y
leads)» y ese dato no volvía a aparecer: se pedía lo único que justifica variar y se tiraba. Su uso:
- **Se varía lo que FUNCIONA.** Si la pieza no tiene leads, variarla multiplica una ejecución que no
  ha demostrado nada: se dice y se propone variar la que sí rinde.
- **Va anotado en `specs_Tanda<N>.md`** (CPL y leads de la original), que es el único sitio donde
  después se puede comparar si las variaciones batieron a su madre.
- **Si Dirección pasa la pieza sin el dato, se trabaja igual** —no se para por esto— y se anota «sin
  rendimiento conocido» en el specs.

**Si la pieza es de otro cliente** —una referencia de la competencia o de otra cuenta—, se avisa
y se para: esta skill varía piezas **del cliente**, no copia las de otros.

### 2. Reunir material real

> ⚡ **Primero lo que ya hay en local** (13-09-2026): el manifiesto de `preparar_tanda.py` lista las fotos,
> personas y reseñas que pasó Dirección o que ya estaban en `Insumos/`. **Solo si con eso no salen las
> imágenes distintas que hacen falta** se mira el Drive, con la tabla de abajo. El paso 3 de esta tabla
> (`2. Ads/`, para no repetir imagen) se resuelve con la copia local `Ads/GPT/`; Drive, solo si está vacía.

**Dónde se mira, en este orden y con estas rutas:**

| | Dónde |
|---|---|
| 1 | `1. Branding` del Drive del cliente — logo, paleta, tipografías |
| 2 | Sus carpetas de fotos y vídeos: obra, producto, equipo, local, antes/después |
| 3 | `2. Ads/` — lo que ya se usó, para **no repetirlo** |
| 4 | Capturas hechas ahora de su web, su panel o su ficha de Google |

**Hacen falta 3 imágenes distintas, una por variación.** Si no salen del material del cliente:

1. Se le pide a Dirección **con la lista concreta** de lo que falta, no «mándame fotos».
2. Se avisa (**`--cliente` es obligatorio**: sin él `avisar.py` sale con error y el correo no se manda —
   es como estaba escrito antes y por eso el material no se pedía nunca):
   ```bash
   python3 ~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/avisar.py \
       --cliente "<Cliente>" --nivel aviso \
       --asunto "Faltan fotos para las variaciones de <Cliente>" --cuerpo "<la lista concreta>"
   ```
3. **Se para SOLO esa variación, no la tanda.** Se hacen las que sí tengan imagen, se anota la que
   falta en `specs_Tanda<N>.md` y se cuenta **una sola vez, al final** — nunca se interrumpe a
   mitad para preguntar (`references/calidad-y-autoqc.md §F`). Lo que no se hace es rellenar con stock
   genérico ni inventar la escena con IA para no frenar la entrega.

Solo cuando de verdad no hay material propio para una escena concreta se va a **stock gratuito**
(Pexels, Unsplash, Pixabay), y **se anota la fuente y el id** de cada foto.

### 3. Generar cada variación

**Con el GPT «Generador Ads Imagen» vía Claude-in-Chrome, igual que la skill hermana** — recipe exacto
en `references/prompts-gpt.md`, manejo del navegador en `references/chrome-rapido.md`, cuenta y
comprobación de sesión en `references/produccion-render.md §4` (**siempre `<correo-cuenta-de-trabajo>`**,
nunca `<correo-direccion>`).

> ### ⛔ EL PRIMER MENSAJE AL GPT NO LLEVA ADJUNTOS (Dirección, 11-09-2026)
> La pantalla de bienvenida del GPT trae la sugerencia **«Pídeme brief, referencias visuales y
> ángulo…»**. **Ese es el Mensaje 1 y va SOLO**, sin la pieza de referencia, sin el logo y sin las
> fotos. Se toca, se envía, el GPT contesta pidiendo lo que necesita, y **todo se adjunta en el
> Mensaje 2**. En la bienvenida el chat aún no está activo y el `input` de fichero puede ni existir:
> ahí es donde una subida falla en silencio y sale una pieza construida sobre nada. Si la sugerencia
> no aparece, se escribe a mano lo mismo, sin adjuntos. `references/chrome-rapido.md` §0.

Lo que cambia respecto a la tanda de 9 es **el mensaje**, no el motor:

1. **En el Mensaje 2 se adjunta el 1:1 de la pieza ORIGINAL**, además del logo oficial y la foto real de esta variación,
   y se le dice qué queda congelado: *«misma estructura de formato, mismo ángulo, mismo avatar, misma
   promesa y mismo CTA que la pieza adjunta. Cambia la foto, la composición, el reparto del texto y la
   estructura del titular.»*
2. **La foto real va adjunta en CADA mensaje** (1:1, 9:16 y cada CAMBIOS): el condicionamiento visual
   no se arrastra entre turnos y sin ella el modelo **inventa** una cara, que es lo único prohibido.
3. **Un titular con otra estructura, no sinónimos**: si la original pregunta, esta afirma; si da cifra,
   esta da consecuencia. Mismo ángulo, otra entrada.
4. **Los dos ratios, en pasos** (1:1 → 9:16 nativo re-adjuntando el 1:1 aprobado), con los márgenes del
   ratio que toque: 1:1 **54 px**; 9:16 **270 arriba / 384 abajo / 107 a los lados**. Siempre en
   píxeles, y **un solo juego de números por mensaje**.
5. **NORMALIZAR el PNG en cuanto se descarga, ANTES de auditarlo** — este paso iba en §5 y era un
   error de orden con consecuencia: el GPT no entrega 1080 (en la tanda real salieron a **1254 y 941**)
   y `zonas_seguras.py` **no mide nada que no sea 1080×1080 o 1080×1920**: devolvía «no medida» y la
   compuerta dura no llegaba a medir NUNCA.
   ```bash
   python3 ~/.claude/skills/variaciones-estaticos-meta/scripts/normalizar_png.py <carpeta de la tanda>/
   ```
   Y se normaliza **con este script, nunca con PIL a pelo**: el escalado normal se lleva la credencial
   C2PA y convierte la declaración de IA en manual (§«`_PEND` y la DECLARACIÓN DE IA»).
6. **Auditar en cuanto esté normalizada cada imagen**, antes de pedir nada más (§4).

**Plan B — plantillas HTML** (`templates/` + `templates/render.py`), igual que en la hermana. Es el plan
B, no el estándar: se usa si el GPT o la cuenta no están disponibles.
- ✅ **Cubre ya los 9 formatos** con 6 plantillas (`references/produccion-render.md §6`): `testimonio` (3),
  `antes-despues` (2), `editorial` (1), `titular-lista` (4·7·9), `dos-bloques` (5·6) y `numero` (8).
  **Recomponen por ratio**: en 9:16 aplican el patrón de la casa (texto arriba, foto a sangre abajo);
  en 1:1 el margen de 54 px. **Nunca se cambia de formato porque no haya plantilla:** el formato lo
  manda la pieza de referencia.
- `templates/render.py` **falla si falta un token** y **avisa si `LOGO_SRC` viene vacío** (el logo va como imagen,
  nunca recompuesto con tipografía) y si no hay red para las tipografías de marca.
- ⚠️ **El plan B no produce credencial C2PA**: una pieza montada con plantilla no la lleva nunca, así
  que su `IA declarada` es **MANUAL PENDIENTE** salvo que la foto de fondo viniese del GPT. No es un
  fallo del script: la genera el modelo, no el render.

### 4. Auditar cada una

Sin rebajas, y en este orden:

- **§0 JUICIO DE DIRECTOR CREATIVO + §G checklist visual** de `references/calidad-y-autoqc.md`, enteros.
  > **No hay "Ad Score" numérico.** La métrica estaba derogada en `estaticos-meta` y aquí seguía viva
  > con un corte en 85 — pero la rúbrica de 10 dimensiones vive en `references/informe-b2b-enciclopedia.md`, que
  > ninguna fase abre, **3 de sus 10 dimensiones son B2B puro** (software, logos de clientes, escala
  > corporativa) y por tanto inalcanzables para Cliente 13 o un tatuador, y el umbral superior del
  > informe está **físicamente en blanco** («Puntuación Puntos: APROBADO PARA ESCALA») porque se perdió
  > al extraer el .docx. Un corte de 85 sobre 70 puntos alcanzables no es un umbral, es un bloqueo.
  > Lo que decide es pasar §0 + §G + los audits + el panel.
- **EL COPY, con el `references/calidad-y-autoqc.md §H` entero** — es un checklist propio, no una línea: los **16 checks de Ogilvy** con sus severidades (`../fundamentos-copy/references/ogilvy-reglas-reales.md`) · el **titular contra `../fundamentos-copy/references/headlines-playbook.md`** (de qué tipo es de los 7, si respeta su límite de caracteres, y sus 6 puntos) · el **audit del formato** en `references/audit-copy-por-formato.md` · **Schwartz sobre la pieza terminada**. 
  - En variaciones hay un check extra que solo aplica aquí: **el titular tiene que cambiar de ESTRUCTURA, no de sinónimos** (si el original pregunta, este afirma; si da cifra, este da consecuencia) **manteniendo el ángulo**. Un titular reformulado con las mismas palabras en otro orden no abre público nuevo: es la misma pieza para Meta.
- **Compliance de Meta** (`../fundamentos-copy/references/lo-que-no-funciona.md`) — **no estaba en
  ninguna fase y es lo que tumba cuentas.** Dos reglas que importan especialmente al VARIAR, porque
  una variación **propaga el patrón de riesgo del ganador** sin que nadie lo vuelva a mirar:
  - **Atributos Personales** (la causa nº 1 de desaprobación): el hook no puede dar por hecho un
    atributo del lector. Los hooks modelo de la casa son justo eso — «¿Te atracas… y después te odias
    por ello?» (`references/patrones-diseno-estaticos.md`) vive al filo. Si la original pasó, la
    variación **no hereda el permiso**: se revisa igual.
  - **Categoría especial** (vivienda, crédito, empleo): media cartera es inmobiliaria. Si la pieza
    original iba declarada, la variación también.
- **Zonas seguras MEDIDAS** con `scripts/zonas_seguras.py`, en **los dos ratios** (mide 1:1 y 9:16):
  ```bash
  python3 ~/.claude/skills/variaciones-estaticos-meta/scripts/zonas_seguras.py <carpeta de la tanda>/
  ```
  Tres veredictos y sale con código 1 si alguno no es «limpia». **1:1 → los 4 bordes se dictaminan
  (54 px). 9:16 → arriba (270) el veredicto vale; abajo (384) hay que MIRAR con `--marcar`**, porque el
  patrón de la casa es foto a sangre por abajo y eso no es invasión si no es texto/logo/CTA. Laterales:
  objetivo 107 px, mínimo duro 65. Detalle: `references/calidad-y-autoqc.md §A-sexies`.
- **Los 5 checks V** de `references/calidad-y-autoqc.md` (son **cinco, V-1 a V-5**; no hay V-6 aunque
  `../fundamentos-copy/references/panel-expertos.md` lo dijera): que sea una variación de verdad, que respete el ángulo, que haya una
  **imagen real debajo con su fuente anotada**, que no se repita ninguna imagen **entre variaciones**
  —el 1:1 y el 9:16 de la misma variación sí comparten foto, a propósito— y que el fondo cambie.
- **Panel de expertos**: todas ≥7 y media ≥8.
- **La prueba de la miniatura**, contra la original y contra las otras dos.

**El bucle tiene tope: ~3-4 iteraciones por pieza** (`references/calidad-y-autoqc.md §F`, punto 6). Al
agotarlo **no se sigue regenerando**: se guarda el mejor intento con **`_PEND`**, se anota en el specs qué
quedó pendiente y se cuenta en el resumen final. Sin ese tope el bucle no tiene suelo — y cada
regeneración aleja la variación de la pieza madre, que es justo lo que NO debe cambiar.

### ⛔ FRENO DE EMERGENCIA — la única vez que se para y se espera (consejo, 11-09-2026)

El bucle de auto-QC se corrige solo y **no tiene suelo**: si el modelo se autoconvence, no hay ningún
punto del sistema donde eso salga a la luz. Faltaba en esta skill y sí estaba en la hermana — y aquí
hace más falta, porque una variación que se regenera muchas veces **deja de parecerse a la pieza madre**,
que es lo único que no debe cambiar.

Se **para la tanda y se manda `avisar.py --nivel urgente`** cuando pase UNA de estas:

- **las 3 variaciones acaban con `_PEND`** (con 3 piezas, que fallen todas es el sistema, no la pieza)
- una variación **agota sus 3-4 CAMBIOS dos veces**
- **la misma causa de fallo en las 3** variaciones
- **el medidor sale con código 1 en las 3** piezas de un ratio
- **el perfil de Chrome no es `<correo-cuenta-de-trabajo>`** y no se puede cambiar
- **no se consigue leer el ángulo de la pieza de referencia** (es la única pregunta que hace esta skill)

Entonces: se deja de producir (lo hecho no se tira), se avisa con qué falló y qué hace falta, se anota en
`specs_Tanda<N>.md`, se sigue con lo que no dependa de ello (subidas, specs, ESTADO.md) y **no se
reanuda hasta que Dirección conteste**. Es la ÚNICA excepción a «nunca termines el turno con trabajo
ejecutable pendiente»: aquí repetirlo daría el mismo fallo. **No dispara el freno** una variación suelta
con `_PEND` ni un CAMBIOS puntual: eso es funcionamiento normal.

### 5. Guardar y registrar

- ⛔ **Naming del fichero (Dirección, 14-09-2026): el nombre dice de qué madre sale, qué variación, qué
  formato, qué versión y qué ratio.** Antes era `VAR<n>_<formato>_<angulo>_<ratio>`: en Drive no se
  sabía de qué pieza era cada variación, y cada ronda nueva se llamaba igual que la anterior.
  ```
  Madre<m>_VAR<v>_<formato>_<angulo>_v<k>_<1x1|9x16>[_PEND].png
  Madre1_VAR1_caracteristica-beneficio_conciliar-3pasos_v1_1x1.png
  Madre1_VAR1_caracteristica-beneficio_conciliar-3pasos_v1_9x16.png
  Madre1_VAR1_caracteristica-beneficio_conciliar-3pasos_v2_1x1.png   ← ronda 2 del 1:1 (CAMBIOS)
  Madre1_VAR2_caracteristica-beneficio_conciliar-3pasos_v1_1x1.png
  Madre2_VAR1_review-claim_confianza_v1_1x1.png
  ```
  | Campo | Qué es |
  |---|---|
  | `Madre<m>` | la pieza a variar, por el orden en que Dirección la pasó (`Insumos/variar/01_…` = `Madre1`) |
  | `VAR<v>` | la variación **dentro de esa madre**: vuelve a empezar en 1 en cada madre. Es el `V<v>` del nombre del anuncio en Meta (el ángulo ya separa las madres) |
  | `<formato>` y `<angulo>` | los de la madre, en minúsculas con guiones, iguales en el fichero, el specs y Meta |
  | `v<k>` | la **versión = la ronda** (`--ronda k` de `recoger_png.py`). Cada ronda de CAMBIOS es una versión nueva: **nunca se reutiliza un nombre**; el script se niega a pisar uno que ya existe |
  | `1x1` / `9x16` | el ratio. **Cada variación se sube con los DOS**; `cerrar_tanda.py` avisa si a una le falta uno. Los dos ratios pueden ir en versiones distintas (`v2_1x1` y `v1_9x16`) |

  **Qué versión llega a Drive:** la última de cada variación y ratio. Al recoger la `v<k>`,
  `recoger_png.py` saca del registro las anteriores (se quedan en local, no se suben) y `cerrar_tanda.py`
  manda a la papelera de Drive las que se hubieran subido en un cierre anterior. Si Dirección quiere
  quedarse con dos versiones de la misma variación, se recoge con `--conservar-anteriores` y las dos
  suben con su `v1` / `v2`; la que no esté aprobada lleva `_PEND`.
- **Normalizar los dos ratios** con `scripts/normalizar_png.py` antes de guardar: el GPT no entrega 1080 (en la tanda real salieron a 1254 y 941), y el escalado normal **destruye la credencial C2PA**.
- ⚡ **Subir = `cerrar_tanda.py` en segundo plano** (13-09-2026): fija `N` contra Drive, sube solo lo
  registrado de esta tanda con su estado vivo (`_PEND` o no), sube el specs como Documento de Google y
  verifica. Lo de abajo es lo que hace por dentro, por si hay que hacerlo a mano.
- **Cómo se llega al Drive, que el cuerpo de esta skill no lo decía:** no está montado como carpeta, se
  usa con **`rclone`** (remoto `gdrive:`). Listar para saber qué `N` toca y subir:
  ```bash
  rclone lsd "gdrive:i_<C>/c_<C>/2. Ads/Estáticos/GPT/"        # ¿qué Tandas hay ya? → N = la siguiente
  rclone copy <carpeta local> "gdrive:i_<C>/c_<C>/2. Ads/Estáticos/GPT/Tanda <N>/"
  ```
  (Detalle y rutas exactas en `references/produccion-render.md §6`.) ⚠️ **Aviso con dueño:** el
  `client_id` compartido de rclone caduca durante 2026 y ese día se cae el acceso a Drive de TODAS las
  skills a la vez; lo tiene que crear Dirección en su Google Cloud.
- Los PNG en **`2. Ads/Estáticos/GPT/Tanda <N>/`** del Drive del cliente (mismo árbol que la tanda
  normal; `N` = siguiente número, listando `Tanda *`), y copia local en
  **`~/Desktop/CLIENTES/<cliente>/Ads/GPT/`** — nunca se quedan en Descargas. Con el naming de abajo.
- Un **`specs_Tanda<N>.md`** en la misma carpeta. ⚠️ **Se llama así, NO `specs_VAR_<fecha>.md`**: el
  índice lo abre `armar-campana-meta` al subir los anuncios y **solo busca ese nombre**, así que un
  `specs_VAR_` no lo lee nadie y la skill de campaña «acaba subiendo lo primero que aparece». Empieza con
  una línea que diga **`TANDA DE VARIACIONES de <pieza madre>`**, para que se sepa qué es, y lleva:
  - la **ficha de la pieza de referencia** (y en el caso B, también cuál fue la pieza que falló);
  - **por cada variación:** su **etapa de embudo** (⚠️ campo que exige `armar-campana-meta` para
    colocarla en la escalera del conjunto; sin él no puede), **concepto/ángulo** —el mismo en las tres—,
    **formato**, **avatar**, **ratios**, **fecha**, su titular, su imagen **con la fuente** («Drive del
    cliente», «captura de su web 11-09-2026», «Pexels id 1234567 (licencia)»), si la **persona es
    identificable**, su **nota del panel**, su **veredicto de COPY (§H)** y **`IA declarada`**
    (automática / MANUAL PENDIENTE);
  - el **CPL y los leads de la pieza original**, que es lo único con lo que después se puede comparar;
  - y un aviso en cabecera: **las tres comparten ángulo, así que para Meta son UNA apuesta** — que
    `armar-campana-meta` lo tenga en cuenta al elegir la mezcla de arranque.
### ⛔ `_PEND` y la DECLARACIÓN DE IA — lo que decide si la pieza puede salir (Dirección, 11-09-2026)

**1. `_PEND` en el nombre del fichero, en los DOS ratios**, siempre que la variación: lleve **cita o
testimonio provisional** (con `[REEMPLAZAR]` quemado en el PNG) · **no pase el panel** o el auto-QC y se
guarde el mejor intento · use **branding sustituido** sin validar · o tenga **cara de stock** en una
pieza que sugiere respaldo. **`armar-campana-meta` no sube nada con `_PEND`**: es el único cierre real
del camino por el que un testimonio inventado acababa publicado. Se le quita el sufijo cuando se
resuelve lo que lo puso, renombrando los dos ratios en local y en Drive.

**2. Declaración de IA (C2PA).** La imagen la genera el GPT, así que la pieza **es contenido generado
con IA y Meta exige declararlo**. Meta detecta sola las *Content Credentials* del fichero y etiqueta el
anuncio — pero **el escalado a 1080 con PIL las borra**, y entonces la declaración pasa a ser manual.
Por eso el escalado va con el script que las preserva, y el resultado se anota por pieza:
```bash
python3 ~/.claude/skills/variaciones-estaticos-meta/scripts/normalizar_png.py <carpeta de la tanda>/
```
Dice, por pieza, `IA declarada: automática (C2PA presente)` o `MANUAL PENDIENTE (sin C2PA)`. Ese campo
va al `specs_Tanda<N>.md` y lo lee `armar-campana-meta` para activar el control de divulgación al
subir el anuncio. Sin el campo se asume MANUAL PENDIENTE. En la UE, además, el Reglamento de IA (en
vigor desde agosto de 2026) va más lejos que Meta: **ante la duda, se declara.**

- **Marcar la etapa, con la ruta completa** (hay 10 copias del script en disco; sin ruta se coge la equivocada):
  ```bash
  python3 ~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/marcar_etapa.py \
      "<Cliente>" "Estáticos (tanda)" --nota "Variaciones de <pieza> — <n> piezas, <fecha>"
  ```
  ⚠️ **Es la MISMA etapa que la tanda normal, y `ETAPAS` es una lista lineal de una sola fila por
  etapa:** esta marca **sobreescribe** la fila de la tanda original en `ESTADO.md` y en la hoja del
  Drive. Por eso **la nota es obligatoria y dice que son variaciones y de qué pieza** — es lo único
  que queda de la tanda que había antes. No se inventa una etapa nueva: `marcar_etapa.py` valida
  contra la lista canónica de `estado_cliente.py` y la rechazaría.
- Si Dirección corrigió algo, **entrada en `references/errores-y-aprendizajes.md` en la misma sesión**.

## Predeterminados

Se aplican salvo que Dirección diga otra cosa:

| | Por defecto |
|---|---|
| Cuántas variaciones | **2** por pieza de referencia (rama A). Era 3 |
| | **Por qué 2 y no 3 (datos reales de la cartera, 11-09-2026 — `references/estaticos-ganadores.md`).** Un conjunto sostiene **3-5 anuncios activos** (`../gestion-cuenta-meta/SKILL.md` §2) y las variaciones **comparten ángulo = 1 sola apuesta**: con 3 ocupas 3 de 5 huecos para comprar **una** decisión; con 2 dejas 3 libres para conceptos distintos, que es lo que abre público. Y el dato que lo cierra: en la cartera **el presupuesto no llega a repartirse** — en Cliente 14 2 anuncios se llevan el **84 %** y **12 de 18 no alcanzan los 6 €**; en Cliente 03 hay piezas con **0,36 €** y **0,51 €** que nunca arrancaron. Con nuestros presupuestos, la tercera hermana **no llega a la puerta de datos (3× TCPL)**, así que no produce información: produce coste. Si Dirección pide 3, se hacen 3 |
| Tamaños | **1:1 (1080×1080) y 9:16 (1080×1920)** de cada una |
| El 9:16 | rehace el **encuadre y solo el encuadre**: botón, colores y pesos de letra idénticos al 1:1 |
| Imágenes repetidas | **cero**: cada variación con su foto |
| Idioma | **el de la pieza original**, siempre. Castellano de España por defecto (0 voseo, 0 léxico LATAM), **catalán** en Batlle/Cliente 09 e **inglés** en Cliente 07/Dubái (`references/patrones-diseno-estaticos.md` §2, punto 8 — **no «§2.8»**, que no existe). ⚠️ Ese punto 8 nombra explícitamente **solo Batlle**; Cliente 09 aparece en la tabla de §2 en la misma fila que Batlle con «idioma local», sin decir cuál. **Antes de variar una pieza de Cliente 09 se mira en qué idioma está la pieza original y se respeta**, que es la regla de todos modos; si hay duda se pregunta a Dirección en el resumen. Variar una pieza catalana y devolverla en castellano es cambiar el anuncio |
| Naming | `Madre<m>_VAR<v>_<formato>_<angulo>_v<k>_<1x1\|9x16>[_PEND].png` · **y el anuncio en Meta se llama `IMG \| <ángulo> \| V<v>`** — detalle en §5 «Naming del fichero» |
| | ⛔ **El `\| V<n>` NO es opcional y es exclusivo de esta skill.** El estándar de la casa es `IMG \| <ángulo>` (`../armar-campana-meta/SKILL.md`, naming), y funciona porque en la tanda de 9 **cada pieza tiene un ángulo distinto**. Las variaciones **comparten ángulo por definición**, así que sin el sufijo los tres anuncios salen con **el mismo nombre en Meta y el mismo `utm_content`** → no se distinguen en el informe, no se sabe cuál trajo el lead, y la promesa de esta skill («comparar si las variaciones batieron a su madre») **es imposible por construcción**. El `<angulo>` se escribe IGUAL en el fichero, en el specs y en Meta: es la clave que une la pieza con su CPL; el `V<n>` es lo que separa a las hermanas — el sufijo **`_PEND` es obligatorio** en toda pieza que no esté lista para publicar (ver abajo) |
| Si falta material real | se **pide y se para SOLO esa variación, nunca la tanda** (§2): se entregan las que sí tienen imagen, la que falta se anota en el specs y se cuenta una sola vez al final. No se rellena con IA ni con stock genérico |
| Advertorial | sin logo: masthead de periódico, y el logo a firma de pie |
| Textos provisionales | `[REEMPLAZAR]` **quemado dentro del PNG**, no en una nota aparte |

## Qué NO hace

- No cambia el ángulo ni el formato: para eso, `estaticos-meta`.
- No escribe el copy del anuncio de Meta: eso es `copy-anuncios-meta`.
- No INVENTA personas ni escenarios con IA: siempre hay una foto real debajo que el GPT recrea (§Recrear sí, inventar no).
- No aprueba nada que no pase §0 + §G + el panel, sin la fuente de la imagen anotada, o que a 200 px
  parezca la pieza original (en el caso B, lo que no se aprueba es lo contrario: que se haya ido del
  territorio del ganador).
- **Sobre las zonas seguras, con precisión, porque «código 1» NO es «rechazar»:** lo que rechaza es
  **el 1:1 con contenido en cualquiera de sus 4 bordes**, y el **9:16 con texto, logo o CTA arriba
  (270 px)**. Abajo, los laterales y cualquier pieza **a sangre** salen `revisar` o `no concluyente`:
  ahí **se abre con `--marcar` y se decide** si lo que entra es la foto (pasa) o es texto/logo/CTA
  (CAMBIOS). Y un **`no medida`** no es una pieza mala: es que no se normalizó antes. El único límite
  que no se cruza nunca es el **mínimo duro de 65 px** en los laterales.
