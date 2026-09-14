# ARCHIVO COMPLETO Y MASTER MANUAL DE CREATIVOS META ADS (2026)

> ## ⛔ ESTE FICHERO ES MATERIAL DE CONSULTA, NO DOCTRINA — NO SE EJECUTA NADA DE AQUÍ
> Fuente externa B2B (SaaS, mercado anglosajón). **Se abre a mano y para una cosa concreta: el
> catálogo de arquetipos B2B, las personas de comité y la estética por rol**, cuando el cliente es
> B2B de verdad. **Ninguna regla de este fichero se ejecuta.** Si algo de aquí choca con
> `../SKILL.md`, `calidad-y-autoqc.md`, `audit-playbook-b2b.md`, `audit-rules.json` o
> `reglas-tecnicas-y-copy.md`, **pierde este fichero, siempre.**
>
> Lo que hay aquí dentro y NO vale, porque está escrito en forma ejecutable y se cuela solo:
>
> | Lo que ordena este informe | Lo que hace la casa |
> |---|---|
> | Exportar en **4:5 / 1080×1350** (incluido dentro de reglas `IF/THEN` y de un YAML «canónico») | **1:1 (1080×1080) + 9:16 (1080×1920)**, los dos siempre |
> | **«B2B Ad Score» obligatorio**, «<70: se prohíbe su subida» | **No existe.** Decide §0 + §G + los audits + el panel. Y la rúbrica de aquí está rota: le faltan los números al extraer el .docx |
> | Un **pipeline propio** de 5 etapas («Claude Skill Architecture») | El flujo es el del `SKILL.md`: fases 0-4 |
> | **Prohibir tipografías generadas por IA** | Es el método entero de la casa: el GPT genera la pieza con el texto dentro |
> | **Protocolo de preguntas al usuario** (12 campos en 3 niveles) | Regla raíz 1: **cero preguntas**. La skill decide y sigue |
> | Benchmarks **en dólares y de SaaS** (CPM $12-18, CPL $80-380), frecuencia >2,5 | Nuestros CPL reales van de **2,92 € a 49 €** (`estaticos-ganadores.md`) y el corte de frecuencia lo fija `../../gestion-cuenta-meta/references/parametros-campana.md` |
> | Safe zones propias | **270 arriba / 384 abajo / 107 laterales** (9:16) · **54 px** (1:1). Además, este fichero perdió TODAS las cifras de safe zone al extraerse |
> | El marco **95-5** (Ehrenberg-Bass: compradores dentro y fuera de mercado) | **Es estrategia de marca, no una regla de formato.** No se aplica a la producción de estáticos de captación. *(El banner anterior lo cruzaba con las safe zones, que no tienen nada que ver: error de categoría, corregido el 11-09-2026.)* |
>
> ⚠️ **Cuidado con las cifras de este fichero:** la extracción del .docx se comió números en 18
> pasajes (umbrales, tamaños, porcentajes). Un umbral sin número no es un umbral. Si necesitas una
> cifra de aquí, **no la uses: búscala en los ficheros de la casa.**


Este documento constituye el archivo definitivo y compilado de todas las directrices, especificaciones técnicas, reglas operativas, taxonomías y análisis redactados a lo largo de este proyecto de optimización de creativos para Meta Ads en 2026.

---

## 1. GUÍA DE PARAMETRIZACIÓN Y BUENAS PRÁCTICAS PARA ESTÁTICOS DE META ADS (2026)

### 1. Especificaciones Técnicas (Specs)
*   **Ratios y tamaños exactos por ubicación:**
    *   **Feed (Móvil):** 1080×1350 px (Ratio 4:5 Portrait). Es el ratio que más rinde para captación de leads en 2026 porque ocupa un **30% más de pantalla vertical** que el formato cuadrado (1:1), eliminando distracciones visuales del feed y aumentando el scroll-stopping rate.
    *   **Stories y Reels:** 1080×1920 px (Ratio 9:16 vertical).
    *   **Marketplace / Columna Derecha / Carruseles:** 1080×1080 px (Ratio 1:1 cuadrado).
    *   **Messenger Ads / Columna Derecha de Desktop:** 1200×628 px (Ratio 1.91:1 horizontal).
*   **Zonas seguras (safe zones) para Stories/Reels (9:16):**
    *   Debes dejar libre de texto y logos importantes los **269 px superiores** (14% de la altura) y los **672 px inferiores** (35% de la altura). Los elementos nativos de la interfaz de usuario de Meta (foto de perfil, nombre de usuario, CTA nativo inferior, etc.) cubren estas áreas y un 6% adicional a los lados. El área central segura garantizada es de **950×979 px**.
*   **Resolución mínima, formato de archivo y peso recomendados:**
    *   **Resolución:** Mínimo de 1080 px en el lado más corto. La mejor práctica para pantallas retina es exportar a **1440×1440 px** (para 1:1) o **1440×1800 px** (para 4:5), con un límite recomendado de **2048×2048 px** para evitar que la compresión algorítmica de la API de Meta degrade excesivamente la calidad visual.
    *   **Formato de archivo:** Usa **PNG** para creativos que lleven texto superpuesto o capturas de pantalla (evita la pixelación de bordes de tipografía) y **JPG** de alta calidad (calidad 90%+) únicamente para fotografías realistas sin texto.
    *   **Peso recomendado:** Mantener los archivos de imagen por debajo de los **30 MB** en Meta (y menos de **5 MB** en LinkedIn o **150 KB** para Google Display) para asegurar una carga instantánea en conexiones móviles lentas.
*   **Impacto de texto en la imagen en 2026:**
    *   Aunque Meta ya no aplica la regla restrictiva del 20% para rechazar anuncios de forma directa, **el algoritmo penaliza sistemáticamente la entrega y aumenta los CPMs** de las imágenes con alta densidad de texto superpuesto. Se mantiene como regla absoluta limitar el área de texto a menos del **20% de la superficie total** del canvas para asegurar el máximo alcance orgánico de la subasta.

### 2. Anatomía y Jerarquía Visual
*   **Elementos obligatorios de alta conversión (Estructura Hook-Retención-Acción):**
    1.  **Hook Visual (0-3 segundos):** Elemento de alto contraste, cara humana o patrón disruptivo que interrumpe el scroll inconsciente.
    2.  **Retención (3-10 segundos):** Texto que muestra el beneficio directo o la transformación de manera específica, no las características técnicas del producto.
    3.  **Llamado a la Acción (CTA) Claro:** Un botón gráfico dibujado directamente en el canvas que guíe al usuario hacia el siguiente paso de baja fricción.
    *   *Nota operativa:* Cada anuncio individual debe transmitir **un único mensaje de posicionamiento**. Intentar acumular múltiples ideas diluye la atención del usuario.
*   **Punto focal y dirección de lectura:**
    *   El ojo humano sigue una jerarquía de procesamiento perceptual consistente: **prioriza primero los rostros y figuras humanas, seguido del contenido textual informativo, relegando los logotipos e insignias de marca a la periferia visual**. El 80% central del feed móvil debe albergar el gancho visual y la propuesta de valor principal. Usa composiciones limpias y líneas de contraste para guiar la vista en forma de "Z" o "F".
*   **Proporción de espacio por elemento (Regla de Templates):**
    *   En un template de alto rendimiento como el **Quote Card**, el espacio se divide estrictamente: el **60% superior** se dedica a la cita de cliente (texto en tipografía sans-serif de gran tamaño), mientras que el **40% inferior** se reserva para el producto/mockup, las 5 estrellas de calificación y la atribución con el logo de marca.

### 3. Copy sobre la Imagen
*   **Límites de palabras y legibilidad móvil:**
    *   El titular de la imagen debe tener un **máximo de 7 a 8 palabras por línea**. En plantillas de texto puro (como Quote Cards o Bold Statements), el texto de la cita o frase no debe superar las **15 palabras** en total. El tamaño mínimo de fuente legible en móvil es de **14pt** (o 24px equivalente en canvas).
*   **Fórmulas de titular de alto rendimiento (Tráfico Frío / Respuesta Directa):**
    1.  *Hook de Problema Directo:* "¿Tu equipo de ventas pierde 4 horas al día en tareas manuales?"
    2.  *Hook de Verdad Contraria:* "Deja de hacer pruebas A/B en tu página de inicio. Esto encontramos en su lugar".
    3.  *Hook de Héroe de un Solo Dato (Single-Stat):* Commitearse a una gran métrica ("¿Quieres crecer tus ingresos un 1,800%?" o "127 veces más rápido").
*   **Contraste Texto/Fondo para legibilidad:**
    *   Asegurar un ratio de contraste mínimo de **4.5:1 (norma WCAG AA)**. Usa combinaciones de colores complementarios de alta saliencia, como **turquesa brillante sobre fondo azul marino** o **naranja de seguridad sobre fondo azul oscuro/gris oscuro**, y guarda siempre el archivo como **PNG** para evitar artefactos de compresión.

### 4. Tipologías de Estático (Y Cuándo Usar Cada Una)
> ⚠️ **OJO CON EL NOMBRE: estas «9 plantillas» NO son los 9 formatos de la casa.** Son otra lista, de otra fuente, y coinciden en el número — la colisión más fácil de tragarse de todo el fichero. Los 9 de la casa están en `formatos-visual-spec.md` y son los únicos que se producen. Esto de abajo es material de consulta.

Se codifican las **9 plantillas de diseño probadas por AdRiseLab** que superan en un **32% de CTR** a las fotos de producto estándar:
1.  **Quote Card:** Cita de cliente muy corta (máx. 15 palabras) en el 60% superior, combinada con foto/thumbnail, 5 estrellas y atribución en el 40% inferior. Ideal para generar confianza intermedia.
2.  **Stat Drop:** Un dato numérico de magnitud gigante dominando el canvas, con una imagen de producto secundaria y una pequeña línea de atribución de fuente en la base. Ideal para retargeting técnico y validación racional.
3.  **Before/After Split:** Comparativa directa de transformación. Exige idéntico ángulo de cámara, iluminación y distancia para evitar rechazos por fraude visual. Perfecto para estética, remodelaciones, fitness y servicios tangibles (sin prometer resultados médicos milagrosos).
4.  **Numbered Benefit List:** Lista limpia de 3 a 5 beneficios (nunca exceder de 5; 7 o más abruma al usuario). Ideal para explicar herramientas complejas o de software.
5.  **Product + Callouts:** Imagen del producto en el centro con 3 a 5 líneas de especificación señalando características clave. Excelente para tecnología, gadgets y hardware.
6.  **Comparison Grid:** Tabla comparativa "Viejo método (ultra específico)" vs. "Nuevo método (nuestro producto)". Indispensable en B2B/SaaS para forzar la migración de hábitos tradicionales.
7.  **Stack of Reviews:** 3 o 4 reseñas muy cortas apiladas verticalmente, simulando una acumulación masiva de satisfacción. Excelente para productos de alto costo (AOV alto).
8.  **Bold Statement:** Una declaración corta, audaz y sumamente específica impresa en gran tamaño sobre un fondo sólido de alto contraste. Ideal para tráfico frío.
9.  **Founder Quote:** Fotografía estilo selfie casual del fundador (rinde de un **30% a 50% mejor** que los retratos de estudio corporativos) combinada con su frase de origen o filosofía de producto.

*   **Para captación de leads B2C de servicios (no e-commerce), las tipologías más rentables son:**
    *   **Campañas de Leads con Formularios Instantáneos (Instant Forms):** Reducen el costo por cliente potencial (CPL) entre un 30% y un 45% (especialmente para servicios de ticket medio/bajo), aunque sacrifican entre un 35% y un 55% de tasa de calificación (SQL) frente a las páginas de aterrizaje tradicionales.
    *   **Campañas de Mensajería Directa (Click-to-WhatsApp o Click-to-Messenger):** Altamente eficaces para servicios locales debido a que facilitan la interacción humana en tiempo real, agilizando el agendamiento directo de citas.
    *   **UGC (User Generated Content):** Videos o fotos casuales que muestran testimonios explicativos.

### 5. Prueba Social (Social Proof)
*   **Efecto de la Especificidad:** "La especificidad convierte, la vaguedad decora". Un dato numérico verificado y auditado genera un impacto de conversión drásticamente superior a los adornos genéricos.
*   **Jerarquía de efectividad visual de Prueba Social (estudio de 2,000 páginas):**
    1.  **Named-Customer Count (+22% de conversión):** Enunciar clientes del segmento de forma clara (ej. *"Trusted by 8 of the Fortune 50"* o *"4 de los 10 principales bancos"*).
    2.  **Testimonio de Cliente Individual (+14% de conversión):** Una sola cita excelente acompañada de cara real, nombre, cargo y logotipo corporativo. Supera los muros desordenados de decenas de reseñas.
    3.  **Estadística de Escala Agregada (+9% de conversión):** Menciones de volumen masivo (ej. *"Trusted by 12,400 teams"*). *Restricción:* Esta métrica debe ser mayor a 1,000 para no parecer débil.
    4.  **Logo Strips o barra de logotipos (+8% de conversión):** Impacto modesto. Los usuarios suelen verlos como mera decoración visual corporativa.
    5.  **Logotipos de Prensa o menciones de medios (+5% de conversión):** El formato de confianza más débil. Declaraciones como *"As featured in TechCrunch"* ya no convencen a los compradores técnicos de 2026 por sí solas.

### 6. Llamado a la Acción (CTA)
*   **CTAs visuales en la imagen:** Dibuja botones en la imagen con un color de alta saliencia (contraste complementario) para enfocar visualmente la acción del scroll.
*   **CTAs en Landing Pages:** Utiliza un botón **fijo en la parte inferior móvil (sticky-bottom CTA)**, el cual aporta de forma aislada un **+11% de conversión**, superando las pruebas de botones estáticos sobre el primer pliegue.
*   **Copys de CTA alineados al funnel:**
    *   Para SaaS y herramientas: *"Start Free Trial"* (**+9% de conversión** frente al genérico "Get started").
    *   Para agencias y servicios personalizados: *"Get a Quote"* (**+14% de conversión** frente al genérico "Contact us").
    *   *Evitar:* *"Buy Now"* en campañas B2B ya que genera una penalización de **-4% de conversión** al sentirse excesivamente transaccional para compras complejas de comités.

### 7. Color / Marca / Plantilla
*   **Sensación orgánica (Thumb-stop sin parecer anuncio):** Usa una "imperfección calculada" en tus imágenes. Las fotos estilo selfie y los videos estilo UGC tomados directamente con un teléfono móvil logran el mejor enganche porque se mimetizan con el contenido nativo de los amigos del usuario.
*   **Elementos variables (Para testing a escala):** El titular del gancho de texto, la fotografía del producto/fundador, la cita de testimonio y el color de fondo.
*   **Elementos fijos (Para consistencia de marca):** El logotipo corporativo (colocado típicamente en la esquina superior derecha con un margen del 5%), la tipografía seleccionada y la rejilla de alineación visual.

### 8. Errores que Matan el Rendimiento
1.  **Look Publicitario Clásico (Stock Images):** Usar fotos corporativas de stock (ej. personas sonriendo estrechando la mano o apuntando a laptops) **reduce la conversión un 11%** porque activa de inmediato la ceguera de banners de los usuarios.
2.  **Exceso de Texto:** Superar las densidades de texto recomendadas o acumular múltiples ideas satura el canvas y degrada la entrega del algoritmo.
3.  **Falta de resolución:** Subir imágenes pixeladas o degradadas por el uso incorrecto de formatos de archivo daña las métricas de calidad de subasta en Meta.
4.  **Optimizar para "Tráfico":** El peor error estratégico al buscar captar leads o ventas. Meta enviará clics sumamente baratos y bots que jamás completarán un formulario de conversión.
5.  **No rotar creativos:** Provoca un colapso del CTR debido a la fatiga visual del anuncio.

### 9. Benchmarks y Métricas
*   **CTR para estáticos (Single Image):** Mediana de **0.90%–1.40%** en B2B (los ganadores del cuartil superior logran **1.60%–2.10%**).
*   **CPM B2B en Meta:** Mediana de **$12–$18** en SaaS general (subiendo de **$15-$24** para verticales competidas como FinTech o Cybersecurity).
*   **CPL Promedio en 2026:** **$80–$220** para formularios instantáneos (Lead Ads nativos) y **$120–$380** para conversiones directas en landing pages.
*   **Hook Rate en Video:** Superior al **50%** es considerado excelente.
*   **Alarma de Fatiga Creativa (Mátalo cuando veas al menos dos de estas señales juntas):**
    *   La frecuencia de prospección supera **2.5** en un periodo de 7 días (en retargeting, tolerar entre 5 y 8).
    *   El CTR (promedio móvil de 3 días) cae un **20-25%** por más de tres días consecutivos frente a su promedio de 14 días.
    *   El CPM sube un **15-20%** sin que existan eventos festivos o estacionales que justifiquen una saturación de subasta.
    *   El ratio de impresiones por primera vez (First-time impression ratio) se desploma por debajo del **40%**.

### 10. Producción a Escala y Testing
*   **Pruebas univariables:** Modifica una sola variable creativa a la vez (ej. solo el texto del titular, o solo el color de fondo, o la fotografía del producto) para aislar la causa del rendimiento.
*   **Pipeline de pruebas:** Elige 3 o 4 plantillas exitosas, genera 3 variaciones de cada una y lánzalas como una cohorte en conjuntos de anuncios separados. Otorga a cada creativo un presupuesto mínimo de **$50 a $100 USD** antes de tomar la decisión de pausarlo.
*   **El Efecto Sustitución (Crucial):** Para evitar que el algoritmo entre en un costoso reinicio de fase de aprendizaje, **nunca apagues un anuncio ganador fatigado de golpe**. Mantén el anuncio corriendo a un presupuesto reducido, lanza los nuevos *challengers* (variaciones) en el mismo conjunto de anuncios y, a medida que los nuevos demuestren un costo por lead competitivo y estable, retira gradualmente el presupuesto del anuncio viejo.

### 11. Estrategia por Vertical
*   **Inmobiliaria / Inversión:** Rinden mejor los videos explicativos en formato recorrido o carruseles dinámicos. Reduce la fricción con formularios de reserva nativa directa en el anuncio, lo cual incrementa las citas programadas un **34%**.
*   **Servicios Locales:** Volantes estáticos con ofertas explícitas y sencillas, precios transparentes visibles en la imagen y CTA de alta cercanía (Click-to-WhatsApp).
*   **Salud / Estética:** El médico o especialista debe ser la cara principal del anuncio (Verified Credibility). Usa UGC auténtico. Respeta la política de Antes/Después (luces y encuadres idénticos, evitando mostrar partes del cuerpo explícitas o prometer curas médicas).
*   **B2B / SaaS:** Data Ads centrados en resultados reales, diagramas de flujo simplificados, capturas recortadas de dashboards reales y carruseles educativos comparativos. Conecta las campañas a través de **HubSpot Conversions API** para contrarrestar la pérdida de datos de atribución tras iOS.

### 12. Compliance y Políticas
*   **Categorías Especiales:** Asegúrate de activar las casillas correspondientes de vivienda, empleo, crédito/finanzas o política para evitar suspensiones de cuenta automáticas de Meta.
*   **Comparaciones sin marcas:** No nombres marcas comerciales registradas de tus competidores de forma directa en el texto o la imagen del anuncio. Usa fórmulas alternativas y seguras como la de Zapier, comparando las ventajas de tu producto directamente contra una columna llamada **"No Automation"** o **"Procesos Manuales"**.

---

## 2. STATIC B2B META AD DESIGN AND COMPOSITION RULES (2026)

### Visual Styles and Aesthetics
The visual design of B2B static creative must move past standard stock models and generic gradient backgrounds. It focuses on functional design systems built around the core claims of the product. The eight leading styles are:
*   **Editorial:** Elegant, high-whitespace layouts using serif display type for bold category arguments, desaturated pastel backgrounds (such as Clay's light lavender), and minimal layout clutter.
*   **Product-Led:** Immersive, highly zoomed mockups of actual software dashboards inside minimal device frames, complete with workflow annotations (arrows, highlight circles) outlining feature value.
*   **Brutalist:** Stark, unpolished, high-contrast layouts featuring safety-neon color blocks (yellow/orange), heavy dark borders, system-monospaced fonts, and crossed-out elements to act as a physical scroll-stopper in professional feeds.
*   **Premium:** Pristine, monochromatic layouts utilizing deep gray, black, or near-white backdrops with extensive negative space, sharp product photography, and high-prestige typography designed to reduce enterprise friction.
*   **Meme / Pattern Interrupt:** Hand-drawn flowcharts, post-it notes, whiteboard doodles, or screenshots of professional text posts that feel completely organic to the scrolling user.
*   **Native / Thought-Leader:** Unpolished screenshots of Slack chats, forwarded customer emails, or real G2 reviews coupled with casual phone selfies of founders to prioritize raw trust over overproduced branding.
*   **Report-Style:** Academic publication covers featuring clean grid structures, metadata pills (e.g., "Study 2026"), and professional diagrams representing high-value gated assets.
*   **Data-Driven / Stat Drop:** Oversized numeric statistics displaying specific case study outcomes alongside simple anonymized dashboard cards and clear source lines.

### Composition, Layout, and Visual Hierarchy
A high-converting static ad relies on a disciplined reading flow designed to prevent cognitive fatigue. The perceptual visual hierarchy of the human eye prioritizes **faces first, followed by readable text blocks, and lastly logos or branding markers**.
*   **Visual Hook:** Positioned centrally on the canvas to stop the eye within 1.5 seconds.
*   **Headline:** Set in dominant scale to deliver the main positioning claim.
*   **Supporting Evidence:** Visual mockups or social validation proof explaining the headline claim.
*   **Branding & CTA:** Minimalist logo placement and a clear button drawn at the bottom.

### Spacing, Grids, and Scale
*   **Grid Systems:** Use structured modular grids (like bento layouts) to keep distinct copy blocks and images separate.
*   **Margins:** Maintain at least a **5% margin** away from all canvas borders to prevent mobile UI clipping.
*   **Sizing Hierarchy:** Headlines must be a minimum of **48px**, subheadlines 32-40px, and image body copy at least 24-28px. The canvas must use a maximum of **three hierarchy levels** to prevent clutter.

### Contrast and Whitespace
*   **Negative Space:** Keep at least 40% of the canvas as whitespace or desaturated backgrounds to drive focus to your primary visual hook.
*   **Contrast Standards:** Adhere to a minimum **4.5:1 WCAG AA contrast ratio** for text and CTAs against backgrounds. Use extreme pairings like dark navy backgrounds with high-salience orange or turquoise highlights.

### Mobile Readability & Information Density
*   **The One-Idea Rule:** Limit each static ad variant to **one single positioning claim**. Stacking feature lists on a single canvas decreases conversion.
*   **The 20% Rule:** Although not strictly blocked by Meta, **high text density leads to delivery penalties and higher CPMs**. Text overlays must represent less than 20% of the canvas surface area.

### Generic vs. Distinctive SaaS Design (Polished vs. Lo-Fi)
Category saturation occurs when brands use identical template structures. Distinctive brands break category norms by using ownable assets (colors, specific layout frames). While "polished" enterprise layouts establish baseline credibility, "lo-fi" or native formats (Slack crops, founder selfies) act as powerful feed-level pattern interrupts.

---

## 3. COPYWRITING INSIDE B2B META ADS (2026)

### On-Image Sizing & Caption Limits
*   **Headline Length:** Cap headlines on the image canvas at **7 to 8 words per line**.
*   **Quote Length:** Testimonial quotes on Quote Card templates **must not exceed 15 words** to protect the visual hierarchy.
*   **Primary Caption Truncation:** Meta's mobile feed truncates primary copy after **125 characters**. Front-load your core positioning hook before this break to avoid forcing the user to click "See more."

### Purging Generic Jargon & AI "Tells" (Empirical Evidence)
A large-scale empirical test of **2,000 landing pages (Q4 2025–Q1 2026)** proved that generic marketing language and AI-generated text patterns carry massive conversion penalties.
*   **AI Tells:** The inclusion of terms like **"delve"**, **"leverage"**, **"synergize"**, or **"optimize your experience"** decreases conversions by **-8%**.
*   **Superlatives:** Using unbacked words like "amazing," "innovative," or "cutting-edge" results in a **-4% conversion penalty**.
*   **Punctuation Overhead:** Using more than two em-dashes per 100 words triggers an average **-5% conversion decrease**.

### Proven Headline & Hook Structures
1.  **The Single-Stat Headline (+18% conversion lift):** Committing to a single giant outcome metric (e.g., *"Want to grow revenue 1,800%?"* or *"127x faster"*) drives the highest conversion lift of any headline pattern.
2.  **The Unconsidered Need Hook (+10% persuasive impact):** Introduces a hidden operational bottleneck the buyer has overlooked (e.g., *"There's one ad targeting setting most advertisers never check—and it is costing them 20%+ of their budget"*).
3.  **The Contrarian-Truth Hook:** Challenges standard category playbooks to instantly engage the reader (e.g., *"Stop A/B testing your homepage. Here's what we found instead"*).
4.  **The Problem-Agitation Hook:** Points directly to a daily operational frustration and names its immediate consequence (e.g., *"Your sales team is wasting 4 hours/day on manual CRM entry"*).

### Overcoming Objections & Structuring Social Proof
*   **Speed-to-Value:** Mitigate transition friction with copy structures like: **"[Specific Outcome], Overnight"** (e.g., *"50% Reduction in Time-to-Hire, Overnight"*).
*   **Tool Sprawl/Overlap:** Use consolidation hooks: **"Ramp Cut Tool Costs by 70%"**.
*   **Social Proof Hierarchy (Evidence-Backed Conversion Lift):**
    1.  *Named-Customer Segment Count:* e.g., *"Trusted by 8 of the Fortune 50"* (**+22% lift**).
    2.  *Single Testimonial Card:* One specific quote with name, role, face, and corporate logo (**+14% lift**).
    3.  *Aggregate Scale Stat:* e.g., *"Trusted by 12,400 marketing teams"* (**+9% lift**). *Constraint:* Must be >1,000 to remain credible.
    4.  *Logo Strips:* Row of monochrome partner logos (**+8% lift**).
    5.  *Press Logos:* e.g., *"As featured in TechCrunch"* (**+5% lift**).

---

## 4. VISUALLY PRESENTING PRODUCTS, SAAS UI, AND PROOF

### I. Product UI & Dashboard Presentation Rules
To present software effectively in mobile ads, designers must apply structural simplification to avoid cognitive overload:
*   **The Zoom & Crop Protocol:** Never display an unedited, full-screen desktop dashboard. Isolate a single active screen card, toggle state, or input flow. Crop the graphic tightly and test readability by scaling it down to a **200px thumbnail**; if the UI is unreadable in one second, crop it closer.
*   **Minimal Browser Frames:** Wrap cropped product screenshots in simplified, clean browser margins or device outlines to signal "software" without adding visual noise.
*   **Floating UI Panels:** Set secondary dashboard elements to low opacity or desaturated tones, using bright, high-salience spotlight borders, highlight circles, or visual arrows to focus attention strictly on the active feature panel.
*   **Workflow Annotations:** Annotations must not point to generic labels; they must call out **quantified workflow outcomes** (e.g., "Closes in CRM automatically" instead of "Settings Node").

### II. Visualizing Social Proof & Validation
*   **The Quote Card Template:** Dedicate the upper 60% of the canvas to a customer quote in clean, bold sans-serif text, and the bottom 40% to a simple product shot, a 5-star rating row, and the customer's attribution.
*   **The Slack / G2 Screenshot Format:** Raw, unpolished crops of real reviews, emails, or Slack chats act as powerful pattern interrupts, bypassing banner-blindness by looking like organic workspace communications.
*   **The Testimonial Stack:** For high-AOV enterprise software, stacking 3 to 4 short review snippets vertically on the canvas builds a robust narrative of third-party validation.
*   **In-Creative Trust Badges:** Place G2 badges, security certifications (SOC2, ISO), and partner endorsements directly inside the ad creative to de-risk vendor selection at the very first touchpoint.

### III. Strategic Design Hierarchy Decisions
*   **Product as Hero:** Best for **Middle-funnel consideration and self-serve PLG motions** where the interface is highly intuitive and solves a known workflow bottleneck in a single frame.
*   **Pain as Hero:** Best for **Top-of-Funnel (TOFU) prospecting and cold traffic**. Isolate a painful daily behavior the user recognizes in themselves (e.g., Foleon's ad showing a crossed-out PDF icon with the headline *"Tell me you're not sending PDFs to actual prospects"*).
*   **Proof as Hero:** Best for **Bottom-of-Funnel (BOFU) retargeting and high-contract-value enterprise accounts** evaluating migration risk. Lead with specific case study metrics and G2 ratings.

---

## 5. TAXONOMY OF STATIC B2B META AD ARCHETYPES (2026 EDITION)

### 1. Product-Led Archetype
*   **Layout:** Upper third dedicated to a bold headline positioning a core product action; lower two-thirds showing a highly cropped, high-contrast, zoomed product interface shot inside a device outline or browser frame.
*   **Hero Element:** The cropped, zoomed screenshot of the product workspace showing a task mid-execution.
*   **Headline Type:** Action-focused use-case verb: *"Start accepting payments in minutes, not days"*.
*   **Visual Style:** Premium or product-led aesthetic; crisp light or device-native dark surfaces with high-salience accents.
*   **Proof:** Actual, functional buttons, real data fields, and cropped UI showing product utility.
*   **CTA:** Button on image or Meta button set to *"Start Free"* or *"Request a Demo"*.
*   **Funnel Stage:** Middle-funnel (Education/Validation).
*   **Awareness Stage:** Solution-aware to Product-aware.
*   **Best Personas:** C-Suite economic buyers (CFOs evaluating tool stack) and operational directors.
*   **Best Industries:** B2B SaaS, developer tools, and workflow management.
*   **Common Mistakes:** Attempting to display the entire, uncropped desktop workspace, making all cells and labels microscopic and unreadable on mobile screens.
*   **Useful Variations:** Single-image square (1200x1200px) or 4:5 vertical feed crops (1080x1350px).

### 2. Problem/Solution Archetype
*   **Layout:** Two-part message hierarchy: top half isolates a clear and highly recognizable category question/pain, bottom half introduces the visual product solution in a clean negative space.
*   **Hero Element:** The visual solution (e.g., 10 branded variants generated from one product).
*   **Headline Type:** Direct interrogative hook: *"Still making ad variants one by one?"*.
*   **Visual Style:** Clean, high-contrast layouts; bright colored typography against dark, solid backdrops.
*   **Proof:** Instant visual demonstration of the mechanism that solves the pain.
*   **CTA:** *"Learn More"* or *"Get Started"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) prospecting.
*   **Awareness Stage:** Problem-aware.
*   **Best Personas:** Frontline operators and execution-level team leads.
*   **Best Industries:** Martech, productivity SaaS, and HR Tech.
*   **Common Mistakes:** Introducing too many secondary benefits, which dilutes attention and lowers feed engagement.
*   **Useful Variations:** Headline angle testing (comparing question hook vs. bold stat hook).

### 3. Pain-Led Archetype
*   **Layout:** Highly disruptive single-pane layout. Giant bold typography names a specific, painful operational behavior or broken category process, often paired with a jarring, stripped-back visual.
*   **Hero Element:** The painful category process represented as a simple visual metaphor (e.g., a crossed-out PDF icon).
*   **Headline Type:** Aggressive and direct behavior call-out: *"Tell Me You're Not Sending PDFs to Actual Prospects"*.
*   **Visual Style:** Brutalist or native aesthetic; safety neon backgrounds or raw off-white layouts to break feed wallpaper.
*   **Proof:** Empathy-driven validation of the prospect's daily operational frustration.
*   **CTA:** Low-friction offer: *"Send us a file,"* *"Take a quiz,"* or *"Claim a sample"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) prospecting.
*   **Awareness Stage:** Unaware to Problem-aware.
*   **Best Personas:** Frontline practitioners, marketers, and sales development reps (SDRs).
*   **Best Industries:** Enterprise SaaS, digital content engines, and document platforms.
*   **Common Mistakes:** Over-agitating the pain point to the point of being manipulative or fear-mongering, which alienates B2B buyers.
*   **Useful Variations:** Strikethrough text overlays or digital scribble overlays.

### 4. Outcome-Led Archetype
*   **Layout:** Giant typography centered on the canvas, emphasizing speed and scale of value, with a desaturated product UI card positioned underneath.
*   **Hero Element:** The compressed speed-of-value statement.
*   **Headline Type:** Dual-claim outcome: *"50% Reduction in Time-to-Hire, Overnight"*.
*   **Visual Style:** Confident, high-contrast, minimalist layout with a strict visual focus on the text.
*   **Proof:** Specific, defensible metrics combined with a named enterprise customer.
*   **CTA:** *"Start Free"* or *"Request a Demo"*.
*   **Funnel Stage:** Middle-funnel (Education) to Bottom-funnel (Decision).
*   **Awareness Stage:** Solution-aware.
*   **Best Personas:** Executive buyers, VPs of HR, and operational directors.
*   **Best Industries:** Enterprise software, recruitment tech, and operations platforms.
*   **Common Mistakes:** Leading with vague, non-defensible taglines like "work smarter" instead of a quantified magnitude of transformation.
*   **Useful Variations:** Landscape formats for LinkedIn or vertical 9:16 reframes for Reels/Stories.

### 5. ROI Archetype
*   **Layout:** Structured bento or modular grid cleanly separating the value metric from the customer logo and product interface.
*   **Hero Element:** One specific, verifiable return metric from a named customer outcome.
*   **Headline Type:** Defensible financial return: *"How Notion Saved Us $250K in Tool Spend"* or *"$50M ARR in 6 months"*.
*   **Visual Style:** Premium and authoritative; desaturated monochromatic panels with stark, clear numbers.
*   **Proof:** Marquee customer logo and explicit financial numbers from a real case study.
*   **CTA:** *"Download Comparison"* or *"Calculate Savings"*.
*   **Funnel Stage:** Bottom-of-Funnel (BOFU) decision and retargeting.
*   **Awareness Stage:** Product-aware.
*   **Best Personas:** Chief Financial Officers (CFOs), procurement heads, and executive buyers.
*   **Best Industries:** Financial tech (FinTech), business intelligence, and IT infrastructure.
*   **Common Mistakes:** Presenting "too good to be true" financial percentages without an explicit customer logo or source line.
*   **Useful Variations:** TCO (Total Cost of Ownership) comparisons or interactive calculators.

### 6. Statistic-Led Archetype (The "Stat Drop")
*   **Layout:** Large, bold outcome metric dominating the frame, a secondary product shot placed underneath, and a tiny source line set at the base of the canvas.
*   **Hero Element:** The massive displaying number (e.g., "75%").
*   **Headline Type:** Impact statistical claim: *"9 out of 10 customers see results in 2 weeks"* or *"75% Performance Boost"*.
*   **Visual Style:** Stark and data-focused; bright accent numbers (like electric turquoise or neon orange) set against deep navy or dark gray backdrops.
*   **Proof:** Highly legible source attribution line at the base.
*   **CTA:** *"Read the Study"* or *"Explore Data"*.
*   **Funnel Stage:** Middle-funnel validation.
*   **Awareness Stage:** Solution-aware.
*   **Best Personas:** Technical buyers, engineers, and risk-conscious directors.
*   **Best Industries:** Cybersecurity, developer tools, SaaS analytics, and business intelligence.
*   **Common Mistakes:** Omitting the source line, which causes the metric to be visually discounted by B2B buyers as marketing hype.
*   **Useful Variations:** Multiple metrics in a 3x1 bento layout or single-column stacked display for mobile feeds.

### 7. Case Study Archetype
*   **Layout:** Two-frame split or asymmetrical card: the left/upper half presents the client's problem-outcome stat; the right/lower half features a real, recognizable photo or brand-aligned asset representing the case study client.
*   **Hero Element:** The quantified client outcome and client logo.
*   **Headline Type:** Credible, specific narrative: *"How [Recognizable Client] cut [Metric] by [Number]%"*.
*   **Visual Style:** Editorial, clean brand layout with consistent brand typography and signature palettes.
*   **Proof:** Specific named company logo, real client face, and raw, non-rounded performance data.
*   **CTA:** *"Discover How"* or *"Read Case Study"*.
*   **Funnel Stage:** Middle-to-bottom funnel (Validation).
*   **Awareness Stage:** Solution-aware to Product-aware.
*   **Best Personas:** Department heads and VP-level evaluators looking to reduce migration and implementation risk.
*   **Best Industries:** B2B SaaS, tech consulting, and specialized enterprise services.
*   **Common Mistakes:** Using generic stock photos of smiling people, which reduces landing page conversion rates by 11%.
*   **Useful Variations:** Sequential carousels detailing the before, the process, and the final audited result.

### 8. Testimonial Archetype (The "Quote Card")
*   **Layout:** The customer quote occupies the top 60% of the ad in large, elegant display typography; the bottom 40% features a real product thumbnail, a 5-star rating row, and the customer's name, role, and logo.
*   **Hero Element:** The customer's quote.
*   **Headline Type:** Real, natural-voice client quotation: *"Cut our weekly creative production from 6 hours to 45 minutes"*.
*   **Visual Style:** Clean editorial or native review aesthetic; generous whitespace and high-contrast text surfaces.
*   **Proof:** Verifiable entity attribution (face, name, company role, and corporate logo).
*   **CTA:** *"Request a Demo"* or *"Read the Review"*.
*   **Funnel Stage:** Middle/bottom-funnel retargeting and validation.
*   **Awareness Stage:** Solution-aware to Product-aware.
*   **Best Personas:** Mid-level operators evaluating ease of use and daily workflow fit.
*   **Best Industries:** B2B software, marketing tools, agencies, and professional services.
*   **Common Mistakes:** Writing or using quotes that are too long (exceeding 15 words on the canvas), which completely destroys the visual hierarchy.
*   **Useful Variations:** Multi-card carousels featuring 4-6 distinct slides, each showing one specific result from one named client.

### 9. Comparison Archetype
*   **Layout:** Two distinct visual columns comparing specific parameters side-by-side; the left column represents the competitor/default method, while the right column showcases the product as the superior upgrade.
*   **Hero Element:** The visual upgrade and cost/time differences.
*   **Headline Type:** Direct alternative assertion: *"Framer: It's like Figma but you get a real site"*.
*   **Visual Style:** Clean, tabular grid layout; high contrast color blocks (e.g., gray for the old way vs. brand-accent color for the product).
*   **Proof:** Explicit rows of comparison metrics (time to first output, tools needed, cost per asset).
*   **CTA:** *"Download Comparison Guide"* or *"Start Free"*.
*   **Funnel Stage:** Bottom-of-funnel (Decision) and competitive conquesting.
*   **Awareness Stage:** Product-aware.
*   **Best Personas:** Procurement teams, IT directors, and technical champions.
*   **Best Industries:** Highly crowded B2B categories, web design, and developer tools.
*   **Common Mistakes:** Being vague about the default method (e.g., "the old way is bad" instead of listing exact friction rows like "5 nicks per shave").
*   **Useful Variations:** Dynamic carousels comparing specific feature metrics slide-by-slide.

### 10. Old Way vs. New Way Archetype
*   **Layout:** Side-by-side or stacked split screen: the "old way" panel shows a chaotic workflow, cluttered dashboard, or manual spreadsheets; the "new way" panel shows a clean, automated single-screen canvas.
*   **Hero Element:** The contrast between the two states.
*   **Headline Type:** Contrast-led metric: *"Before: 3 tools and 2 hours vs. After: one canvas and 60 seconds"*, or *"Old Way: 6% Open Rate vs. New Way: 60% Open Rate"*.
*   **Visual Style:** Minimalist split screen; dark/messy desaturated tones on the "old way" side vs. bright, clean dark-mode or light-mode branding on the "new way".
*   **Proof:** Raw performance numbers and visual workflow simplicity.
*   **CTA:** *"See the Difference"* or *"Try Now"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) prospecting and Education.
*   **Awareness Stage:** Problem-aware to Solution-aware.
*   **Best Personas:** Operational managers and overworked end-users.
*   **Best Industries:** Workflow automation SaaS, productivity tools, and data integrations.
*   **Common Mistakes:** Using fake, exaggerated, or non-verifiable numbers that damage trust.
*   **Useful Variations:** Video side-by-sides or simple 2-frame carousels.

### 11. Report Archetype
*   **Layout:** Highly structured publication-cover layout; clean background grid, centered focus, pill label tags for metadata (e.g., "2026 Ebook," "Study 2026"), and abstract geographic or dotted grids.
*   **Hero Element:** The premium-looking cover of the PDF/Ebook itself.
*   **Headline Type:** Authoritative and educational: *"How to Develop an Effective Sales Territory Strategy at an Early Stage Startup"*.
*   **Visual Style:** Report-style and academic aesthetic; pristine layouts that mirror physical high-value industry journals.
*   **Proof:** Publication authority, metadata pills, and professional diagrams.
*   **CTA:** *"Download"* or *"Download the Report"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) demand capture.
*   **Awareness Stage:** Unaware to Problem-aware.
*   **Best Personas:** Executive leaders, strategists, and founders looking to solve highly specific knowledge gaps.
*   **Best Industries:** B2B SaaS, sales intelligence, fintech, and legaltech.
*   **Common Mistakes:** Relying on cheap, generic Canva templates that register as spam and lack perceived production value.
*   **Useful Variations:** Interactive infographics or mini-slide carousels presenting 2-3 key findings.

### 12. Lead Magnet Archetype
*   **Layout:** High-contrast, clean billboard layout displaying the tangible asset cover (checklist, guide, template bundle) alongside a direct value promise.
*   **Hero Element:** The template cover or visual preview of the tool/checklist.
*   **Headline Type:** Benefit-focused and concrete: *"Download the 15-Step B2B Ad Design Checklist"*.
*   **Visual Style:** Editorial, clean, and highly scannable; bold accent colors for the key asset title.
*   **Proof:** Perceived value of the resource, verified steps, and professional covers.
*   **CTA:** *"Download Your Free Article"* or *"Get the Free Guide"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) prospecting.
*   **Awareness Stage:** Problem-aware.
*   **Best Personas:** Execution-level team members and frontline managers.
*   **Best Industries:** Marketing technology (Martech), development, and sales services.
*   **Common Mistakes:** Failing to repeat the exact, identical headline of the ad on the landing page, resulting in massive audience drop-off.
*   **Useful Variations:** Lead generation ads utilizing Meta's Instant Forms, which achieve a 4x conversion rate versus standard landing pages.

### 13. Demo Archetype
*   **Layout:** A crisp, cropped screenshot of a live interface mid-task, annotated with a few simple highlight circles or arrows showing a single, clear outcome.
*   **Hero Element:** The visual action of the software solving a specific task.
*   **Headline Type:** Action-oriented: *"See Fin in Action"* or *"Generate 10 Branded Meta Statics in Minutes"*.
*   **Visual Style:** Product-led aesthetic; device frames, minimalist drop-shadows, and a highly scannable layout.
*   **Proof:** An actual, cropped screenshot of the live, functioning product interface.
*   **CTA:** *"Watch the Demo"* or *"Start Free"*.
*   **Funnel Stage:** Middle-to-bottom funnel (Consideration/Decision).
*   **Awareness Stage:** Solution-aware to Product-aware.
*   **Best Personas:** Technical champions, end-users, and C-Suite evaluators evaluating software speed.
*   **Best Industries:** Highly visual B2B software, automation tech, and CRM systems.
*   **Common Mistakes:** Showing full-page screenshots of complex dashboards that appear dense, overwhelming, and unreadable on mobile screens.
*   **Useful Variations:** 30-second micro-demo video clips focusing exclusively on solving a single pain point.

### 14. Founder POV Archetype
*   **Layout:** An informal, casual photo of the company founder (preferably a phone selfie) on one side, paired with a personal origin or belief quote on the other, attributed underneath.
*   **Hero Element:** The candid founder photo and personal quote.
*   **Headline Type:** Direct, belief-driven hook: *"We built this because we were tired of AI tools making pretty images but no testable Meta ads"*.
*   **Visual Style:** Native, organic, and non-commercial; avoids corporate headshots and professional studio lighting.
*   **Proof:** Real domain credibility, a personal backstory, and raw human face-to-face trust.
*   **CTA:** *"Book a Demo"* or *"Read Our Story"*.
*   **Funnel Stage:** Middle-funnel (Consideration).
*   **Awareness Stage:** Solution-aware to Product-aware.
*   **Best Personas:** Business owners, startup founders, and mission-aligned corporate executives.
*   **Best Industries:** Early-stage startups, bootstrapped SaaS, and high-trust service segments.
*   **Common Mistakes:** Using overly polished, staged corporate portrait photography, which underperforms candid selfies by 30% to 50%.
*   **Useful Variations:** Running as a LinkedIn Thought Leader Ad, which delivers 6.4x higher CTR than standard company-page single-image ads.

### 15. Meme Archetype
*   **Layout:** Styled directly as native, organic social media content; standard single-panel meme frames, Twitter/X post screenshots, or simple handwritten post-it notes.
*   **Hero Element:** The highly relatable, industry-specific professional joke.
*   **Headline Type:** Identity-matching humor: *"Become the hero in your org"* or *"The spreadsheet short built for watching spreadsheets"*.
*   **Visual Style:** Meme or pattern-interrupt aesthetic; unpolished, stark, and native to social feeds.
*   **Proof:** Deep, empathetic alignment with the target audience's professional identity.
*   **CTA:** Low-commitment call-to-action: *"Claim a Sample"* or *"Learn More"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) prospecting.
*   **Awareness Stage:** Unaware to Problem-aware.
*   **Best Personas:** Overworked frontline practitioners who care about how they are perceived at work.
*   **Best Industries:** Productivity software, data-heavy systems, and developer tools.
*   **Common Mistakes:** Attempting to force outdated consumer trends or generic humor templates that fail to connect with the buyer's professional daily reality.
*   **Useful Variations:** Whiteboard-style doodles or flowcharts.

### 16. Screenshot Archetype
*   **Layout:** Raw, unedited, or minimalist-cropped crop of a real digital interaction; a star review screen, G2 badge row, or standard customer interaction.
*   **Hero Element:** The un-designed asset of real third-party validation.
*   **Headline Type:** Conversational, unedited text quote: *"Used by 8 of the Fortune 50"* or *"The demo looked great. Implementation took eight months"*.
*   **Visual Style:** Native review aesthetic; unpolished, stark, and heavily focused on trust over beauty.
*   **Proof:** Real customer entity details, stars, and authentic, conversational quotes.
*   **CTA:** *"Start Free"* or *"Read Reviews"*.
*   **Funnel Stage:** Middle-to-bottom funnel (Validation).
*   **Awareness Stage:** Solution-aware to Product-aware.
*   **Best Personas:** Technical evaluators, risk managers, and mid-level managers.
*   **Best Industries:** High-AOV software, cybersecurity, and enterprise systems.
*   **Common Mistakes:** Staging fake reviews or using highly polished review templates that scream "ADVERTISEMENT" and trigger instant scroll-past.
*   **Useful Variations:** Stacking 3 to 4 short review screenshots vertically to build volume of validation.

### 17. Slack/Email/Spreadsheet Style Archetype
*   **Layout:** Styled to look like a raw, direct piece of standard office communication; a Slack message, a forwarded customer email, or a spreadsheet grid.
*   **Hero Element:** The unpolished interaction layout (e.g., a G2 review screenshot or a customer email with its raw header).
*   **Headline Type:** Authentic voice-of-customer quote: *"This tool cut our weekly creative production in half"*.
*   **Visual Style:** Native review aesthetic; clean, raw, and completely indistinguishable from organic workspace screenshots.
*   **Proof:** Verifiable email headers, actual G2 rating stars, or real un-rounded numbers.
*   **CTA:** *"Watch the Demo"* or *"Learn More"*.
*   **Funnel Stage:** Middle-to-bottom funnel (Validation).
*   **Awareness Stage:** Product-aware.
*   **Best Personas:** Mid-level operators, operations heads, and managers.
*   **Best Industries:** B2B SaaS, automation platforms, and workflow tools.
*   **Common Mistakes:** Polishing the screenshot too much, removing G2 or Slack UI context, which completely breaks the pattern-interrupt signal.
*   **Useful Variations:** Running as a carousel where each card is a different G2 screenshot.

### 18. Diagram Archetype
*   **Layout:** Simple, high-contrast visual flow or abstract architectural diagram explaining how a complex technology works.
*   **Hero Element:** The simplified visual flow or system architecture.
*   **Headline Type:** Explanatory and informative: *"How we process real-time data at scale"* or *"Psychological principles of high-converting sites"*.
*   **Visual Style:** Product-led and data-driven; clean vectors, desaturated backdrops with bright orange or turquoise accent nodes.
*   **Proof:** Clear system mechanics and structural logic.
*   **CTA:** *"Download Your Free Article"* or *"Watch the Demo"*.
*   **Funnel Stage:** Middle-funnel (Education).
*   **Awareness Stage:** Solution-aware.
*   **Best Personas:** Technical buyers, Chief Technology Officers (CTOs), and engineers.
*   **Best Industries:** Highly technical B2B platforms, developer tools, cyber security, and database SaaS.
*   **Common Mistakes:** Designing a diagram that is too dense, cluttered, and complex, making it unreadable on mobile screens.
*   **Useful Variations:** Simple animated GIFs or HTML5 loops showing state transitions.

### 19. Infographic Archetype
*   **Layout:** Structured single-pane layout presenting visual data insights, stylized landing page mockups, and annotated cues.
*   **Hero Element:** The clean, scannable data visualization or stylized mockup.
*   **Headline Type:** Tactical and insight-forward: *"Download your free article"* or *"5 steps to optimize your conversion"*.
*   **Visual Style:** Structured, minimal, and informative; bold, professional navy backgrounds with vibrant accents.
*   **Proof:** Clean visual annotations, dotted location maps, and dollar-pin icons.
*   **CTA:** *"Download"* or *"Download your free article"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) prospecting and Education.
*   **Awareness Stage:** Problem-aware to Solution-aware.
*   **Best Personas:** Marketers, designers, and visual strategists.
*   **Best Industries:** Web design, digital marketing, Martech, and consulting.
*   **Common Mistakes:** Trying to cram a full multi-point infographic into a single 1:1 image, resulting in text-clutter and algorithmic deprioritization.
*   **Useful Variations:** Carousel infographics where each slide covers a step or an error.

### 20. Visual Metaphor Archetype
*   **Layout:** Centered on an unexpected, high-concept visual that highlights a painful daily category reality without showing the software.
*   **Hero Element:** The striking visual metaphor (e.g., a person drowning in spreadsheets).
*   **Headline Type:** Provocative or situational: *"We were tired of pretty images"* or *"Become the hero in your org"*.
*   **Visual Style:** High contrast, minimal visual noise, and large, elegant display typography.
*   **Proof:** Human emotion or deep situational empathy.
*   **CTA:** *"See Examples"* or *"Request a Demo"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) prospecting.
*   **Awareness Stage:** Unaware to Problem-aware.
*   **Best Personas:** Executive leaders and founders looking for immediate category differentiation.
*   **Best Industries:** Creative platforms, high-growth SaaS, and marketing agencies.
*   **Common Mistakes:** Using complex, abstract visual metaphors that require more than one second to comprehend.
*   **Useful Variations:** Short Reels or Stories with kinetic typography overlays.

### 21. AI-Generated Creative Archetype
*   **Layout:** Highly vibrant, polished image generated from prompts, typically layered with a simple headline overlay and branding logo.
*   **Hero Element:** The vibrant, hyper-realistic, or highly stylized background.
*   **Headline Type:** Generic or functional copywriting: *"Create Bold Content"* or *"Optimize your experience"*.
*   **Visual Style:** Highly colorful, vibrant, but often sterile; risks looking identical to category competitors if brand guides are ignored.
*   **Proof:** Rapid concept variation and layout speed.
*   **CTA:** *"Book a Demo"* or *"Learn More"*.
*   **Funnel Stage:** Top-of-Funnel (TOFU) concept testing.
*   **Awareness Stage:** Unaware.
*   **Best Personas:** General audiences, consumer buyers, or early concept testers.
*   **Best Industries:** Retail, DTC ecommerce, and seasonal launches.
*   **Common Mistakes:** Designing a layout that looks identical to competitors due to ChatGPT template reuse, resulting in visual "invisibility".
*   **Useful Variations:** Automated background replacement or format-adapted resizing.

---

## 6. OPERATIONAL RULES FOR AN AI B2B CREATIVE DIRECTOR

### 1. Decision Rules (IF/THEN/BECAUSE/EXCEPT WHEN)
*   **IF** designing a static ad for the primary mobile Feed
    *   **THEN** export at **1080×1350 px (4:5 Portrait)**
    *   **BECAUSE** this ratio captures **30% more vertical mobile height** than a 1:1 square, naturally increasing visual real estate and scroll-stopping rate.
    *   **EXCEPT WHEN** generating ads for LinkedIn feeds or Carousel cards, where **1200×1200 px or 1080×1080 px (1:1)** is the standard to match platform UI and avoid cropping.
*   **IF** designing for vertical Stories and Reels (**1080×1920 px, 9:16**)
    *   **THEN** place all critical text overlays, headlines, screenshots, and CTAs strictly inside the central **950×979 px safe zone**.
    *   **BECAUSE** native platform UI (usernames, share icons, profiles, description fields) covers the top 269 px (14% height) and the bottom 672 px (35% height).
    *   **EXCEPT WHEN** using the background canvas solely for non-informative margins or abstract decorative textures.
*   **IF** choosing a social-proof element to place on the canvas
    *   **THEN** lead with a **named-customer count with segment and revenue context** (e.g., *"Used by 8 of the Fortune 50"*)
    *   **BECAUSE** large-scale conversion testing of 2,000 pages proves this specific format delivers a **+22% conversion lift**, completely outperforming single testimonial cards (+14%), aggregate scale stats (+9%), standard logo strips (+8%), and press logos (+5%).
    *   **EXCEPT WHEN** the client has zero marquee customer accounts, in which case you must default to a **single, highly-specific customer testimonial card** featuring a real name, face, title, and company logo.
*   **IF** selecting an H1 header style for a direct-response prospecting campaign
    *   **THEN** use the **Single-Stat Hero** structure.
    *   **BECAUSE** leading with a massive, specific, and verifiable outcome number (e.g., *"Want to grow revenue 1,800%?"* or *"127x faster"*) generates a **+18% conversion lift** compared to standard headlines.
    *   **EXCEPT WHEN** the product's primary value proposition is workflow-based or relies on a visual transformation, where an **annotated product UI mockup** (+12% lift) or a **before/after comparison split** is more intuitive.
*   **IF** selecting a CTA verb for a B2B SaaS free-trial signup flow
    *   **THEN** hardcode the button copy as **"Start Free Trial"**
    *   **BECAUSE** it generates a **+9% conversion lift** over the generic "Get started" baseline by clarifying the low-friction path.
    *   **EXCEPT WHEN** writing copy for agency, consulting, or professional service funnels, where **"Get a Quote"** must be used to drive a **+14% conversion lift**.

### 2. Creative Review Checklist
*   **Attention:** Does the ad capture attention in the first 1.5 seconds using a bold color contrast, a stark layout, or an unexpected pattern interrupt?
*   **Clarity:** Does the ad pass the 3-second comprehension test? Can a mobile viewer understand the exact job the buyer is hiring the product to do in a single glance?
*   **Hierarchy:** Does the eye process the elements in the correct order: (1) Visual scroll-stopper, (2) Headline, (3) Supporting proof/UI, and (4) CTA/Brand logo?
*   **Copy:** Is the primary copy written in the buyer's words, and has all generic category language ("work smarter, not harder," "workflow optimization") been purged?
*   **Product:** Is the SaaS UI cropped and zoomed tightly around a specific feature use case rather than displaying an unreadable, full-screen desktop dashboard?
*   **Proof:** Is there a verifiable, named proof point present (customer logo, specific metric, G2 badge)?
*   **Trust:** If a statistic is displayed, is there a tiny, highly legible source attribution line at the base to prevent it from reading as hollow marketing hype?
*   **Typography:** Is the font selection a clean sans-serif (Helvetica, Arial, Open Sans, Roboto, Montserrat) for maximum readability on screens?
*   **Color:** Is there a high-contrast relationship (meeting at least a 4.5:1 WCAG AA contrast ratio) between the copy/CTA and the background canvas?
*   **Spacing:** Are all critical text blocks and logos set with a minimum 5% margin away from the canvas boundaries to prevent platform UI clipping?
*   **Mobile Readability:** Does the headline text remain fully readable when the completed ad graphic is scaled down to a 200 px thumbnail on a mobile display?
*   **Distinctiveness:** Does the ad visual break category conventions (e.g., avoiding generic stock photos of smiling teams around laptops, which penalizes conversion by -11%)?
*   **Offer:** Is the offer single-minded and focused on one specific positioning claim instead of trying to stack a diluted list of features?
*   **CTA:** Is there a high-contrast, context-specific CTA button drawn directly onto the image canvas that matches the temperature of the target audience?

### 3. Creative Specification Template
```markdown
# Creative Specification: [Insert Internal Variant Name]

### 1. Strategy & Audience
*   **Concept:** [Describe the core positioning theme, e.g., Cost Consolidation]
*   **Angle:** [The specific hook perspective, e.g., CFO cost-cutting objection]
*   **Funnel Stage:** [TOFU Prospecting / MOFU Consideration / BOFU Retargeting]
*   **Target Persona:** [e.g., CFO, Operations Director, IT Buyer]

### 2. Copy & Messaging
*   **Primary Hook (Under 125 chars):** [Hook copy before truncation]
*   **On-Image Headline (Max 7-8 words):** [Primary display copy on canvas]
*   **Supporting Subhead/Quote:** [Secondary text, e.g., max 15-word customer quote]

### 3. Visual & Layout Specifications
*   **Visual Style Aesthetic:** [Product-Led / Editorial / Brutalist / Premium / Meme / Native / Report-Style / Data-Driven]
*   **Layout Structure Template:** [Quote Card / Stat Drop / Before-After / Numbered List / Product + Callouts / Comparison Grid / Review Stack / Bold Statement / Founder Quote]
*   **Hero Element:** [Identify the central visual focal point, e.g., Cropped billing dashboard]
*   **Product Presentation:** [Screenshot crop details, device frame choice, and annotations]

### 4. Proof, Offer & Action
*   **Proof Element:** [Specific social proof, e.g., Notion logo + "Ramp cut costs 70%" + small source line]
*   **CTA Button Copy:** ["Start Free Trial" (+9% lift) / "Get a Quote" (+14% lift) / Custom low-friction]
*   **Brand Presence:** [Logo placement (e.g., top-right corner at 5% margin, max 40px height)]

### 5. Design & Typography Parameters
*   **Typography:** [Sans-serif font name]
*   **Font Sizing (Desktop equivalent):** [Headline: 48px+ / Sub: 32-40px / Body: 24-28px]
*   **Color Palette:** [Specify high-contrast colors, e.g., dark navy (#0B192C) with safety orange (#FF6500) accents]
*   **Information Density:** [Low / Standard / Bento Grid. Ensure text-overlay is under 20% of area]
```

### 4. Directives for Execution
*   **Choosing Visual Style & Layout:** Match style to the user's current funnel stage. Use Brutalist or Meme formats to disrupt scrolling at the top of the funnel (TOFU) where audiences are cold. Move to Product-Led or Data-Driven formats in the middle of the funnel (MOFU) to show real software screenshots. Adopt Native (Slack screenshots) or Premium designs at the bottom of the funnel (BOFU) to build validation and trust.
*   **Choosing Headline Type:** Headlines must use natural-voice, action-oriented verbs. Swap generic slogans like "work smarter" for *"Automate your employee onboarding"*. Match your headline argument directly to the visual hero of your canvas.
*   **Showing SaaS UI:** Apply a strict zoom and crop protocol. Desaturate non-essential areas of the dashboard and use high-contrast arrows or highlight shapes to focus the viewer's eye on the active use-case. Put your cropped screenshots inside a minimalist browser frame to signal "software."
*   **Showing Proof:** Verifiable proof relies on specificity. Specific odd numbers (e.g., *"\$42.50"* or *"127x faster"*) naturally register in the human brain as audited data points, whereas rounded numbers (e.g., *"50%"* or *"90%"*) are often visually ignored as marketing hype. Always include a small source attribution line at the bottom of your data-driven static ads.
*   **Adjusting by Persona & Funnel:** Align CTAs and offers with audience temperature. Cold prospecting campaigns (TOFU) must use low-friction, educational CTAs like *"Download the Report"* or *"Get the Free Guide"* to capture interest. Retargeting campaigns (BOFU) targeting in-market buyers should employ higher-intent, action-oriented CTAs like *"Request a Demo"* or *"Start Free Trial"* to drive pipelines.
*   **Avoiding Generic SaaS Aesthetics & AI Slop:** Standard stock images of smiling teams around laptops reduce conversions by **-11%** because they trigger banner blindness in buyers. Use real, unpolished founder photos (style-selfie) or real product interface screenshots instead. Systematically audit all text-generation models to strip out recognizable AI patterns. Ensure that terms like **"delve"**, **"leverage"**, **"synergize"**, or **"optimize your experience"** are completely banned; their inclusion reduces conversion rates by **8%**. Limit your copy to a maximum of two em-dashes per 100 words to avoid a **5% conversion penalty**.
*   **Iterating Winning Creatives:** Monitor creative fatigue using leading indicators (7-day frequency, CTR decay, and CPM creep) rather than waiting for Meta's official status, which only triggers after costs have already doubled. Do not pause a fatigued winning ad abruptly, as this forces the algorithm to reallocate spend to unproven creatives still in the learning phase. Run a **creative substitution**: launch 2-4 fresh hook or visual variations alongside the fatigued winner, let them exit the learning phase, and only phase out the fatigued ad once the new variants have proven their performance.

---

## 7. THE 100 MOST IMPORTANT RULES FOR DESIGNING STATIC B2B META ADS IN 2026

### Sizing, Specifications & Placements
1. Feed-first static ads must be designed at **1080×1350 px (4:5)** to capture 30% more vertical mobile height than square formats.
2. Stories and Reels placements require **1080×1920 px (9:16)** assets.
3. LinkedIn single-image ads require **1200×1200 px (1:1)** layout dimensions.
4. Carousel ad cards must be formatted at **1080×1080 px (1:1)** to maintain visual consistency across devices.
5. Google Display medium rectangles (300×250) must be exported at **600×500 px (2x resolution)** to prevent blurriness and quality penalties.
6. Keep file sizes for all static images strictly below **30 MB** on Meta and under **5 MB** on LinkedIn to ensure rapid loading speeds.
7. For Google Display static assets, the maximum allowable file size is a strict **150 KB**.
8. Stories and Reels safe zones require leaving the top **269 px (14% height)** completely clear of text and logos.
9. Stories and Reels safe zones require leaving the bottom **672 px (35% height)** completely clear of CTAs and logos.
10. All critical layout elements must be kept at a **minimum 5% margin** away from all canvas edges.

### Typography & Readability
11. Clean **sans-serif typefaces** (Helvetica, Arial, Open Sans, Roboto, Montserrat) must be your default font family.
12. Serif typefaces are restricted to large, editorial display headlines and must never be used for body copy.
13. Ornate script, decorative, or highly compressed fonts are banned due to mobile screen legibility limits.
14. Headlines displayed on a mobile image canvas must be a **minimum of 48px** to remain legible.
15. Subheadlines on an image canvas must be set to a **minimum of 32-40px**.
16. Supporting body copy on the image canvas must be a **minimum of 24-28px**.
17. Fine print and disclaimer text must be removed from the image canvas entirely.
18. Limit your ad copy on the image canvas to a **maximum of three hierarchical levels** (Primary, Secondary, Tertiary).
19. Text lines on an image canvas must contain a **maximum of 7 to 8 words per line** to ensure fast reading.
20. Set headline leading (line height) tightly to **100% to 120%** of the font size.
21. Set body copy leading generously to **120% to 145%** to prevent overlapping on mobile screens.
22. Slightly expand letter-spacing (tracking) for all-caps display headlines to improve legibility.
23. Avoid placing text overlays directly over busy backgrounds; always apply a semi-transparent dark solid block behind the text.
24. Apply the **Squint Test**: if you cannot easily read the headline while squinting at your mobile screen, the text size is too small.
25. To guarantee clarity, choose sans-serif typography over graphic complexity; communication always beats decoration.

### Color & Contrast
26. Every visual element must maintain at least a **4.5:1 WCAG AA contrast ratio** against the background.
27. For text-focused layouts, aim for extreme contrast pairs such as pure **black-on-white (21:1)** or **white-on-black (21:1)**.
28. Use high-salience accent colors (such as electric turquoise or bright orange on deep navy) to highlight CTA buttons.
29. Create ownable visual brand assets (like Stripe’s typography or Clay’s lavender) to build instant recognition.
30. To maintain visual quality, always save your final ad files in **PNG format** to prevent pixelation around text edges.
31. Dark-mode creatives with near-black backdrops and desaturated accents signal technical sophistication and reduce eye strain.
32. Ensure that your dark-mode designs meet the same 4.5:1 contrast standards as your light variants.
33. Avoid generic blue-to-purple color gradients; they blend into standard feed wallpaper and are ignored by buyers.
34. Keep your brand colors consistent across different sizes and platforms to build long-term recognition.
35. The background color of your static ad can be tested as a variable, but only after your message and layout are locked.

### Copywriting & Messaging
36. Front-load your primary ad hook into the first **125 characters** of the caption before mobile truncation kicks in.
37. On LinkedIn, keep your headline within **70 characters** and your visible intro text under **150 characters**.
38. Headlines must name the **exact job** the buyer is looking to solve instead of using generic marketing jargon.
39. Translate vague slogans like "work smarter, not harder" into clear, functional verbs such as *"Automate your employee onboarding"*.
40. Eliminate all AI-generated filler words; using **"delve"**, **"leverage"**, or **"synergize"** reduces conversion by **8%**.
41. Limit the use of em-dashes to a **maximum of two per 100 words** to avoid a **5% conversion penalty**.
42. Avoid generic superlatives (*amazing*, *innovative*, *cutting-edge*); their inclusion drops landing page conversions by **4%**.
43. Do not include your brand name in the first sentence; leading with your brand name increases scroll-past rates.
44. Keep your headline short and benefit-focused, aiming for a **maximum of 5 to 7 words**.
45. In copywriting, **specificity converts and vagueness decorates**; write copy in the exact words your buyers use.
46. Address the two largest B2B software objections—**implementation delay** and **tool overlap**—directly in your ad copy.
47. To address implementation delay, use the proven copy structure: **"[Specific Outcome], Overnight"**.
48. To address tool overlap, lead with co-branded cost savings: **"[Respected Customer] cut tool costs by 70%"**.
49. Do not use emojis in B2B copy targeting analytical or enterprise audiences.
50. Your ad copy's role is to earn attention; the job details and technical specifications belong on the landing page.

### Product Presentation & SaaS UI
51. Never show an uncropped, full-page desktop screenshot on mobile feeds.
52. Product screenshots must be cropped and zoomed tightly around **one specific action or visual outcome**.
53. Wrap cropped product screenshots in a **minimalist, simplified browser frame** to instantly signal "software".
54. Scale your completed ad graphic down to a **200px thumbnail**; if the interface is not understood in 1 second, crop it tighter.
55. Crop screenshots to focus exclusively on real, functional interface buttons, inputs, or workflow steps.
56. Use colorful callouts that name **quantified workflow outcomes** (e.g., "Saves 14 hours" instead of "Feature X").
57. For analytics software, the product's data visualizations *are* the product; make clean data charts your visual hero.
58. In product-led static layouts, the UI screenshot must be **visually dominant, occupying 50% to 60% of the canvas**.
59. Keep brand logos and wordmarks small and restricted to the bottom margin to avoid distracting from the product.
60. Ensure the headline claim precisely matches the screenshot use case; otherwise, the ad will be dismissed as a stock template.

### Social Proof, Trust & Verification
61. Avoid generic claims like "trusted by thousands"; unquantified social proof is indistinguishable from no social proof at all.
62. For maximum trust, display **named-customer counts with segment and revenue context** above the fold (+22% lift).
63. Place G2 ratings, G2 leader badges, and security certifications (SOC2, ISO) directly inside the ad creative.
64. Testimonials are strongest when the quote is specific (e.g., *"Cut our weekly production from 6 hours to 45 minutes"*).
65. Keep testimonial copy on Quote Card templates under a **maximum of 15 words** to maintain visual impact.
66. Testimonial quotes must be paired with a real customer name, face, title, and company logo to ensure credibility.
67. Raw screenshots of G2 reviews, forwarded emails, or Slack messages outperform highly polished testimonial templates.
68. Stacking **3 to 4 short review screenshots** vertically builds aggregate validation and handles multiple objections.
69. Use **specific, unrounded, odd numbers** (e.g., 42.5%, 127x) because they naturally register as real, audited data.
70. Avoid naming competitors directly on the canvas; use safe labels like **"Manual Sheets"** to prevent trademark complaints.

### CTA & Lead Generation Strategy
71. Every static B2B ad must have a **single, context-specific CTA button** drawn directly onto the image canvas.
72. Place your high-contrast CTA button inside the **bottom 15% of the canvas**.
73. Align your CTA verbs with the user's intent: use **"Start Free Trial"** (+9% lift) for self-serve software campaigns.
74. Use **"Get a Quote"** (+14% lift) for agencies, consulting, and custom professional services.
75. Avoid high-friction CTA copy like **"Buy Now"** (-4% penalty) for considered B2B purchases.
76. Match CTA friction to audience temperature: use low-commitment offers like *"Get Free Guide"* for cold traffic.
77. For lead magnets, keep your forms under **3 fields**; each extra field past 4 roughly halves your conversion rate.
78. On landing pages, use a **sticky-bottom CTA** to drive a **+11% conversion lift**.
79. Do not waste design effort stacking above-fold and sticky CTAs; the sticky CTA absorbs almost all of the conversion benefit.
80. If your product has a contract value (ACV) under £25k, use **Lead Ads with Instant Forms** to reduce CPL.

### Creative Testing & Iteration
81. Test creative variables in this order of impact: **Message/Hook first, visual format second, CTA third, design elements fourth**.
82. Maintain a strict **one-idea-per-ad** constraint; trying to convey multiple claims on a single static canvas destroys conversion.
83. Test 4 to 7 distinct layout templates around one offer before scaling variants within the winning format.
84. Keep the audience, offer, and CTA consistent across variants in a creative test; change only the creative format.
85. Give each ad variant in a dynamic creative test at least **\$50 to \$100 USD** of budget before deciding to pause it.
86. Benchmark single-image static ads against a target **median CTR of 0.90% to 1.40%**.
87. Budget your testing pipeline so that 1 or 2 high-performing "winners" carry the account's ad spend.
88. Run creative tests as a system: the research layer must feed the creative layer, which in turn feeds the testing loop.
89. Review ad performance metrics weekly at the **CRM pipeline level (Net New ARR)** rather than optimizing solely for CTR.
90. Establish separate, industry-specific benchmarks for CPMs based on vertical competition (e.g., \$15-\$24 for Fintech/Cybersecurity).

### Creative Fatigue & Account Health
91. Monitor creative fatigue using leading indicators (frequency, CTR decay, CPM creep) instead of waiting for Meta's status.
92. For cold prospecting audiences, flag creative fatigue for review once your **7-day frequency passes 2.5**.
93. For retargeting audiences, tolerate higher exposures, flagging creative fatigue once **frequency crosses 5 to 8**.
94. Watch for **CTR decay of 20% to 25%** sustained over 3+ days against your trailing 14-day baseline.
95. Flag potential fatigue if you see a **15% to 20% sustained creep in CPM** without an auction-wide holiday event.
96. Video ads require monitoring video-specific hook rates; a **15% sustained drop in 3s views** indicates creative fatigue.
97. A real fatigue diagnosis requires **at least two leading signals moving together** (e.g., rising frequency + falling CTR).
98. Do not pause a fatigued winner abruptly; apply the **Substitution Effect** to avoid throwing the campaign back into learning.
99. Keep the fatigued winner active at a lower budget, launch replacements alongside it, and phase the winner out only once replacements prove themselves.
100. Balance your creative pipeline based on spend volume: accounts spending over \$50k/month require an always-on creative refresh pipeline to prevent performance plateaus.
