# LEEME — `copy-anuncios-meta`

> Paquete **creatividades**. Esto es lo que hay que tener en cuenta **antes** de usar la skill.
> Las instrucciones de trabajo están en `SKILL.md`; esto son las condiciones y los límites.

## Qué hace

Escribe el COPY de un anuncio de Meta (texto primario + título + descripción + botón CTA) basándose en el ESTÁTICO (la imagen del anuncio: la produce la skill `estaticos-meta` con el GPT) y el GUION del video de ese anuncio, más el contexto del brief del cliente. Copy corto y persuasivo estilo Ogilvy (respuesta directa).

## Antes de empezar necesitas

- **El paquete `fundamentos` instalado al lado** (`npx skills add <usuario-github>/flowboost-skills-fundamentos --copy`). Esta skill lee Ogilvy, Schwartz y el compliance de Meta desde `../fundamentos-copy/`. **Si no está, la skill funciona a medias y NO avisa.**
- La skill **`estaticos-meta`** (paquete *creatividades*): lee ficheros suyos.
- El estático ya producido y el guion del vídeo de ese anuncio.

## Lo que NO se puede hacer

- ⛔ Inventar cifras o testimonios: lo que falte se marca `[FALTA]`.

## Ojo con esto

- Da 2-3 variantes por campo para testear. Alimenta a `armar-campana-meta`.

## Accesos que toca

Google Drive del cliente (solo lectura salvo entregables).

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

*Generado el 21-09-2026 desde el sistema de Flowboost. Se regenera con `gen_leeme.py`; no editar a mano.*
