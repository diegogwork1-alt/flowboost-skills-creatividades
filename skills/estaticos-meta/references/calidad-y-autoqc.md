# Calidad y AUTO-QC — la skill se supervisa sola (Dirección NO revisa cada pieza)

Regla de Dirección: **"yo no puedo estar supervisando tanto".** La skill debe **auto-evaluar cada creatividad y re-iterar sola** (mandar CAMBIOS al GPT con instrucciones concretas) hasta que pase el bar, y recién ahí guardar. Dirección solo ve el resultado final en Drive.

## §0. JUICIO DE DIRECTOR CREATIVO (gate que MANDA sobre todo el checklist)
Un checklist que aprueba un anuncio mediocre NO SIRVE. Antes de tildar nada, juzgar como DC crítico: **¿esto es un buen anuncio — para el scroll, se ve premium y on-brand, y da ganas de clickear — o es genérico/mediocre?** Si es mediocre/genérico/aburrido → **REJECT y regenerar**, aunque pase todas las casillas. Fallos de calidad que el checklist NO ve y hay que cazar SÍ o SÍ:
- **Persona genérica tipo stock / cara IA sin alma** (sonrisa corporativa, modelo de banco de imágenes) → REJECT. Las caras deben verse **auténticas** (cliente real / UGC). Un placeholder de testimonio puede llevar cara, pero NO puede parecer stock genérico. (Matiz: sí se permite **buscar una persona en stock gratuito como REFERENCIA para que el GPT la RECREE** —SKILL Fase 2.5— elegida natural/candid y acorde al avatar; lo que se juzga acá es el RESULTADO: si la cara final se ve posada/corporativa/IA → REJECT igual.)
- **Diseño genérico "de anuncio"** que no frena el scroll → REJECT.
- **DIVERSIDAD en la tanda:** cada uno de los 9 debe ser **visiblemente distinto**. NO repetir el **mismo CTA** en todos (variar el CTA por pieza), ni el mismo layout/estructura/encuadre/mecanismo. *(Ojo a no confundirlo con §A-quinquies: el CTA varía **entre piezas distintas**, pero es IDÉNTICO entre el 1:1 y el 9:16 de la MISMA pieza.)* Si dos piezas se parecen → REGENERATE la segunda con otro recurso.
- **CERO arrastre de otro formato:** elementos de un formato NO pueden aparecer en otro. Ej: **"IDEAS PERSONAS PATRIMONIO"** y el masthead editorial son SOLO del advertorial (Anuncio 1); si aparecen en Antes/Después, Review, etc. → REGENERATE sacándolos. Cada formato con su propio chrome.
- **Copy tibio/genérico** (aunque cumpla el techo de palabras) → REJECT; el hook debe tener tensión/beneficio real.
- **NADA de texto/frasecitas en props** (tazas, camisetas, carteles de atrezo, post-its con eslóganes tipo "TU PATRIMONIO TRABAJA", "DEMASIADO TIEMPO", "MEJORES PERSONAS MEJORES CIUDADES") → REJECT. Dirección NO quiere ese recurso cutre. El copy va en la jerarquía del anuncio (titular/apoyo/CTA), no metido en objetos de la escena.
- **MINIMALISMO real (1 idea, mucho aire) — regla dura:** si la pieza tiene RUIDO VISUAL (muchos elementos compitiendo: dos columnas + pilas de papeles + persona + fondo recargado + badges + CTA todo a la vez) → REJECT y **simplificar a UNA sola idea con máximo espacio negativo**. Ej. Feature→Beneficio: NO comparativa recargada Sin/Con con atrezo; SÍ un visual limpio (persona o inmueble) + titular-beneficio + máx 3 checks cortos + CTA, con aire. Entre dos opciones, la de MENOS elementos. (Doctrina `sistema-director-creativo.md`.)
- **ANATOMÍA / artefactos de IA:** revisar que las personas estén BIEN (2 brazos, 2 manos, dedos correctos, cara sin deformar, nada fundido con el fondo). Un brazo/mano/dedo mal o "que falta" → REJECT/REGENERATE ("corrige la anatomía: la persona debe tener ambos brazos y manos naturales"). Los modelos de imagen deforman cuerpos: mirarlo SIEMPRE.
- **NINGÚN elemento cortado/clippeado por el borde** (regla dura de Dirección): grids, tarjetas, columnas (ej. la caja "CON Cliente 04"), textos, logo, CTA, personas clave — TODO entero dentro del marco, sin que se corte contra el borde del lienzo. Si un grid/tarjeta/palabra queda cortado o pegado al borde → REGENERATE ("centra y encoge el grid para que entre completo dentro de la safe zone, sin cortes"). Revisar los 4 bordes en cada pieza (1:1 y 9:16).
Regla: ante la duda de si es "lo bastante bueno", NO lo es → regenerar. Dirección no tiene que ver anuncios mediocres.

## §0-bis. IDIOMA: ESPAÑOL DE ESPAÑA — SIEMPRE (regla dura, REJECT)
Regla de Dirección (error real: borró una tanda entera del Drive por tener "toques argentinos"). **Todo el copy — titular, apoyo, cita, CTA, kicker, cualquier palabra visible — se redacta en español de ESPAÑA.** El GPT recibe esta instrucción explícita en el prompt y el auto-QC la audita como REJECT.
- **Voseo PROHIBIDO.** Nada de imperativos ni conjugaciones argentinas: ❌ Descubrí, Dejá, Empezá, Sumate, Hacé, Descargá, Aceptá, Cancelá, Conseguí, Ahorrá, Mirá, Fijate, tenés, querés, seguís, sabés. ✅ formas de España: Descubre, Deja, Empieza, Únete, Haz, Descarga, Acepta, Cancela, Consigue, Ahorra, Mira, Fíjate, tienes, quieres, sigues, sabes.
- **Tuteo de España** (tú / vosotros), NO "vos" ni "ustedes" (salvo registro de usted formal si el brief lo pide). Nada de "che", "acá" (→ "aquí"), "recién" con sentido temporal raro, diminutivos rioplatenses.
- **Léxico de España, no LATAM:** ✅ "reserva/reservar", "coche", "móvil", "vale", "piso", "presupuesto", "gestionar". Evitar "agendar" (→ "reservar/pedir cita"), "celular", "carro", "departamento", "checar", "aplicar" (en sentido de postularse).
- El **CTA** también: ✅ "RESERVA TU CITA →", "PIDE PRESUPUESTO →", "DESCUBRE CÓMO →". ❌ "AGENDÁ", "SUMATE".
- **CERO anglicismos en el texto visible** (error real: el GPT puso el CTA "INVIERTE EN REAL ESTATE"): ✅ "inmobiliario", "vivienda", "rentabilidad", "reforma" — ❌ "real estate", "flip", "cash flow", "house flipping", "start now", "book a call". Aunque el sector los use internamente, en el creativo van en español.
- ⚠️ **PRIMERO: ¿en qué idioma va ESTA pieza?** Esta sección entera aplica **cuando la pieza va en
  castellano**, que es lo normal — pero **4 de los 13 clientes no van en castellano**: **catalán** en
  Batlle y Cliente 09, **inglés** en Cliente 07 y Flowboost Dubái (14 de las 94 referencias). El idioma lo fija el
  brief / `patrones-diseno-estaticos.md §2.8`. Aplicar el REJECT de abajo a una pieza catalana o inglesa
  **la rompe**: lo prohibido es el voseo y el léxico LATAM, no el idioma del avatar.
- **Check del auto-QC (solo en castellano):** leer TODO el texto de la pieza; si aparece UNA sola forma no-España → REJECT/CAMBIOS: "reescribe en español de España, cambia «X» por «Y»". No se guarda nada con toques argentinos/LATAM.
- Nota: los ejemplos de los playbooks (`audit-copy-por-formato.md`, `../../fundamentos-copy/references/headlines-playbook.md`) que quedaron en voseo son solo ilustrativos del mecanismo — el copy final SIEMPRE va en España.

## §0-ter — Dos compuertas rápidas de copy (Dirección, 06-09-2026)
- **Test "Ahora puedes…"**: antepuesto al titular. Si sale vago, obvio o exagerado → reescribir. ("Ahora puedes ver qué empresas visitan tu web" pasa; "ahora puedes tener una plataforma potente" falla.)
- **Diversidad de formatos**: la tanda recorre LOS 9 FORMATOS siempre, sin acumularse en los 2-3 favoritos — la diversidad de plantilla es diversidad de ángulo, y el ganador casi nunca es el que habríamos elegido a mano. (Elegir 5 ganadores entre 50 conceptos rinde más que entre 10.)
## §0-quater — PRECEDENCIA de límites de palabras (cierra la contradicción ≤8 vs piezas aprobadas)
El techo de la doctrina (titular ≤5, **total ≤8 palabras**) aplica al **NÚCLEO del mensaje: titular + apoyo**. **NO cuentan para el techo** los elementos de interfaz del formato: CTA del botón, sello/etiqueta de garantía, checks de características, precio "desde X", kicker ni disclaimers — las 12 piezas APROBADAS de Cliente 04 los llevan y son la vara. El `headlines-playbook` (25-40 caracteres) es orientación de estilo: incumplirlo = IMPROVE, nunca REJECT.

**DOS FORMATOS ESTÁN EXENTOS DEL TECHO (regla raíz 2 del `SKILL.md`): Artículo/Noticia (advertorial) y Review+Claim.** Son editoriales/citables y llevan por diseño titular + subtítulo + entradilla/bullets, o una cita de hasta 15 palabras: contarles 8 palabras es pedirles que dejen de ser su formato. Se les acepta pasar del 20 % de densidad de texto (§audit-playbook UNIVERSAL-VISUAL 4) — **pero no están exentos: Meta no exime a ningún formato.** Quitó la regla dura, y el algoritmo sigue penalizando entrega y CPM con mucho texto; lo que aguanta en estos formatos es el *rendimiento*, no la penalización. Es un coste asumido a cambio del formato, y por eso no se estira más de lo necesario. Lo que NO se les relaja: una sola idea, jerarquía clara y todo lo demás del checklist.

**Si dos límites de palabras chocan en cualquier documento de esta skill, gana esta sección.**

## §0-quinquies — La rúbrica que SÍ existe (y por qué NO es una compuerta)
Contrastado el 11-09-2026 con las fuentes reales (NotebookLM «Creativos Meta»): **existe una rúbrica de
puntuación de creatividades, pero NO tiene umbrales de corte.** La fuente la propone para *forzar un
juicio* y para detectar dónde puntúa bajo la competencia, no para aprobar o rechazar.

**Eso confirma que el «Ad Score ≥85 / 70-84 / <70» estaba inventado:** ninguna fuente fija esos cortes.
Sigue sin haber Ad Score numérico, y lo que decide es §0 + §G + los audits + el panel.

Dicho eso, las **cinco dimensiones de la rúbrica sí son útiles** y, al revés que la del informe B2B,
**valen igual para B2C**. Se usan como guía al juzgar, cada una de 1 a 5:

| Dimensión | Peso | 1 punto | 5 puntos |
|---|---|---|---|
| **Especificidad del gancho** | 25 % | frase genérica de categoría | el problema, **en las palabras del comprador** |
| **Claridad de la oferta** | 25 % | sin precio, términos ni plazo | precio, términos y fecha visibles |
| **Prueba** | 20 % | solo adjetivos | números, clientes con nombre o valoraciones de terceros |
| **Anuncio ↔ página** | 20 % | la promesa del anuncio no está en la landing | mismo titular y misma oferta, arriba del pliegue |
| **Ajuste de producción** | 10 % | un recurso reaprovechado | hecho nativo para esa ubicación |

Las dos primeras pesan la mitad: **el gancho y la oferta deciden**. Y «anuncio ↔ página» es el único
check de toda la skill que mira **fuera** de la pieza — si el titular no aparece en la landing, la pieza
puede estar perfecta y el funnel roto igual.

## A. HOOKS — deben frenar el scroll y llevar beneficio
- **Stop-scroller:** pattern-interrupt, tensión, curiosidad fuerte, aversión a la pérdida o especificidad. NADA de titulares tibios/correctos.
- **Beneficio a la vista:** el hook debe insinuar el beneficio/transformación real del brief (no solo curiosidad vacía). Sin inventar cifras.
- ≤8 palabras en el núcleo (titular + apoyo), titular ≤5 — con las exenciones y las exclusiones de **§0-quater** (advertorial y Review+Claim exentos; CTA/sellos/checks/kicker no cuentan).
- Malos (rechazar): "El inmobiliario vuelve a captar el interés de los ahorradores" (titular de diario tibio), "¿Y si tus ahorros pudieran trabajar en lugar de esperar?" (curiosidad sin beneficio claro ni tensión).
- Mejores (dirección, adaptar al brief y sin claim inventado): loss-aversion ("Tu dinero parado hoy vale menos mañana"), barrera rota ("Invertir en inmobiliario ya no es solo para ricos"), específico del avatar ("Ahorros quietos = dinero que se encoge").

## A-bis. TÍTULOS NUNCA CON PUNTO FINAL (regla dura, todos los anuncios)
- Ningún titular de anuncio termina en **punto** (frena la lectura; Ogilvy). Sin punto final. (Signos de ? ! sí pueden ir si el hook lo pide; el punto NO.) Check obligatorio del auto-QC → si el titular tiene punto, CAMBIOS: "quita el punto final del titular".

## A-ter. ¿SEGMENTA el titular? (regla dura, REGENERATE — Dirección, 08-09-2026)
**Tapa el nombre del cliente y lee el titular. Si le sirve a cualquier negocio del sector, no segmenta
→ REGENERATE.** El que no es el cliente tiene que ver de un vistazo que no va con él.

**Cómo se comprueba: las tres pruebas del §H.3** (nombrar la tarea concreta · efecto fiesta de cóctel ·
pregunta que autocalifica). **Basta con que pase una.**

> ⚠️ **Matiz que antes se leía como contradicción.** Aquí ponía que «no vale enunciar la etiqueta
> («si tienes un piso», «para autónomos»)», y el §H.3 dice que apelar al rol **sí** funciona. Las dos
> cosas son ciertas y la diferencia es esta: **la etiqueta SOLA no filtra** —cualquiera con un piso se
> da por aludido— pero **la etiqueta + la situación sí**. «Para autónomos» no segmenta; «Autónomos que
> facturan por encima de X y siguen haciendo las facturas a mano» segmenta. Lo que filtra es el
> **detalle que solo tu avatar reconoce como suyo**: el miedo con su coste, el pueblo (no la
> provincia), la cifra que solo él maneja, o el momento exacto en el que está.

**Y tiene que coincidir con el gancho del guion y con la primera línea del copy.** Tres piezas
segmentando a tres avatares distintos es un anuncio que se contradice solo.

## A-quater. ¿ESTO ES DEL CLIENTE DE VERDAD? (regla dura, REJECT — Dirección, 08-09-2026)
Si el brief no llegó a subirse, el GPT **se inventa el cliente** y la pieza sale impecable pero falsa.
La auditoría visual no lo pilla: hay que buscarlo a propósito.

**En cada pieza, contrastar contra el brief lo que se puede contrastar:** el servicio que anuncia, la
ciudad/zona, la cifra que aparezca, el nombre de la marca y el tipo de cliente al que le habla.
**¿Hay algo que el brief no dice? → REJECT y volver a generar CON el brief adjunto y comprobado.**

Señal típica de pieza inventada: todo genérico y plausible, sin un solo dato que solo pueda salir del
brief. Si la pieza le vale igual a un competidor, es que se generó sin brief.

## A-quinquies. 1:1 CONTRA 9:16 — ¿son la MISMA pieza? (CAMBIOS — Dirección, 08-09-2026)
Los dos ratios son **el mismo anuncio en dos formatos**, no dos anuncios parecidos. Al aprobar el 9:16,
**abrir las dos imágenes a la vez** y comparar, en este orden:

1. **El botón del CTA** — mismo texto, forma, color, redondeo, grosor de letra **y efectos** (halo,
   borde degradado, sombra). *Es el que más deriva:* en `05_objeciones` de Flowboost Dubái el botón
   perdió el halo degradado al pasar a 9:16 y quedó negro plano.
2. **Dónde vive el color de acento.** Si en 1:1 el degradado está en el botón, en 9:16 **sigue en el
   botón** — no salta al titular. En esa misma pieza el titular se coloreó en 9:16 y el botón se apagó:
   la jerarquía quedó invertida entre los dos ratios del mismo anuncio.
3. **Los pesos de letra.** La palabra o frase en bold del subtítulo **sigue en bold**. En el par citado
   desapareció y con ella el énfasis de la refutación.
4. **Las píldoras y etiquetas** (ANTES/DESPUÉS, kickers, sellos): mismo relleno y mismo borde. En
   `02_antes-despues` la píldora `AFTER` pasó de blanca sólida a degradada, y la línea del split de
   blanca fina a franja degradada.
5. **La FOTO es la misma foto.** Reencuadrada, sí; **regenerada, no.** Mismos props, misma pose, misma
   ropa, misma persona. En ese par el teléfono que sostenía el broker desapareció en 9:16 y con él la
   narrativa del anuncio. Si el GPT devuelve otra escena, es CAMBIOS, no una variante.
6. **El logo** — mismo dibujo y mismas proporciones (y los dos contra el PNG oficial).
7. **La paleta y las tipografías.**
8. **El copy, palabra por palabra.**

**Lo que SÍ tiene que cambiar** (y si no cambia, también es CAMBIOS): el encuadre. La foto se recompone
en vertical, un split lateral **rota a horizontal** (dos columnas en 9:16 son inservibles) y el texto se
reordena para la altura. Lo que **no** vale es la salida perezosa: la cuadrada centrada en un lienzo alto
con fondo vacío arriba y abajo (`01_articulo` de Flowboost Dubái: ~250 px muertos arriba, ~350 abajo).
El patrón bueno está en `refs/00_9x16-verticales/`: texto en la mitad superior, foto a sangre por abajo.

> **Las 7 parejas de `FlowboostDubai_*` son el caso de estudio.** Antes de auditar un 9:16, leer
> `refs/FlowboostDubai_LEEME.md` §DERIVA: tiene las tres derivas medidas sobre la misma pieza.

**Cualquier diferencia → CAMBIOS sobre el 9:16, re-adjuntando el 1:1 aprobado.** No se corrige el 1:1:
ese ya pasó su auditoría.

**Por qué importa:** los dos ratios corren en la misma campaña. Si el botón cambia entre feed y
stories, el cliente lo ve como dos anuncios distintos y la marca se lee descuidada.

## A-sexies. LAS ZONAS SEGURAS SE MIDEN, NO SE MIRAN (regla dura — test 08-09-2026)
**Ninguna vertical se aprueba sin pasarla por el medidor.** A ojo no se ve: 40 px de invasión no se
notan en el monitor y en el móvil dejan el CTA debajo de la interfaz de Meta.

```bash
python3 ~/.claude/skills/estaticos-meta/scripts/zonas_seguras.py <pieza_9x16.png>
```

**El script MIDE, no opina — y lo que mide es contenido de alto contraste, no "texto".** Devuelve tres
veredictos y **sale con código 1 si alguna pieza no es «limpia»**; código 1 significa *hay que mirar esa
franja*, no *rechazar la pieza*:

| Veredicto | Qué significa | Qué se hace |
|---|---|---|
| **✓ limpia** | nada de alto contraste en las dos franjas | aprobar (sigue el resto del §G) |
| **👁 revisar** | hay contenido dentro de una franja | depende de la franja, ver abajo |
| **? no concluyente** | el detector casi no ve nada (navy sobre crema, p. ej. el advertorial) | juzgar la pieza **a ojo, entera**; nunca darla por limpia |

> ⛔ **Y una cosa más, que casi cuesta una tanda entera (consejo, 11-09-2026).** Si la pieza va **a
> sangre** —el fondo o la foto llegan al borde, que es el patrón de la casa— **el script NO puede
> distinguir la foto del texto** y por tanto **no dictamina: solo informa**. Antes sí dictaminaba, y
> el resultado fue que **11 de las 12 piezas `Cliente 04-APROBADO` —el estándar de oro— salían «CAMBIOS»**
> por una invasión que no existía. Cada pieza habría quemado sus 3-4 iteraciones corrigiendo un
> fantasma, se habría degradado al regenerar, habría acabado `_PEND`, y la campaña no habría subido
> nada. El script ya lo detecta solo y lo dice en su salida: cuando veas «va a sangre», **abre la
> pieza con `--marcar` y decide tú** si lo que entra en la franja es fondo o es texto.

- **ARRIBA (270 px): el veredicto vale. Invade → CAMBIOS**, citando el número: *«el CTA entra 206 px en
  la franja de abajo»*. Pedir «respeta la zona segura» sin la cifra no funciona: ya se probó.
  - ⚠️ **Las propias referencias aprobadas lo incumplen:** colocan el primer elemento a **117-226 px**
    (`refs/00_9x16-verticales/LEEME.md`). La tensión está anotada y sin resolver, y **mientras Dirección no
    diga otra cosa manda la safe zone de 270 px** — es la que evita que Instagram tape el titular. Así
    que una pieza nuestra con el titular a 200 px es CAMBIOS aunque la referencia lo haga.
- **ABAJO (384 px): el veredicto NO es concluyente por sí solo.** El patrón de la casa es **foto a sangre
  por abajo**, así que en una pieza buena hay contenido de alto contraste ahí. **Hay que mirar con
  `--marcar salida.png` y decidir:** si lo que entra es la **foto**, pasa; si es **texto, logo o CTA**,
  CAMBIOS. (Antes este documento decía que los falsos positivos eran solo laterales. No es verdad, y por
  eso el script marcaba 3 de las 6 verticales aprobadas.)
- **LATERALES: no se dictaminan, se informan.** Con fondos a sangre da falsos positivos. El criterio es
  el **margen de composición de la casa, 107 px**; **65 px es el mínimo técnico** que no se puede cruzar.
  El script avisa de los dos casos por separado, y `--marcar` pinta la franja 65-107 en naranja.
- **Filtro del script (11-09-2026):** descarta las filas cuya máscara cubre **>60 % del ancho** — son
  líneas estructurales y bordes de panel o de foto, no glifos. Sin eso, el split del Antes/Después daba
  «entra 270 px arriba y 384 abajo» en una pieza aprobada.

**Por qué no basta con pedirlo en el prompt:** se probó en píxeles, en porcentaje y por franjas. El
modelo no acierta con ninguna. Se le sigue pidiendo en píxeles porque acerca, pero **la compuerta es
la medición**.

## B. TITULAR SEGÚN FORMATO
- **Advertorial / Artículo-Noticia:** el titular va en **tono EDITORIAL** (como nota de prensa real, creíble, tercera persona o interpelación seria), NO una pregunta de marketing ni un eslogan. Debe leerse como titular de medio.
- **Direct-response (Testimonio, Antes/Después, Pain, Oferta):** ahí sí hook DR punchy (dolor/beneficio/tensión).
- **⛔ ADVERTORIAL: en la cabecera va el NOMBRE DE UN MEDIO, NO el logo del cliente (Dirección, 08-09-2026).**
  Un masthead tipo `BARCELONA ACTUAL` / `EL DIARIO INMOBILIARIO`, coherente con el sector y la ciudad del
  avatar. **Ver el logo de la marca arriba delata que es publicidad** y tira abajo lo único que aporta
  este formato: que se lea como noticia. Si el logo tiene que estar, va **abajo y pequeño**, junto a la
  oferta o el CTA, como el anunciante en una página real de prensa. **Nunca un medio real** (*El País*,
  *Expansión*…): eso es suplantación y Meta lo tumba.

## C. ÉNFASIS / RESALTADO — según el REGISTRO de la marca
- El **subrayado tipo marcador NO va en marcas premium/editoriales ni imita a un diario serio** — se ve cutre. Solo va en marcas ruidosas/comunidad (ej. Cliente 05, amarillo).
- **Premium/editorial (Cliente 04, Diana, Cliente 11, Batlle):** énfasis editorial = **itálica serif, negrita, versalitas, o un filete/regla fina** — o SIN resaltado. Nunca marcador.
- Si se resalta, resaltar **la palabra que carga el mensaje**, no una cualquiera.

## D. LA REFERENCIA DEBE MATCHEAR EL REGISTRO DE LA MARCA (no solo el formato)
- Error cometido: pasé **Cliente 05 (advertorial ruidoso)** como referencia para **Cliente 04 (editorial premium sobrio)** → salió con marcador cutre.
- **Regla:** elegir el estático ganador de referencia cuyo **registro visual coincida con la marca del cliente**:
  - Premium/editorial/lujo/legal → referencia sobria serif (Diana, Cliente 11, Batlle), NO Cliente 05.
  - Ruidoso/comunidad/local → Cliente 05, MMS.
- Cruzar SIEMPRE registro de marca (del manual) × formato antes de elegir la referencia a subir al GPT.

## E. TEXTO RENDERIZADO SIN ERRORES (los modelos de imagen tipean mal)
- Los modelos de imagen **deforman letras y acentos** (ej. "encuentran" con la "a" mal formada).
- **QC obligatorio:** tras generar, LEER el texto de la imagen (zoom/OCR visual) y verificar **ortografía, acentos y que no haya letras deformes**. Cualquier error → CAMBIOS: "corrige el texto, la palabra X está mal escrita; el copy debe decir exactamente: ...".
- Dar el copy EXACTO al GPT entre comillas para que lo renderice tal cual.

## F. EL LOOP DE AUTO-QC (autónomo, sin Dirección)
Después de cada generación, la skill corre este check y **actúa sola**.

> ⚠️ **Este bucle son los TRES, no solo lo de abajo (11-09-2026):** los pasos 1-6 de aquí, **el §G
> (checklist visual) entero** y **el §H (audit de copy) entero**. Lo de abajo nació cuando el §H no
> existía y se leía como si el bucle terminara en el punto 6 — que es justo cómo el copy se quedó sin
> auditar durante semanas.
1. **Formato correcto** (advertorial plano, no foto de objeto). ❌ → CAMBIOS con la referencia del registro correcto.
2. **Titular** en el tono del formato (editorial si advertorial) + **hook stop-scroller con beneficio**. ❌ → CAMBIOS con un hook mejor (de §A/§B).
3. **Énfasis** acorde al registro (sin marcador en premium). ❌ → CAMBIOS.
4. **Texto sin typos/acentos rotos** (§E). ❌ → CAMBIOS con el copy exacto.
4-bis. **Español de España** (§0-bis): 0 voseo, 0 léxico LATAM. ❌ → CAMBIOS: "reescribe en español de España, «X»→«Y»".
5. **Fidelidad de marca** (paleta/tipos/logo del manual) + **safe zones** + **≤8 palabras en el NÚCLEO** (titular + apoyo; no cuentan CTA, sellos, checks, precio ni kicker — §0-quater, y advertorial y Review+Claim están exentos) + **sin claims inventados**.
5-bis. **Nada cortado por el borde** (grid/tarjeta/texto/CTA/logo entero dentro del marco) + **cero texto en props** (tazas/carteles/camisetas). ❌ → CAMBIOS.
5-ter. **Personas = reales recreadas de stock** (estética española), no caras IA inventadas ni stock corporativo. ❌ → CAMBIOS con la referencia de persona.
6. Repetir hasta pasar (máx ~3-4 iteraciones). **Solo cuando pasan los tres —F, G y H—** → descargar y guardar en Drive. Si tras el máximo no pasa → guardar el mejor intento + anotar en `specs_Tanda<N>.md` qué quedó pendiente (**nunca** se le consulta ni se le narra: ni siquiera cuando falta un insumo real — eso se anota y se cuenta en el resumen final de la tanda).

> Objetivo: Dirección abre Drive y encuentra piezas ya buenas. Si tiene que corregir hooks, tipos o resaltados, la skill falló en su trabajo de auto-QC.

## G. CHECKLIST VISUAL OBLIGATORIO — MIRAR la imagen renderizada (no basta copy/idioma/marca)
Aprendizajes reales del run de Cliente 04 (Dirección corrigió en vivo). En CADA imagen (1:1 y 9:16), antes de aprobar, mirar de verdad y verificar TODO esto; cualquier fallo → CAMBIOS/REGENERATE, no se guarda:
1. **Minimalismo:** 1 sola idea, mucho espacio negativo, sin ruido visual (nada de comparativas Sin/Con recargadas + atrezo + fondo saturado). Entre dos, la de menos elementos.
2. **Persona real recreada de stock** (estética española), NO cara IA inventada ni stock corporativo posado. **COMPARAR la cara generada con la foto de referencia** (rostro, pelo, gafas, edad): si no se parece, el GPT inventó una persona → REGENERATE **re-adjuntando la foto en ese mismo mensaje**. ⚠️ La referencia visual NO persiste entre turnos: hay que adjuntarla en CADA generación (1:1, 9:16 y cada CAMBIOS) o saldrá cara de IA. Si el formato lleva persona y no hay foto real del cliente → referencia de stock (Unsplash/Pexels, previsualizada, solo la elegida) adjuntada al GPT para recrear.
3. **Anatomía correcta:** brazos, manos, dedos, cara sin deformar ni fundirse con el fondo (los modelos fallan aquí). Un brazo/mano que falta o mal → REGENERATE.
4. **Nada cortado por los 4 bordes:** grids, tarjetas, columnas, texto, logo, CTA, persona clave — todo entero dentro del marco: **54 px** de margen (1:1) / safe zone 9:16: 270 arriba · 384 abajo · laterales a 107 (mínimo duro 65). Revisar los 4 bordes.
5. **Cero texto en props** (tazas, carteles, camisetas, post-its con eslóganes). El copy va solo en titular/apoyo/checks/CTA.
6. **Español de España** (0 voseo/LATAM) en TODO el texto visible + **título sin punto final** + **sin typos/acentos rotos** (leer el texto de la imagen). ⚠️ **Escribir SIEMPRE el copy al GPT CON TILDES correctas** (Tú, gestión, inversión, más, aquí…): si se le pasa el texto sin tildes "para evitar problemas de tecleo", **el creativo sale sin tildes** (error real: salió "Tu inviertes" en vez de "Tú inviertes"). El campo de ChatGPT acepta acentos y ñ: usarlos.
7. **Marca:** paleta/tipografías; énfasis por registro (premium → itálica/serif, nunca marcador).
7-bis. **LOGO — fidelidad exacta (regla dura, error real de Cliente 04):** los modelos de imagen **redibujan el logo y lo van DEFORMANDO** a lo largo de la cadena (cada formato sale peor). Dirección: "el logo no es ese, se fue deformando a medida que pasaban los formatos".
   - **Estándar (decidido por Dirección): ADJUNTAR el PNG oficial del logo en CADA generación** (1:1, 9:16 y cada CAMBIOS), igual que la foto de la persona → así el modelo lo dibuja bien y no deriva. **Nunca pedir piezas sin logo por iniciativa propia.** (Fallback sólo si Dirección lo pide: componer el PNG oficial en post con `../templates/poner_logo.py`.)
   - Si por lo que sea el modelo lo dibuja: **comparar SIEMPRE el logo generado contra el archivo oficial** (`Insumos/logo/`) — proporciones del isotipo, tipografía del naming, grosores. Cualquier deformación → REGENERATE (re-adjuntando el PNG del logo) o tapar componiendo el oficial.
   - Revisar el logo en **CADA pieza**, no solo en la primera: la deriva es acumulativa.
8. **Claims reales** del brief (sin cifras inventadas), sin nombrar competidores (usar genéricos).
9. **9:16:** llena TODO el lienzo (sin bandas vacías), nativo, con la safe zone libre (270 arriba / 384 abajo / laterales a 107, mínimo duro 65).
10. **Diversidad en la tanda:** CTA y layout distintos entre los 9; sin arrastre de chrome de otro formato.
11. **FECHAS VISIBLES — tienen que ser de HOY, nunca pasadas (regla de Dirección).** El advertorial imita una página de medio y suele llevar **fecha de portada**; el modelo la inventa y casi siempre pone una **anterior** (arrastra la de su entrenamiento o la de la referencia). Una fecha vieja delata que el anuncio es viejo y mata la credibilidad de todo el formato editorial.
   - **Consultar la fecha real del sistema, NUNCA la de memoria:** `date +%d/%m/%Y` (y `date +%Y` para el año). El modelo —y tú— os equivocáis de fecha con total seguridad; el shell no.
   - **Comparar carácter a carácter** la fecha impresa en la imagen con la del sistema. Distinta o pasada → **CAMBIOS** (regenerar con la fecha correcta dictada explícitamente). Nunca se guarda una pieza con fecha pasada.
   - Aplica a **cualquier fecha visible de cualquier formato**, no solo al advertorial: cabecera/dateline, pills de metadata ("INFORME 2026", "ESTUDIO 2026" → el **año** tiene que ser el año en curso), "válido hasta", fechas de evento o de convocatoria.
   - **Ojo al desgaste:** la tanda vive semanas, así que una fecha exacta envejece sola a los pocos días. Si la pieza no depende de un día concreto, **mejor sin día**: mes y año, o solo el año. Si lleva día, hay que tener presente que caduca — y una fecha futura tampoco vale (parece error).
12. **JERARQUÍA DE LA LISTA — anti-empaste (Dirección, 07-09-2026).** En toda pieza con checks, pasos o ítems de oferta: ¿la lista queda **por debajo** del titular en peso visual, o compite con él? ¿Lleva peso **solo la palabra clave** de cada ítem, o está el ítem entero en negrita? ¿Son **paralelos y de longitud parecida** (≤5 palabras, sin punto final)? ¿Hay **más aire entre ítems que entre las líneas internas**? ¿Mismo icono, mismo tamaño, alineados? **Test de la miniatura: a 200 px tienen que verse N líneas separadas, no una mancha gris.** Si se empasta → CAMBIOS: quitar ítems o palabras, **nunca** achicar el cuerpo. Regla completa en `reglas-tecnicas-y-copy.md §3`.
13. **COLISIONES CON LÍNEAS INTERNAS (Dirección, 07-09-2026 — el punto 4 solo miraba los BORDES del lienzo).** Ningún texto puede tocar, cruzar ni pegarse a una **línea estructural de dentro** de la pieza: el **split del Antes/Después**, el marco de una tarjeta, el filete de una cabecera editorial, el borde de la pastilla del CTA, la costura entre dos paneles. Mirar específicamente el titular: **el fallo real fue un titular que bajó demasiado y chocó con la línea que divide antes y después**. Holgura mínima = el alto de una línea del propio texto. Si no cabe → acortar el texto o mover la línea; nunca pegarlos. → CAMBIOS.
14. **EL 9:16 ES NATIVO, NO EL 1:1 PEGADO (Dirección, 07-09-2026).** Mirar el vertical: ¿hay un cuadrado incrustado, marcos, bordes o bandas, o la composición está rediseñada y repartida por toda la altura? **El advertorial es el que más lo hace.** Incrustado → CAMBIOS con la frase literal de `prompts-gpt.md` §Paso 3; no se aprueba.
15. **SAFE ZONES EN PÍXELES Y COMPROBADAS (Dirección, 07-09-2026 — los 4 verticales de una tanda las violaron).** 1:1: nada de texto/logo/CTA en los **54 px** de cada borde. 9:16: nada en los **270 px** de arriba ni en los **384 px** de abajo, y los laterales **a 107 px** (65 px es el mínimo técnico infranqueable, no el objetivo). Si al pedirlas se usó un porcentaje, el GPT las ignora: **repetir el prompt en píxeles**, no dar por bueno el resultado.
16. **ANTES/DESPUÉS: ¿el contraste ES la oferta?** ¿Se entiende qué se vende y qué se lleva el cliente? Si el "después" es algo que el avatar podría conseguir solo, o el par de estados no tiene que ver con el servicio, el anuncio no se entiende → REGENERATE cambiando los estados (ver `formatos-visual-spec.md §2`).
17. **¿La franja del titular está diseñada o es un bloque blanco por defecto?** Si es blanco liso sin registro de marca ni jerarquía → IMPROVE/REGENERATE (`reglas-tecnicas-y-copy.md §3`).
18. **RESEÑA/TESTIMONIO: ¿derriba una objeción o es elogio genérico? (Dirección, 07-09-2026).** ¿Qué duda, miedo o barrera concreta responde esta cita? Si no sabés decirlo en una frase, es genérica → REGENERATE. **Test:** si la cita valdría para un competidor o para otro sector, no sirve. Comprobar también que **el testimonio es del MISMO avatar al que habla la tanda** (fallo real: tanda a inversores con testimonio de propietario) y que la atribución no es un marcador (si lo es: la pieza NO es publicable, se anota como pendiente). Ver `formatos-visual-spec.md §3`.
19. **¿LLEVA UNA CIFRA CONCRETA? (panel suspendido 07-09-2026: cero cifras en las 5 piezas de una tanda).** Cada pieza necesita **al menos un dato específico del brief** — un número, un plazo, un porcentaje, una cantidad. Es la regla de Ogilvy que más se incumple (O2). "Sin complicaciones" no es un dato; "en 48 h" sí. **Si el brief no tiene cifra utilizable para ese ángulo, en este orden:** (1) usar **otro dato concreto y verificable** del brief, que también cuenta como específico — un plazo ("en 48 h"), un alcance ("los 4 documentos del proceso"), una condición ("sin adelantar el dinero"), una antigüedad ("35 años"), un número de algo que se pueda contar; (2) si tampoco hay, **cambiar el ángulo** a uno que sí tenga dato; (3) y si el brief **no tiene ni un dato duro en todo el documento** —pasa— entonces el específico es el **verbatim crudo del cliente** (§20) y la pieza se apoya en el patrón *muro de citas «Antes X. Ahora Y.»* de `formatos-visual-spec.md`. **Lo que NUNCA se hace es inventar la cifra para cumplir este check**, ni bloquear la tanda por no tenerla: se anota en `specs_Tanda<N>.md` que el cliente no tiene datos duros y se pide en el resumen final. → REGENERATE solo si la pieza se queda sin NINGUNA de las tres cosas.
20. **¿ESTÁ ESCRITO CON EL VERBATIM DEL CLIENTE O CON LENGUAJE DE FOLLETO?** Fallo real: se usó "sin complicaciones" y "en buenas manos" **teniendo en el brief el verbatim crudo sin usar** ("no les daba la vida", "son un coñazo"). Antes de dar por bueno el copy: abrir el brief, buscar cómo lo dice el cliente **con sus palabras** y usar esas. Lenguaje de folleto → REGENERATE.
21. **COBERTURA DE LA TANDA (se comprueba al cerrar la tanda, no por pieza).** ¿El **ángulo más diferencial del brief** está en alguna pieza? Fallo real: el mejor ángulo de Cliente 02 —"a veces te decimos que no compres"— no aparecía en ninguna de las cinco. Además: ¿hay **2-3 caras distintas** y ninguna repetida en más de 2 piezas? ¿Todas las piezas hablan **al avatar de la tanda**? Si algo falla, se rehace la pieza que corresponda antes de dar la tanda por buena.
22. **¿LA PERSONA PEGA CON EL ANUNCIO? (Dirección, 07-09-2026 — fallo real: una chica que no tenía nada que ver con la pieza, fuera de lugar).** Ojo: el punto 2 comprueba que la cara generada **sea fiel a la foto de referencia**; esto es distinto y va antes en la cadena — comprueba que **la referencia fuera la adecuada**. Una recreación impecable de la persona equivocada pasa el punto 2 y aun así arruina el anuncio. **Test: tapa el copy y mira solo a la persona — ¿quién es y de qué va el anuncio?** Si no apunta al avatar y al tema de la pieza (edad, perfil, contexto, ropa, actitud, registro de precio), → REGENERATE **con otra foto de referencia**, no con la misma. Criterios completos en `SKILL.md` §Protocolo, paso 2-bis.
23. **9:16 CONTRA LAS REFERENCIAS REALES (Dirección, 07-09-2026).** Comparar el vertical con `references/refs/00_9x16-verticales/` (6 piezas aprobadas de Cliente 01 con sus márgenes medidos): ¿el texto vive en la mitad superior y la **foto va a sangre por abajo**, sin bandas ni marcos? ¿El **margen lateral es de ~107 px**, no de 65? (65 px es el mínimo técnico; las piezas aprobadas respiran a 107 y por eso se ven premium). ¿El logo va pequeño arriba, el kicker en píldora de acento, y el titular con una línea en el color de acento? Si el vertical no se parece a esas seis en aire y composición, → CAMBIOS.
26. **¿ESTA PIEZA SALE O LLEVA `_PEND`? (Dirección, 11-09-2026 — último check, y es binario).** Antes de
    guardar, decidir el estado y **escribirlo en el nombre del fichero**, en los dos ratios. Lleva
    `_PEND` si: hay **cita o testimonio provisional** (`[REEMPLAZAR]` en el píxel) · **no pasó el panel**
    o el auto-QC y se guarda el mejor intento · el **branding se sacó de la web** sin validar · hay
    **cara de stock** en una pieza que sugiere respaldo. Si NO lleva `_PEND`, se está afirmando que puede
    publicarse tal cual — porque la skill de campaña lee esa carpeta y sube lo que no esté marcado.
27. **¿ESTÁ DECLARADA LA IA?** La pieza la generó un modelo y Meta exige declararlo. Correr
    `../scripts/normalizar_png.py` (escala preservando la credencial **C2PA**, que el escalado normal
    con PIL borra) y anotar por pieza `IA declarada: automática (C2PA presente)` o `MANUAL PENDIENTE`.
    Sin ese campo, la skill de campaña asume MANUAL PENDIENTE y activa la divulgación a mano.

> Regla de Dirección: "el audit debe MIRAR de verdad la imagen". Un checklist que aprueba una pieza con ruido, anatomía rota, grid cortado, texto en tazas o voseo NO sirve.


24. **Si es ADVERTORIAL: ¿qué hay en la cabecera?** Tiene que haber el **nombre de un medio**, no el logo del cliente. Logo de la marca presidiendo la cabecera → **REGENERATE**: el formato entero deja de funcionar, porque lo que compra es que parezca una noticia. Comprobar además que el medio inventado **no es una cabecera real**.


25. **¿EL HOOK SEGMENTA? (Dirección, 08-09-2026 — regla dura, bloqueante).** El hook tiene que decir **a quién
    le habla**, para que el avatar se reconozca en el primer vistazo y el que no lo es siga scrolleando.
    **Test:** tapa la marca y lee solo el titular — *¿sabrías decir a quién va dirigido?* Si la respuesta
    es "a cualquiera" o "a alguien que quiere más clientes", **no segmenta → REGENERATE**.
    - Vale segmentar por **identidad** ("Dubai realtors:"), por **situación** ("Llevas seis meses
      publicando y ni un listing") o por **dolor/creencia** ("Otra vez el mismo lead que tienen otros
      cinco agentes"). Con una basta.
    - **No cuenta:** beneficio universal, pregunta genérica, o tener el segmento solo en el logo, el pie,
      el CTA o la segmentación de Meta. Va **en el hook**, que es lo único que se lee antes de decidir.
    - **Varía la forma de segmentar entre las piezas de la tanda** (identidad / situación / dolor): nueve
      hooks que empiezan igual son un anuncio repetido y los tumba §0.
    - Si hay **dos avatares**, cada pieza le habla a **uno**. Regla completa: `../../fundamentos-copy/references/headlines-playbook.md`.


## §H. AUDIT DE COPY — se corre EN CUANTO LLEGA LA IMAGEN, con todo (Dirección, 11-09-2026)

> **Por qué existe y de dónde sale.** Hasta hoy el protocolo mandaba correr **solo el §G, que es el
> checklist VISUAL**. Dirección: *«las putas skills no auditan el puto copy, solo el diseño»*. Tenía razón:
> el material de copy estaba en el índice de fuentes y en ningún paso ejecutable.
> **Estos checks NO son un resumen mío: salen del NotebookLM «Creativos Meta» (80 fuentes), con sus
> umbrales y sus datos de impacto.** Donde una fuente y la doctrina de la casa chocan, manda la casa y
> se dice.

> **Los NÚMEROS no viven aquí: viven en `parametros-copy.md`**, que es a los copys lo que
> `../../gestion-cuenta-meta/references/parametros-campana.md` es a las campañas — fuente única, con cada cifra y de dónde sale (el
> NotebookLM «Creativos Meta» de Dirección, sus PDF académicos, y los dos libros de la casa). **Este §H
> es el checklist que los EJECUTA pieza por pieza.** Si un número de aquí y uno de allí no cuadran,
> gana `parametros-copy.md`.

**Se corre ENTERO, por pieza, en el mismo momento que el §G** — nada más recibir el creativo del GPT,
antes del otro ratio y antes de descargar. **El copy se lee de la IMAGEN, no del prompt.**

### H.0 · EL ORDEN EN QUE SE JUZGA (esto manda sobre todo lo demás)
No todos los fallos pesan igual. Orden estricto de las fuentes — **si falla un nivel, no se sigue
bajando: se arregla ese**:

| | Nivel | Qué decide |
|---|---|---|
| **1** | **Claridad y UNA sola idea** | *«Clarity converts, confusion kills».* La claridad manda sobre el ingenio. Ambiguo o con dos mensajes → se rechaza sin mirar nada más |
| **2** | **Encaje con la temperatura del embudo** | La etapa del comprador manda sobre el CTA. En frío, gancho de dolor o educativo con CTA blando |
| **3** | **Especificidad y lenguaje del comprador** | Las palabras reales del cliente y los datos concretos mandan sobre la jerga y el eslogan |
| **4** | **Límites técnicos** | Caracteres y truncado. Si el titular pasa de 40, se recorta — aunque esté bien escrito |
| **5** | **Pulido de estilo** | Muletillas de IA y superlativos. Es el último filtro, no el primero |

### H.1 · LOS 13 CHECKS DE LAS FUENTES, con su PASS y su FAIL
*(Son 13 y son los del NotebookLM. **Los 16 checks de Ogilvy son otro instrumento distinto** y se corren aparte, en §H.8. Que los dos vivan en el §H no los mezcla.)*
| # | Check | PASS | FAIL |
|---|---|---|---|
| 1 | **Caracteres del titular** | **25-40 car.**, óptimo **~27** en feed | >40 → se trunca con `...` en móvil |
| 2 | **Una sola idea** | exactamente **1 promesa / 1 ángulo** | dos o más beneficios apilados |
| 3 | **Cita / testimonio** | **≤15 palabras** sobre la imagen | más → rompe la jerarquía |
| 4 | **Densidad de texto** | **<20 %** de la superficie | más → Meta penaliza entrega y sube el CPM |
| 5 | **Lenguaje del comprador** | nombra **la tarea o el resultado** que él busca | jerga, nombre de módulo, eslogan vacío |
| 6 | **Cifras** | **específicas, no redondeadas**, con contexto | «mejora un 50 %», «miles de clientes» |
| 7 | **Limpieza de IA** | vocabulario natural | muletillas de IA · superlativos · **>2 rayas largas /100 palabras** |
| 8 | **El valor va DELANTE** | empieza por el beneficio o un verbo | lo entierra al final, **o empieza por la marca** |
| 9 | **Si es pregunta, con «tú»** | dolor concreto + **tú / tu** | pregunta genérica de categoría |
| 10 | **Ítems de lista** | **3-5** | **7 o más** destroza la retención; menos de 3 se queda corto |
| 11 | **CTA por temperatura** | frío = baja fricción · caliente = acción clara | pedir la llamada a un desconocido |
| 12 | **Fuente del dato** | línea pequeña al pie de la cifra | estadística gigante sin fuente |
| 13 | **Veracidad** | escasez y garantía **reales y verificables** | urgencia falsa o perpetua |

### H.2 · EL TITULAR SEGÚN EL NIVEL DE CONSCIENCIA — fórmula y longitud exacta
Lo que Schwartz dice en abstracto, aquí con la fórmula y los caracteres. **Primero se ubica al avatar,
y de ahí sale el tipo de titular; no al revés.**

| Nivel del avatar | Con qué se le abre | Fórmula | Car. |
|---|---|---|---|
| **Inconsciente** | historia o **advertorial**, o una verdad incómoda | contraria: «Por qué [creencia común] es en realidad [resultado malo]» | — |
| **Consciente del problema** | **pregunta de dolor** | «¿Cansado de [dolor concreto]?» | **~28** |
| **Consciente de la solución** | **cómo / dato / viejo vs nuevo** | «Cómo [resultado] en [métrica medible]» | **~27** |
| **Consciente del producto** | **caso, testimonio o comparativa** | «[Verbo] + [cifra impar] + [identidad] + [resultado]» | **~37** |
| **Totalmente consciente** | **oferta directa, precio, garantía** | «[Verbo] + [beneficio concreto] + [condición]» | **~28** |
| *(BOFU, urgencia real)* | aversión a la pérdida | «[Plazo]: [oferta] termina [cuándo]» | **~36** |

- **Mercado saturado** (todos prometen lo mismo): el titular descriptivo se vuelve invisible. Se pasa a
  **necesidad no considerada / contraria** — **+10 % de impacto persuasivo** frente a validar una
  necesidad que ya conoce. Es el Schwartz de «cuando el claim está gastado, toca mecanismo».
- **Una pregunta con «tú / tu» rinde +175 % de CTR** frente a una afirmación (una pregunta genérica ya
  da +150 %: el «tú» es la mitad del efecto). Y **una cifra específica o impar sube hasta +30 %**.
- **Máx. 7-8 palabras por línea** en el canvas, para que se escanee.
- **Reels con texto superpuesto: 10 caracteres.** No es una errata.

### H.3 · ¿SEGMENTA? — tres pruebas, y basta con que pase una
*(Es la comprobación del §A-ter, que es donde está la regla y su severidad.)*
El creativo no solo atrae al bueno: **descarta activamente al que no lo es.**
1. **Nombra la tarea u operación concreta.** «Trabaja mejor, no más» no segmenta: le vale a cualquiera.
   «Automatiza las altas de tu personal» sí: el que no da altas sabe al instante que no va con él.
2. **Efecto fiesta de cóctel.** Apela a la identidad o al rol («Autónomos que facturan por encima
   de…», «Si tienes un local en Gràcia…»). El cerebro se desengancha de lo general y se engancha con
   su propio rol o problema.
3. **Pregunta que autocalifica.** El que no es cliente contesta «no» mentalmente y sigue; el que lo es
   contesta «sí, exactamente». *«¿Sigues metiendo los leads a mano en el Excel?»*

### H.4 · LA PRUEBA DE LA MINIATURA, que ahora tiene respaldo
La regla de la casa —mirar la pieza a **200 px**— no era una manía: las fuentes la fijan igual, y le
ponen tiempo: **a 200 px de ancho, la propuesta de valor o el titular tienen que entenderse en menos
de 1 segundo.** Si a ese tamaño no se lee el titular, da igual lo bien escrito que esté.

### H.5 · LOS TRES CHECKS QUE SALEN DE LOS PDF ACADÉMICOS
No estaban en ninguna parte y son de los que más deciden:
1. **¿CURIOSIDAD O CEBO?** El titular que **esconde el sujeto o la solución** para forzar el clic
   («no te vas a creer lo que hace este método») puntúa alto en *baitness* y penaliza. El bueno lleva
   **densidad factual**: un dato, un porcentaje o el beneficio nombrado. Y ojo — **el titular vago no
   es curiosidad, es fricción**: medido con eye-tracking, aumenta las fijaciones y las relecturas
   porque el lector busca con ansiedad, no con interés.
2. **¿LA JERARQUÍA RESPETA DÓNDE MIRA EL OJO?** Cara **16-19,5 %** · titular **~25 %** · logo
   **0,8-2,3 %**. Si el logo está en el centro o pasa del 10 % del canvas, **se salta por ceguera de
   banner**. El titular va arriba o centro-izquierda, que es donde caen las fijaciones.
3. **¿HAY DOBLE CONTRASTE?** El color y el contraste enganchan el ojo en el primer milisegundo
   (*bottom-up*), pero **lo que sostiene la mirada es el dato útil** (*top-down*). Un botón vistoso
   sin un dato al lado = mirada que rebota. Un dato sin contraste = no llega a mirarse.

⛔ **Y una que es de proceso:** **no se valida un diseño con mapas de calor de IA.** Sobreestiman la
atención al titular hasta un **61,47 %** cuando los humanos reales le dedican el **25,07 %**. La
compuerta es `../scripts/zonas_seguras.py` + mirar la pieza.

### H.6 · ANTI-PATRONES, con lo que cuestan
Los que traen dato medido, para saber qué duele más:
- **Muletillas de IA** («delve», «leverage», «optimiza tu experiencia») → **−8 % de conversión**.
- **Superlativos vacíos** («increíble», «innovador», «revolucionario», «el mejor») → **−4 %**.
- **Más de 2 rayas largas por cada 100 palabras** → **−5 %** (delata texto sintético).
- **CTA de alta fricción en frío** → dispara el rebote y encarece el CPL.
- **Titular genérico de categoría** («¿Quieres hacer crecer tu negocio?») → **invisible en el feed**.
- **Cifra redondeada sin fuente** → se descarta como propaganda.
- **Urgencia falsa** → la gente reporta u oculta el anuncio y **sube el CPM de toda la cuenta**.
- **Empezar por la marca** («En Flowboost presentamos…») → permiso inmediato para pasar de largo.

### H.7 · LOS TIEMPOS, que son el listón real
El anuncio no se lee: se decide. Por eso los límites de arriba no son estética:
- **1,5-1,7 s** — la ventana en la que el ojo decide si para o sigue.
- **0,4 s** — lo que tarda el gancho en activar la respuesta de orientación.
- **3 s** — el tope para que se entienda el valor.
- **Prueba de los 5 segundos:** si alguien de fuera no sabe explicar la oferta en 5 segundos, **se
  reescribe**. Es la que decide cuando las demás empatan.

### H.8 · Y ADEMÁS, lo de la casa (que no está en las fuentes y manda igual)
- **Los 16 checks de Ogilvy** con sus severidades → `../fundamentos-copy/references/ogilvy-reglas-reales.md`.
  - **De copy, se corren aquí: O1-O7, O10, O12-O15.**
  - **O9** (foto real, no ilustración) y **O16** (el diseño no compite con el mensaje) los cubre el §G (§G.2 y §G.1).
  - **O8** (*story appeal*: la imagen despierta curiosidad, no es decorativa) **no lo mira ningún checklist**: se juzga en el **§0, el juicio de director creativo**. Si la foto no cuenta nada, la pieza es genérica aunque pase todo lo demás.
  - **O11** (titular debajo de la imagen, +10 % de lectura) **solo aplica cuando la foto es la protagonista absoluta, y como IMPROVE**: la anatomía de la casa (kicker y titular en el tercio superior) manda, y el eye-tracking la respalda — las fijaciones caen arriba y en el centro-izquierda (`reglas-tecnicas-y-copy.md §3` y `parametros-copy.md §3`).
- **El audit del FORMATO que toca** → `references/audit-copy-por-formato.md`. **Si no lo has abierto,
  el copy NO está auditado.** Incluye su §0: toda fecha o año visible se comprueba contra
  `date +%d/%m/%Y`, nunca contra la memoria del modelo.
- **SCHWARTZ SOBRE LA PIEZA TERMINADA** → `../fundamentos-copy/references/breakthrough-schwartz.md`.
  Era el agujero más silencioso: se usaba de ENTRADA (Fase 1) y **nadie comprobaba la salida**.
  ¿Abre por donde toca para ese nivel de consciencia? ¿La sofisticación pide mecanismo en vez de
  promesa directa? ¿Canaliza un deseo que ya existe? **Si falla, no es un CAMBIOS: es cambiar el
  ángulo y rehacer la pieza.**
- **Compliance** → `../fundamentos-copy/references/lo-que-no-funciona.md` — **se abre, no se cita**:
  **¿El cliente es de salud, estética, odontología, nutrición o fitness?** Entonces el **antes/después
  está restringido**: mismo encuadre, misma luz, misma distancia, y **nada de prometer resultado
  médico**. Es el formato más arriesgado ahí. Además: **Atributos Personales**
  (causa nº 1 de desaprobación; el hook no puede dar por hecho un atributo del lector), **categoría
  especial** (vivienda y crédito: media cartera), y **nunca nombrar a un competidor** en el canvas.
- **Los CTA son los NUESTROS.** Las fuentes son de SaaS y citan «prueba gratis» o «ver demo»: aquí no
  vendemos software y **el funnel siempre acaba en llamada**. Sirve el mecanismo (fricción según
  temperatura), no el texto. Los de la casa: `reglas-tecnicas-y-copy.md §7` y la ficha del formato.
- **Español de España** y el resto de checks de copy que ya viven en el §G: **§G.6** (idioma y título
  sin punto) · **§G.18** (la reseña derriba una objeción) · **§G.19** (hay un dato concreto) ·
  **§G.20** (verbatim del cliente, no lenguaje de folleto) · **§G.25** (el hook segmenta).

### H.9 · VEREDICTO (se anota en el specs, junto al del §G)
`COPY: pasa` · `COPY: CAMBIOS — <nº de check y la frase exacta>` · `COPY: rehacer ángulo (Schwartz)`.
**El CAMBIOS se manda con la frase que tiene que decir la pieza, entre comillas y con sus tildes**: el
GPT la copia literal (`references/prompts-gpt.md`).


