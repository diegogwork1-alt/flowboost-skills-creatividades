# Recipe de prompts para el GPT "Generador Ads Imagen" (probado con Cliente 04, Tanda 1)

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

Reglas de entrada: enviar con clic JS al botón (`document.querySelector('button[data-testid="send-button"]').click()`), no por coordenada/Enter. Todo lo que se le pide al GPT va en **español de España** (tú, nunca voseo).

## MODELO: el GPT crea, la skill AUDITA
El **GPT ya tiene sus instrucciones** (doctrina, Schwartz, hooks, los 9 formatos): **él escribe el copy desde el brief y diseña**. La skill **NO le dicta el copy** ni enumera reglas que ya tiene. Lo que SÍ le da en cada mensaje son: los **adjuntos** (que NO persisten entre turnos) y **la línea de restricciones duras** de la casa. Luego **audita la salida** y manda CAMBIOS **solo por lo que el audit marca**.

## FLUJO EN CADENA (mismo chat) — reconciliado con el PROTOCOLO POR ANUNCIO del SKILL
- **Solo el Anuncio 1** lleva el brief (Paso 1).
- **Del 2 al 9:** se aprueba el anterior y se pide el siguiente. **Corto y sin dictar copy**, PERO cada mensaje de generación lleva **siempre**: (a) **logo oficial adjunto**, (b) **avatar adjunto** si el formato lleva persona, (c) **una frase con la estructura propia del formato** (de `formatos-visual-spec.md`), (d) la **línea de restricciones**. No es "re-explicar": es lo que evita que el GPT invente una cara, deforme el logo o repita el layout del anuncio anterior.
- **Tras cada uno: AUDITAR.** Un fallo → un **CAMBIOS corto y puntual**, re-adjuntando logo/avatar. Repetir hasta pasar. Luego el 9:16 (Paso 3) y descargar.

### Línea de restricciones (va en TODOS los mensajes de generación)
> ⚠️ **El trozo de los márgenes es el ÚNICO que cambia según el ratio que estés pidiendo.** En el mensaje del 1:1 van los 54 px; en el del 9:16, los 270/384/107. Nunca los dos juegos de números en el mismo mensaje: el GPT se queda con uno y casi siempre con el equivocado.
> "Todo el texto en español de España (tuteo tú, sin voseo), **con sus tildes y eñes tal cual te las escribo**, título sin punto final, sin texto en tazas/carteles/atrezo, minimalista (una idea, mucho aire). **El texto que te escribo tiene que salir en la imagen EXACTAMENTE igual, letra por letra y con las tildes puestas, perfectamente legible: no lo reescribas, no lo traduzcas y no inventes texto de relleno ni caracteres raros.** **Deja libres de texto, logo y CTA los márgenes que te indico en este mensaje** (en 1:1: los 54 px de cada borde; en 9:16: los 270 px de arriba, los 384 px de abajo y 107 px a cada lado) y no cortes nada. Reproduce el logo EXACTAMENTE como el PNG adjunto. Recrea EXACTAMENTE a la persona de la foto adjunta (mismo rostro, pelo, gafas, edad), con anatomía correcta."

> **De dónde sale ese trozo nuevo (08-09-2026).** Es la técnica de *bloqueo de texto* de la librería
> pública `awesome-gpt-image-2`: a los modelos de imagen hay que **exigirles explícitamente** que el
> texto salga legible y exactamente el indicado, porque si no lo reinterpretan, y en idiomas con
> acentos lo corrompen. Es lo único que se tomó de ahí; **la librería entera no se instaló** (ver abajo).
> Refuerza la regla 2: escribir el copy con tildes **y además** pedirle que las respete.

> ### ⚠️ DOS REGLAS QUE SE APRENDIERON FALLANDO (Dirección, 07-09-2026) — no se negocian
> **1-CORREGIDA (test, 08-09-2026): las zonas seguras NO se consiguen pidiéndolas. Se MIDEN.**
> Se probó en píxeles, en porcentaje y por franjas: **no acierta con ninguna**. Las 7 verticales de
> esa tanda hubo que ajustarlas midiendo y encajando en post. Se sigue pidiendo en píxeles porque
> **acerca** —y en porcentaje directamente lo ignora—, pero **dar por buena una vertical sin medirla
> es garantía de que sale mal**, y 40 px de invasión no se ven en el monitor: se ven en el móvil, con
> el CTA debajo del botón de Meta.
>
> **Obligatorio antes de aprobar cada vertical:**
> ```bash
> python3 ~/.claude/skills/variaciones-estaticos-meta/scripts/zonas_seguras.py <pieza_9x16.png>
> ```
> Dice hasta qué píxel llega el texto y cuántos entra en cada franja. Si invade → CAMBIOS con el
> número exacto («el CTA entra 206 px en la franja de abajo»), que es mucho más eficaz que «respeta la
> zona segura». Con `--marcar salida.png` dibuja las franjas encima para verlo.
>
> **1-original (sigue valiendo para redactar el prompt).** Las zonas seguras **en PÍXELES, nunca en porcentaje.** Dicho en porcentaje («margen del 5 %», «el 14 % superior») **el GPT lo ignora**: los cuatro verticales de la tanda violaron la safe zone. Dicho en píxeles concretos («deja libres los primeros 270 px y los últimos 384 px») **lo respeta a la primera**. Traducción de la casa: 1:1 → **54 px** por lado; 9:16 → **270 px arriba, 384 px abajo y 107 px a los lados** (107 es el margen de composición de la casa y es lo que se PIDE; 65 px es solo el mínimo técnico que no se puede cruzar — `refs/00_9x16-verticales/LEEME.md`). Si escribes un porcentaje en un prompt, lo estás incumpliendo.
> **2. El copy SIEMPRE con tildes.** El GPT **copia literal lo que le escribes**: si le mandas el texto sin acentos «para evitar problemas de tecleo», en la imagen sale «comision» y «como funciona». Ocurrió de verdad. El campo de ChatGPT acepta tildes y ñ: úsalas siempre, aunque estés esquivando otro problema. (Mismo aprendizaje que `calidad-y-autoqc.md §G.6`.)

> ### ⛔ EL BRIEF SE ADJUNTA EN TEXTO, NO EN PDF (Dirección, 08-09-2026)
> ```bash
> python3 ~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/brief_a_texto.py "<Cliente>"
> ```
> Deja `Insumos/Brief_<Cliente>_para_GPT.txt` y escribe su ruta. **Eso es lo que se adjunta.**
>
> **Por qué:** el PDF pesa entre 56 KB y casi 1 MB (Cliente 02: 142 KB de PDF contra **18 KB** de texto,
> ocho veces menos). Con el logo, el avatar y el brief en la misma llamada, el PDF acerca al tope de
> 10 MB — y la subida **ya falló una vez**, se envió el mensaje igual y el GPT se inventó el cliente.
> Además el modelo **lee el texto directo** en vez de tener que interpretar un PDF.
>
> Sale del `Brief_<Cliente>.md` canónico si existe; si solo hay PDF, lo extrae. **Si del PDF salen
> menos de 400 caracteres, para**: es un PDF escaneado y adjuntarlo sería mandar imágenes sin texto.

> ### ⛔ COMPROBAR QUE EL ADJUNTO SUBIÓ ANTES DE ENVIAR (Dirección, 08-09-2026)
> Pasó: se adjuntó el brief, **la subida falló y el mensaje se envió igual**. El GPT generó sin brief,
> inventándose el cliente. **La pieza salió bonita y con todo inventado** — este fallo no lo detecta la
> auditoría visual. Después de cada `file_upload`, buscar el nombre del fichero en el composer; si no
> aparece, reintentar una vez y, si sigue sin aparecer, **PARAR sin enviar**. Detalle en
> `chrome-rapido.md` §1-bis.

> ### ⛔ EL PRIMER MENSAJE NO LLEVA ADJUNTOS: es la sugerencia del centro (Dirección, 11-09-2026)
> Al abrir el GPT sale su pantalla de bienvenida con la sugerencia **«Pídeme brief, referencias
> visuales y ángulo…»**. **Eso es el Mensaje 1, y va SOLO: ni brief, ni logo, ni fotos.** Se toca, se
> envía, el GPT contesta pidiendo lo que necesita, y **los insumos van en el Mensaje 2** (Paso 1).
> Hasta que no se toca ese cuadro el chat no está activo: no se puede escribir y el `input` de fichero
> puede ni existir. Soltar los cinco ficheros ahí es de donde salen las subidas que fallan en silencio
> y la pieza con el cliente inventado. Orden completo en `chrome-rapido.md` §0.

## Paso 0 — Mensaje 1: la sugerencia, SIN adjuntos
Clic en **«Pídeme brief, referencias visuales y ángulo…»** → comprobar el composer → enviar.
Si la sugerencia no aparece, se escribe a mano lo mismo y **igualmente sin adjuntos**:
> "Pídeme el brief, las referencias visuales y el ángulo que necesitas."

Se espera su respuesta. Solo entonces se pasa al Paso 1.

## Paso 1 — Mensaje 2: los insumos (y el Anuncio 1)
**Ahora sí se adjunta, contestando a lo que ha pedido:** **el brief EN TEXTO** (`Brief_<Cliente>_para_GPT.txt`, ver abajo — **no el PDF**) + **logo oficial** + **fotos reales del cliente** (+ avatar si el formato 1 lleva persona). **NO adjuntar estáticos de otros clientes** (Dirección: el GPT se confunde); el registro/estilo se le describe con palabras.
> "Aquí lo tienes. Adjunto el brief real de <Cliente> (única fuente de verdad), el logo oficial y fotos reales. Genera el Anuncio 1 (Artículo/Noticia) trabajando SOLO desde el brief y con la identidad de marca del manual (tipografías: <serif display / sans>; paleta: <colores>). Registro <premium-editorial | directo-comunidad>. [+ línea de restricciones]"

## Paso 1-bis — Anuncios 2 a 9
> "Aprobado el Anuncio N. Ahora el Anuncio N+1 (<formato>) en 1:1 (1080×1080). Estructura propia de este formato: <una frase de `formatos-visual-spec.md`>; nada de la estructura de los anteriores. [+ línea de restricciones]" + adjuntos (logo, avatar).

## Paso 2 — Versión 1:1 (si el GPT dio otro ratio primero)
> "Aprobado ese diseño. Ahora EXACTAMENTE el mismo anuncio (mismo copy, colores, foto, logo y estilo) rediseñado NATIVO en CUADRADO 1:1 (1080×1080), ocupando TODO el cuadrado y dejando libres de texto, logo y CTA los 54 px de cada borde. Solo el 1:1." + adjuntos.

## Paso 3 — Versión 9:16 (re-adjuntar logo, avatar **y EL 1:1 YA APROBADO**)

> ### ⛔ ADJUNTAR EL 1:1 APROBADO EN EL MENSAJE DEL 9:16 (Dirección, 08-09-2026)
> **El problema:** el 9:16 sale con diferencias estéticas respecto al 1:1 — **sobre todo el botón del
> CTA**, que cambia de forma, de color o de grosor. Y el logo y las tipografías derivan un poco.
>
> **La causa:** al 9:16 se le pide «el mismo anuncio» **de palabra**, sin enseñarle el anuncio. Y ya
> sabemos que **el condicionamiento visual NO se arrastra entre mensajes** — es exactamente por lo que
> el logo y la foto de la persona se re-adjuntan en cada generación. A la pieza no se le estaba
> aplicando la misma regla. El modelo no está adaptando: **está generando otra vez desde cero**, y dos
> generaciones nunca dan el mismo botón.
>
> **La regla: en el mensaje del 9:16 se adjunta el PNG del 1:1 ya aprobado**, además del logo y el
> avatar. Y se le dice qué tiene que quedar CLAVADO:
>
> > "Adjunto el 1:1 ya aprobado. **Tienen que quedar IDÉNTICOS**: el botón del CTA (mismo texto, misma
> > forma, mismo color, mismo redondeo y mismo grosor de letra), el logo, la paleta, las tipografías y
> > el copy palabra por palabra. **Lo único que cambia es la composición**, que pasa a vertical."
>
> Sin esa frase, el modelo se toma el botón como algo que puede rediseñar.


⚠️ NO decir "adapta/reencuadra" (devuelve el 1:1 con bandas). El fondo llena todo el lienzo; solo texto/logo/CTA respetan la safe zone.
⚠️ **El advertorial es el que más falla en 9:16: devuelve el CUADRADO INCRUSTADO dentro del vertical** (el 1:1 flotando sobre un fondo, con marco o con bandas). Pasa a menudo, así que la frase va SIEMPRE explícita en el prompt: **"NO incrustes ni pegues la versión cuadrada dentro del vertical: nada de marcos, bordes, bandas ni el 1:1 flotando sobre un fondo. Rediseña la página editorial DESDE CERO para 1080×1920, con los elementos redistribuidos a lo largo de toda la altura."** Si vuelve incrustado → CAMBIOS citando esa frase, no aprobar.
- **Advertorial:** > "El mismo anuncio NATIVO en 9:16 (1080×1920). La PÁGINA editorial ocupa TODO el lienzo de borde a borde, dejando libres de texto, logo y CTA los primeros 270 px de arriba, los últimos 384 px de abajo y **107 px** a cada lado (mínimo técnico 65, pero se pide 107). Masthead + sección + titular serif + subtítulo arriba; la foto como IMAGEN EDITORIAL grande dentro de la nota (figura de artículo, NO un póster a sangre); pie con CTA abajo. Distribuido en toda la altura, sin bandas vacías. Mismo copy, colores y logo. Solo el 9:16."
- **En los dos casos, la coletilla final:** > "El botón del CTA, el logo, la paleta, las tipografías y el copy quedan IDÉNTICOS al 1:1 adjunto. Solo cambia la composición."
- **Resto de formatos:** > "El mismo anuncio NATIVO en 9:16 (1080×1920): la composición ocupa TODA la altura de borde a borde (la foto puede ir a sangre), con texto, logo y CTA fuera de los primeros 270 px de arriba, de los últimos 384 px de abajo y **107 px a cada lado** (el lateral de las piezas aprobadas de la casa; 65 px es el mínimo técnico, no el objetivo: con 65 la pieza se ve apretada). Sin bandas vacías. Mismo copy, colores y logo. Solo el 9:16."

### ⚠️ Tras RECARGAR la página, la primera escritura con acentos sale CORRUPTA (07-09-2026)
Detectado en el test, dos veces, y costó una generación cada vez: después de recargar el chat, el primer mensaje que lleva tildes llega al GPT convertido en basura del tipo `éá«»íóúññí`. No es que haya que quitar las tildes —eso rompe el creativo (§ regla 2 de arriba)—: hay que **comprobar el texto en el composer ANTES de enviar**.

**Procedimiento obligatorio en el primer mensaje después de cada recarga:**
1. Escribir el mensaje en el composer.
2. **Leerlo por JS antes de enviar** y compararlo con lo que querías escribir:
   ```js
   document.querySelector('div[contenteditable="true"], #prompt-textarea')?.innerText
   ```
3. Si no coincide (tildes rotas, caracteres de más): **vaciar el composer y volver a escribirlo**, y comprobar otra vez.
4. **Solo cuando el texto coincide**, pulsar enviar (clic JS al `button[data-testid="send-button"]`).

No dar por bueno el tecleo a ciegas: el fallo es silencioso y solo se ve en la imagen ya generada, cuando ya has gastado la generación.

### Fechas: dictárselas, no dejar que las invente
Cuando el formato lleve fecha o año visibles (advertorial y sus pills, oferta/escasez con plazo), **sacar la fecha real del sistema** (`date +%d/%m/%Y`, `date +%Y`) y **escribírsela literal en el prompt**: "la fecha de cabecera es 07/09/2026, escríbela exactamente así". Si no se le dicta, el modelo pone una fecha pasada por su cuenta y hay que regenerar. Si la pieza no depende de un día concreto, pedirle **mes y año** (o solo el año) para que no envejezca durante la tanda.

## CAMBIOS típicos (citando el audit) — en español de España
- Tipografía genérica → "Usa la tipografía de la marca: titulares en serif display de alto contraste tipo <X>, texto en sans tipo <Y>."
- Cifra inventada → "Sin inventar datos: usa solo lo que está en el brief."
- Persona distinta a la referencia → "No es la persona de la foto: recréala EXACTAMENTE (rostro, gafas, barba, edad)." + re-adjuntar.
- Logo deformado → "El logo no coincide con el PNG adjunto: reprodúcelo exacto, sin cambiar proporciones ni tipografía." + re-adjuntar.
- Elemento cortado → "La tarjeta/grid de la derecha queda cortada: céntrala y encógela para que entre completa dentro del margen."
- Texto en atrezo → "Quita el texto de la taza/cartel; el copy va solo en titular, apoyo y CTA."
- Ruido visual → "Simplifica: una sola idea, quita <elementos>, más aire."
- Voseo / LATAM → "Reescribe en español de España: «X» → «Y»."
- **Safe zone violada** → "Deja libres de texto, logo y CTA los primeros 270 px de arriba, los últimos 384 px de abajo y 107 px a cada lado." **En píxeles; en porcentaje lo ignora.** Y **con el número medido**: "el CTA entra 206 px en la franja de abajo" funciona; "respeta la zona segura" no (ya se probó).
- **Tildes comidas** ("comision", "como funciona") → reescribir el copy en el prompt **con las tildes puestas** y pedir: "Escribe el texto exactamente así, respetando tildes y eñes: «…»."
- **9:16 con el 1:1 incrustado** (típico del advertorial) → "No incrustes la versión cuadrada dentro del vertical: nada de marcos, bandas ni el cuadrado flotando. Rediseña la composición desde cero para 1080×1920, repartida por toda la altura."
- **Fecha pasada / año viejo** → "La fecha de la cabecera es incorrecta: escribe exactamente 07/09/2026." (o "cambia «INFORME 2025» por «INFORME 2026»"). Dictar siempre la fecha buena sacada del sistema; no decir solo "pon la fecha de hoy", porque el modelo no sabe qué día es.

## Localizar y descargar la imagen del último turno (mecanismo que FUNCIONA)
Las imágenes generadas **no** cuelgan del nodo `[data-message-author-role]`; hay que ir por el turno:
```js
const turns=[...document.querySelectorAll('[data-testid^="conversation-turn"]')];
const last=turns[turns.length-1];
const ids=[...new Set([...last.querySelectorAll('img')].map(i=>{const m=(i.src||'').match(/id=([^&]+)/);return m?m[1]:null;}).filter(Boolean))];
// ids[ids.length-1] = imagen del último turno. Comprobar naturalWidth>0 (si es 0, aún carga).
```
Descargar (sin salir de la página):
```js
const img=[...document.querySelectorAll('img')].find(i=>(i.src||'').includes('<ID>'));
const b=await (await fetch(img.src)).blob(); const u=URL.createObjectURL(b);
const a=document.createElement('a'); a.href=u; a.download='<Cliente>_Tanda<N>_<Formato>_<1x1|9x16>.png'; document.body.appendChild(a); a.click(); a.remove();
```
Cae en la carpeta de descargas de Chrome (`~/Desktop/Cliente 25/`) → **mover de inmediato** a `~/Desktop/CLIENTES/<cliente>/Ads/GPT/` → si el 9:16 sale a 941×1672 u otro tamaño, **escalar a 1080×1920** (PIL, LANCZOS) → `rclone copy` a `gdrive:i_<C>/c_<C>/2. Ads/Estáticos/GPT/Tanda <N>/`.
Fin de generación = desaparece `button[data-testid="stop-button"]` **y** la imagen del turno tiene `naturalWidth>0`.


## Advertorial: qué pedirle SIEMPRE al GPT (Dirección, 08-09-2026)
En el prompt del formato 1 (Artículo/Noticia) hay que decirlo explícito, porque el modelo mete el logo de la marca en la cabecera por su cuenta:

> En la cabecera va el nombre de una publicación, tipo «BARCELONA ACTUAL», con su kicker de sección. **NO pongas el logo de la marca en la cabecera.** Si la marca aparece, que sea abajo y pequeña, junto a la oferta. No uses el nombre de ningún medio que exista de verdad.


## Sobre `awesome-gpt-image-2` (investigada el 08-09-2026 — NO se instala)
Librería pública de 544 prompts para **GPT-Image-2 por API** (MIT). Se revisó y **se descartó**:

- **Es para otro motor.** Aquí se genera con el GPT «Generador Ads Imagen» dentro de ChatGPT, vía
  Claude-in-Chrome. Sus prompts no se aplican igual.
- **Choca con la doctrina de la casa:** «el GPT crea, la skill AUDITA; no le dictes el copy ni el
  diseño» (`SKILL.md`). Esa librería es justo lo contrario: dictarle la composición al modelo.
- **No cubre lo que duele aquí:** no trae relación de aspecto (1:1 + 9:16), ni zonas seguras de Meta,
  ni forma de imponer paleta o logo de marca — lo reconoce su propio README. Y «póster» no es «anuncio
  de respuesta directa»: no hay ni una categoría de publicidad de captación.

**Lo único que se tomó:** la línea de bloqueo de texto de arriba. Su otra regla útil —escribir el copy
como cadena literal y no dejar que el modelo elija las palabras— **ya estaba** aquí, aprendida fallando.
