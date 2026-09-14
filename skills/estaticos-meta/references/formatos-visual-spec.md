# Spec VISUAL de los 9 formatos — cómo se ve CADA uno (héroe + estructura ÚNICA)

*(Los 9 de la tanda, del 1 al 9. Al final hay una §10 «Tres pasos» que es un formato maestro histórico **fuera de la secuencia**: está documentada para que no se meta en la tanda por error.)*

Regla de Dirección (dura): **cada uno de los 9 formatos tiene una estructura visual PROPIA y distinta.** No se repite el layout de un formato en otro. Antes de generar/auditar cada anuncio, mirar aquí "qué es el héroe" y "qué NO debe parecer". Error real: hice el Ad 5 (objeciones) con la misma estructura que el Ad 4 (persona + 3 checks + CTA) → Dirección: "eso no es el formato del anuncio". Se van **guardando los parámetros según se aprueban** (marcado ✅ = confirmado con pieza aprobada de Cliente 04).

> Fuentes: `patrones-diseno-estaticos.md`, `audit-playbook-b2b.md` (por formato), `audit-copy-por-formato.md`, `../../fundamentos-copy/references/headlines-playbook.md`. Todo bajo doctrina de minimalismo (1 idea, aire) + safe zones + español de España + persona real de stock recreada + sin texto en props + nada cortado.

## 📁 REFERENCIAS VISUALES — `refs/` (una carpeta POR FORMATO)
Biblioteca en `references/refs/<NN_formato>/` — carpetas `01_articulo-noticia` … `09_garantia` + `10_tres-pasos`, archivos `<Cliente>_<formato>_<n>.jpg`. **94 piezas en total:** **62 estáticos reales** de los 13 clientes del Drive (68 si se cuentan los 6 verticales de `00_9x16-verticales`, que es como los suma `refs/README.md`) y las **12 piezas aprobadas** (`Cliente 04-APROBADO_<formato>_<1x1|9x16>.jpg`), que son el **estándar vigente** de cada formato. Más las **14 de Flowboost Dubái** (`FlowboostDubai_<formato>_<1x1|9x16>.png`): 7 formatos con sus **dos ratios completos**, B2B en inglés, marca propia — ver `refs/FlowboostDubai_LEEME.md`. Ver `refs/README.md` (incluye el mapa de registros premium vs ruidoso).
- **Cómo se usan (regla de Dirección): las miro YO** antes de generar, y traduzco la estructura a **instrucciones escritas** para el GPT. **NO se le adjuntan piezas de otros clientes: se confunde** (mezcla marcas y mensajes).
  - **Excepción, solo urgencia:** si tras **varios intentos** el GPT no coge la estructura del formato, entonces sí adjuntar UNA como último recurso, dejando claro que es solo estructura.
  - Dentro del MISMO cliente sí se puede adjuntar su propia pieza aprobada (p. ej. el 1:1 para sacar su 9:16).
- ⚠️ Son referencia **estructural, NO de marca**: los colores, tipografías, logo, avatar y copy se toman SIEMPRE del cliente que toque (nunca el navy de Cliente 04 ni su avatar en otro cliente).
- **Pendientes de guardar:** formatos 1 (Artículo/Noticia), 2 (Antes/Después) y 3 (Review+Claim) — añadir sus piezas aprobadas cuando se descarguen.

## 1. Artículo/Noticia (Advertorial) *(sin pieza aprobada guardada aún)*
- **Héroe:** la PÁGINA editorial (parece nota de prensa/medio, no anuncio).
- **Estructura:** masthead/cabecera de medio + kicker de sección + **titular editorial serif grande** + foto como **imagen de artículo (figura, NO full-bleed)** + 2-3 bullets/entradilla + pills de metadata ("INFORME 2026", "ESTUDIO"). Grid limpio, aire.
- **⛔ EN LA CABECERA VA EL NOMBRE DEL MEDIO, NUNCA EL LOGO DEL CLIENTE (Dirección, 08-09-2026).**
  Este formato funciona porque **roba la autoridad de un periódico**: el lector lo lee como noticia y
  baja la guardia. En cuanto ve el logo de la marca arriba, sabe que es publicidad y se acabó el efecto
  — te quedas con un anuncio feo y encima disfrazado.
  - **En el masthead va un titular/nombre de diario o revista**, tipo `BARCELONA ACTUAL`, `EL DIARIO
    INMOBILIARIO`, `INFORME PYME 2026`. Coherente con el sector y la ciudad del avatar.
  - **El logo del cliente NO va arriba.** Si tiene que aparecer, va **abajo y pequeño**, dentro del
    bloque de la oferta o del CTA, como aparecería el anunciante en una página real de prensa.
  - **Nada de inventar un medio que existe de verdad.** Un nombre plausible y genérico, nunca *El País*,
    *Expansión* ni ninguna cabecera real: eso es suplantar a un medio y Meta lo rechaza.
- **NO debe parecer:** un anuncio con botón grande / foto de producto / mockup de periódico impreso 3D
  / **una pieza de marca con el logo del cliente presidiendo la cabecera**.
- **Fecha de cabecera:** si la lleva, **tiene que ser la de HOY** — sacarla del sistema (`date +%d/%m/%Y`), dictársela al GPT en el prompt y verificarla en la imagen (`calidad-y-autoqc.md §G.11`). El modelo pone fechas pasadas por su cuenta, y una fecha vieja delata el anuncio. Lo mismo con el año de las pills tipo "INFORME 2026". Si la pieza no depende de un día concreto, mejor sin día (mes y año, o solo el año): la tanda vive semanas y el día envejece.
- **CTA:** discreto, baja fricción ("Leer más / Descargar informe").

## 2. Antes/Después *(sin pieza aprobada guardada aún)*
- **Héroe:** el CONTRASTE de dos estados.
- **Estructura:** split izquierda/derecha (o arriba/abajo): **antes** apagado/gris/caótico vs **después** luminoso/limpio; mismo ángulo/luz; etiquetas/métricas concretas y no redondeadas. X vs ✓ si aplica.
- **EL CONTRASTE TIENE QUE SER EL RESULTADO DE LA OFERTA (Dirección, 07-09-2026).** Fallo real en Cliente 02: piso vacío → piso amueblado, cuando lo que se vende es **gestionarle la inversión al propietario**. El "después" no era lo que el cliente compra, así que **ni se entendía el anuncio ni se entendía la oferta**: el contraste era decoración, no promesa.
  - **"Antes" = la situación del avatar SIN el servicio. "Después" = exactamente lo que el servicio le entrega.** Nada más.
  - **Test:** si el cambio que se ve lo podría conseguir por su cuenta sin contratarte, el formato está mal usado → cambiar el par de estados, no el diseño.
  - **La oferta tiene que leerse en la pieza** (qué se vende y qué se lleva). Un contraste bonito sin oferta legible no es un anuncio: es una foto de antes y después.
  - En servicios donde el cambio no es visual (gestión, inversión, asesoría), el contraste va sobre **el estado del avatar o sus números**, no sobre un espacio bonito.
- **⛔ SECTORES REGULADOS — salud, estética, odontología, nutrición, fitness (11-09-2026, fuentes de Dirección).** Ahí **Meta rechaza o restringe los antes/después**, y nos toca de lleno: **Cliente 03** y cualquier cliente de bienestar. Para que pase: **mismo encuadre, misma luz y misma distancia** en las dos fotos, y **prohibido prometer resultado médico o curativo** — el «después» es un estado del avatar, no una cura. **En esos sectores el formato 2 es el más arriesgado de los 9: ante la duda, se elige otro.** Y en salud, **el 77 % de los usuarios exige contenido revisado por un profesional**, así que un testimonio sin respaldo pesa menos que en cualquier otro sector. Detalle: `../../fundamentos-copy/references/lo-que-no-funciona.md §H.1`.
- **NO:** un solo estado; números vagos; ángulos distintos; que el contraste no tenga que ver con lo que se vende.
- **TITULAR — no puede chocar con la línea del split (Dirección, 07-09-2026).** El error real: el titular baja demasiado y **choca con la línea que separa el antes del después**. La línea divisoria es un elemento ESTRUCTURAL del formato: manda ella, el texto se aparta.
  - **Split vertical (izq/der):** el titular va **entero por encima** del split, cruzando las dos mitades, en el tercio superior. Nunca centrado sobre la línea ni partido por ella.
  - **Split horizontal (arriba/abajo):** el titular va sobre el estado de arriba, **sin invadir** la banda de la línea.
  - **Holgura mínima entre el titular y la línea: el alto de una línea de texto del propio titular.** Si no cabe con esa holgura, se acorta el titular o se sube el split; **no se pega el texto a la línea**.
  - **Ojo al EJE COMPARTIDO (caso real Cliente 02, 07-09-2026):** con split vertical, la divisoria cae en el centro… y un titular centrado cae en el MISMO eje. El extremo superior de la línea apunta justo a la última línea del titular y parece que la línea "nace" del texto. Con poca holgura el choque es inevitable aunque nada se solape. Se arregla de una de estas dos formas: **(a)** subir el titular / bajar el inicio de las fotos hasta dejar **una línea de texto completa** de aire, o **(b)** romper la coincidencia de eje (titular alineado a la izquierda, o divisoria que arranca más abajo).
  - Las etiquetas de cada estado ("ANTES"/"DESPUÉS") sí viven dentro de su mitad, no sobre la línea.
- **CTA:** medio.

## 3. Review+Claim *(sin pieza aprobada guardada aún)*
- **Héroe:** la CITA real (es el titular).
- **Estructura:** quote-card dominante, cita entre comillas grande + **★★★★★** + **atribución real (cara + nombre + cargo)** + foto UGC/orgánica. ~60% cita / 40% persona. (Cliente 04: "Por primera vez invierto… sin encargarme de nada" — Tomás G.)
- **LA RESEÑA TIENE QUE DERRIBAR UNA OBJECIÓN CONCRETA (Dirección, 07-09-2026).** Es el fallo real del formato: salen reseñas correctas pero **genéricas**, que no resuelven ninguna duda, objeción ni barrera mental. Que lleve cifra y nombre no basta: una cita puede tener número y no responder a nada de lo que frena al comprador.
  - **Antes de escribir la cita, elige LA objeción** de la lista del brief (miedo, riesgo, desconfianza, coste, "esto no es para mí", "ya lo intenté", "seguro que hay letra pequeña") y **pon la cita a contestar esa**. Una pieza, una objeción.
  - **La cita cuenta el ANTES dudoso y el DESPUÉS** en palabras del cliente: "pensaba que X… y resultó que Y". El giro es lo que derriba la barrera; el elogio liso no derriba nada.
  - **Test de la reseña genérica:** si la cita valdría igual para un competidor, o para otro sector, no sirve. Tiene que ser imposible de reutilizar.
  - **Descartar de plano:** "muy profesionales", "gran servicio", "muy contentos", "los recomiendo" — y cualquier variante de elogio sin objeción detrás.
  - **La prueba tiene que venir del MISMO avatar al que habla la tanda.** Fallo real: tanda dirigida a inversores con testimonio de un propietario. **No se sustituye por el de otro avatar** — antes que eso, cita provisional del avatar correcto.
  - **Atribución de marcador = pieza NO PUBLICABLE, pero la pieza SÍ se produce.** `[FALTA]` aquí **no significa omitir el anuncio** (eso es solo para cifras, ofertas y garantías): la regla raíz 4 del `SKILL.md` manda escribir una **cita PROVISIONAL** que haga el trabajo del formato —derriba una objeción concreta, con el giro antes/después, del avatar de la tanda, imposible de reutilizar por un competidor— para que sustituirla por la real sea un cambio de una línea.
  - ⛔ **La marca `[REEMPLAZAR]` va QUEMADA DENTRO DEL PNG, en el píxel.** Anotarla solo en `specs_Tanda<N>.md` es exactamente lo que falló el 09-09-2026 (la pieza viaja sola y la nota se queda atrás): la imagen se leía como tres testimonios reales con nombre y rol. Además se anota en `specs_Tanda<N>.md` y en ESTADO.md como *pendiente de testimonio real y autorización*, y se recuerda en el resumen final. Sin la marca en el píxel, la pieza vale como referencia de composición y **no se sube a ninguna cuenta**.
- **NO:** anónimo/"- J.S."; elogio genérico; look de stock corporativo. (Distinto del testimonio-benefit: aquí manda la voz del cliente.)
- **CTA:** "Quiero saber más".

## 4. Característica→Beneficio ✅
> Confirmado con Cliente 04: salón luminoso + avatar real a la izquierda + titular «Tú inviertes, nosotros lo gestionamos todo» + 3 checks navy + CTA «Invierte sin gestionar». Logo compuesto arriba centrado.
- **Héroe:** el BENEFICIO (traducción de la gestión integral a tranquilidad).
- **Estructura:** visual limpio (persona relajada o inmueble) + **titular-beneficio** + **máx 3 checks cortos** + CTA. Mucho espacio negativo, 1 sola idea. (Cliente 04: "Tú inviertes, nosotros lo gestionamos todo" + 3 checks.)
- **NO:** comparativa Sin/Con recargada + atrezo; más de 3 checks; ruido. Los 3 checks van **por debajo** del titular en peso, con acento solo en la palabra clave y aire entre ellos (`reglas-tecnicas-y-copy.md §3`, jerarquía de lista): es el formato donde más se empasta.
- **CTA:** "Invierte sin gestionar".

## 5. Responder objeciones/haters (Contrarian) ✅ — ⚠️ NO es un checklist
> Confirmado con Cliente 04: **«Esto es solo para ricos» | La realidad es otra** + refutación de 1 frase + CTA "Invierte con confianza", con el avatar escéptico a la izquierda. Dos bloques separados por filete vertical dorado. Ese es el patrón.
- **Héroe:** la OBJECIÓN incómoda del avatar, puesta de frente y **volteada**.
- **Estructura (distinta del 4):** la objeción entrecomillada / en 1ª persona como elemento dominante ("«Creía que invertir en pisos era solo para ricos»", "«¿Y si me engañan?»") **y su refutación cruda y directa** debajo — recurso de contraste/tachado o "lo que crees vs la realidad". Tono contrarian, lenguaje crudo, **1ª persona / founder POV**. Puede ir sin persona o con founder/avatar mirando a cámara.
- **NO:** que parezca el Ad 4 (persona + 3 checks + CTA pulido); ni un testimonio elogioso (eso es el 3). Aquí se ataca una objeción, no se enumeran beneficios.
- **CTA:** baja fricción ("Descubre cómo funciona").

## 6. Resolver el pain (Problem-Solution) ✅
> Confirmado con Cliente 04: billetes derritiéndose + «Tu dinero pierde valor» / «La inflación no se detiene» arriba → flecha → maqueta de edificio + «Haz que tu dinero trabaje» + CTA «Invierte en inmobiliario».
- **Héroe:** el DOLOR concreto del avatar (dinero parado perdiendo valor).
- **Estructura:** pattern-interrupt del problema ARRIBA (metáfora visual del dolor: dinero quieto/inflación que come ahorros) + la solución ABAJO; 1ª línea problem-aware específica (<125 car.). El problema es lo que frena el scroll.
- **NO:** pregunta genérica ("¿quieres crecer?"); clip-art; que parezca el 5 (objeción) — aquí es un dolor, no una objeción a la marca.
- **CTA:** alineado al dolor.

## 7. Oferta/Escasez ✅
> Confirmado con Cliente 04: «Invierte desde 5.000 €» gigante + «Plazas limitadas por orden de llegada» + sello «Si no hay beneficio, Cliente 04 no cobra» + CTA «Invierte ahora».
- **Héroe:** la OFERTA/condición + la ESCASEZ real.
- **Estructura:** stack escaneable con la oferta como elemento más grande; **escasez REAL del brief** (plazas por orden de entrada, cupo del proyecto), risk-reversal ("modelo alineado: si no ganas, no cobramos"), condiciones/ticket visibles ("desde 5.000€"). 
- **NO:** urgencia inventada; precio escondido; que parezca editorial.
- **CTA:** transaccional pero baja fricción a llamada.

## 8. Prueba social (Stat Drop) ✅
> Confirmado con Cliente 04: «700.000 €» gigante + «cubiertos en dos semanas» + línea de contexto, fondo sobrio desaturado, sin persona.
- **Héroe:** UN número gigante (no redondeado), domina el 60% superior.
- **Estructura:** el dato real del brief en tipografía enorme ("700.000 € cubiertos en 2 semanas", "un proyecto cubierto en 30 minutos", "16 operaciones") + **fuente/contexto obligatorio** al pie + fondo desaturado sin ruido. Si el diseño compite con la métrica, mal.
- **NO:** número redondeado sin fuente; ruido gráfico; foto protagonista.
- **CTA:** medio.

## 9. Garantía (Risk Reversal) ✅
> Confirmado con Cliente 04: «Si no hay beneficio, nosotros tampoco cobramos» + «Inversión alineada. Confianza real.» + los 4 documentos reales (Dossier, Contrato de préstamo, Documento KIC, Informe final) con sus etiquetas.
- **Héroe:** el COMPROMISO defendible que quita el miedo.
- **Estructura:** el término de garantía real del brief como titular ("Si no ganas, nosotros tampoco cobramos" = modelo alineado) + sellos/términos (transparencia documental: dossier, contrato, informe final) en bento sobre el midpoint; sobrio, de confianza.
- **NO:** promesa hueca; "prueba gratis" con muro; sellos borrosos; que parezca el 5.
- **CTA:** baja fricción.

## 10. Tres pasos — FORMATO MAESTRO HISTÓRICO, **fuera de la secuencia de 9** (no se produce en la tanda)
Existe la carpeta `refs/10_tres-pasos/` (4 piezas: MMS, Cliente 13, Cliente 14, Cliente 12, Batlle) y
`patrones-diseno-estaticos.md §1.C` lo llama "el caballo de batalla" de la casa. **Aun así NO es uno de
los 9 y NO se produce en la tanda**, porque la secuencia del GPT está cerrada en 9 formatos. Se deja
escrito para que nadie lo meta por su cuenta ni lo eche en falta:
- **Dónde va su trabajo:** el freno "no sé cómo funciona / da miedo / es complicado" se resuelve **dentro
  del Anuncio 4 (Característica→Beneficio)**, cuyos **3 checks** pueden redactarse como los 3 pasos del
  proceso (`1 · 2 · 3`), manteniendo la estructura del 4.
- **Cuándo sí se produce como pieza aparte:** solo **si Dirección lo pide explícitamente**. Entonces va
  **además** de los 9, no en lugar de uno, y se numera como `10_tres-pasos` en el naming.
- **Héroe:** el MÉTODO (que haya un camino simple). **Estructura:** hook de dolor/curiosidad como titular
  + subtítulo "el proceso en 3 pasos" + `1·2·3` con icono lineal, título corto y una línea de detalle +
  CTA. Manda la **jerarquía de lista** de `reglas-tecnicas-y-copy.md §3` (≤5 palabras por ítem, acento
  solo en la palabra clave, más aire entre ítems que dentro). **NO:** más de 3 pasos; pasos que son
  features; que parezca el Anuncio 4 con checks sueltos.

> Al APROBAR cada formato con Cliente 04 (u otro cliente), actualizar aquí la línea con lo que quedó (marcar ✅) para consolidar el estándar visual de la casa.


---

# Dos patrones nuevos, sacados de la tanda de Flowboost Dubái (09-09-2026)

## Prueba social · MURO DE CITAS `"Antes X. Ahora Y."` — cuando NO hay cifras
El formato 08 se apoya normalmente en una **estadística**. Cuando el cliente no tiene ni una cifra que se
pueda sostener, **no se inventa una: se cambia el héroe de la pieza por un muro de 3 citas.**

- **3 tarjetas** apiladas, borde fino en el degradado/acento de marca, fondo oscuro, comilla grande de
  acento a la izquierda de cada una.
- **Cada cita, dos frases con la misma estructura:** `Antes <situación vieja>. Ahora <situación nueva>.`
  Es la que hace el trabajo: convierte un elogio en una **transformación concreta**.
- **Cada cita derriba una barrera DISTINTA.** En la pieza real: el tipo de lead que entra, el tiempo que
  se pierde, y la dependencia de los portales. Tres citas que dicen lo mismo con otras palabras es una
  cita repetida tres veces.
- **Firma `Nombre │ Rol, Ciudad`** debajo, con un filete corto delante. El rol y la ciudad hacen el
  reconocimiento del avatar; el nombre solo, no.
- **CTA en píldora clara** al pie, con verbo de pertenencia (`Join other <avatar>s →`).
- ⚠️ Si las citas son **generadas**, la marca `[REEMPLAZAR]` va **dentro del PNG**. Ver
  `errores-y-aprendizajes.md` (09-09-2026).

Referencia: `refs/08_prueba-social-stat/FlowboostDubai_prueba-social-stat_1x1.png`.

## Advertorial · el MASTHEAD sustituye al logo (cómo se aplica la regla de Dirección)
La regla es *en advertorial no se pone logo, se pone título de diario*. Cómo se ejecuta:

1. **Masthead inventado para la pieza**, en serif de periódico, centrado arriba. Nombre corto que suene a
   publicación del sector del avatar (`THE BROKER BRIEF` para agentes inmobiliarios).
2. **Kicker de sección** a la izquierda (`REAL ESTATE`) y **fecha** a la derecha (`September 2026`), en
   sans espaciada, pequeños, **entre dos filetes horizontales**.
3. **Titular en serif** a 2-3 líneas y **entradilla en serif** a 3-4 líneas: párrafo de noticia, no
   bullets ni claims.
4. **Foto encajada en columna con márgenes** — a sangre no, porque a sangre deja de parecer un artículo.
5. **Pie con dos filetes:** a la izquierda un descriptor en versalitas, a la derecha el **CTA en píldora
   de borde de acento** y, debajo, el logo pequeño como **firma** (`By <marca>.`).

**El logo no desaparece: baja a firma de pie.** Sin eso el anuncio no lleva marca en ningún sitio.

Referencia: `refs/01_articulo-noticia/FlowboostDubai_articulo-noticia_1x1.png`.
