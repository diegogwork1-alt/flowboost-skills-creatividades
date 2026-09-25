# LEEME — `estaticos-meta`

> Paquete **creatividades**. Esto es lo que hay que tener en cuenta **antes** de usar la skill.
> Las instrucciones de trabajo están en `SKILL.md`; esto son las condiciones y los límites.

## Qué hace

Director Creativo Ejecutivo autónomo de estáticos de Meta Ads para clientes de Flowboost (B2C y B2B). Replica el sistema del GPT de Dirección "Generador Ads Imagen": minimalismo extremo (1 idea, ≤8 palabras), la marca como fuente de verdad, Breakthrough Advertising (Schwartz), la secuencia de 9 formatos, y GENERA la imagen final (no prompts).

## Antes de empezar necesitas

- **El paquete `fundamentos` instalado al lado** (`npx skills add <usuario-github>/flowboost-skills-fundamentos --copy`). Esta skill lee Ogilvy, Schwartz y el compliance de Meta desde `../fundamentos-copy/`. **Si no está, la skill funciona a medias y NO avisa.**
- La skill **`armar-campana-meta`** (paquete *meta-ads*): lee ficheros suyos.
- La skill **`gestion-cuenta-meta`** (paquete *meta-ads*): lee ficheros suyos.
- El **brief real** del cliente (`0. Onboarding/Brief_<Cliente>.pdf`) **convertido a TXT** con `brief_a_texto.py` — el PDF a veces no sube al GPT y falla en silencio.
- **Branding de Drive** (`1. Branding`): logo oficial, paleta y tipografías del MANUAL, no de un anuncio viejo. Si falta, se pide; no se inventa la marca.
- Sesión de ChatGPT en el workspace de **Flowboost empresa**.

## Lo que NO se puede hacer

- ⛔ **Entrar con `<correo-direccion>`.** El GPT se usa SIEMPRE con `<correo-cuenta-de-trabajo>`. Verificar el perfil de Chrome ANTES de pegar nada.
- ⛔ **Adjuntar estáticos de otros clientes** al GPT: se confunde. El registro visual se le describe con palabras.
- ⛔ Publicar una pieza con **testimonios generados** si la marca `[REEMPLAZAR]` no está **dentro del PNG**.

## Ojo con esto

- **Primero los estáticos, después los guiones.** Es el orden que fijó Dirección para lanzar en 48 h.
- En **advertorial no va el logo**: va un masthead de periódico, y el logo baja a firma de pie.
- **El hook SEGMENTA**: cada pieza habla a un avatar distinto, variando el eje (identidad / situación / dolor / creencia).
- **El 9:16 rehace el ENCUADRE y solo el encuadre.** Botón, halo, pesos de letra, dónde vive el color y los props de la foto: idénticos al 1:1. Ver `references/refs/FlowboostDubai_LEEME.md` §DERIVA.
- Safe zones de Stories: **270 px arriba, 384 px abajo**; margen lateral de la casa **107 px** (65 es el mínimo técnico, no el objetivo).

## Lectura obligatoria antes de trabajar

Esta skill **aprende de los errores**. Leer y, cuando Dirección corrija algo, **añadir la entrada en la misma sesión**:

- `references/errores-y-aprendizajes.md`

## Scripts que trae

- `references/refs/contar_refs.py`
- `scripts/normalizar_png.py`
- `scripts/zonas_seguras.py`
- `templates/poner_logo.py`
- `templates/render.py`

## Accesos que toca

Google Drive del cliente (solo lectura salvo entregables), cuenta de Meta Ads — **solo lectura** (para mirar los ganadores reales), Chrome con sesión de ChatGPT, VPS por SSH, n8n, Tally (formulario).

## Reglas de la casa (valen para todas las skills)

- **Todo el texto para clientes en español de España** (tú/vosotros). Nunca voseo ni LATAM.
- **No se inventa nada**: cifras, testimonios, fechas, garantías o casos. Lo que falte se marca `[FALTA]` y se pide.
- **Las fechas salen del reloj del sistema** (`date +%d/%m/%Y`), nunca de memoria.
- **Los ficheros de un cliente van a `~/Desktop/CLIENTES/<cliente>/`**, nunca sueltos en Descargas.
- **El Drive del cliente es de SOLO LECTURA**, salvo los entregables en su subcarpeta correcta. No se mueve, borra ni renombra nada.
- **Nunca se sube un `.md` crudo al Drive del cliente**: se convierte a Google Doc.
- **Nunca se teclean contraseñas, claves de API ni tokens**, aunque te los den. Los pone Dirección.
- **Para avisar a Dirección se usa `avisar.py`** (`--nivel urgente|aviso|info`), no un mensaje suelto que nadie lee.

---

*Generado el 25-09-2026 desde el sistema de Flowboost. Se regenera con `gen_leeme.py`; no editar a mano.*
