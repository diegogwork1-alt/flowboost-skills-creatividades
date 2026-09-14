# Audit Playbook (COPY + VISUAL) — motor del auto-QC (fuente NotebookLM de Dirección)

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

Sistema de auditoría objetivo. Fuentes: Digital Applied 2026, AdRiseLab 2026, 6sense 2025, SaaSHero 2026, Adrio 2026, Ryze AI, Grafit Agency, VibeMyAd, ROASPIG, Superads, Omnibound (2.000 landings, 320 tests A/B, comités de compra). **Es el checklist que corre el AUTO-QC** (`calidad-y-autoqc.md`; severidades en `audit-rules.json`). Severidades: **REJECT / REGENERATE / APPROVE WITH IMPROVEMENTS**.

> **TAMAÑO — regla de la casa (Dirección, definitiva): SIEMPRE los dos, 1:1 (1080×1080) Y 9:16 (1080×1920).** NO 4:5. (El playbook menciona 4:5 como opción; en Flowboost el feed es 1:1.) 9:16: el fondo llena todo el lienzo; texto/logo/CTA fuera de **top 14% (~270px) / bottom 20% (~384px) working** (laterales: se pide **107 px**, el margen de la casa; **65 px es el mínimo técnico** infranqueable) — el 35%/672 es solo Reels-safe extremo. (Las menciones de 672/950×979 más abajo son del playbook original = versión conservadora; la casa usa 384.) Enrutado B2C/B2B: lo B2B puro (SOC2, columnas de competidor, dashboards, CTA SaaS) solo en clientes B2B.

## UNIVERSAL — COPY
1. **Hook antes del corte móvil (125 car.).** El gancho/valor más fuerte va en los primeros **125 caracteres** del texto primario (LinkedIn 150). No empezar con saludo corporativo ni marca ("Acme se enorgullece…"). FAIL: hook tras el "ver más". **Major/REGENERATE.**
2. **Purga de AI tells.** Prohibido "delve", "leverage", "synergize", "optimize your experience" (−8%); superlativos vacíos (amazing/innovative/cutting-edge/revolucionario/state-of-the-art) (−4%); máx **2 em-dashes/100 palabras** (−5%). Voz del cliente real. **Critical/REJECT.**
3. **Traducción de vocabulario (comprador vs jerga de categoría).** Verbos de uso concreto ("Automatiza el onboarding", "Ahorra 4 horas de carga manual") en vez de jerga ("workflow optimization", "data enrichment", "trabaja más inteligente"). **Major/REGENERATE.**

## UNIVERSAL — VISUAL
1. **Dimensión & safe zone.** Feed 1:1 (1080×1080) [regla casa] — el playbook también admite 4:5 1080×1350; NO usar 4:5 en Flowboost. 9:16 (1080×1920) con texto/logo/CTA fuera del **14% superior (270) y del 20% inferior (384)**, laterales **a 107 px** (mínimo duro 65) — regla de la casa; el 35%/672 (central 950×979) del playbook original es solo Reels-safe extremo. FAIL: texto/logo en esas zonas muertas; 1.91:1 sin adaptar. **Major/REGENERATE.**
2. **Tipografía (test del bizco).** >90% del B2B ve en móvil. Titular ≥48px, subtítulo 32-40px, cuerpo 24-28px; **7-8 palabras/línea** máx; interlineado 100-120% del titular. FAIL: <24px, líneas >8 palabras, serif/script para cuerpo. **Major/REGENERATE.** [Nota Flowboost: para marcas premium el serif SÍ va en display/titular editorial; el ban de serif es para cuerpo.]
3. **Contraste WCAG AA ≥4.5:1** (ideal negro/blanco 21:1, o acentos vivos sobre navy). FAIL: gris claro sobre off-white, azul sobre gradiente oscuro. **Major/REGENERATE.**
4. **Texto <20% de la superficie.** El algoritmo despriorioriza text-heavy (más CPM). **Major/REGENERATE.** ⚠️ *Corregido el 11-09-2026: aquí ponía que Artículo/Noticia y Review+Claim estaban «exentos». **Meta no exime a ningún formato** — quitó la regla dura del 20 %, pero el algoritmo sigue penalizando entrega y CPM. Lo que aguanta en esos dos es el RENDIMIENTO, no la penalización: se les acepta pasarse (APPROVE WITH IMPROVEMENTS) como coste asumido del formato, no como excepción, y por eso no se estira más de lo necesario.*
5. **Jerarquía cara→texto→logo.** Scroll-stopper (cara/UI alto contraste/stat) dominante y central; titular 2º; logo en esquina/pie a 5% de margen, <10% del canvas. FAIL: logo > titular o central. **Major/REGENERATE.**
6. **Nitidez & export.** PNG si lleva texto/mockup; JPG 90%+ si foto sin texto; <30MB. **Tamaño de entrega de la casa: exactamente 1080×1080 y 1080×1920** (el GPT devuelve tamaños raros → escalar con PIL/LANCZOS). El "ideal 1440" del playbook solo aplica si el generador ya lo entrega: **no se interpola hacia arriba**, no añade detalle y engorda el fichero (`reglas-tecnicas-y-copy.md §1`). FAIL: pixelado/artefactos, >30MB. **Minor/APPROVE WITH IMPROVEMENTS** (rehacer export). [En `audit-rules.json` el >30MB y pixelado figuran como REJECT del playbook anterior — umbral concreto: REJECT si el titular no se lee a 200 px de miniatura o el fichero pesa >30 MB; el resto Minor.]

## POR FORMATO — resumen COPY + VISUAL (los 9)
1. **Artículo/Noticia (advertorial):** **cabecera con NOMBRE DE MEDIO, nunca el logo del cliente** (Dirección, 08-09-2026: el logo arriba delata el anuncio y anula el formato; si el logo va, abajo y pequeño). H1 citable estilo publicación ("Cómo desarrollar…") + 2-3 bullets + pills de metadata ("2026 STUDY"/"EBOOK"); layout académico/editorial, grid limpio, UI desaturada/secundaria. FAIL copy: pitch de producto/tagline genérico. FAIL visual: banner comercial ruidoso/vector art. **REGENERATE.** [Flowboost premium: titular editorial real, énfasis serif itálico, NO marcador.]
2. **Antes/Después:** métricas crudas **no redondeadas** ("6% → 60%"), asume comprador inteligente; split izq/der desaturado→limpio, **mismo ángulo/luz/distancia** (compliance salud/estética). FAIL: números vagos/redondeados; ángulos distintos. **REGENERATE.**
3. **Review+Claim:** cita ≤15 palabras con resultado tangible; grid 60% cita / 40% producto+★★★★★+atribución **real (cara+nombre+cargo+logo)**. FAIL: cita larga/genérica, "- John S.", stock. **REGENERATE.**
4. **Feature→Beneficio:** máximo 3 callouts a **resultados cuantificados** (no nombres técnicos); UI recortada en frame minimal, test 200px. FAIL: dashboard entero, >5 callouts, callouts técnicos. **REGENERATE.**
5. **Responder objeciones/haters:** hook contrario + lenguaje crudo de entrevistas; visual tipo screenshot orgánico (G2/Slack/LinkedIn), desde perfil de ejecutivo. FAIL: copy de producto pulido, gradientes corporativos. **REGENERATE.**
6. **Resolver el pain:** 1ª línea problem-aware específica <125 car. ("Tu equipo pierde 4h/día en carga manual"); pattern-interrupt (PDF tachado, post-it, scribble) arriba + solución abajo. FAIL: pregunta genérica ("¿querés crecer?"), clip art. **REGENERATE.**
7. **Oferta/Escasez:** stack escaneable (3-5 ítems, precio/términos, risk-reversal "sin tarjeta"/"cancela cuando quieras") + CTA baja fricción; oferta = elemento más grande. FAIL: precio oculto, CTA alta fricción con recurso gratis. **REGENERATE.**
8. **Prueba social (Stat Drop):** 1 número **impar/no redondeado** en tipografía gigante (60% superior) + logo reconocible + **línea de fuente obligatoria**; fondo desaturado sin ruido ("si el diseño compite con la métrica, el diseño está mal"). FAIL: redondeado sin fuente/logo, ruido gráfico. **REGENERATE.**
9. **Garantía:** términos explícitos/defendibles (SOC2 Type II, SSO, audit logs) + CTA baja fricción; bento con sellos sobre el midpoint. FAIL: "Free Trial" que choca con muro de tarjeta; sellos chicos/borrosos. **REGENERATE.**

## CRITICAL — REJECT inmediato
1. AI tells en copy ("delve/leverage/synergize/optimize your experience"). 2. Foto de stock corporativo (equipos sonriendo, apretón, señalar laptop) −11%. 3. Marca de competidor nombrada en el canvas (usar "Sin automatización"/"Proceso manual"). 6. Screenshot de escritorio sin recortar (ilegible a 375px). 7. Texto/logo/CTA en top 270 / bottom 384 del 9:16 (valores de la casa).
## CRITICAL — REGENERATE
4. CTA de alta fricción ("Comprar", "Contratar", demo de producto) en TOFU frío. **Excepción de la casa: "Reserva una llamada breve" es el CTA estándar del funnel Flowboost y NO se marca** (el destino siempre es llamada). 5. Métrica redondeada sin logo/fuente en Stat Drop.

## APPROVE WITH IMPROVEMENTS (optimizaciones)
1. "Get started" → "Start Free Trial" (+9%) en SaaS (trial sin muro de tarjeta). 2. "Contact us" → "Get a Quote" (+14%) en servicios/agencia. 3. Prensa (+5%) → recuento de clientes nombrados (+22%) o testimonio con cara+cargo (+14%). 4. Retrato de estudio → selfie candid (30-50% mejor). 5. Variante dark-mode de mockups de software.

## Reglas machine-readable (IF/THEN) para el agente
- IF copy CONTIENE ("delve"|"leverage"|"synergize"|"optimize your experience") → **REJECT** (−8%).
- IF visual CONTIENE stock corporativo/equipo posando → **REJECT** (−11%).
- IF copy nombra marca de competidor en el canvas → **REJECT** (usar "Manual Sheets"/"No Automation").
- IF placement=9:16 Y (texto|logo|CTA) EN (top 270 | bottom 384) → **REGENERATE**. (672 solo si la pieza debe ser Reels-safe extremo.)
- IF formato=Feature→Beneficio Y (mockup=full-desktop | ilegible@200px) → **REGENERATE**.
- IF formato=Social Proof Y métrica=redondeada Y (logo ausente | fuente ausente) → **REGENERATE**.
- IF funnel=TOFU Y CTA IN ("Book a Demo","Book a Sales Call","Buy Now") → **REGENERATE**.
- IF texto_overlay >20% → **REGENERATE**, salvo formato IN ("Artículo/Noticia","Review+Claim") → **IMPROVE** (coste asumido del formato: **no es una exención de Meta**, que no exime a ninguno).
- IF formato == "Artículo/Noticia" Y hay_logo_de_marca_en_cabecera → **REGENERATE**.
- IF formato == "Artículo/Noticia" Y nombre_del_medio ES una cabecera real → **REJECT** (suplantación).
- IF contraste <4.5 → **REGENERATE**.
- IF SaaS Y CTA="Get started" → **IMPROVE** (+9% con "Start Free Trial").
- IF social_proof IN ("Press Logos","Media Mentions") → **IMPROVE** (preferir clientes nombrados +22%).
- IF Founder Quote Y foto=estudio → **IMPROVE** (selfie candid +30-50%).
