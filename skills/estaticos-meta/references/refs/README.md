# refs/ — Biblioteca de referencias visuales, ORGANIZADA POR FORMATO

Carpeta matriz de referencias. **Una carpeta por formato**, sin separar por cliente; cada archivo se llama `<Cliente>_<formato>_<n>.jpg`. Así se busca "¿cómo se ve un Antes/Después?" y se ven todos los clientes juntos.

## Contenido (94 piezas)
- **68 estáticos REALES ya publicados** de clientes de Flowboost, sacados de sus Drives y revisados uno a uno.
- **12 piezas APROBADAS por Dirección** (`*-APROBADO_<formato>_<1x1|9x16>.jpg`) → son el estándar visual al que hay que parecerse.
- **14 piezas de Flowboost Dubái**, la tanda más reciente.

| Carpeta | Piezas |
|---|---|
| `00_9x16-verticales` | 6 (verticales de referencia para medir la deriva del 9:16) |
| `01_articulo-noticia` | 4 |
| `02_antes-despues` | 8 |
| `03_review-claim` | 16 |
| `04_caracteristica-beneficio` | 15 |
| `05_objeciones-haters` | 11 |
| `06_resolver-el-pain` | 12 |
| `07_oferta-escasez` | 10 |
| `08_prueba-social-stat` | 6 |
| `09_garantia` | 2 |
| `10_tres-pasos` | 4 (formato maestro de la casa, fuera de la secuencia de 9) |

*Recuento regenerado con `contar_refs.py`. Si editás la carpeta, volvé a correrlo.*
## ⚠️ Cómo se usan — REGLA DURA
**Las miro YO, no se le adjuntan al GPT.** Dirección: *"al GPT no le adjuntes cosas de otros clientes porque se confunde, solo en casos de urgencia que no te entienda el formato después de varios intentos"*.
1. Antes de generar un formato → abrir su carpeta, mirar cómo lo resuelven los clientes del **mismo registro**, y traducirlo a **instrucciones escritas**.
2. Priorizar la pieza `Cliente 04-APROBADO_*` como estándar de estructura vigente.
3. **Excepción (urgencia):** si tras varios intentos el GPT no coge la estructura, adjuntar UNA sola, aclarando que es solo estructura.
4. Dentro del MISMO cliente sí se puede adjuntar su propia pieza aprobada (p. ej. su 1:1 para sacar el 9:16).

## Elegir por REGISTRO de marca (no solo por formato)
Error real: pasé Cliente 05 (ruidoso) como referencia para Cliente 04 (premium) → salió cutre. Ver `calidad-y-autoqc.md §D`.
- **Premium / editorial / lujo / legal** (serif sobrio, sin marcador): `Cliente08`, `Cliente11`, `Cliente10`, `Cliente09`, `Cliente 16`, `Cliente 02`, `Cliente 04`
- **Ruidoso / comunidad / local / direct-response** (condensada bold, alto contraste, marcador permitido): `Cliente 05`, `Cliente 03`, `Cliente 13`, `Cliente 14`, `Cliente12`, `Cliente 17`

## Nota
Referencia de **estética y estructura**, nunca de marca ajena: colores, tipografías, logo, avatar y copy salen SIEMPRE del cliente que se produce. No copiar textos ni cifras de estas piezas.
La ficha escrita de cada formato (héroe, estructura, qué NO debe parecer) está en `../formatos-visual-spec.md`.
