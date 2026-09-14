# Manejar ChatGPT por Chrome sin que tarde una eternidad

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

Dirección, 08-09-2026: *«tarda un montón en mandar la instrucción, en subir las fotos y en tocar los botones».*
Casi todo eso no es lentitud de ChatGPT: es **cómo se está manejando el navegador**. Cuatro reglas.

---

## 0. EL ORDEN. El PRIMER mensaje es la SUGERENCIA del centro, sin adjuntar nada (Dirección, 11-09-2026)
Al abrir el GPT, ChatGPT muestra su **pantalla de bienvenida** con el cuadro de mensaje en el centro y,
debajo, la **sugerencia del propio GPT: «Pídeme brief, referencias visuales y ángulo…»**.

**Esa sugerencia ES el primer mensaje. No se adjunta nada en él.** Se toca, se envía, y se deja que el
GPT conteste pidiendo lo que necesita. **Los insumos —brief, logo, fotos, avatar— van en el SEGUNDO
mensaje**, contestando a lo que ha pedido.

> **Por qué (Dirección, 11-09-2026).** Arrancar soltándole los cinco ficheros de golpe en la pantalla de
> bienvenida es lo que venía haciéndose y es justo donde fallaba: el chat aún no está activo, el
> `input` de fichero puede no existir todavía, y una subida que falla en silencio acaba en una pieza
> bonita con el cliente inventado. Dejando que el GPT **pida primero**, el chat ya está abierto, el
> input existe seguro, y los adjuntos van contra una pregunta concreta suya.

**Orden correcto, y no es negociable:**
```
1. navigate   → la URL del GPT
2. computer   → CLIC en la sugerencia «Pídeme brief, referencias visuales y ángulo…»
3. read_page  → comprobar qué ha quedado en el composer
4. javascript → send-button.click()          ← MENSAJE 1: va SOLO, sin un solo adjunto
5. esperar    → a que el GPT conteste pidiendo brief / referencias / ángulo
                (find "brief", o read_page del último turno; no a capturazos — §4)
--- ahora, y solo ahora, los insumos ---
6. find       → "file input"                  (ya existe seguro: el chat está activo)
7. file_upload→ brief .txt + logo + fotos/avatar → y COMPROBAR que subieron (§1-bis)
8. computer   → type   el prompt del Paso 1 de `prompts-gpt.md`
9. javascript → document.querySelector('button[data-testid="send-button"]').click()   ← MENSAJE 2
                 NO key Return, NO clic por coordenada (el botón se mueve). El clic JS es el fiable;
                 por `ref` también vale. Ver `errores-y-aprendizajes.md §5b` paso 5.
```

**Los pasos 1-4 van en un solo `browser_batch`.** El 5 es una espera por condición. El 7 va aparte
porque hay que comprobarlo. El 8-9, otro batch.

**Si la sugerencia no está** (ChatGPT no siempre la pinta, o el chat ya está empezado): se hace clic en
el cuadro de mensaje del centro para activar el chat y **se escribe a mano el mismo primer mensaje**,
igualmente **sin adjuntos**: *«Pídeme el brief, las referencias visuales y el ángulo que necesitas.»*
Lo que no se hace nunca es saltar directo a soltar los ficheros.

**Al recargar la página se vuelve al paso 2.** La pantalla de bienvenida reaparece y el chat vuelve a
estar inactivo — es el mismo motivo por el que, tras recargar, el primer texto con acentos sale
corrupto (ver `prompts-gpt.md`).

## 1. NUNCA clicar el botón de adjuntar (es la que más tiempo se come)
El clip de ChatGPT abre un **diálogo nativo del sistema operativo**, que el agente **no ve ni puede
manejar**. Se queda dando vueltas, hace capturas para ver qué pasa, reintenta… y ahí se van los minutos.

**Se sube directo al `input` de fichero:**
```
find        → "file input"                  (devuelve ref_N)
file_upload → { ref: "ref_N", paths: ["/ruta/logo.png", "/ruta/avatar.jpg"] }
```
- **Varios ficheros en UNA llamada** (`paths` es una lista): logo + avatar + brief van juntos.
- **Tope de 10 MB por llamada.** Con el **brief en texto** (`brief_a_texto.py`, ~18 KB en vez de 142 KB
  de PDF) no se llega ni de lejos. Si aun así se pasara, se sube en dos llamadas — **nunca** se recorta
  el material para que quepa.
- Si `find` no encuentra el input, `read_page --filter interactive` y buscar `input[type=file]`.
  **Nunca** volver al clic sobre el clip.

## 1-bis. ⛔ COMPROBAR QUE EL ADJUNTO SUBIÓ, ANTES DE ENVIAR (Dirección, 08-09-2026)
**Pasó de verdad: se adjuntó el brief, la subida falló, y el mensaje se envió igual.** El GPT generó
sin brief — o sea, **inventándose el cliente entero**. Y no saltó ningún error: la pieza salía, con
buena pinta, y estaba construida sobre nada.

**Regla dura: después de cada `file_upload`, se comprueba que el fichero está en el composer. Si no
está, NO se envía el mensaje.**

```
file_upload → { ref, paths: [...] }
find        → "<nombre del fichero>"      ← tiene que aparecer la ficha del adjunto
```

| Qué pasa | Qué se hace |
|---|---|
| Aparece la ficha con el nombre | seguir, enviar el mensaje |
| No aparece | **reintentar la subida UNA vez** |
| Sigue sin aparecer | **PARAR ESE MENSAJE. No se envía nada.** Anotarlo en `PROGRESO-Tanda<N>.md` y seguir: **"parar" es no enviar ese mensaje, NO terminar el turno** (regla raíz 1: prohibido devolver el control con trabajo ejecutable pendiente). Se reintenta la subida en un chat nuevo y, si no hay manera, se pasa a lo que no necesite navegador y **se cuenta una sola vez en el resumen final** — el aviso con `avisar.py --nivel aviso` va al cerrar, no a mitad |

**Nunca «lo mando igual y ya veremos».** Una pieza sin brief no se detecta en la auditoría visual: sale
bonita y con el copy inventado. Es el peor tipo de fallo, porque pasa los controles.

**Sospechas habituales cuando falla:**
- **Se pasó de 10 MB** en esa llamada. Comprobar el tamaño de los ficheros y **partir en dos llamadas**
  — nunca quitar material para que quepa. (Si el brief que se está subiendo es el **PDF**, ése es el
  fallo: va el `.txt` de `brief_a_texto.py`, ~18 KB contra 142 KB.)
- Se subió al `input` equivocado (la página tiene más de uno): volver a localizarlo con `read_page`.
- La página se recargó entre medias y se perdió el adjunto: se vuelve a subir.

## 2. Todo lo que se pueda prever, en UN `browser_batch`
Cada llamada suelta es un viaje de ida y vuelta. Un mensaje a ChatGPT son 4 acciones (clic en el
campo → escribir → clic en enviar → comprobar) y por separado son 4 viajes.

```
browser_batch([
  {computer: click en el campo de texto},
  {computer: type   el prompt entero},
  {computer: left_click ref del button[data-testid="send-button"]},   // Return NO dispara el envío
  {computer: wait   3},
])
```
**Regla:** si podés prever dos pasos o más, van en un batch. El batch se para solo si algo falla.

## 3. Para SABER, `read_page`/`find`. Para JUZGAR la imagen, captura
Una captura es una imagen grande: cuesta tiempo y contexto. **No hace falta para saber si un botón
está, si el texto se escribió o si terminó de generar** — eso se lee del árbol de la página, que es
texto y va mucho más rápido.

| Para qué | Con qué |
|---|---|
| ¿Está el botón? ¿Se escribió el prompt? ¿Terminó? | `find` o `read_page --filter interactive` |
| ¿Cómo quedó la imagen generada? (auditoría §G) | **captura, y mirándola de verdad** |
| Ver la página entera de contexto | `computer screenshot` con `scale: 0.5` |

**La auditoría visual NO se recorta.** Mirar la pieza generada es innegociable: ahí sí hay que ver la
imagen, entera y bien. Lo que se recorta es todo lo demás.

## 4. Esperar por CONDICIÓN, no a capturazos
Generar una imagen tarda. **No** se hacen capturas cada pocos segundos para ver si está: se espera a que
aparezca el elemento.

```
browser_batch([ {computer: wait 10}, {find: "imagen generada"} ])
```
Y si no está, se repite el batch. Cada intento son 2 acciones en un viaje, no 6 capturas.
*(Superado por el §5: la espera va dentro de la misma llamada que descarga.)*

## 5. ENVIAR, ESPERAR y DESCARGAR: dos llamadas por imagen, no diez (13-09-2026)
Antes, por imagen: enviar → `wait` + `find` repetidos → localizar el turno → descargar → mover →
normalizar → medir. Ahora son **dos `javascript_tool` y un Bash**. Con varias pestañas (§6), cada
llamada lleva su `tabId`.

**A. Enviar** (tras escribir el prompt y comprobar los adjuntos, §1-bis). Guarda qué imágenes había ya,
para que la espera no confunda la del turno anterior con la nueva:
```js
window.__idsVistos=[...document.querySelectorAll('img')].map(i=>((i.src||'').match(/id=([^&]+)/)||[])[1]).filter(Boolean);
document.querySelector('button[data-testid="send-button"]').click(); 'ENVIADO'
```

**B. Esperar y descargar en la MISMA llamada.** Sustituye `<NOMBRE>` por el nombre final sin `_PEND`
(`Madre<m>_VAR<v>_<formato>_<angulo>_v<ronda>_<1x1|9x16>.png`, `SKILL.md` §5 «Naming del fichero»). Cada
ronda de CAMBIOS sube el `v`: nunca se descarga con el nombre de la ronda anterior. Espera hasta ~100 s; si la imagen no ha salido, devuelve
`PENDIENTE` y se vuelve a lanzar la misma llamada, sin capturas:
```js
await (async()=>{
  const NOMBRE='<NOMBRE>', t0=Date.now(), vistos=new Set(window.__idsVistos||[]);
  const nueva=()=>{
    if(document.querySelector('button[data-testid="stop-button"]')) return null;
    const turns=[...document.querySelectorAll('[data-testid^="conversation-turn"]')];
    const imgs=[...(turns.at(-1)?.querySelectorAll('img')||[])].filter(i=>{
      const id=((i.src||'').match(/id=([^&]+)/)||[])[1]; return id && !vistos.has(id) && i.naturalWidth>0;});
    return imgs.at(-1)||null;
  };
  let img; while(!(img=nueva()) && Date.now()-t0<100000) await new Promise(r=>setTimeout(r,2500));
  if(!img) return 'PENDIENTE — repetir esta llamada';
  const b=await (await fetch(img.src)).blob(), u=URL.createObjectURL(b), a=document.createElement('a');
  a.href=u; a.download=NOMBRE; document.body.appendChild(a); a.click(); a.remove();
  return `DESCARGADA ${NOMBRE} ${img.naturalWidth}x${img.naturalHeight} en ${Math.round((Date.now()-t0)/1000)} s`;
})()
```
Si la página se recargó entre A y B, `__idsVistos` se pierde: antes de B, comprobar con `find` que el
último turno es la respuesta nueva.

**C. Recoger** (Bash, una llamada): `python3 ~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/recoger_png.py "<C>" <NOMBRE> --tanda N --pieza Madre<m>_VAR<v> --ronda r --skill variaciones-estaticos-meta`
(la `r` tiene que ser la misma que el `v<r>` del nombre; si no, o si el nombre ya existe, sale con 1)
→ mueve de `Cliente 25`, normaliza conservando la C2PA, mide zonas y devuelve un JSON. La auditoría se
hace sobre ese PNG, no sobre una captura.

## 6. VARIACIONES EN PESTAÑAS PARALELAS (13-09-2026 — probar en la primera tanda)
Las variaciones **no son una cadena**: cada una lleva en su Mensaje 2 la pieza madre, el logo y su foto,
y no necesita lo que se habló en otra. Así que no hace falta hacerlas una detrás de otra en el mismo chat:
1. Una **pestaña y un chat nuevo del GPT por variación** (`tabs_create_mcp`), el mismo agente las maneja.
2. Mensaje 1 en todas (batch por pestaña) → Mensaje 2 en todas → mientras generan, se recoge y audita
   la que termine primero.
3. **Si ChatGPT no deja generar dos a la vez** (mensaje de límite, o la segunda se queda esperando a que
   acabe la primera), se vuelve a una sola pestaña y se anota en `errores-y-aprendizajes.md` para no
   volver a probarlo. No se insiste: el límite es de la cuenta.
4. La cuenta (`/api/auth/session`) se comprueba **una vez**: todas las pestañas comparten la sesión.

---

## Lo que NO cambia
- **Comprobar la cuenta antes de escribir nada** (`/api/auth/session`): si devuelve
  `<correo-direccion>`, se para. Sigue siendo obligatorio.
- **Adjuntar logo y avatar en CADA generación**: el condicionamiento visual no se arrastra entre
  mensajes. Lo que cambia es **cómo** se adjuntan, no si se adjuntan.
- **Descargar el PNG con `javascript_tool` + `fetch(img.src)`**, que ya funciona.
- **El auto-QC visual de `calidad-y-autoqc.md` §G**, entero.
