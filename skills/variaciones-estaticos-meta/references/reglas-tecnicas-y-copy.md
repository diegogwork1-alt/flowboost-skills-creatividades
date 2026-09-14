# Reglas técnicas, de composición y copy para estáticos (probadas)

> # ⚠️ AVISO PARA ESTA SKILL (variaciones-estaticos-meta)
> Este fichero es la copia **al día** del de `estaticos-meta` (sincronizada el 11-09-2026). Se lee
> igual: composición, copy, formato, safe zones, auditoría y doctrina valen tal cual.
> **Lo único que cambia aquí es QUÉ se produce:** allí son 9 piezas nuevas; aquí, **3 variaciones de
> una pieza que ya existe**, con el ángulo y el formato congelados (ver `../SKILL.md`).
> **El motor es el MISMO:** se genera con el GPT adjuntándole la imagen real, bajo la regla
> **«recrear sí, inventar no»** (`../SKILL.md` §RECREAR SÍ, INVENTAR NO). Donde este fichero diga
> «la tanda son los 9», aquí son **3 variaciones del mismo formato**: la regla de diversidad se
> cumple entre variaciones, no entre formatos.
> **Si un fichero cita una sección del `SKILL.md` que aquí no existe** (§"Ruta B2C vs B2B",
> §"Protocolo por anuncio, paso 2-bis", "Fase 2.5", "Fase 3" como auto-QC), es del `SKILL.md`
> de `estaticos-meta`: está ahí, y aplica igual. Aquí las fases son **1 a 5**.

Fuente: los dos informes 2026 de Dirección — el de 100 reglas (original *complete-b2b-creative-director-archive-2026*, **copia local en `informe-b2b-100-reglas.md`**) y la Enciclopedia de 26 partes (original *Investigación Creativos Meta B2B.docx*, **copia local en `informe-b2b-enciclopedia.md`**) — **cruzados** con los estáticos ganadores reales de Flowboost (`patrones-diseno-estaticos.md`, `estaticos-ganadores.md`). Funnel de la casa: anuncio → landing VSL + form Tally / form nativo → llamada.

> **Flowboost trabaja clientes B2C y B2B.** Este documento son las reglas **universales** (specs, composición, copy, prueba social, CTA) que valen para AMBOS y que los ganadores reales confirman. El **enrutado por tipo de cliente** (qué formato/estética/prueba usar según sea servicio B2C local o empresa B2B) está en el SKILL.md §"Ruta B2C vs B2B". Lo B2B de los informes (dashboards, SOC2/G2, personas de comité, ROI/TEI, terminal dark, etc.) **se usa solo cuando el cliente es B2B** — no se fuerza en un cliente B2C.

---

## 0-bis. LAS CIFRAS, Y DE DÓNDE SALE CADA UNA (contrastado el 11-09-2026 con las fuentes reales)
Se preguntó al NotebookLM «Creativos Meta» (80 fuentes) porque **dos de nuestros números no tenían
fuente y uno estaba al revés**. Esto es lo que hay:

| | **Lo que publica Meta** (fuente) | **Lo que usa la casa** | Estado |
|---|---|---|---|
| 9:16 arriba | **269 px · 14 %** | 270 px | ✔ coincide |
| 9:16 abajo | **672 px · 35 %** — *«la zona tapada por la barra del CTA nativo, los subtítulos y los botones»* | **384 px · 20 %** | ⚠️ **apuesta de la casa**, no cifra de Meta |
| 9:16 laterales | **65 px · 6 %** | 107 px | ⚠️ **sin fuente**: es el margen medido en 2 de las 6 piezas aprobadas de Cliente 01 |
| Área central garantizada | **950×979 px** | — | dato de Meta |
| Stories vs Reels | **las mismas cifras**: Meta publica UNA sola zona segura 9:16 | — | ✔ |
| Feed | **4:5 (1080×1350)**, unánime: 30 % más de pantalla y más CTR | **1:1 (1080×1080)** | ⚠️ decisión de la casa — ver abajo |

**Qué significa en la práctica, y qué NO cambia:**
- **Los 384 px siguen siendo la regla de trabajo**, pero ahora se sabe lo que cuestan: entre **y=1248 y
  y=1536** la pieza no invade nuestro valor **pero sí la franja que Meta declara tapada**. Ahí **no puede
  haber CTA, logo ni claim**; fondo o foto, sí. `scripts/zonas_seguras.py` lo avisa por separado.
- **Los 107 px son una preferencia de composición, no un estándar.** Se siguen pidiendo porque las piezas
  aprobadas respiran así, pero **la cifra que no se puede cruzar es 65**, y eso es lo único con fuente.
- **El 1:1 es una decisión consciente y tiene coste.** Las fuentes recomiendan 4:5 para feed móvil
  (30 % más de altura en pantalla, más CTR, menos *scroll past*) y sitúan el 1:1 como el **«cuadrado
  seguro»: un solo activo comodín que funciona en el 80 % de las ubicaciones sin presupuesto para
  adaptar variaciones** — que es exactamente el motivo de la casa. O sea: la regla es defendible, pero
  se está cambiando CTR por no duplicar producción. **Si algún día se produce un tercer ratio, el
  candidato es 4:5, no otro.**

## 1. Specs técnicas (obligatorias) — REGLA DE LA CASA (Dirección)
Cada estático se produce SIEMPRE en **dos tamaños**, porque se suben a **todas** las ubicaciones:
- **Cuadrado 1:1 → 1080×1080 px** (feed, marketplace, etc.).
- **Vertical 9:16 → 1080×1920 px** (stories, reels).
- (No usamos 4:5, **y las fuentes lo recomiendan**: ver §0-bis. Es una decisión consciente — un solo activo para todas las ubicaciones — con un coste de CTR asumido.)
- **Resolución de entrega: exactamente 1080×1080 y 1080×1920.** El GPT devuelve tamaños raros (941×1672 y similares) → **se escala a 1080 con PIL/LANCZOS** antes de guardar (`prompts-gpt.md` §Localizar y descargar). El 1440×1440 / 1440×2560 de los informes ("retina", tope 2048) **solo aplica si el generador ya entrega ese tamaño**: nunca se interpola hacia arriba para "subir de calidad", porque no añade detalle y engorda el fichero.
- **Formato de archivo:** **PNG** si lleva texto superpuesto (evita bordes pixelados); JPG 90%+ solo para foto realista sin texto.
- **Peso:** < 30 MB.
- **Densidad de texto < 20% de la superficie.** Meta ya no rechaza por la regla del 20%, pero **penaliza la entrega y sube el CPM** con mucho texto. Regla firme.

## 2. Zonas seguras (para los dos tamaños)
- **1:1 (1080×1080):** margen mínimo del **5%** (≈54 px) en los 4 bordes. Texto/CTA/logo dentro de ese marco.
- **9:16 (1080×1920):** el **fondo/diseño llena TODO el lienzo**; solo el **texto/logo/CTA** respeta las zonas muertas → **270 px arriba** (~14%, perfil/controles) y **384 px abajo** (~20%, zona de trabajo de Stories), con el CTA por encima de esa franja.
  - **Laterales — los dos números y para qué sirve cada uno, que es donde se lía:** **107 px es el margen de COMPOSICIÓN de la casa** (≈10% del ancho) y **es lo que se pide en el prompt**. *Ojo al dato, corregido el 11-09-2026:* la cifra exacta la usan **dos** de las seis piezas aprobadas de `refs/00_9x16-verticales/LEEME.md`, no cinco como ponía aquí — lo que la tabla sí sostiene es que **ninguna baja de 106 px**, así que el suelo real de composición está ahí y no en 65; **65 px (6%) es el MÍNIMO TÉCNICO de Meta, la línea que no se puede cruzar**, y es lo que inyecta `../templates/render.py` como tope duro. Con 65 la pieza se ve apretada: 65 aprueba, 107 es el objetivo.
  - El **35% inferior (≈672 px)** es la versión extra-conservadora **solo para Reels-safe** (deja el central 950×979), no la regla.
  - Resumen: **270 / 384 / 107 es lo que se pide; 270 / 384 / 65 es lo que no se puede incumplir.**
- El texto clave NUNCA en los bordes que el móvil recorta. (Valores exactos inyectados por `../templates/render.py` según el tamaño; `--guides` los dibuja para QA.)

## 3. Anatomía y jerarquía visual (la que usan los ganadores)
*(Precedencia: esta anatomía de la casa MANDA; el O11 de Ogilvy —titular debajo de la imagen— solo aplica cuando la foto es la protagonista absoluta de la pieza, y como IMPROVE.)* Orden de lectura que el ojo procesa: **1) rostro/figura humana → 2) texto → 3) logo** (el logo va a la periferia, pequeño). Estructura de arriba a abajo (aplica a 1:1 y 9:16):
- **Tercio superior:** kicker/categoría pequeño (ej. "TESTIMONIO", "MADRID | TESTIMONIO") + **titular primario** dominante.
- **Tercio central:** el elemento probatorio (foto real del avatar / antes-después / cita / pasos).
- **Tercio inferior:** prueba social + trust badges + **botón de CTA (**en 1:1**; en 9:16 va POR ENCIMA de los 384 px inferiores, que son zona muerta de Stories)** dibujado en el canvas.
- **La franja del titular NO puede ser un bloque blanco sin diseñar (Dirección, 07-09-2026).** Fallo real: logo + titular oscuro sobre una banda blanca lisa = parece una plantilla a medio terminar, no una pieza de marca. Esa zona es lo primero que se ve y tiene que llevar **el registro de la marca**: color de marca de fondo, la foto continuando por detrás con overlay para contraste, un filete o kicker que la ancle, o textura/profundidad. Blanco liso solo vale si es una decisión de marca sostenida en toda la tanda (premium editorial) **y** el titular lleva jerarquía real (peso, acento, kicker). Nunca por defecto ni por no haber diseñado la zona.
- **El texto se aparta de las líneas estructurales, no al revés.** Split, filetes, marcos y costuras entre paneles definen la retícula; el titular y las etiquetas se colocan **dentro de una zona**, nunca encima de la línea que separa dos. Holgura mínima: el alto de una línea del propio texto. (Ver `calidad-y-autoqc.md §G.13` y el formato Antes/Después.)
- **Ley de la fuerza gravitatoria única:** UN solo centro visual dominante por anuncio. Nada de competir titular + foto + lista + sellos a la vez.
- **Una sola idea de posicionamiento por anuncio** (one-idea rule). Apilar mensajes baja la conversión.
- **JERARQUÍA DENTRO DE LA LISTA (checks, pasos, ítems de oferta) — la regla anti-empaste (Dirección, 07-09-2026).** Es donde se rompe la jerarquía: en cuanto hay varias líneas, salen todas con el mismo peso y el bloque se lee como una mancha gris en vez de como N ideas.
  - **La lista NUNCA compite con el titular:** es el **tercer nivel**, por debajo de titular y apoyo. Si la lista pesa igual que el titular, hay dos centros visuales y se incumple la ley de la fuerza gravitatoria única.
  - **Dentro de cada ítem, solo la PALABRA CLAVE lleva peso** (bold o color de acento); el resto en peso normal. Un ítem entero en negrita no jerarquiza: aplana. Es la misma regla del acento del titular, aplicada al ítem.
  - **Ítems paralelos:** misma estructura gramatical y **longitud parecida** entre ellos (todos empiezan por verbo, o todos por sustantivo). Un ítem de 2 palabras junto a uno de 9 desordena el bloque aunque cada uno esté bien escrito.
  - **Ítems ultracortos:** **≤5 palabras**, sin frases completas, sin punto final. Si un ítem no cabe en 5 palabras, sobra el ítem, no se encoge la letra.
  - **Cantidad:** **3 ítems** por defecto (máx. 5 solo en Oferta/Escasez). Cuatro ítems flojos valen menos que tres fuertes.
  - **Aire entre ítems ≥ el interlineado de dentro del ítem.** Es lo que separa "tres líneas" de "un párrafo": si los ítems están más juntos entre sí que las líneas internas, el ojo los funde. **Este es el mecanismo concreto del empaste.**
  - **Iconos:** uno solo por ítem, **mismo estilo y tamaño**, alineados en columna. El icono marca el inicio de línea; no decora.
  - **Test de la miniatura (el que decide):** a 200 px, ¿se distinguen N líneas separadas o es un bloque gris? Si es un bloque → quitar ítems o palabras, nunca reducir el cuerpo.
- **Espacio negativo: al menos el 40 % del canvas libre** (o fondo sólido limpio). *Corregido el 11-09-2026: aquí ponía 25-35 %, que venía del informe B2B —hoy solo consulta—. La cifra con respaldo es **≥40 %**, y sale de la investigación de carga cognitiva: los estáticos de baja complejidad reciben **+9 % de fijaciones** y se valoran **+4,4 % más atractivos**. Detalle en `parametros-copy.md §4`.* No saturar las esquinas.

## 4. Tipografía y color
- **Sans-serif** (condensada bold) para lead-gen directo y legibilidad → MMS, Cliente 13, Cliente 14, Cliente 12, Cliente 17.
- **Serif editorial** SOLO para display grande de lujo/autoridad → Diana, Cliente 11, Batlle, Cliente 16, Cliente 05. Nunca serif para cuerpo.
- Máximo **3 niveles jerárquicos** de texto. Tamaños mínimos legibles: titular grande, subtítulo medio, cuerpo ≥ 24-28px equivalente. **Test del pulgar/miniatura:** el titular tiene que leerse a 200px de miniatura; si no, agrandar/recortar.
- **Contraste mínimo 4.5:1** (WCAG AA) entre texto/CTA y fondo. Pares extremos funcionan (negro/blanco, o fondo oscuro + 1 acento vivo).
- **1 solo color de acento** sobre la palabra clave del titular (regla confirmada en TODOS los ganadores). Evitar degradados azul→violeta genéricos (se funden con el feed).
- Fondo del anuncio: variable de test, pero solo después de fijar mensaje y layout.

## 4b. Copy con principios Ogilvy (sustancia — de `../../fundamentos-copy/references/ogilvy-reglas-reales.md`, extraído del libro)
**El copy lo escribe el GPT desde el brief (no la skill).** Estos principios de Ogilvy son la **lente con que se AUDITA** ese copy (y lo que debe embodiar), no algo que dicte la skill. Se toma la **sustancia** de Ogilvy; el **formato** lo manda el ganador de Flowboost (mayúsculas condensadas sobre foto con overlay — Ogilvy lo desaconseja para landings, pero en estáticos de Meta rinde y es el estilo de la casa).
- **Beneficio en el titular** (se lee 4× más que sin beneficio) y **flag al nicho/avatar** (que se reconozca).
- **Específico > genérico:** un número, un plazo, un dato concreto (74 leads, "cero okupas en 4 años", "35 años"). Nada de generalidades.
- Fórmulas que rinden: **"Cómo [X] sin [Y]"**, **"Por qué…"**, y la **pregunta de dolor** del avatar.
- **Voz del cliente (VoC):** usar las **palabras textuales** del cliente en la cita/testimonio ("el ciclo atracón-culpa"), no traducirlas a jerga.
- **Aversión a la pérdida:** mostrar qué PIERDE por no actuar (Cliente 13 "coste del error" fue ganador). Perder duele el doble que ganar.
- **Story appeal:** el testimonio como micro-historia (dolor → proceso → resultado), no manual técnico.
- **Cero autobombo** ("somos los mejores"): cada afirmación con hecho/cifra. **Honestidad total:** nunca inventar cifras, testimonios ni fechas.
- **Lenguaje simple, sin jerga.** Frases cortas.
- Salvedades de formato Ogilvy que en estáticos NO aplican tal cual: el all-caps condensado y el texto sobre foto SÍ se usan (con overlay oscuro para contraste ≥4.5:1). El "sin punto final" y "1 sola palabra en mayúscula" de Ogilvy se sustituyen por la regla de la casa: **1 palabra en color de acento** dentro del titular.

## 5. Copy sobre la imagen (límites duros)
> ⚠️ **La doctrina manda (`sistema-director-creativo.md`): 0–6 palabras visibles, MÁXIMO 8 en el NÚCLEO (titular + apoyo)**; titular ≤5, apoyo ≤3. Los números de abajo son solo el techo técnico de legibilidad, no el objetivo.
> **Qué NO cuenta para ese techo y qué está exento (manda `calidad-y-autoqc.md §0-quater`):** no cuentan CTA del botón, sellos/etiquetas, checks, precio "desde X", kicker ni disclaimers; y **los formatos Artículo/Noticia (advertorial) y Review+Claim están exentos** (son editoriales/citables: titular + subtítulo + entradilla o cita). Si dos límites de palabras chocan en cualquier documento de esta skill, gana §0-quater.
- **Titular:** ≤5 palabras (techo técnico 7-8/línea si por excepción hiciera falta). Empieza por dolor/miedo/curiosidad/deseo, NUNCA por el nombre del servicio.
- **Cita/testimonio:** lo más corto posible. El techo de **15 palabras** es el del formato Review+Claim / Quote Card (que está exento del ≤8) — no es una licencia para el resto de formatos.
- **Carga total del NÚCLEO (titular + apoyo):** ≤8 palabras. **No cuentan** CTA, sellos, checks, precio «desde X», kicker ni disclaimers, y **advertorial y Review+Claim están exentos** (`calidad-y-autoqc.md §0-quater`). Si necesitas más → cambia el concepto, no achiques la letra.
- **Texto primario de Meta (el de la publicación):** front-load el hook en los primeros **125 caracteres** (después Meta lo corta con "ver más"). >80% de la gente no lo lee hasta que la imagen ya validó la relevancia → el peso cae en el creativo.
- Titulares que retienen: empezar con **"Por qué…" / "Cómo…"** rinde más que el imperativo genérico.

## 6. Prueba social (jerarquía de efectividad)
De más a menos potente (adaptado a lo que Flowboost tiene y usa):
1. **Testimonio individual real** con **cita específica + cara + nombre + rol/edad + ★★★★★** → es el formato ganador confirmado (MMS `IMG|Testimonio` 74 leads @€2,92; Cliente 11; Cliente 02). Cita concreta > muro de reseñas.
2. **Recuento/estadística de escala** ("+1000 ya han…", "+120 reformas entregadas") → **debe ser > 1.000** o una cifra concreta creíble para no parecer débil.
3. **Cifras específicas / impares / no redondeadas** ("cero casos de okupas en 4 años", "35 años") registran como dato auditado; los redondos se ignoran como marketing.
- Trust badges de contexto en la base para servicios sensibles ("CONFIDENCIAL · 100% ONLINE", "profesional, humano y legal").

## 7. CTA
- **Un solo botón** de CTA dibujado en el canvas, alto contraste, con **verbo + flecha →**.
  - **Dónde va, por ratio:** en **1:1**, en el **15% inferior** (dentro de los 54 px de margen). En **9:16, NO**: ahí los 384 px de abajo son zona muerta de Stories, así que el CTA va **por encima** de esa franja (≈ entre y=1100 y y=1536). Poner el CTA "en el 15% inferior" de un 9:16 es meterlo debajo de la interfaz de Meta — el fallo real que obligó a medir cada vertical.
- Copy conversacional y de baja fricción (coherente con tráfico frío a llamada), **en español de España** (ver `calidad-y-autoqc.md §0-bis`): "RESERVA UNA LLAMADA BREVE →", "¿TE PASA LO MISMO? HABLEMOS →", "SOLICITA TU PRESUPUESTO GRATIS →", "DESCUBRE CÓMO FUNCIONA →". (Evitar "agendar"/"cotización"/voseo.)
- Igualar la fricción del CTA a la temperatura del público: frío = CTA blando (reservar una llamada / descubrir), no "compra ahora". **Criterio de la casa:** nuestro funnel SIEMPRE termina en llamada, así que "reserva una llamada breve" NO cuenta como fricción alta en TOF; lo prohibido en frío es pedir compra o demo de producto.

## 8. Foto / estética (thumb-stop sin parecer anuncio)
- **Foto real y contextual del avatar**, con "imperfección calculada" (estilo natural, no estudio plástico). Es lo que hacen todos los ganadores.
- En viajes/lujo **la foto ES el producto** (Cliente 16, Diana): copy mínimo + promesa emocional + datos concretos (fechas, itinerario).
- Antes/Después: mismo ángulo, luz y distancia; el "antes" apagado/gris, el "después" luminoso.

## 9. Elementos fijos vs variables (para testear a escala)
- **Fijos (marca):** logo pequeño (esquina, margen 5%), tipografía, grilla de la casa.
- **Variables (test):** hook/titular, foto, cita de testimonio, color de fondo. Testear en ese orden de impacto: **mensaje/hook → formato visual → CTA → detalles de diseño**. Las variaciones cosméticas (color de botón) NO mueven la aguja: no perder tiempo ahí.

## 10. Mix y rotación
- **La tanda son los 9 formatos** (nueva cada DOS SEMANAS, no mensual — `../../gestion-cuenta-meta/references/parametros-campana.md` §9) (1:1 + 9:16 cada uno); lo que se publica es un subconjunto, y **lo decide `armar-campana-meta` (montaje) o `gestion-cuenta-meta` (reemplazos semanales) aplicando los parámetros** — no se elige a mano. El histórico de referencia es ~5 estáticos + 5 vídeos EGC/mes activos.
- **Rotar creativos** antes de que caigan: no matar de golpe al ganador fatigado — dejarlo a presupuesto bajo y meter challengers al lado (efecto sustitución) para no reiniciar el aprendizaje del algoritmo. Señales de fatiga: frecuencia **>3,0** en prospección (2,5-3,0 es solo ALERTA). El número manda desde `../../gestion-cuenta-meta/references/parametros-campana.md` §9 — aquí no se duplica, CTR cae 20-25% sostenido, CPM sube 15-20% sin estacionalidad.
