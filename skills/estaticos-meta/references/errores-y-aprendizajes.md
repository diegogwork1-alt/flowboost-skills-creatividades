# Errores y aprendizajes (para NO repetirlos) — run real Cliente 04 05-09-2026

Cosas que fallaron o no tenía en cuenta al correr la skill por primera vez de verdad. **Leer antes de cada run.**

## 1. BRIEF — no improvisar, subir el real de Onboarding
- **Error:** escribí un brief a mano deducido del anuncio. Mal.
- **Regla:** el brief real vive en **`0. Onboarding/Brief_<Cliente>.pdf`** (lo genera la skill `brief-desde-onboarding`). Se descarga, **se convierte a texto con `brief_a_texto.py` y se sube el `.txt`** — **el PDF NO se sube al GPT** (pesa hasta 8 veces más, acerca al tope de 10 MB de la llamada y ya provocó una subida fallida en la que el GPT se inventó el cliente). Ver `prompts-gpt.md` §EL BRIEF SE ADJUNTA EN TEXTO. No inventar ni parafrasear el brief.
- En `0. Onboarding` suele haber además: **`Reseñas/`** (testimonios reales → ads Review/Prueba social) y dosieres con **datos reales** (para ROI/oferta, solo si están verificados). Usar esos, nunca inventar cifras.

## 2. LOGO — usar el final y verificarlo contra la web
- **Error:** usé un logo de `Logos Antiguos/` (viejo). Mal.
- **Regla:** el logo actual está en **`1. Branding/.../Archivos_Finales_<Cliente>_2025/RGB/02_PNG/`** con variantes **Logotipo / Isotipo / Naming** en **Color (navy) / Blanco / Negro / Alt**. Elegir la variante por fondo (blanco para fondo oscuro, navy para fondo claro). NUNCA `Logos Antiguos`.
- **Verificación obligatoria:** contrastar el logo elegido con el de la **web home del cliente** (abrir su sitio y comparar). Si no coincide → es el logo equivocado, buscar el correcto. (Cliente 04: isotipo de edificios + wordmark serif "Cliente 04" navy #272B59.)

## 3. COLORES/TIPOGRAFÍA — del manual, no de un anuncio
- **Error:** saqué el color de un ad viejo (dorado brillante #f4bb21). Mal.
- **Regla:** sacar la paleta y las tipografías del **manual de identidad** (`1. Branding`), no de un anuncio. Si el manual es PDF → renderizar con fitz (`pip install PyMuPDF`; poppler no está) y leer las páginas de "colores" y "tipografía". (Cliente 04 real: Navy #272B59, Gris Niebla #D2D2D2, Arena Dorada #C6B491 —dorado APAGADO—, Acero #4A4F5A; Stardom serif display + Myriad Pro sans.)

## 4. Acceso a Drive por ID de carpeta
- Si Dirección pasa un link de carpeta de Drive, acceder por su ID con `rclone ... --drive-root-folder-id=<ID> "gdrive:"` (el remoto `gdrive:` está rooteado en la carpeta madre Clientes; el flag lo re-apunta).
- Descargas grandes/muchas → correr en background (rclone puede tardar > 120s).

## 5. Manejar el GPT en Chrome (Claude-in-Chrome) — quirks
- **Cuenta:** 2 Chrome conectados → hay que pedir a Dirección cuál (regla del tool). **La cuenta del GPT es la de Flowboost EMPRESA, pero se entra por el Google `<correo-cuenta-de-trabajo>`.** Son dos cosas distintas y hay que tenerlas claras: el **workspace** de ChatGPT es el de la empresa (se ve como «Flowboost Marketing» / «Flowboost Marketing Empresa») y eso es lo CORRECTO — ver ese nombre NO significa que estés en la cuenta equivocada. Lo que identifica la sesión buena es el **email de Google con el que se ha iniciado sesión**, que tiene que ser `<correo-cuenta-de-trabajo>`. **NUNCA `<correo-direccion>`**, aunque ese email también lleve a un workspace de Flowboost. O sea: workspace «Flowboost Marketing Empresa» = bien; lo que hay que mirar es el email de la sesión. Verificar el perfil antes de generar.
- **GPT:** "Generador Ads Imagen - Agosto 2026" (creado por Operaciones Peña), modelo GPT-5.6 Sol. URL en el SKILL.
- **Input de texto corrompe € y acentos:** el `type` en el composer de ChatGPT mezcló/rompió los caracteres `€` y tildes. → **REGLA ÚNICA (cierra la contradicción con §G.6):** las **instrucciones operativas** al GPT van sin `€` (usar "EUR"); pero **cualquier texto que deba RENDERIZARSE en la pieza va SIEMPRE con sus tildes correctas** (si se le pasa sin tildes, el creativo sale sin tildes: error real "Tu inviertes"); o mejor, **subir el brief como archivo** y dar solo una instrucción corta. Verificar el texto con screenshot ANTES de enviar.
- **Quitar un adjunto a veces no responde al primer clic** (el botón "Quitar archivo N" quedó tras 2 clics). → Para empezar limpio, usar **"Nuevo chat"** en vez de quitar adjuntos de a uno; así se resetean los archivos.
- **Subir archivos:** NO clickear el botón "+/Agregar archivos" (abre el file picker nativo, invisible). Usar `file_upload` contra el `<input type=file>` (buscarlo con read_page; ref del input dentro del `form`).
- **Verificar adjuntos con `read_page` del form** (grupos "Quitar archivo N: nombre") antes de enviar, para confirmar que están los correctos y no sobra ninguno.

## 5b. Secuencia de comandos FIABLE para manejar el GPT (probada — usar esta, es la rápida)
Para no perder tiempo la próxima, esta es la secuencia que funcionó (los métodos tachados fallaron):
1. **Resetear/abrir chat limpio:** `navigate` a la URL del GPT (deja el chat vacío, sin adjuntos viejos). NO ir quitando adjuntos de a uno.
1-bis. **Mensaje 1 SIN adjuntos:** clic en la sugerencia **«Pídeme brief, referencias visuales y ángulo…»** y enviar. Se espera a que el GPT conteste pidiendo los insumos. **Los pasos 2-5 de abajo son el Mensaje 2**, no el primero.
2. **Conseguir el ref del input de archivos:** `read_page` con `ref_id` del `main` y `filter:"all"` → buscar el `button ... type="file"` dentro del `form` (ej. ref del `<input type=file>`). 
3. **Subir TODO junto:** `file_upload` con ese ref y `paths:[Brief_<Cliente>_para_GPT.txt, logo_navy.png, logo_blanco.png, foto1.jpg, foto2.jpg]` en UNA sola llamada (≤10MB). **El brief va en .txt, nunca el PDF.** Y después, **comprobar que los adjuntos subieron antes de enviar** (`chrome-rapido.md §1-bis`): una subida que falla en silencio produce una pieza bonita con el cliente inventado.
4. **Escribir instrucción:** `left_click` en el textbox del composer (ref "Chatear con ChatGPT") y `type` el texto **sin `€` (usar "EUR") pero CON TILDES**. Las tildes van siempre: salió «Tu inviertes» por saltárselas. Lo que se quita es solo el símbolo de euro. Verificar con `read_page` del form que el texto entró (a veces el 1er click no toma foco → reintentar el click en el textbox).
5. **ENVIAR (lo importante):** `read_page` del `form` → enviar con **clic JS** `document.querySelector('button[data-testid="send-button"]').click()` (lo más fiable) o clickeando el `button "Enviar mensaje"` por su ref. ⚠️ NO sirve: clickear por coordenada (el botón se mueve) ni pulsar `Return`/Enter.
6. **Confirmar envío:** el composer se vacía, aparece el **botón de stop** (cuadrado azul) y la URL cambia a `/c/<id>`. 
7. **Esperar la imagen:** puede tardar ~30-90s. Poll con `screenshot` cada ~15-20s hasta que aparezca la creatividad; entonces localizarla por el último `conversation-turn` y descargarla con el fetch→blob de `prompts-gpt.md` (el `save_to_disk` del screenshot NO sirve).

## 6. Flujo correcto del run (resumen corregido)
1. Descargar de Drive: `Brief_<Cliente>.txt` (convertido con `brief_a_texto.py`; **el PDF NO se sube al GPT**: ya falló una vez y el GPT se inventó el cliente) (Onboarding), logo final correcto (Archivos_Finales), paleta/tipos del manual, fotos reales, reseñas reales.
2. Verificar logo vs web home del cliente.
3. En Chrome (cuenta <cuenta-de-trabajo>), abrir el GPT → **Mensaje 1: la sugerencia del centro «Pídeme brief, referencias visuales y ángulo…», SIN adjuntar nada** → esperar a que el GPT pida lo que necesita → **Mensaje 2:** subir **brief en .txt + logo + fotos**, comprobar que subieron, y escribir la instrucción corta **sin el símbolo `€` (escribir "EUR") pero CON TODAS LAS TILDES** pidiendo el Anuncio N. (Lo que se quita es solo el euro; sin tildes el creativo sale sin tildes — «Tu inviertes».) Orden exacto en `chrome-rapido.md §0`.
4. Verificar adjuntos y texto por read_page/screenshot → enviar.
5. Esperar la imagen, descargarla, QC (doctrina + safe zones + claims reales), guardar en Drive `2. Ads/Estáticos/GPT/Tanda <N>/` *(ruta corregida: antes decía "Estaticos/<fecha>", que ya no existe)*.


## 7. EL GPT TIENE QUE ENTENDER EL FORMATO (error grave del 1er run) — hoy: se le DESCRIBE, no se le adjuntan piezas ajenas
- **Error:** vi las referencias (patrones-diseno-estaticos) pero NO se las pasé al GPT. Resultado: para "Artículo/Noticia" el GPT hizo una **foto de un diario impreso sobre una mesa** (mockup 3D) — malísimo, no se parece a nada de la casa.
- **Regla vigente (Dirección, 06-09):** el GPT necesita entender la ESTRUCTURA del formato, pero **NO se le adjuntan estáticos de otros clientes** ("se confunde"). Lo que se hace: mirar YO la biblioteca `references/refs/<NN_formato>/` (eligiendo el **registro** de la marca: premium/editorial → Diana/Cliente 11/Batlle; ruidoso/comunidad → Cliente 05/MMS; ver `calidad-y-autoqc.md §D`) y **describirle la estructura con palabras** (la frase de `formatos-visual-spec.md`). Ej. advertorial: *"un ADVERTORIAL ESTÁTICO PLANO, página editorial a canvas completo, NO una foto de un periódico/objeto real"*. Del **mismo cliente** sí se puede adjuntar su propia pieza aprobada. Adjuntar una pieza ajena **solo como último recurso**, tras varios intentos fallidos, aclarando que es solo estructura.
- **"Artículo/Noticia" ≠ foto de un diario.** Es un **layout editorial plano a canvas completo** que imita una nota de prensa (flat design). El registro (ruidoso vs premium) lo define la marca; pasarle SIEMPRE el ejemplo del formato Y del registro correcto.
- **Contrastar la salida del GPT contra la referencia** antes de aceptar. Si se parece a un mockup de objeto/foto de producto impreso en vez de un estático diseñado → CAMBIOS.

## 8. Hooks más STOP-SCROLLER
- Los hooks tienen que **frenar el scroll**: más disruptivos, tensión/curiosidad/pattern-interrupt, no titulares de periódico correctos y aburridos. (Ej. malo: "El inmobiliario vuelve a captar el interés de los ahorradores" = titular de diario tibio. Mejor: algo que interpele y genere curiosidad inmediata, dentro del ángulo y sin claim inventado.) Cruzar con Schwartz (awareness) y el ≤8 palabras.

## 9. INSTRUCCIÓN CORRECTA PARA EL 9:16 (error repetido — instrucción mía mala)
- **Error:** pedí el 9:16 como "foto en la mitad inferior" / "adaptá el diseño" → el GPT devolvió **el 1:1 metido en un lienzo 9:16 con bandas de fondo vacías** (parece cuadrado centrado). Mal, dos veces.
- **Instrucción correcta (guardar y usar tal cual):** *"El anuncio debe OCUPAR TODO el lienzo 9:16 (1080×1920) de borde a borde, SIN bandas de fondo vacías: el fondo/foto va **a sangre (full-bleed)** en todo el alto y ancho, y la composición usa **TODA la altura**. Deja libre de texto/logo/CTA SOLO la **safe zone** (14% arriba ≈270px, 20% abajo ≈384px). Es un advertorial editorial **nativo 9:16**, NO el diseño cuadrado con márgenes."*
- Regla general para CUALQUIER formato en 9:16 y en 1:1: **el creativo llena TODO el lienzo del ratio pedido menos la safe zone**; nunca dejar el diseño de otro ratio centrado con fondo vacío alrededor. Lo mismo vale al pedir 1:1 (llenar el cuadrado, no un vertical encogido).
- Al pedir cada ratio, decir explícito "rediseñá NATIVO para \<ratio\>, ocupando todo el lienzo menos la safe zone", no "adaptá/reencuadrá".
- **MATIZ (error siguiente):** decir "foto full-bleed en todo el 9:16" hace que **pierda el aspecto advertorial** (queda como anuncio de producto/inmobiliario, no nota de prensa). Para ADVERTORIAL, lo que llena el 9:16 es la **PÁGINA editorial** (fondo/paper del diario, masthead, titular, nota), NO la foto. La foto va **grande, como imagen de artículo dentro de la nota (con su encuadre/columna), no como póster a sangre**. Instrucción correcta advertorial 9:16: *"la PÁGINA editorial (fondo cream, estilo periódico) ocupa todo el 9:16 menos la safe zone; masthead+titular+subtítulo arriba, la foto como IMAGEN EDITORIAL grande dentro de la nota (figura de artículo, no full-bleed), y el pie con CTA; distribuido en toda la altura, manteniendo estética editorial premium."* → El "full-bleed" aplica a la PÁGINA/fondo del formato, no necesariamente a la foto (depende del formato: en Testimonio o Pain sí puede ser foto full-bleed; en Advertorial NO, la foto es figura de artículo).

## 10. NO dictar el copy + tipografía de marca + safe zones (correcciones de Dirección)
- **NUNCA escribas TÚ el copy del anuncio.** Error: le dicté al GPT "usá exactamente este titular: …" inventado por mí. MAL. **El copy se REDACTA DESDE EL BRIEF** (lo hace el GPT leyendo el brief, o la skill `copy-anuncios-meta`) siguiendo la doctrina (Schwartz, hook stop-scroller, ≤8 palabras en DR / editorial en advertorial, Ogilvy, sin inventar). La skill operadora da **brief + assets + formato + reglas**, y DEJA que el copy salga del brief. (Coherente con la regla transversal: trabajar del brief, no de interpretaciones — y escribir yo el copy ES una interpretación.) Si se pasa "copy exacto" al GPT de imagen para evitar typos, ese copy tiene que **venir del brief/copy-skill, no inventado en el momento**.
- **Tipografía de la marca, no genérica.** El GPT usaba serif genérico; Cliente 04 es **Stardom (serif display alto contraste) + Myriad Pro (sans)**. Instruir explícito en cada pedido: "usá la tipografía de la marca: titulares en serif display de alto contraste tipo Stardom, texto en sans humanista tipo Myriad Pro" (el modelo no carga la fuente exacta, pero debe emular el estilo). Es un check del auto-QC (fidelidad de marca). Si la fidelidad tipográfica es crítica, el fallback HTML con la fuente real es más exacto.
- **Safe zones**: reforzar en cada pedido y verificar en el QC (nada de texto/logo pegado a los bordes). **Siempre en píxeles, nunca en porcentaje** (en porcentaje el GPT lo ignora): 1:1 → **54 px** por lado; 9:16 → **270 arriba / 384 abajo / 107 a los lados** (65 px es el mínimo técnico). Y la compuerta es **medir** con `../scripts/zonas_seguras.py`, no pedirlo.

## 11. LÍMITE del GPT de imagen: no carga las fuentes exactas de la marca
- El modelo de imagen (ChatGPT) **no puede usar los archivos de fuente reales** del cliente (ej. Cliente 04: Stardom + Myriad). Solo **emula el estilo** (serif display de alto contraste + sans humanista). → La tipografía NUNCA será 100% la de marca por la vía GPT.
- **Opciones:** (a) aceptar la emulación de estilo (rápida, buena para tests); (b) para **fidelidad tipográfica exacta**, usar el **fallback HTML** (`templates/`) que sí incrusta la fuente real (o pasar el creativo a un diseñador/Canva con la fuente). Decidir por cliente/pieza según cuán crítica sea la marca. El auto-QC de "fidelidad de marca" debe puntuar la tipografía como "aproximada" cuando sale del GPT.

## 12. FLUJO EN CADENA, MISMO CHAT (regla de Dirección) — el GPT ya sabe la secuencia
- **Los 9 anuncios se hacen EN CADENA, en el MISMO chat.** El GPT ya conoce su secuencia (Anuncio 1..9) y cada formato. **Se le aprueba el anterior y se le dice "sigue con el siguiente" — nada más.** NO re-explicar el formato, NO dictar copy, NO pegar instrucciones largas (el GPT ya las tiene). El GPT escribe el copy y diseña.
- **Error mío:** en el Anuncio 2 me puse a dictarle formato + copy + reglas → lo ensucié (arrastró chrome, etc.). Lo correcto: `"VALIDAR / aprobado el Anuncio 1. Segui con el Anuncio 2."` y listo.
- **Mi único rol tras cada generación: AUDITAR** con el playbook y, SOLO si algo falla, mandar un CAMBIOS **puntual** (ej. "respeta safe zones", "usa la tipografia de la marca", "sin cifras inventadas"). Un fallo → un CAMBIOS corto, no un rediseño dictado.
- Límite del GPT (informar, no bloquea): safe zones/fuentes quedan **aproximadas** (generativo); el CAMBIOS puntual las acerca. Fallback HTML solo si se necesita precisión exacta.

## 13. ESPAÑOL DE ESPAÑA — SIEMPRE (error real: Dirección borró una tanda entera del Drive)
- **Error:** una tanda salió con **"toques argentinos" (voseo)** y Dirección la **borró completa del Drive**. Flowboost es España: el público es español y el voseo/léxico LATAM delata que no es de aquí.
- **Regla dura (REJECT):** TODO el texto visible en **español de España** — tuteo **tú/vosotros, 0 voseo** (❌ Descubrí/Dejá/Empezá/Sumate/Hacé/Descargá/Conseguí/Ahorrá/tenés/querés/seguís → ✅ Descubre/Deja/Empieza/Únete/Haz/Descarga/Consigue/Ahorra/tienes/quieres/sigues) y **léxico de España** (❌ agendar/celular/cotización/departamento/carro → ✅ reservar-pedir cita/móvil/presupuesto/piso/coche). El CTA también.
- **Cómo se aplica:** (a) se le dice explícito al GPT en cada pedido ("todo el texto en español de España, tuteo tú, sin voseo argentino"); (b) el auto-QC lee TODO el texto de la pieza y si ve UNA forma no-España → CAMBIOS "reescribe en español de España, «X»→«Y»". No se guarda nada con toques argentinos. Detalle: `calidad-y-autoqc.md §0-bis` + regla raíz 7 del SKILL.
- **OJO propio:** mis playbooks (`audit-copy-por-formato.md`, `../../fundamentos-copy/references/headlines-playbook.md`) tenían ejemplos en voseo (los escribí yo) — ya corregidos; si vuelvo a escribir ejemplos, en España.

## 14. PERSONAS de stock, texto en props y grids cortados (errores reales del run de Cliente 04 Ad 4)
- **Persona real recreada, NO IA a mano:** aprobé el Ad 4 con personas generadas por IA. Dirección: "por qué aprobaste si no tiene la imagen de una persona real sacada de la librería de stock". Regla: si el formato lleva persona → **buscar en stock gratuito una persona real de estética española y adjuntarla al GPT para que la RECREE**. (Ver SKILL Fase 2.5 + `calidad-y-autoqc.md §0`.)
- **Revisar ANTES de descargar:** bajé ~15 fotos basura a la carpeta. Dirección: "tenés que revisar antes de descargar, me vas a llenar de fotos basura... cuando terminás borrame todas esas boludeces que no usaste". Regla: **previsualizar miniaturas en el navegador, descargar SOLO la elegida, y borrar descartes al terminar**. Unsplash > Pexels para lifestyle premium con estética española.
- **CERO texto en props:** el GPT metió frases en las tazas ("TU PATRIMONIO TRABAJA", "DEMASIADO TIEMPO"). Dirección: "saca ese comentario de la taza, no quiero ese tipo de cosas". Regla dura: **nada de copy en tazas/carteles/camisetas/atrezo**; el copy va en titular/columnas/CTA.
- **NADA cortado por el borde:** aprobé el Ad 4 con la caja "CON Cliente 04" (grid derecho) **cortada** contra el borde. Dirección: "no aprueba porque está cortado el grid de la derecha". Regla dura del auto-QC: **revisar los 4 bordes; ningún grid/tarjeta/texto/CTA/logo puede quedar cortado o pegado al borde** → CAMBIOS "centra y encoge para que entre completo con margen 5%".
- **Ruido visual / poco minimalista:** el Ad 4 salió recargado (Sin/Con + pilas de papeles + persona + fondo). Dirección: "hay mucho ruido visual, poco minimalista". La comparativa Sin/Con con atrezo mata el minimalismo. Regla: **1 idea + máximo aire**; para Feature→Beneficio, visual limpio + titular + máx 3 checks + CTA, sin columna de estrés ni atrezo.
- **Anatomía IA:** el hombre "parecía que le faltaba un brazo". Revisar SIEMPRE anatomía (brazos/manos/dedos/cara) → REJECT si hay artefactos.
- **La referencia de persona NO persiste entre turnos:** adjunté la foto real para el Ad 5, pero al REGENERAR (sin re-adjuntarla) el GPT **inventó una cara de IA** distinta (la mía llevaba gafas). Dirección: "usó a una persona IA el anuncio". Regla: **adjuntar la foto en CADA mensaje de generación** (1:1, 9:16 y cada CAMBIOS) + decir "recrea EXACTAMENTE a la persona de la foto adjunta, no inventes otra" + **comparar la cara generada con la referencia** en el audit.
- **Cada formato tiene estructura propia:** hice el Ad 5 (objeciones) con el layout del Ad 4 (persona+3 checks+CTA). Dirección: "eso no es el formato del anuncio... ya tenés que ir guardando los parámetros de cómo se va viendo cada formato". → Creado `formatos-visual-spec.md` (héroe + estructura + qué NO debe parecer de los 9); se consulta ANTES de generar y en el primer check del audit, y se actualiza al aprobar cada formato.
- **LOGO deformado y con deriva acumulativa:** el GPT redibuja el logo en cada generación y se fue **deformando formato a formato**. Dirección: "el logo no es ese, se fue deformando a medida que pasaban los formatos, es algo que tenés que revisar". ~~Pedir la pieza sin logo y componer en post~~ **MÉTODO DESCARTADO por Dirección** (ver el punto siguiente): la solución vigente es **adjuntar el PNG oficial en CADA generación**. Componer en post (`../templates/poner_logo.py`) queda SOLO como plan B si Dirección lo pide. Y siempre, **compararlo contra el archivo oficial en CADA pieza** (no solo la primera) → regenerar/tapar.
- **NO cambiar el método por cuenta propia:** ante la deformación del logo decidí yo solo generar las piezas **sin logo** y componerlo en post. Dirección: "¿cuándo te autoricé a eso? jamás, es un error garrafal". **La solución correcta (suya): adjuntarle el PNG del logo en CADA generación**, igual que la foto de la persona — así lo dibuja bien. Regla: los cambios de proceso los decide Dirección; yo aplico el protocolo y le señalo el problema, no invento un pipeline nuevo.
- **NO adjuntar material de OTROS clientes al GPT:** Dirección: "al GPT no le adjuntes cosas de otros clientes porque se confunde, solo en casos de urgencia que no te entienda el formato después de varios intentos". Las referencias (biblioteca `references/refs/<NN_formato>/`) las **miro yo** y las traduzco a instrucciones escritas. Dentro del mismo cliente sí se puede adjuntar su propia pieza aprobada.
- **Meta-lección (Dirección: "no tengo que estar repitiendo todo, esto debe estar en la skill"):** cada corrección se codifica **en el momento** y en forma de **procedimiento ejecutable** (ver `SKILL.md` → PROTOCOLO POR ANUNCIO), no como nota suelta. Si Dirección tiene que repetir algo, es que faltó protocolo.
- Lección transversal: **el audit debe MIRAR de verdad la imagen** (bordes, props, autenticidad de la persona, anatomía, ruido/minimalismo) antes de aprobar; no basta con copy/idioma/marca.

## Advertorial con el logo del cliente en la cabecera (Dirección, 08-09-2026)
**Qué pasó:** en los advertoriales se ponía el logo del cliente arriba, como en cualquier otra pieza.
**Por qué está mal:** este formato solo aporta una cosa —que se lea como una noticia y el escéptico
baje la guardia—. El logo en la cabecera dice «esto es publicidad» en el primer vistazo, así que se
pierde eso y queda un anuncio peor que uno normal, encima disfrazado.
**Cómo se aplica:** arriba va el **nombre de un medio** (`BARCELONA ACTUAL`, `EL DIARIO INMOBILIARIO`),
coherente con el sector y la ciudad del avatar. El logo, si va, **abajo y pequeño** junto a la oferta.
**Nunca un medio que exista de verdad**: eso es suplantar a un medio y Meta lo tumba.
Checks: `calidad-y-autoqc.md` §B y §G.24.

## Las zonas seguras no se consiguen pidiéndolas (test, 08-09-2026)
**Qué pasó:** se probó pedirle las zonas seguras al GPT en píxeles, en porcentaje y por franjas.
**No acierta con ninguna.** Las 7 verticales de la tanda hubo que ajustarlas midiendo y encajando
en post. Esto **corrige** la regla del 07-09 que decía que en píxeles lo respetaba a la primera:
acerca, pero no acierta.

**Cómo se aplica:** `../scripts/zonas_seguras.py` mide hasta qué píxel llega el texto y cuánto entra en
cada franja. **Ninguna vertical se aprueba sin pasarla.** Si invade, el CAMBIOS lleva el número
exacto — pedir «respeta la zona segura» ya se probó y no funciona.

**Por qué no vale mirarlo:** 40 px de invasión no se ven en el monitor. Se ven en el móvil del
cliente, con el CTA tapado por la interfaz de Meta.

**Lo que el script NO dictamina:** los laterales. Con fondos a sangre da falsos positivos —marcaba 5
de las 6 verticales aprobadas de Cliente 01, que a ojo están bien—. Arriba y abajo sí, que es donde la
interfaz se come el anuncio de verdad.

---

## 09-09-2026 · Tanda Flowboost Dubái: lo que dejó como referencia y como aviso

14 piezas (7 formatos × 1:1 y 9:16) incorporadas a `refs/`. Detalle en `refs/FlowboostDubai_LEEME.md`.
Tres cosas que no estaban escritas en ningún sitio y ahora sí:

**1. El advertorial sin logo no es "quitar el logo".** La regla de Dirección (08-09) decía *no poner logo,
poner título de diario*. La pieza `01_articulo` resuelve el vacío que dejaba: se pone un **masthead
inventado para la pieza** (`THE BROKER BRIEF`) con kicker de sección y fecha entre dos filetes, y el
logo **no se elimina, se degrada a firma de pie** (`By flowboost.` abajo, junto al CTA). Sin eso, el
anuncio no lleva marca en ninguna parte, que tampoco es lo que se quiere.

**2. Antes/Después con persona: la MISMA persona, la misma ropa.** Lo que cambia es la **luz** (fría y
oscura → cálida y luminosa) y el **entorno** (torre de papeles → vegetación y skyline claro). Si el
generador devuelve dos personas distintas, o la misma con otra ropa, la comparación deja de leerse como
una transformación y pasa a leerse como dos fotos de archivo.

**3. Testimonio generado sin marca dentro del PNG = pieza que no sale de referencias.** Dirección autorizó
reseñas generadas (08-09) con la condición de que derriben una objeción concreta y vayan marcadas
`[REEMPLAZAR]`. En `08_prueba-social` la marca quedó **en el fichero de specs pero no en la imagen**: la
pieza renderizada se lee como tres testimonios reales con nombre y rol. **La condición se cumple cuando
la marca está en el píxel, no en el .md.** Si no está, la pieza vale como referencia de composición y no
se sube a ninguna cuenta.

## 11-09-2026 · Consejo en Opus sobre `variaciones-estaticos-meta` (5 asesores + 5 revisiones cruzadas)

Lo que más importa no es la lista de fallos: es **qué clase de fallo se nos escapa**. Los cuatro de abajo
habían pasado todas las capas de auditoría anteriores, y los cuatro tienen el mismo perfil: **un
instrumento que informa OK sobre algo que no ha comprobado.**

1. **La credencial de IA (C2PA) se declaraba de MENOS.** `normalizar_png.py` reinyectaba el chunk `caBX`
   byte a byte tras reescalar y decía `automática (C2PA presente)`. Pero un manifiesto C2PA **firma un
   hash de los píxeles**: al reescalar, el chunk sobrevive y **el manifiesto deja de validar**. Meta no lo
   lee → no etiqueta → y nosotros habíamos anotado que no hacía falta declararlo a mano. Eso es
   desaprobación del anuncio y penalización en la cuenta. Ahora el veredicto mira **las dos cosas**
   (credencial Y si hubo reescalado) y una pieza reescalada dice **MANUAL PENDIENTE** y sale con código 1.
   *La lección: «el dato sigue ahí» no es «el dato vale».*

2. **El medidor de zonas seguras decía «a revisar» sobre piezas que no había medido.** Su veredicto por
   defecto era `revisar`, y cuando el tamaño no era 1080 exacto **retornaba antes de medir un píxel**. Las
   12 piezas `Cliente 04-APROBADO` (900×900 y 900×1600) salían «12 a revisar, código 1» — y eso se leyó como
   «el medidor suspende el estándar de oro». No lo suspendía: **no lo miraba**. Ahora el default es
   `no_concluyente` y dice `NO MEDIDA` con el motivo.

3. **Y al revés: daba «✓ limpia» con texto fuera del mínimo duro.** En 9:16 los laterales se «informaban»
   y **nunca tocaban el veredicto**, así que una pieza a sangre con el titular a x=0 salía `✓ limpia` con
   código 0 mientras imprimía «por debajo del mínimo 65». Como **el patrón de producción de la casa ES
   foto a sangre**, ese hueco estaba abierto en casi toda la producción real, no en un caso raro. Ahora: a
   sangre **nunca** puede decir `limpia` (techo `no_concluyente`), y un lateral por debajo de 65 degrada a
   `revisar`.

4. **Se medía antes de normalizar.** El medidor estaba en §4 y el normalizado en §5; el GPT no entrega
   1080 → la compuerta dura **no llegaba a medir nunca**. El normalizado se ha movido al final de §3.

Y dos de contrato, que es donde nadie mira porque cada lado «funciona» por separado:

5. **Tres anuncios con el mismo nombre.** El estándar de la casa es `IMG | <ángulo>` y funciona porque en
   la tanda de 9 cada pieza tiene un ángulo distinto. Las variaciones **comparten ángulo por definición**:
   los tres anuncios salían con el mismo nombre y el mismo `utm_content`, así que **la comparación que
   justifica toda la skill era imposible por construcción**. Ahora llevan `| V<n>`.

6. **El índice se llamaba como nadie lo busca.** La skill escribía `specs_VAR_<fecha>.md` y
   `armar-campana-meta` solo abre `specs_Tanda<N>.md`. El campo `IA declarada` y la etapa de embudo no
   llegaban al otro lado. Unificado.

**Para la próxima auditoría:** a un script no se le pregunta qué hace, se le da una entrada conocida y se
mira la salida. Las cuatro primeras se cazaron ejecutando, no leyendo.
