# Estáticos ganadores de Flowboost (por leads, campañas activas de Clientes Potenciales)

Extraído por MCP (read-only) el 04-09-2026, últimos 30 días, solo **anuncios activos en campañas OUTCOME_LEADS**, solo **estáticos** (naming `IMG`/`EGC`; `MOV`=video se excluye). Es la base real de qué estático convierte por vertical → referencia para automatizar buenos estáticos.

## Ranking de estáticos ganadores (leads / CPL)
| Cliente (vertical) | Estático (ángulo) | Leads | CPL | CTR |
|---|---|---|---|---|
| **Cliente 03** (adicciones) | **IMG \| Testimonio** | **74** | **€2,92** | 2,28% |
| **Cliente 13** (cuidadoras) | **EGC \| Ahorro de dinero (coste del error)** | 24 | €16,76 | 1,29% |
| Cliente 14 (reformas) | MOFU__IMG__2 (form nativo) | 16 | €28,02 | 2,06% |
| Cliente 13 | IMG \| VACACIONES \| Riesgo de hacerlo por cuenta propia | 13 | €22,33 | 1,78% |
| Cliente 13 | IMG \| Nuevo FORM \| ¿Te cuesta saber por dónde empezar? | 12 | €25,54 | 1,62% |
| Cliente 14 | AD1-TOFU-Reforma integral sin adelantar todo el dinero | 6(30d)/20(90d) | €44-49 | 1,6% |
| Cliente 13 | IMG \| Nuevo FORM \| Una cuidadora inadecuada | 5 | €32,70 | 2,02% |

## Dónde el estático NO es el que trae leads
- **Cliente 06** (inmobiliaria, venta piso): los estáticos rinden CTR pero casi 0 leads; **el VIDEO trae los leads** ("TOFU__MOV__SI TIENES UNA CASA" 11 leads @ €42,60). → en esa cuenta el estático es TOFU/MOFU, no el cierre.
- **Cliente 02** (inversión): campaña nueva (~10 días), sin leads aún; estáticos EGC/UGC/IMG en test.

## Patrones de los estáticos que GANAN (para replicar/automatizar)
1. **Testimonio** = el formato más potente y barato (MMS 74 leads @ €2,92). Cara/palabra de cliente real.
2. **Ángulo de pérdida / "coste del error"** (Cliente 13 24 leads) — lo que pierdes si lo haces mal o por tu cuenta.
3. **Miedo a hacerlo por cuenta propia / "no sé por dónde empezar"** (Cliente 13 12-13 leads) — parálisis del avatar.
4. **Oferta/proceso concreto** (Cliente 14 "sin adelantar todo el dinero", form nativo) — quita-miedo financiero.
5. Funnel: los ganadores son **form nativo (MOFU/leadgen)** con hook de dolor claro.

## Convenciones de naming de creativos (ya existen, estandarizar)
- Cliente 06: `ETAPA__TIPO__ÁNGULO__FECHA` (TIPO = IMG/MOV; ETAPA = TOFU/MOFU).
- Cliente 13 / Cliente 02 / MMS: `TIPO | ÁNGULO | (detalle)` con TIPO = IMG / EGC / UGC.
- Estándar recomendado para todos: etiquetar SIEMPRE tipo (IMG/EGC/UGC/MOV) + ángulo → permite rankear ganadores solo.

## Método para actualizar esto (read-only)
Por cuenta: `ads_get_ad_entities` level=ad, date_preset last_30d, fields [name, effective_status, lead, cost_per_lead, ctr, spend] → filtrar effective_status ACTIVE + naming IMG/EGC + lead>0, ordenar por leads. Para ver la imagen real del ganador: abrir su anuncio en la Ad Library o pedir la imagen por su creativo. (Con el token de Meta en el VPS, esto se puede correr solo cada semana.)

---

# REFRESCO CON DATOS REALES — 11-09-2026 (MCP de Meta, solo lectura, últimos 30 días)

> Extraído con `ads_get_ad_entities` sobre las cuentas consultables. **Esto sustituye al ranking de
> arriba como foto actual**; lo de arriba se queda como histórico del 04-09.

## Cliente 03 (adicciones · form nativo)

| Anuncio | Gasto | Leads | CPL | CTR | Frec. |
|---|---|---|---|---|---|
| **IMG \| Testimonio** | **281,93 €** | **~97** | **2,91 €** | 2,36 % | 2,25 |
| IMG \| ¿Cuántos lunes te dices «esta semana lo dejo»? | 7,96 € | 4 | **1,99 €** | **4,03 %** | 1,50 |
| IMG \| Llevas años intentando dejar tu adicción… | 18,08 € | 3 | 6,03 € | 2,37 % | 1,54 |
| IMG \| Un programa pensado para dejar el consumo | 9,69 € | 1 | 9,69 € | 2,53 % | 1,21 |
| IMG \| Dejar de consumir no es solo decidirlo | **0,36 €** | 0 | — | 3,08 % | 1,07 |
| IMG \| Contestamos a lo que muchos piensan | **0,51 €** | 0 | — | 5,26 % | 1,24 |

## Cliente 13 (cuidadoras a domicilio)

Activos (tanda VERANO, **6 piezas**): septiembre empieza 17,51 €/2 leads/**8,76 €** · El cuidado de tus
padres 9,59 €/1/9,59 € · Se acaba el verano 3,10 €/1/3,10 € · EGC Tu cuidadora de siempre ha fallado
19,90 €/1/19,90 € · EGC Tus familiares 10,09 €/**0** · Tu te reincorporas **1,72 €**/0 (CTR 0,85 %).

Histórico con volumen suficiente para creer el dato:

| Anuncio | Gasto | Leads | CPL |
|---|---|---|---|
| **EGC \| Ahorro de dinero (coste del error)** | 370,17 € | **17** | 21,77 € |
| IMG \| VACACIONES \| Riesgo de hacerlo por cuenta propia | 337,13 € | 13 | 25,93 € |
| **IMG \| VACACIONES \| Proceso complicado / No saber cómo hacerlo** | 120,48 € | 7 | **17,21 €** ← mejor CPL |
| IMG \| Nuevo FORM \| Una ciudadora inadecuada *(sic: «ciudadora», typo publicado)* | 195,07 € | 7 | 27,87 € |
| IMG \| Nuevo FORM \| Te cuesta saber por donde empezar | 254,69 € | 7 | 36,38 € |
| IMG \| VACACIONES \| Culpa / Miedo a dejarlos solos | 184,15 € | 4 | 46,04 € |
| **IMG \| VACACIONES \| Prueba social / Testimonial verano** | 53,87 € | **1** | **53,87 €** ← el PEOR |

## Cliente 14 (reformas · form nativo) — **18 anuncios activos a la vez**

| Anuncio | Gasto | Leads | CPL | Frec. |
|---|---|---|---|---|
| MOFU__IMG__2 | **596,30 €** | 20 | 29,82 € | 2,53 |
| AD1-TOFU \| Reforma integral sin adelantar todo el dinero | **453,34 €** | 12 | 37,78 € | 2,33 |
| MOFU__IMG__1 - Copia | 64,54 € | 0 | — | 1,86 |
| MOFU-IMG-1 DIRECTOR-29ENE | 51,39 € | 0 | — | **3,09** |
| MOFU-MOV-RETRASOS - Copia | 41,19 € | 0 | — | 1,77 |
| MOFU__IMG__4 | 22,32 € | 0 | — | 1,68 |
| **otros 12 anuncios** | **0,32 € – 5,03 € cada uno** | 0 | — | — |

---

# ⛔ LO QUE ESTOS DATOS CAMBIAN (y es lo importante, más que el ranking)

## 1. «El Testimonio es el formato más potente y barato» NO es una regla de la casa: es un cliente
Arriba está escrito como patrón nº 1 para replicar en todos. Con los datos de hoy:
- **Cliente 03: 2,91 €** de CPL y ~97 leads. El mejor de su cuenta, con diferencia.
- **Cliente 13: 53,87 €** de CPL con **1 lead**. **El peor de su cuenta**, con diferencia.

Es el mismo formato y el resultado es opuesto. **Lo que viaja entre clientes no es el formato: es el
ÁNGULO.** Y ahí sí hay señal repetida: **«el coste del error / el riesgo de hacerlo por tu cuenta»** gana
en Cliente 13 (370 € → 17 leads) y en Cliente 14 («sin adelantar todo el dinero», 453 € → 12 leads).
El árbol de decisión no debe proponer Testimonio por defecto: debe proponer **el ángulo que ya rinde en
esa vertical**, y el formato después.

## 2. El cuello de botella NO es producir creativos: es que no reciben presupuesto
- Cliente 14: **2 anuncios se llevan 1.050 € de ~1.253 € (84 %)**, y **12 de 18 no llegan a 6 €**.
- Cliente 03: el Testimonio se lleva 281,93 € y **dos piezas tienen 0,36 € y 0,51 €** — no han
  arrancado. Una de ellas con **CTR 5,26 %**, el segundo mejor de la cuenta: no es que sea mala, es que
  no se le ha dado tirada.
- Cliente 13 tiene **6 activos** (por encima del 3-5 de la casa) y el último recibió **1,72 €**.

Es exactamente lo que avisa `../gestion-cuenta-meta/SKILL.md §3`: «si mezclas anuncios nuevos con
ganadores en el mismo conjunto, **Meta le da todo el presupuesto al ganador** y los nuevos no arrancan».
Está pasando, medido, en las tres cuentas. **Producir más piezas no arregla esto: lo empeora**, porque
reparte el mismo dinero entre más candidatos y ninguno llega a la puerta de datos (3× TCPL).

## 3. Hay creativos DUPLICADOS compitiendo entre sí
En Cliente 14 cada `MOFU__IMG__N` existe dos veces (`N` y `N - Copia`): **14 anuncios de 7 piezas**.
Dos copias del mismo creativo en la misma cuenta se quitan presupuesto y ensucian el ranking.

## 4. El TCPL real por vertical (para calibrar, porque no se parecen en nada)
- **Adicciones (MMS): 2-10 €.** · **Cuidadoras (Cliente 13): 17-46 €.** · **Reformas (Cliente 14):
  30-38 €.** Un «CPL alto» en MMS es un CPL buenísimo en reformas. Cualquier umbral de la casa escrito en
  euros absolutos, sin vertical, no significa nada.

## 5. El naming está roto donde más falta hace
El ganador de toda la cartera se llama **`IMG | Testimonio`** — sin ángulo. Y Cliente 14 usa
`MOFU__IMG__2`, que no dice ni el ángulo ni el formato. Sin el ángulo en el nombre no se puede saber qué
ángulo ganó, que es justo el dato que hace falta para decidir qué producir. Y hay un typo publicado:
**«Una ciudadora inadecuada»**.

## Cómo refrescar esto (funciona, probado el 11-09-2026)
`ads_get_ad_accounts` → por cada cuenta consultable, `ads_get_ad_entities` con `level=ad`,
`date_preset=last_30d`, `fields=[name, effective_status, amount_spent, ctr, cost_per_lead, lead,
impressions, frequency]` y `filtering` por `effective_status IN [ACTIVE]` si solo interesan los vivos.
**No hace falta el token del VPS: el MCP ya da acceso de lectura.** Ojo: `actions` no es un campo válido
a nivel de anuncio; el de leads es `lead` y el de coste, `cost_per_lead`.
