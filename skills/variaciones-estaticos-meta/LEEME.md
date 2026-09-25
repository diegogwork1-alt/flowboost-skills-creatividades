# LEEME — `variaciones-estaticos-meta`

> Paquete **creatividades**. Esto es lo que hay que tener en cuenta **antes** de usar la skill.
> Las instrucciones de trabajo están en `SKILL.md`; esto son las condiciones y los límites.

## Qué hace

Hace VARIACIONES de un estático de Meta que ya existe, en vez de crear uno desde cero. Dirección pasa la pieza de referencia y la skill devuelve variaciones claras del MISMO formato y el MISMO ángulo, cambiando todo lo demás — fondo, foto, composición, redacción.

## Antes de empezar necesitas

- **El paquete `fundamentos` instalado al lado** (`npx skills add <usuario-github>/flowboost-skills-fundamentos --copy`). Esta skill lee Ogilvy, Schwartz y el compliance de Meta desde `../fundamentos-copy/`. **Si no está, la skill funciona a medias y NO avisa.**
- La skill **`armar-campana-meta`** (paquete *meta-ads*): lee ficheros suyos.
- La skill **`funnel`** (paquete *direccion*): lee ficheros suyos.
- La skill **`gestion-cuenta-meta`** (paquete *meta-ads*): lee ficheros suyos.
- **La pieza de referencia** en PNG/JPG, captura, enlace del Drive o de la Biblioteca de Anuncios. Si no se lee el titular y no se ve la imagen, se pide otra vez.
- **El rendimiento de esa pieza** (CPL y leads) si se sabe: se varía lo que funciona. Sin el dato se trabaja igual, pero se anota «sin rendimiento conocido».
- **3 imágenes reales distintas**, una por variación: material del cliente → capturas de su web → stock gratuito (anotando fuente e id).
- Sesión de ChatGPT en el workspace de **Flowboost empresa** (el motor es el mismo que la tanda normal).

## Lo que NO se puede hacer

- ⛔ **INVENTAR** una cara o un escenario con IA. Recrear una persona REAL que se le adjunta, sí; inventarla, no. Si la cara no se parece a la referencia, el modelo la inventó → regenerar re-adjuntando la foto.
- ⛔ **Cambiar el ángulo o el formato.** Eso ya no es una variación: es una pieza nueva y va por `estaticos-meta`.
- ⛔ **Variar una pieza de otro cliente** (competencia u otra cuenta). Se avisa y se para.
- ⛔ **Sacar a campaña una pieza con cara de stock y testimonio** sin cara y autorización del cliente real: los bancos gratuitos no dan derechos para sugerir respaldo.

## Ojo con esto

- **Se dispara a petición de Dirección, NO por fatiga.** Ante frecuencia >3,0 la cuenta pide un concepto distinto, no una variación: 5 variaciones del mismo ángulo cuentan como 1 apuesta.
- **La prueba de los 200 px decide:** las tres juntas y la original a ese tamaño; si no se distinguen, se rehace.
- **Marca la misma etapa que la tanda normal** («Estáticos (tanda)») y por tanto **sobreescribe su fila** en ESTADO.md: la nota tiene que decir que son variaciones y de qué pieza.
- **Cero imágenes repetidas ENTRE variaciones** — pero el 1:1 y el 9:16 de la misma variación llevan la misma foto a propósito.

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

Google Drive del cliente (solo lectura salvo entregables), Chrome con sesión de ChatGPT, VPS por SSH, n8n, Tally (formulario).

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
