# Audit de COPY por formato (los 9) — fuente NotebookLM de Dirección

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

Reglas estrictas de redacción por formato para auditar el COPY de cada estático. Complementa `audit-playbook-b2b.md` (visual) y `calidad-y-autoqc.md` (§0 juicio de DC). El auto-QC (SKILL Fase 3) corre ESTO sobre el copy de cada pieza; cualquier Fail → CAMBIOS/REGENERATE con la severidad indicada. (B2B-oriented; en B2C adaptar el vocabulario al avatar, misma lógica de pass/fail.)

> ⛔ **LOS CTA QUE CITA ESTE DOCUMENTO SON DE SaaS, NO DE LA CASA.** "Empezar gratis", "Ver demo",
> "Empieza tu prueba gratis", "Start Free Trial", "Sin tarjeta", "Cancela cuando quieras" vienen de la
> fuente B2B original y **NO se usan en Flowboost**: no vendemos software, no hay prueba gratis y
> **el funnel SIEMPRE termina en llamada**. Sirve el *mecanismo* (fricción acorde a la temperatura,
> risk-reversal visible), no el texto. Los CTA reales están en `reglas-tecnicas-y-copy.md §7` y, por
> formato, en `formatos-visual-spec.md`: "RESERVA UNA LLAMADA BREVE →", "PIDE PRESUPUESTO →",
> "DESCUBRE CÓMO FUNCIONA →". Lo mismo con el vocabulario de cumplimiento del formato 9 (SOC 2, SSO,
> audit logs): **solo en clientes B2B de software**; en un cliente B2C la garantía es la real del brief.

## 0. REGLA TRANSVERSAL — FECHAS Y AÑOS (vale para los 9 formatos)
Todo lo que sea fecha o año **en el copy** (no solo lo dibujado en la imagen) se comprueba contra el **reloj del sistema**, nunca contra la memoria del modelo: `date +%d/%m/%Y` y `date +%Y`.
- **Fecha del día → tiene que ser la de HOY.** Pasada = FAIL. Futura = FAIL (parece errata).
- **Año en pills, informes y promociones** ("INFORME 2026", "ESTUDIO 2026", "promoción 2026") → el **año en curso**. Un año viejo convierte el anuncio en material caducado.
- **Plazos y vigencias** ("válido hasta el X", "quedan N plazas de junio") → la fecha tiene que seguir viva cuando el anuncio se publique, y coherente con lo que diga la landing.
- **Desgaste:** la tanda vive semanas. Si el mensaje no depende de un día concreto, **fuera el día** (mes y año, o solo el año): así no caduca a los tres días.
- **Severidad: REGENERATE** (fecha pasada o año viejo). No se entrega copy con fecha caducada.

## 1. Article/News (Advertorial)

> **Cabecera: nombre de un medio, NO el logo del cliente** (Dirección, 08-09-2026). El formato vive de parecer
> una noticia; el logo arriba lo delata y deja de servir. Logo, si acaso, abajo y pequeño. Nunca un medio real.

- **Hook:** titular de artículo útil / playbook aplicable al ICP ("Cómo desarrollar…"). Tono **citable, formal, sin adjetivos comerciales**.
- **Estructura:** headline editorial + 2-3 bullets de datos + metadata en pills ("2026 STUDY","EBOOK"). CTA baja fricción: "Descargar / Descargar el informe". **La fecha de cabecera y el año de las pills se verifican contra el sistema (§0): fecha pasada o año viejo = REGENERATE.**
- **PASS:** suena a periodismo de datos/investigación práctica. **FAIL:** ganchos de venta directos ("Descubre por qué somos el líder") o sin pills de metadata. **Severidad: REGENERATE.**

## 2. Before/After
- **Hook:** comparación con **cifras exactas** ("Antes: 3 tools y 2h vs Después: 1 canvas y 60s"; "6% → 60%"). Asume comprador inteligente (no explica la categoría).
- **Estructura:** texto ultra-restringido: los dos estados + etiqueta temporal ("3 semanas de uso"). El resto va en la landing.
- **PASS:** cambio dramático pero **defendible**, sin adornos. **FAIL:** vaguedad ("caos manual vs automatización") o promesas milagrosas irreales (bloqueos de Meta). **REGENERATE.**

## 3. Review+Claim
- **Hook:** la **cita real** ES el titular; resultado operativo incómodo/sorprendente ("Bajamos la producción semanal de 6h a 45min"). Palabras del cliente, tono orgánico sin editar; nada de elogios genéricos ("gran software").
- **Estructura:** cita ≤ **15 palabras**. CTA de la casa: **"Quiero saber más →"** (los "Ver demo / Empezar gratis" del informe original no aplican: no vendemos software y el funnel acaba en llamada).
- **PASS:** cita con cifra + lenguaje crudo + **atribución verificable (nombre, cargo, cara real, logo)** + **derriba UNA objeción concreta del brief** (Dirección, 07-09-2026: salían reseñas genéricas que no resolvían dudas ni barreras). **FAIL:** anónimo/semi ("- John S."); **o cita que valdría igual para un competidor o para otro sector**; o testimonio de un avatar distinto al de la tanda. **REGENERATE.** (Nota Flowboost: la reseña puede ir **PROVISIONAL**, y entonces la marca **`[REEMPLAZAR]` va quemada DENTRO del PNG, en el píxel** —no solo en el specs: eso ya falló el 09-09-2026— con la atribución creíble, no stock. Detalle: regla raíz 4 del `SKILL.md` y `formatos-visual-spec.md §3`.)

## 4. Feature→Beneficio
- **Hook:** línea Job-To-Be-Done ("Acepta pagos en minutos, no días").
- **Reglas:** los callouts se traducen a **beneficios/resultados de flujo** ("Cierra en el CRM solo", "Ahorra 14h"), NUNCA a features técnicas ("REST API","Panel de ajustes").
- **Estructura:** 1 titular + **máximo 3 callouts** máx (>5 abruma). CTA de la casa: **"Reserva una llamada breve →"** o **"Descubre cómo funciona →"**.
- **PASS:** cada línea = resultado de negocio concreto. **FAIL:** explica infraestructura técnica en vez de la consecuencia. **REGENERATE.**

## 5. Responder objeciones/haters (Contrarian)
- **Hook:** afirmación/pregunta contraria audaz ("Por qué tus ads de LinkedIn generan clics pero cero pipeline", "Deja de hacer A/B testing en tu home").
- **Reglas:** lenguaje crudo de llamadas de venta/quejas reales ("El demo se veía genial, implementarlo tardó 8 meses"). 1ª persona ("Lo construimos porque…"). Máx 3 oraciones cortas de apoyo.
- **PASS:** genera "ajuste de identidad" con el operador cansado. **FAIL:** agresivo poco constructivo o "nosotros lo hacemos mejor" sin validar el dolor. **REGENERATE.**

## 6. Resolver el pain (Problem-Solution)
- **Hook:** desafía un comportamiento doloroso actual ("¿Sigues haciendo las variantes una por una?"). Traduce jerga a acciones del comprador.
- **Estructura:** front-load el hook en los **primeros 125 caracteres** (visible en móvil antes de "ver más"). CTA baja fricción alineada al dolor ("Haz el test","Descarga la guía").
- **PASS:** dolor tan específico que el comprador se siente observado. **FAIL:** pregunta genérica ("¿Querés crecer?") = invisible. **Severidad: CRITICAL (REJECT/REGENERATE).**

## 7. Oferta/Escasez
- **Hook:** acción transaccional de valor directo, con la oferta REAL del brief ("Desde 5.000 €", "Plazas limitadas por orden de llegada"). *(No "prueba gratis": eso es del informe SaaS.)* **El año de la promoción y cualquier plazo se verifican contra el sistema (§0).**
- **Reglas:** **precio/condiciones visibles** (transparencia). Lista escaneable 3-5 ítems + precio/ahorro + risk-reversal ("Sin tarjeta","Cancela cuando quieras").
- **PASS:** valor acumulado + reversión de riesgo claros en 3s. **FAIL:** esconde precio/cancelación tras formulario. **REGENERATE.**

## 8. Prueba social (Stat Drop)
- **Hook:** número sorprendente, masivo y **NO redondeado** ("16 operaciones cubiertas en 2026", "700.000 € cubiertos en dos semanas"). *(El ejemplo que había aquí —«Ramp bajó costos 70%»— rompía tres reglas duras de la casa a la vez: 70 % es **redondo** y la propia línea dice que redondo = hype descartado; **nombra a un competidor**, que es REJECT en `audit-playbook-b2b.md`; y «costos» es **léxico LATAM**, REJECT en `calidad-y-autoqc.md §0-bis`. Corregido el 11-09-2026.)* Impares/decimales (42,5%) = reales; redondos (50/100%) = hype descartado.
- **Estructura:** 1 métrica gigante + logo de cliente reconocible + **línea de fuente obligatoria** en chico ("- Encuesta clientes 2026"). Sin fuente = pierde credibilidad.
- **PASS:** dato específico, verificable, anclado a cliente real del ICP. **FAIL:** métrica sin fuente ni logo. **Severidad: CRITICAL (REJECT/REGENERATE).**

## 9. Garantía (Risk Reversal)
- **Hook:** el compromiso REAL del brief que quita el miedo ("Si no hay beneficio, no cobramos", "Cero casos de okupas en 4 años"). *(SOC 2 / SSO / audit logs es vocabulario del informe SaaS: solo si el cliente es B2B de software. En B2C la garantía es la del brief, y si no hay garantía real la pieza se omite.)*
- **Reglas:** vocabulario de seguridad/finanzas del comité (CFO/CIO); garantías contractuales/rapidez. Puntos claros: "Cancela cuando quieras","SSO/RBAC activo". CTA baja fricción.
- **PASS:** ataca las barreras burocráticas/seguridad que congelan el trato. **FAIL:** "prueba sin riesgo" pero pide tarjeta antes de acceder. **REGENERATE.**

## 10-maestro. Tres pasos (FUERA de la secuencia de 9 — solo si Dirección lo pide)
Tiene ficha visual (`formatos-visual-spec.md §10`) pero **no tenía audit de copy**: el día que se
produjera, pasaba por 1 de las 4 capas de auditoría. Queda cubierto:
- **Hook:** el freno del avatar («no sé cómo funciona / da miedo / es complicado»), no el nombre del servicio.
- **Los pasos son ACCIONES del cliente, no fases internas nuestras.** ❌ «Análisis · Propuesta · Ejecución» (eso es nuestro organigrama); ✅ «Nos cuentas tu caso · Te damos un precio cerrado · Empezamos».
- **Reglas de lista:** exactamente **3**, **≤5 palabras** cada uno, paralelos (todos empiezan por verbo o todos por sustantivo), sin punto final. Manda `reglas-tecnicas-y-copy.md §3`.
- **PASS:** al leer los tres se entiende qué tiene que hacer y qué pasa después. **FAIL:** pasos genéricos que valdrían para cualquier negocio, más de 3, o pasos que son features. **REGENERATE.**
- **CTA:** baja fricción, alineado al paso 1 («Cuéntanos tu caso →»).

## MARCO por formato: ¿CÓMO comunicar? (tono/estructura/límites) vs ¿QUÉ comunicar? (mensaje/métrica/prueba)
Al redactar/auditar cada formato, separar las dos preguntas. **Tono por formato** (el "cómo"):
1. **Artículo/Noticia:** citable, periodístico, formal, sin adjetivos comerciales (autoridad técnica). Qué: hallazgo de industria o playbook aplicable + oferta de descarga de alto valor.
2. **Antes/Después:** directo, ágil, inteligente (asume que conoce la terminología, omite básicos). Qué: transformación dramática pero defendible + métrica exacta de caso real.
3. **Review+Claim:** conversacional, crudo, sin editar, 1ª persona, entre comillas. Qué: alivio de fricción laboral + resultado sorprendente con atribución verificable (cara/nombre/cargo/logo).
4. **Feature→Beneficio:** funcional, orientado a la acción (Job-to-be-Done). Qué: consecuencia de negocio de usar la interfaz (no la feature técnica) + demo visual resolviendo la tarea.
5. **Objeciones/haters:** desafiante, honesto, empático, 1ª persona. **Corre desde perfil de un ejecutivo (Thought Leader Ads = 6.4x CTR).** Qué: verdad incómoda de la categoría + por qué fundaste/rediseñaste para resolverla.
6. **Resolver el pain:** crudo, directo, empatía situacional aguda. Qué: cuello de botella diario hiperespecífico del ICP + el producto como vía rápida para sacárselo de encima.
7. **Oferta/Escasez:** transaccional, directo, transparente. Qué: desglose de lo que recibe + precio visible + risk-reversal + CTA alineado a la fricción.
8. **Prueba social (Stat):** incontestable, basado en datos auditados. Qué: 1 cifra de impacto **no redondeada** + logo reconocible + línea de fuente obligatoria.
9. **Garantía:** confiable, formal, de cumplimiento. Qué: estándares técnicos reales / garantía de rapidez; ojo con "free trial" que esconde muro de tarjeta.

## 10. Regla de oro legal (comparaciones)
- IF el copy compara contra competidores o el statu quo → **NUNCA nombres marcas registradas de rivales** en texto/imagen → BECAUSE dispara revisión de trademark y rechazo de cuenta → EXCEPT WHEN uses la estructura tipo Zapier: comparás contra una columna genérica de dolor ("Sin automatización","Proceso manual").
