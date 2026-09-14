# Producción de estáticos — cómo se llega al PNG final

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

> **Modelo vigente (decidido por Dirección):** el **GPT "Generador Ads Imagen" genera la imagen FINAL con el copy ya dentro**, a partir del brief + logo + fotos/avatar adjuntos. La skill **audita** y manda CAMBIOS. Las plantillas HTML de `templates/` son **solo el plan B** (si el GPT/cuenta no está disponible o hace falta tipografía exacta). *(La versión anterior de este doc describía un "sistema híbrido" —ChatGPT hace el fondo y una plantilla HTML pone el texto—; ese modelo quedó descartado el 05-09 cuando Dirección pasó la config de su GPT.)*

> Regla que se rompió una vez y NO se vuelve a romper: **las safe zones son restricción dura**. Ningún texto, logo ni CTA fuera del área segura. Ver §3.

---

## 1. Cantidad: la tanda
- **Una TANDA = la secuencia de 9 formatos del GPT** (Anuncio 1..9, en cadena, mismo chat), **cada uno en 1:1 + 9:16**.
- **Cadencia oficial (Dirección, 07-09-2026):**
  - **Tanda de LANZAMIENTO: mínimo 6 piezas aprobadas**, en los días 1-2. Con eso se sale al aire; no se espera a las 9.
  - **A partir de ahí: una tanda de 9 cada DOS SEMANAS.** No mensual.
- La skill **siempre genera los 9**; **qué sale a rodar lo decide `armar-campana-meta`** (montaje inicial) o `gestion-cuenta-meta` (reemplazos semanales, por causa de muerte). Producir no es publicar.
- **Al cerrar cada tanda se le manda al cliente el mensaje de entrega** (`Documentos-Flowboost/Onboarding/mensaje-estaticos.md`) con plazo de revisión de **3 días**, y un aviso `info` a Dirección con `avisar.py`. Sin ese mensaje el cliente no se entera de que hay material nuevo.

## 2. Pipeline por pieza (resumen — el detalle operativo es el PROTOCOLO POR ANUNCIO del SKILL)
1. **Insumos** (Fase 0): `Brief_<Cliente>.txt` (convertido con `brief_a_texto.py`; **el PDF NO se sube al GPT**: ya falló una vez y el GPT se inventó el cliente), logo oficial (`Insumos/logo/`), paleta/tipos del manual, fotos reales de `1. Branding`.
2. **Persona**: si el formato la necesita y no hay foto real del cliente → persona real de stock gratuito (Unsplash/Pexels/Pixabay), **estética española**, natural, previsualizada antes de bajar, **2-3 por tanda y la misma cara como mucho en 2 piezas** (ver SKILL §Personas: una sola cara repetida anula el set) (`~/Desktop/CLIENTES/<cliente>/Insumos/personas/avatar_<cliente>_<desc>.jpg`, + copia en scratchpad para subirla). El GPT la **recrea**; no se usa el stock literal.
3. **Generar con el GPT** (Fase 2.5): en cada mensaje van adjuntos **logo oficial + avatar**; se pide la estructura del formato, español de España, título sin punto, sin texto en atrezo, los 54 px de cada borde libres (en píxeles, nunca en porcentaje) y nada cortado.
4. **Auditar** (Fase 3): §0 juicio de DC + §G checklist visual + Ogilvy O1-O16 + titulares + copy por formato + playbook visual. CAMBIOS puntuales hasta que pase.
5. **Los dos ratios**: 1:1 y luego 9:16 nativo (re-adjuntando logo y avatar), auditados los dos.
6. **Guardar** (Fase 4): descargar → `~/Desktop/CLIENTES/<cliente>/Ads/GPT/` (nunca dejarlo en Descargas) → `rclone copy` a `gdrive:i_<C>/c_<C>/2. Ads/Estáticos/GPT/Tanda <N>/` + `specs_Tanda<N>.md`.

## 3. Safe zones (restricción DURA — valores de la casa)
- **1:1 (1080×1080):** margen mínimo **5% (≈54 px)** en los 4 bordes. Texto, CTA y logo dentro.
- **9:16 (1080×1920):** el fondo/diseño llena TODO el lienzo; el texto/logo/CTA respetan las zonas muertas:
  - **Arriba 14% ≈ 270 px** libre (perfil/controles).
  - **Abajo 20% ≈ 384 px** libre — **valor de trabajo de la casa** (Stories); el CTA por encima. → área útil de texto ≈ **1080 × 1266 px**.
  - **Laterales: 65 px es el MÍNIMO TÉCNICO (6 %); el margen de composición de la casa es 107 px.** Sale de las 6 piezas 9:16 aprobadas de Cliente 01 (`refs/00_9x16-verticales/LEEME.md`). **Corrección del 11-09-2026: la cifra exacta la usan DOS de las seis** (advertorial y review), más «sin papeleos» en el lado que se pudo medir; las otras tres van a 106, 110-134 y 138-142. Antes aquí ponía «cinco de seis», que la propia tabla desmiente. Lo que sí sostiene la tabla: **ninguna baja de 106**, o sea que **el suelo real de la casa está en ~107, no en 65**. **Se pide 107 en el prompt**; 65 es solo la línea que no se puede cruzar. Con 65 la pieza se ve apretada.
  - El **35 % ≈ 672 px** abajo (área central 950×979) **es la cifra que publica Meta**, no una versión extrema. ⚠️ **Ojo al origen de estos números (§0-bis de `reglas-tecnicas-y-copy.md`, contrastado con las fuentes el 11-09-2026): Meta publica 269 arriba / 672 abajo / 65 lados. Los 384 son una apuesta de la casa y los 107 una preferencia sin fuente. Entre y=1248 y y=1536 no puede ir CTA, logo ni claim, aunque nuestro valor lo permita.**
- `../templates/render.py` (plan B) inyecta estos valores como variables CSS por tamaño (`story` = 270/384/65; `story35` = 270/672/65) y con `--guides` dibuja las zonas para QA.

## 4. Cuenta y navegador (regla firme)

> **Por qué Claude-in-Chrome y no el navegador interno de Claude Code.** Comprobado el 06-09-2026: el navegador interno (`mcp__Claude_Browser__*`) **no tiene herramienta de subida de archivos** — no existe `file_upload` ni `upload_image`, solo las hay en `mcp__claude-in-chrome__*`. Sin poder adjuntar, no se puede cumplir la regla de mandarle al GPT **el logo oficial y el avatar en cada generación**, que es justo lo que arregló la deformación del logo. Además, el navegador interno abre un perfil limpio, sin la sesión de `<correo-cuenta-de-trabajo>`, así que habría que iniciar sesión a mano en cada uso. Para leer una web, comprobar una landing o mirar la consola, el navegador interno vale y es más barato. **Para el GPT de imágenes, Claude-in-Chrome es obligatorio.**
- Se genera en ChatGPT vía **Claude-in-Chrome**. **La cuenta del GPT es la de Flowboost EMPRESA, pero se entra por el Google `<correo-cuenta-de-trabajo>`.** Son dos cosas distintas y hay que tenerlas claras: el **workspace** de ChatGPT es el de la empresa (se ve como «Flowboost Marketing» / «Flowboost Marketing Empresa») y eso es lo CORRECTO — ver ese nombre NO significa que estés en la cuenta equivocada. Lo que identifica la sesión buena es el **email de Google con el que se ha iniciado sesión**, que tiene que ser `<correo-cuenta-de-trabajo>`. **NUNCA `<correo-direccion>`**, aunque ese email también lleve a un workspace de Flowboost.
- **Comprobación obligatoria antes de enviar nada:** `/api/auth/session` devuelve el email del usuario. Si devuelve `<correo-cuenta-de-trabajo>` → adelante (el workspace dirá «Flowboost Marketing»: correcto). Si devuelve `<correo-direccion>` → **hay que cambiar de perfil de Chrome. Cómo se hace, que no estaba escrito en ningún sitio:**
  1. `mcp__claude-in-chrome__list_connected_browsers` → lista los Chrome conectados.
  2. Si hay más de uno, `select_browser` / `switch_browser` con el que corresponda, y **volver a comprobar `/api/auth/session`**.
  3. Si solo hay uno y es el equivocado, el cambio de perfil **lo tiene que hacer Dirección en Chrome** (icono de perfil → el de `<correo-cuenta-de-trabajo>`). Entonces: `avisar.py --nivel urgente` diciendo exactamente eso, **se sigue con todo lo que no necesite el GPT** (branding, insumos, specs, subidas de lo ya descargado) y se cuenta en el resumen final. **No se genera ni una pieza con la cuenta equivocada, y no se espera de brazos cruzados.** Nunca te guíes por el nombre del workspace para decidir: el workspace es el mismo de la empresa en los dos casos.
- Envío con clic JS al botón (`button[data-testid="send-button"]`), no por coordenada/Enter. Adjuntos con `file_upload` sobre el input de archivo. Mecanismo de descarga y localización de la imagen del último turno: ver `prompts-gpt.md`.

## 4-bis. SI SE CAE CHROME: RECUPERARSE SOLO, NUNCA ESPERAR (Dirección, 07-09-2026)
Chrome se cae a mitad de tanda y **el agente NO puede quedarse esperando a que Dirección lo levante**. Pasó dos veces en el test ("te dejo el punto exacto", "cuando vuelva Chrome sigo"): eso convierte una tanda automática en una tarea manual de Dirección.

**Anotar el avance SIEMPRE, para poder retomar sin pensar.** Tras cerrar cada anuncio, escribir una línea en `~/Desktop/CLIENTES/<cliente>/Ads/GPT/PROGRESO-Tanda<N>.md`: anuncio, ratio, estado (auditado / pendiente 9:16 / nota del panel) y la **URL del chat del GPT**. Ese fichero es lo que hace la recuperación determinista.

**Al detectar que el navegador no responde** (la herramienta da error, no hay pestañas, la pestaña está en blanco):
1. **Reintentar la conexión**: listar navegadores/pestañas otra vez; si no hay ninguna, abrir una nueva.
2. **Volver al chat del GPT** por su URL guardada en PROGRESO y **verificar la sesión** (`/api/auth/session` → tiene que devolver `<correo-cuenta-de-trabajo>`).
3. **Retomar desde la última línea del PROGRESO**, no desde el principio: si el 1:1 del anuncio N estaba aprobado y faltaba el 9:16, se pide el 9:16.
4. **Hasta 3 intentos**, con una espera creciente entre ellos. Si a la tercera sigue caído: anotarlo en PROGRESO y en `specs_Tanda<N>.md`, **seguir con todo lo que no necesite navegador** (specs, subidas a Drive de lo ya descargado, ESTADO.md) y contarlo **solo en el resumen final**.
5. **Prohibido** terminar el turno con un "cuando vuelva Chrome sigo" o dejarle el punto exacto a Dirección para que lo retome él.


## ⚠️ RENDERIZAR CON CHROME: usar SIEMPRE `render_chrome.py` (Dirección, 07-09-2026)
**Chrome headless genera el fichero y NO se cierra.** Un `subprocess.run(chrome …)` sin timeout se queda colgado esperando a un proceso que nunca termina, y cada pasada deja procesos vivos: catorce renders del PDF de la guía dejaron **45 procesos y ~2,9 GB de RAM** ocupados en el Mac. En una tanda de estáticos, con sus iteraciones, es peor.

**Nunca invocar Chrome a mano.** Para cualquier HTML → PDF o PNG:
```bash
python3 ~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/render_chrome.py \
    entrada.html salida.pdf                 # PDF
python3 …/render_chrome.py entrada.html salida.png --size 1080x1920   # PNG
```
Lanza Chrome en su propia sesión con perfil temporal, **espera al FICHERO y no al proceso**, y **mata el árbol entero y borra el perfil en un `finally`**: salga bien, falle o se cuelgue, no queda nada corriendo.

## 5. Branding — origen y fallback
- **Origen:** `1. Branding` del cliente en Drive (logo final en `Archivos_Finales_*/RGB/02_PNG/`, **nunca `Logos Antiguos`**; verificar contra la web del cliente). Manual de identidad → paleta y tipografías. La skill lo saca sola; Dirección no sube nada.
- **Si falta branding en Drive → SACARLO DE LA WEB DEL CLIENTE (Dirección, 07-09-2026). No se para ni se pregunta.** La URL está en el brief. Orden:
  1. **Logo:** buscarlo en la web en el mejor tamaño disponible — el `<img>` de la cabecera, el del pie, el `og:image`, el SVG si lo hay (un SVG es lo mejor: escala sin perder), y como último recurso el favicon de mayor resolución (`apple-touch-icon`). **Preferir siempre PNG con transparencia o SVG**; si solo hay logo sobre fondo, recortarlo limpio. Guardarlo en `~/Desktop/CLIENTES/<cliente>/Insumos/logo/`.
  2. **Paleta:** muestrear los colores reales del CSS de la web (color de marca del botón/CTA, del encabezado, del fondo) — no inventarlos "a ojo" desde una captura.
  3. **Tipografías:** leerlas del CSS (`font-family`, los `@font-face`, el enlace de Google Fonts). Si es una fuente de pago que no tenemos, usar la equivalente libre más cercana y **anotar la sustitución**.
  4. **Anotar el origen** en `Insumos/FALTA_BRANDING.md`: qué se sacó de la web, de qué URL y qué quedó sustituido, para que Dirección lo valide cuando quiera. **Esto NO bloquea la tanda: se produce igual.**
  - Solo si el cliente **no tiene web ni logo en ninguna parte** se deja constancia y se sigue con los formatos que no dependan del logo. Ni se para ni se avisa a mitad.
- **Si falta el brief — fallback vigente:** (1) NO inventar marca; (2) dejar `~/Desktop/CLIENTES/<cliente>/Insumos/FALTA_BRANDING.md` con la lista exacta de lo que falta; (3) seguir con lo que sí se pueda producir y llevarlo al **resumen final** de la tanda — nunca cortar a mitad para avisar. El aviso automático por **email vía n8n** (webhook `estaticos-branding-faltante`) es el canal que Dirección eligió pero **está PENDIENTE de construir en el VPS**; hasta entonces aplica el fallback manual.

## 6. Plantillas HTML (`templates/`) — PLAN B, ahora con los 9 formatos cubiertos
Se usan cuando el GPT/la cuenta no están disponibles, y cuando hace falta **fidelidad tipográfica exacta** (el GPT no puede cargar las fuentes reales de la marca, solo emularlas — `errores-y-aprendizajes.md §11`).

- `../templates/testimonio.html` → **3 · Review+Claim** (lo que en la casa se llama «Testimonio»)
- `../templates/antes-despues.html` → **2 · Antes/Después**
- `../templates/editorial.html` → **1 · Artículo/Noticia** — masthead de medio en vez de logo, foto como figura de artículo y logo a firma de pie
- `../templates/titular-lista.html` → **4 · Característica→Beneficio**, **7 · Oferta/Escasez** y **9 · Garantía** (cambia qué es la lista: checks / ítems de oferta / sellos)
- `../templates/dos-bloques.html` → **5 · Objeciones** («lo que crees» vs «la realidad») y **6 · Pain** (problema arriba, solución abajo)
- `../templates/numero.html` → **8 · Prueba social (Stat Drop)** — la cifra domina, con su línea de fuente obligatoria al pie
- `../templates/render.py` — rellena tokens y exporta PNG (`--size cuadrado|story|story35|WxH`, `--guides` para QA, `--sin-logo` para el advertorial). **Falla si falta un token** y **falla si `LOGO_SRC` viene vacío** sin `--sin-logo`.
- `../templates/poner_logo.py` — compone el PNG oficial del logo en post. **Solo si Dirección lo pide.**
- **Recomposición por ratio:** `render.py` marca el `<body>` con `size-cuadrado` / `size-story`, y las plantillas cambian de composición — en 9:16 aplican el patrón medido de la casa (**texto en la mitad superior, foto a sangre por abajo**). Sin eso, una maqueta de 4:5 estirada a 1920 abría un agujero del 38-44 % antes del CTA. Si la pieza va **sin foto**, se añade `sin-foto` y el contenido se reparte por toda la altura en vez de dejar muerto el tercio inferior.
