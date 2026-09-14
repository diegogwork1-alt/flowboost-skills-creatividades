# Parámetros de COPY para estáticos — fuente única

> **Qué es esto.** Lo que `../../gestion-cuenta-meta/references/parametros-campana.md` es para las campañas, esto lo es para el **copy de
> los estáticos**. **Regla de precedencia: si un número de copy aparece en dos sitios y no coinciden,
> gana este.** (No promete que no se repitan: en un corpus así los números aparecen citados en varios
> ficheros a la vez, y eso está bien mientras coincidan. Lo que no puede haber es dos valores
> distintos.) **Las zonas seguras y las specs técnicas NO son copy** y viven en
> `reglas-tecnicas-y-copy.md`: ahí manda ese fichero, no este.
>
> **De dónde sale.** Del NotebookLM **«Creativos Meta»** de Dirección (80 fuentes), consultado el
> 11-09-2026, más los dos libros de la casa (`../../fundamentos-copy/references/breakthrough-advertising.pdf` y
> `../../fundamentos-copy/references/ogilvy-on-advertising.pdf`). **No es un resumen de nadie:** cada cifra lleva de dónde viene.
>
> **Vale igual para `estaticos-meta` y para `variaciones-estaticos-meta`.**
> El checklist que lo EJECUTA, pieza por pieza, es `calidad-y-autoqc.md §H`.

---

## 1. EL ORDEN EN QUE SE JUZGA UN COPY
No todos los fallos pesan igual, y auditar en desorden hace perder el tiempo puliendo frases de una
pieza que había que tirar. **Si falla un nivel, se arregla ese y no se sigue bajando.**

| | Nivel | Qué decide | Si falla |
|---|---|---|---|
| **1** | **Claridad y UNA sola idea** | *«Clarity converts, confusion kills»*. La claridad manda sobre el ingenio | se rechaza sin mirar nada más |
| **2** | **Encaje con la temperatura del embudo** | la etapa del comprador manda sobre el CTA | se cambia el CTA o el gancho |
| **3** | **Especificidad y lenguaje del comprador** | sus palabras y un dato concreto mandan sobre la jerga | se reescribe con el verbatim |
| **4** | **Límites técnicos** | caracteres y truncado | se recorta, aunque esté bien escrito |
| **5** | **Pulido de estilo** | muletillas de IA, superlativos | último filtro, nunca el primero |

*(Fuentes: Grafit Agency · SaaS Hero · Coinis · Digital Applied.)*

---

## 2. LOS NÚMEROS (todos, en un sitio)

### 2.1 Longitud
| Qué | Cifra | Fuente |
|---|---|---|
| **Titular en feed de Meta** | **25-40 caracteres**, óptimo **~27** | GetHookd · Coinis · Ryze AI |
| Pasarse de 40 | **se trunca con `...`** en móvil | Coinis |
| **Texto superpuesto en Reels** | **10 caracteres** | Coinis |
| **Palabras por línea en el canvas** | **máx. 7-8** | ROASPIG |
| **Cita / testimonio sobre la imagen** | **máx. 15 palabras** | AdRiseLab |
| **Texto principal de Meta (el de la publicación)** | el beneficio dentro de los **primeros 125 car.**, antes del «ver más» | Ryze AI · Verde Media |
| Titular de impacto directo | **5-7 palabras** | fuentes de titulares |
| Gancho de desafío directo | **≤12 palabras** | fuentes de titulares |

> **Ojo:** estos son los topes técnicos. **La doctrina de la casa es más estricta** (0-6 palabras
> visibles, máx. 8 en el núcleo titular+apoyo) y **manda** — con las exenciones de
> `calidad-y-autoqc.md §0-quater`: advertorial y Review+Claim están fuera del techo.

### 2.2 Cantidad
| Qué | Cifra | Fuente |
|---|---|---|
| **Ideas por anuncio** | **1**, estricto | SaaS Hero · Adrio · Coinis |
| **Ítems de lista / callouts** | **3-5**. **7 o más destroza la retención** | AdRiseLab |
| **Palabras de poder** («gratis», «probado») | **máx. 1** por titular | fuentes de titulares |
| **Emojis** | **máx. 1**; abusar activa revisión de política | Coinis |
| **Rayas largas (—)** | **máx. 2 por cada 100 palabras** | Digital Applied |
| **Niveles tipográficos** | **máx. 3** | (regla de la casa, `reglas-tecnicas-y-copy.md §4`) |
| **Densidad de texto** | **<20 %** de la superficie | Ads Uploader · Ryze AI |
| **Canvas despejado** | **≥40 %** libre, por carga cognitiva | JoCTEC · HCI review |

### 2.3 Tiempos — el listón real
El anuncio no se lee: se decide.
| Ventana | Qué pasa | Fuente |
|---|---|---|
| **0,4 s** | lo que tarda el gancho en activar la respuesta de orientación del cerebro | Aden's Lab |
| **1,5-1,7 s** | la ventana en la que el ojo decide si para o sigue | Aden's Lab · ROASPIG |
| **<1 s a 200 px** | a tamaño miniatura, el titular o la propuesta **tienen que entenderse** | Grafit Agency |
| **3 s** | tope para que se entienda el valor | Coinis |
| **5 s** | **prueba de comprensión**: si alguien de fuera no sabe explicar la oferta en 5 s, se reescribe | Coinis · Osh |

> La **prueba de la miniatura a 200 px** que ya usaba la casa **tiene respaldo**: no era una manía.

---

## 3. DÓNDE MIRA EL OJO (eye-tracking, medido)
Esto decide la jerarquía, no el gusto. Porcentaje del tiempo total de fijación:

| Elemento | % de atención | Qué implica |
|---|---|---|
| **Rostro humano** | **16,07-19,50 %** | es lo primero. Si hay cara, manda ella |
| **Titular principal** | **24,50-25,07 %** | segundo nivel, y el que más tiempo se lee |
| Titular secundario / apoyo | 4,40-7,20 % | tercero |
| **Logo** | **0,80-2,30 %** | **periferia. Nunca en el centro** |

- **Orden de lectura obligatorio: cara → titular → logo.** Es el mismo que ya tenía la casa en
  `reglas-tecnicas-y-copy.md §3`; ahora se sabe cuánto pesa cada uno.
- **El logo no pasa del 10 % del canvas** y va a una esquina. En el centro, el ojo lo salta por
  ceguera de banner.
- **El titular va en la franja superior o en el centro-izquierda**, que es donde caen las fijaciones.
- La **estética de la imagen explica el 40,3 % de la varianza** de la atención que luego recibe la
  marca. Y que la estética encaje con el entorno **sube la fijación un 22 %**.

*(Fuentes: SciELO/Kawano 2019 · Zoi Zoupanou 2026 · HCI & Digital Advertising Effectiveness.)*

---

## 4. CARGA COGNITIVA — por qué el minimalismo no es estética
| Dato | Fuente |
|---|---|
| Los estáticos de **baja complejidad visual reciben un 9 % más de fijaciones** | Balaban 2023 · Im 2021 |
| y se valoran como un **4,4 % más atractivos** | ídem |
| El desorden visual **reduce el tiempo de permanencia** en la pieza | JoCTEC |
| La sobreestimulación dispara **fatiga de decisión** y rechazo inmediato | HCI review |

**Regla:** un bloque de titular, una imagen clara, un CTA. **Se rechaza** la pieza con varias
tarjetas, iconos flotantes sueltos o más de 3 niveles tipográficos.

---

## 5. CURIOSIDAD vs CLICKBAIT — la frontera, medida
La curiosidad funciona; el cebo penaliza. Se mide con dos índices de 0 a 1 (*Clickbait detection*,
arXiv 2026):

| Índice | Qué mide | Titular bueno | Clickbait |
|---|---|---|---|
| **Baitness** | puntuación exagerada, mayúsculas, emoción artificial, frases que **ocultan** la información | **0,21** | 0,82 |
| **Informativeness** | densidad factual: números exactos, el beneficio nombrado | **0,79** | 0,18 |

**Cómo se audita sin calcular nada:**
- ⛔ **Rechazar el titular que esconde el sujeto o la solución para forzar el clic** — «No te vas a
  creer lo que hace este método».
- ✅ **Exigir densidad factual**: un dato, un porcentaje o el nombre exacto del beneficio.

**Y el titular vago no es curiosidad: es fricción.** Medido con eye-tracking, los titulares breves y
ambiguos **aumentan la duración de la fijación y el número de relecturas** (z = 2,54 y z = 2,66;
p = 0,02) — el lector no está intrigado, está **buscando con ansiedad** qué le quieren decir. El
titular concreto resuelve la incertidumbre **sin cobrar ese peaje**. *(Towards Gaze-Informed AI
Disclosure Interfaces, arXiv 2026.)*

---

## 6. NEUROMARKETING — el doble contraste
El ojo trabaja en dos modos:
- **Bottom-up (exógeno):** el **color, el contraste y los bordes** capturan la mirada
  automáticamente, en el primer milisegundo.
- **Top-down (endógeno):** lo que **sostiene** la mirada y genera preferencia es la **relevancia del
  texto** — el dato útil que el comprador buscaba.

**Regla:** un color de alto contraste en el botón o la palabra clave **para enganchar**, e
inmediatamente al lado **un dato operativo** para cerrar. Solo contraste = mirada que rebota. Solo
dato = no llega a mirarse. *(Biometric tools in neuromarketing, Prisma Social · SciELO.)*

---

## 7. EL TITULAR SEGÚN EL NIVEL DE CONSCIENCIA
Schwartz, con fórmula y longitud. **Primero se ubica al avatar; de ahí sale el tipo de titular.**

| Nivel del avatar | Con qué se abre | Fórmula | Car. |
|---|---|---|---|
| **Inconsciente** | historia, **advertorial**, o una verdad incómoda | contraria: «Por qué [creencia común] es en realidad [resultado malo]» | — |
| **Consciente del problema** | **pregunta de dolor** | «¿Cansado de [dolor concreto]?» | **~28** |
| **Consciente de la solución** | **cómo / dato / viejo vs nuevo** | «Cómo [resultado] en [métrica medible]» | **~27** |
| **Consciente del producto** | **caso, testimonio o comparativa** | «[Verbo] + [cifra impar] + [identidad] + [resultado]» | **~37** |
| **Totalmente consciente** | **oferta directa, precio, garantía** | «[Verbo] + [beneficio] + [condición]» | **~28** |
| *(BOFU, urgencia REAL)* | aversión a la pérdida | «[Plazo]: [oferta] termina [cuándo]» | **~36** |

- **Mercado saturado:** el titular descriptivo se vuelve invisible → **necesidad no considerada /
  contraria**, **+10 % de impacto persuasivo** frente a validar lo que ya sabe. Es el Schwartz de
  «cuando el claim está gastado, toca mecanismo».
- **Pregunta con «tú/tu»: +175 % de CTR** frente a una afirmación. (Una pregunta genérica ya da
  +150 %: **el «tú» es la mitad del efecto**.)
- **Cifra específica o impar: hasta +30 % de CTR.**

---

## 8. ¿SEGMENTA? — tres pruebas, basta con pasar una
El creativo no solo atrae al bueno: **descarta activamente al que no lo es.**
1. **Nombra la tarea u operación concreta.** «Trabaja mejor, no más» no segmenta. «Automatiza las
   altas de tu personal» sí: el que no da altas lo sabe al instante.
2. **Efecto fiesta de cóctel.** Apela a la identidad o al rol («Autónomos que facturan más de…», «Si
   tienes un local en Gràcia…»). El cerebro se desengancha de lo general y se engancha con lo suyo.
3. **Pregunta que autocalifica.** El que no es cliente contesta «no» y sigue; el que lo es contesta
   «sí, exactamente». *«¿Sigues metiendo los leads a mano en el Excel?»*

---

## 9. ANTI-PATRONES, con lo que cuestan
| Anti-patrón | Impacto medido |
|---|---|
| **Muletillas de IA** («delve», «leverage», «optimiza tu experiencia») | **−8 %** de conversión |
| **Superlativos vacíos** («increíble», «innovador», «revolucionario», «el mejor») | **−4 %** |
| **>2 rayas largas por 100 palabras** | **−5 %** (delata texto sintético) |
| **CTA de alta fricción en frío** | dispara el rebote y encarece el CPL |
| **Titular genérico de categoría** («¿Quieres hacer crecer tu negocio?») | **invisible** en el feed |
| **Cifra redondeada sin fuente** | se descarta como propaganda |
| **Urgencia falsa o perpetua** | la gente reporta u oculta el anuncio → **sube el CPM de toda la cuenta** |
| **Empezar por la marca** («En Flowboost presentamos…») | permiso inmediato para pasar de largo |
| **Foto de stock corporativo** (equipo sonriendo, apretón de manos) | **−11 %** |
| Testimonio con **cara, nombre y cargo reales** | **+14 %** |

---

## 10. LA IA, Y CÓMO LA LEE EL LECTOR
Tres hallazgos que afectan directo a lo que producimos:
1. **Aversión a la IA.** Cuando el lector percibe que el contenido es generado, **baja la
   credibilidad**: asume automatización sin supervisión humana.
2. **Se nota aunque no se sepa por qué.** El texto generado provoca **fijaciones más largas** —cuesta
   más leerlo— por discordancias sutiles de estilo, **aunque las fórmulas de legibilidad digan que es
   fácil**. → Se purga la redacción rígida y se escribe con el verbatim del cliente.
3. ⛔ **No validar un diseño con mapas de calor de IA.** Los predictores tipo Attention Insight
   **sobreestiman la atención al titular hasta un 61,47 %** cuando los humanos reales le dedican el
   **25,07 %**, y también inflan el logo. Sirven para nada en esta casa: la compuerta es
   `scripts/zonas_seguras.py` + el ojo.

*(Fuentes: Towards Gaze-Informed AI Disclosure Interfaces, arXiv · SciELO · Altay & Gilardi 2024 ·
Longoni 2022.)*

---

## 11. LO QUE MANDA POR ENCIMA DE TODO ESTO
Las fuentes son de mercado anglosajón y en buena parte de SaaS. **Donde choquen con la casa, gana la
casa**, y estos son los tres choques conocidos:
1. **Los CTA.** Las fuentes citan «prueba gratis», «ver demo», «empezar gratis». **Aquí no vendemos
   software y el funnel SIEMPRE acaba en llamada.** Sirve el mecanismo (fricción según temperatura),
   no el texto. Los nuestros: `reglas-tecnicas-y-copy.md §7` y la ficha de cada formato.
2. **El techo de palabras.** La doctrina de la casa (0-6 visibles, máx. 8 en titular+apoyo) es **más
   estricta** que los 25-40 caracteres de las fuentes, y manda. Exenciones en §0-quater.
3. **El idioma.** Todo lo de arriba está pensado en inglés. Aquí: **castellano de España** (0 voseo,
   0 léxico LATAM), **catalán** en Batlle y Cliente 09, **inglés** en Cliente 07 y Dubái.

---

## 12. DE DÓNDE SALE CADA COSA
- **NotebookLM «Creativos Meta»** (80 fuentes), consultado el 11-09-2026: los números de longitud,
  cantidad, tiempos, anti-patrones con impacto, fórmulas de titular y pruebas de segmentación.
- **PDF académicos del mismo cuaderno**: eye-tracking (HCI review · SciELO/Kawano · Zoi Zoupanou),
  carga cognitiva (JoCTEC), clickbait (arXiv Kuntur 2026), concreción y percepción de IA (arXiv
  Prajod 2026), neuromarketing (Prisma Social).
- **Libros de la casa**: `../../fundamentos-copy/references/breakthrough-advertising.pdf` (Schwartz:
  deseo, consciencia, sofisticación) y `../../fundamentos-copy/references/ogilvy-on-advertising.pdf` (los 16 checks O1-O16, extraídos
  en `../../fundamentos-copy/references/ogilvy-reglas-reales.md`).
- **No aplican a estáticos** y por eso no están aquí: `estructura-vsl.pdf` (vive en `guion-vsl`) y
  `estructura-guiones-egc.pdf` (en `guiones-egc`) — los dos son de vídeo, el *META Q4 2025 Earnings Call* (financiero) y
  *Social-First Trends 2026* de SAMY (tendencias cualitativas, sin datos de composición).
