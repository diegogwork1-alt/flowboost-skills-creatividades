---
name: copy-anuncios-meta
description: Escribe el COPY de un anuncio de Meta (texto primario + título + descripción + botón CTA) basándose en el ESTÁTICO (la imagen del anuncio: la produce la skill `estaticos-meta` con el GPT) y el GUION del video de ese anuncio, más el contexto del brief del cliente. Copy corto y persuasivo estilo Ogilvy (respuesta directa). NUNCA inventa cifras, testimonios ni datos: lo que falta lo marca [FALTA]. Da 2-3 variantes por campo para testear. Alimenta a armar-campana-meta. Usar cuando Dirección pida "el copy del anuncio", "copy para Meta", "textos del ad" a partir del estático y/o el guion.
---


> 📐 **PARÁMETROS DE COPY DE LANDING, CON SU FUENTE:** `../fundamentos-copy/references/parametros-landing.md`. Ahí están una sola vez y **con la fuente de cada una** las reglas que antes estaban repartidas y desiguales entre las 9 skills de landing: frases ≤15 palabras · párrafos ≤2 oraciones · **prohibido el guion largo (—)** · el titular responde «¿por qué me importa?» · **2-3 testimonios reales** y nunca en carrusel en móvil · **nunca «sin compromiso» ni «gratis»** bajo el CTA · y **qué cifras NO están en las fuentes** (los umbrales de Core Web Vitals y el impacto de la velocidad en conversión: si alguien las cita como dato propio, es una alucinación).
# Copy de anuncios para Meta (desde el estático + el guion)

> **Idioma (regla dura de Dirección):** todo texto destinado al cliente o a su público sale en **español de España** (tuteo tú/vosotros, léxico de España). Cero voseo ni léxico LATAM (❌ vos/tenés/agendá/celular → ✅ tú/tienes/reserva/móvil). Única excepción: clientes cuyo mercado no sea España (hoy Cliente 07, en inglés).

Generás el **texto del anuncio de Meta** de UN anuncio, coherente con dos cosas: la **pieza estática** (la produce `estaticos-meta` en `2. Ads/Estáticos/GPT/Tanda N/`) y el **guion del video** de ese mismo anuncio. El copy nunca contradice lo que muestra el estático ni lo que dice el guion; los refuerza. Estilo: **respuesta directa, corto y persuasivo, principios Ogilvy**.

> **FUENTES DE AUDITORÍA — las mismas que audita el copy del estático** (unificado 07-09-2026; antes esta skill solo tenía el resumen destilado y por eso el texto del post se juzgaba con menos vara que el texto de la imagen). Una sola copia de cada documento para todo el agente; se leen de la skill de estáticos:
> - **`../fundamentos-copy/references/ogilvy-reglas-reales.md`** — las reglas REALES sacadas del libro (`../fundamentos-copy/references/ogilvy-on-advertising.pdf`), con los **16 checks O1-O16**. **Manda sobre `../fundamentos-copy/references/ogilvy-principios.md`** de esta skill, que es un resumen de memoria y quedó superado para auditar (vale como recordatorio al REDACTAR, nunca para auditar: para auditar manda `../fundamentos-copy/references/ogilvy-reglas-reales.md` (16 checks O1-O16, extraídos del libro)).
> - **`../estaticos-meta/references/audit-copy-por-formato.md`** — informes NotebookLM de Dirección: qué debe decir y qué es FAIL **en el formato del estático** al que acompaña este copy (advertorial, antes/después, review, stat drop, oferta…). Incluye la **§0 de fechas y años**.
> - **`../fundamentos-copy/references/headlines-playbook.md`** — patrones de titular que rinden.
> - **`../fundamentos-copy/references/breakthrough-schwartz.md`** (+ `../fundamentos-copy/references/breakthrough-advertising.pdf`) — **nivel de consciencia y sofisticación** del avatar: decide cuánto hay que explicar y por dónde entra el copy. Tráfico frío no lee lo mismo que retargeting.
> - **`../estaticos-meta/references/informe-b2b-100-reglas.md`** y **`../estaticos-meta/references/informe-b2b-enciclopedia.md`** — solo cuando el cliente es **B2B** (los dos informes 2026).
> - **`../fundamentos-copy/references/lo-que-no-funciona.md`** — anti-patrones y compliance de Meta.
>
> Al redactar: Ogilvy (beneficio en el titular, específico con número/plazo, "flag" al nicho, "Cómo X sin Y", Voice of Customer, sin jerga, sin auto-bombo, prueba con hecho/cifra, honestidad) + el nivel de consciencia de Schwartz.

## Entradas (por anuncio)
1. **Estático:** la imagen del anuncio (local `~/Desktop/CLIENTES/<cliente>/Ads/GPT/` o Drive `2. Ads/Estáticos/GPT/Tanda N/`). **Miralo** (léelo como imagen): qué titular/claim trae, qué muestra, a qué avatar apunta, qué promesa o gancho ya comunica. El copy tiene que **encajar** con eso, no repetirlo palabra por palabra ni contradecirlo.
2. **Guion del video** del anuncio (`.md`, de `2. Ads/EGC/Guiones/Tanda <N>/`): el ángulo, el hook, el dolor, el mecanismo y el CTA hablado. El copy toma de ahí el ángulo y el wording real.
3. **Brief del cliente** (`0. Onboarding`): marca, **tono de voz**, avatar, oferta, prueba/autoridad, **idioma/mercado**, y **claims prohibidos/compliance**. Si falta, `[FALTA — preguntar]`.

Si falta el estático o el guion, avisá y pedilo; podés hacer un borrador con lo que haya, marcado como provisorio.

## Salida (campos de Meta, con límites)
Por cada anuncio, entregá:
- **Texto primario** (primary text) — el gancho arriba del "ver más". Ideal **≤125 caracteres** la primera línea; podés seguir después. **2-3 variantes.**
- **Título** (headline) — beneficio concreto, **≤40 caracteres** ideal. **2-3 variantes.**
- **Descripción** (opcional, ≤30 caracteres ideal).
- **Botón CTA** — de la lista de Meta (Más información / Enviar mensaje / Reservar / Registrarte / Obtener oferta…). Elegí el que matchee la acción real del funnel (normalmente el que lleva a la landing/formulario).

Formato de entrega:
```
### Anuncio N — <ángulo>
Texto primario:
  A) ...
  B) ...
Título:
  A) ...   B) ...
Descripción: ...
Botón CTA: <...>
Notas: (qué del estático/guion se usó; [FALTA] si hubo huecos)
```

## Reglas (Ogilvy + honestidad)
- **Beneficio y especificidad** en el titular; "flag" al nicho cuando aplique.
- **Voice of Customer:** usá las palabras reales del cliente/avatar del brief, no jerga corporativa.
- **Sin auto-bombo:** cada afirmación con un hecho/cifra del brief; si no hay respaldo, no la hagas.
- **NUNCA inventes** cifras, resultados, testimonios, plazos ni garantías. Si el estático o el guion muestran un número, usalo tal cual; si no está respaldado en el brief, no lo pongas.
- **Compliance:** respetá los claims prohibidos del brief y las políticas de Meta (salud/finanzas: sin promesas absolutas ni segmentación por condición personal).
- **Fechas y años: contra el reloj del sistema, no de memoria** (`date +%d/%m/%Y`, `date +%Y`). Toda fecha visible tiene que ser de **hoy o futura** y todo año ("informe 2026", "promoción 2026") el **año en curso**: una fecha pasada hace ver el anuncio caducado. Si el mensaje no depende de un día concreto, mejor sin día — el copy vive semanas. Los plazos ("válido hasta…") tienen que seguir vivos al publicar y coincidir con la landing.
- **Idioma/tono:** los del brief. Corto: frases y palabras cortas.
- Coherencia total estático ↔ guion ↔ copy (mismo ángulo y promesa).

## Variantes para testear
Por defecto 2-3 variantes de texto primario y de título (distinto ángulo/énfasis del MISMO mensaje real, no claims nuevos). Sirven para que Meta optimice.
**Nomenclatura fija:** las variantes se nombran A/B/C y quedan atadas al anuncio: `AnuncioN-copyA`, `AnuncioN-copyB`. Si el video editado tiene variantes de hook (hookA/hookB), el copy A acompaña al hook A, etc. — misma letra, mismo ángulo.

## Idioma
El del **brief** del cliente. Por defecto español; hoy el único funnel en inglés es **Cliente 07**. Nunca mezclar idiomas entre estático, guion y copy.

## Auditoría del copy (ANTES de entregar — no es opcional)
Se corre sobre cada variante, igual que el audit del estático corre sobre cada imagen. Cualquier fallo → reescribir, no entregar.
1. **Los 16 checks de Ogilvy** (`../fundamentos-copy/references/ogilvy-reglas-reales.md`): beneficio en el titular, específico y no genérico, no "ciego", sin juegos de palabras, cita entrecomillada si la hay, sin auto-bombo, honestidad total.
2. **El formato del estático** (`../estaticos-meta/references/audit-copy-por-formato.md`): el copy tiene que sonar a SU formato; ahí está el PASS/FAIL y la severidad de cada uno. Un advertorial con gancho de venta directa es FAIL aunque el copy esté bien escrito.
3. **Schwartz**: ¿el copy entra por el nivel de consciencia real del avatar, o le habla como si ya conociera la solución?
4. **Fechas y años** (`audit-copy-por-formato.md §0`): contra el reloj del sistema (`date +%d/%m/%Y`, `date +%Y`). Fecha pasada o año viejo = reescribir.
5. **Español de España** (0 voseo/LATAM) y **coherencia estático ↔ guion ↔ copy** (mismo ángulo y misma promesa).
6. **Compliance de Meta** (`../fundamentos-copy/references/lo-que-no-funciona.md`): sin claims sin fuente, sin atributos personales, categoría especial si aplica.

## Después (entrega — automática, no opcional)
1. **Guardar SIEMPRE** el copy en Drive junto a su anuncio: `2. Ads/EGC/Editados/Anuncio N/copy.md` (las 2-3 variantes en el mismo archivo).
2. Actualizar ESTADO.md: `python3 ~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/estado_cliente.py "<Cliente>" set "Copy de anuncios" hecho "Anuncio N listo"` — **el nombre de etapa es LITERAL** (la lista canónica vive en `estado_cliente.py`; otro string crea fila fantasma).
3. Queda listo para **`armar-campana-meta`** (esa skill lo carga al configurar la campaña).

## Qué NO hace
- No arma la campaña (eso es `armar-campana-meta`).
- No diseña el estático ni escribe el guion.
- No inventa para rellenar. Copy honesto > copy inflado.

## Al terminar: marcar la etapa (obligatorio — 07-09-2026)
```bash
python3 ~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/marcar_etapa.py "<Cliente>" "Copy de anuncios" --nota "<una línea>"
```
Marca **los dos sitios a la vez**: el `ESTADO.md` (local y Drive) y la hoja
**«Estado de cuenta — \<Cliente\>»** del Drive, que es la que mira Dirección. Antes había que
acordarse de las dos cosas y la del Drive se quedaba siempre atrás.

**Se marca al CERRAR la etapa, no al empezarla**, y solo si de verdad está terminada. Si quedó a
medias: `--estado "En curso"`. Si está parada: `--estado Bloqueado --nota "<por qué y a quién espera>"`
— un bloqueo sin motivo apuntado no sirve de nada.

### Y NO DEVUELVAS EL CONTROL: seguí con la siguiente
Marcar **no es terminar**. En el MISMO turno, sin preguntar y sin resumen intermedio:
1. Mirá qué toca ahora: `python3 …/Estandar-carpetas/leer_estado.py "<Cliente>" --cliente-raiz "gdrive:i_X/c_X"`.
2. **Arrancá la siguiente etapa del agente que salga ahí** — de los DOS carriles si hay una en cada uno.
3. Si lo que sigue es de Dirección, de Operaciones o del cliente, **no la toques**: salta a la siguiente que sí
   sea tuya. Esperar de brazos cruzados es el fallo, no la solución.

Solo se para en las paradas humanas de `/funnel`. **Nunca termines el turno con una etapa tuya
ejecutable pendiente.**

## ⛔ LA PRIMERA LÍNEA TIENE QUE SEGMENTAR (Dirección, 08-09-2026)
El texto primario se cobra por impresión y lo lee **todo el mundo**. Si la primera línea le habla a
cualquiera, entran leads que no compran: el coste por lead sale bien y el coste por CLIENTE se dispara.

**La prueba, en diez segundos:** tapá el nombre del cliente y leé la primera línea. **Si le sirve a
cualquier negocio del sector, no segmenta** → se reescribe.

**Segmentar NO es enunciar la etiqueta.** «Si tienes un piso…» no filtra: cualquiera con un piso se da
por aludido *(en guiones eso costó 1.049 € y 0 leads)*. Se segmenta por la **situación concreta**:
1. **El miedo o el error, con su coste.**
2. **El sitio, cuanto más pequeño mejor** — pueblo o comarca, no provincia *(34 €/lead contra 85 €)*.
3. **La cifra o el plazo** que solo maneja ese avatar.
4. **El momento** en el que está, no quién es.

**Y tiene que coincidir con el gancho del guion y con el titular del estático.** Si el vídeo filtra a un
avatar y el copy a otro, el anuncio se contradice solo y el clic llega frío a la landing.
