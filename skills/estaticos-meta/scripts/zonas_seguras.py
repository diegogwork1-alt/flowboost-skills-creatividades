#!/usr/bin/env python3
"""Mide dónde cae el contenido de alto contraste de un estático respecto a las zonas muertas de Meta.

Acepta **los dos tamaños de la casa**: 9:16 (1080×1920, franjas de Stories) y 1:1 (1080×1080, margen
de 54 px en los cuatro bordes). Hasta el 11-09-2026 solo medía 9:16 y a un 1:1 perfecto le contestaba
«NO es 1080x1920»: con la regla «zona segura invadida = se rehace», la mitad de cada entrega entraba
en bucle. El 1:1 sí se dictamina en los cuatro bordes — ahí no hay foto a sangre que confunda.

Por qué existe (test del 08-09-2026): *«no acierta las zonas seguras ni en píxeles, ni en
porcentaje, ni en franjas; las 7 verticales hubo que ajustarlas midiendo y encajando en post»*.
Pedirlo en el prompt no basta, y **mirarlo a ojo tampoco**: 40 px de invasión no se ven en el
monitor y en el móvil dejan el CTA debajo de la interfaz de Meta.

**MIDE, NO OPINA — y lo que mide no es "texto", es contenido de alto contraste.** Esto hay que tenerlo
claro o el script engaña (se comprobó contra las 6 verticales aprobadas de Cliente 01, 11-09-2026):

- **Arriba (270 px) el veredicto vale.** Si hay contenido ahí, hay que mirarlo: el titular o el logo
  entran en la franja del perfil. *Las propias referencias aprobadas lo incumplen* —colocan el primer
  elemento a 117-226 px— y eso está anotado y sin resolver en `../references/refs/00_9x16-verticales/LEEME.md`:
  **mientras Dirección no diga otra cosa, manda la safe zone de 270 px.**
- **Abajo (384 px) el veredicto NO es concluyente por sí solo.** El patrón de la casa es **foto a sangre
  por abajo**, así que en una pieza buena hay contenido de alto contraste ahí y no es una invasión. Lo
  que importa es si lo que entra es **texto, logo o CTA**, y eso lo decide el ojo: `--marcar` y mirar.
- **Los laterales no se dictaminan:** con fondos a sangre da falsos positivos (marcaba 5 de las 6
  verticales aprobadas, y a ojo están bien). Se informan, nada más.
- **Hay paletas que no ve:** un advertorial navy sobre crema no llega a "casi blanco / casi negro" y el
  script no detecta nada (`Cliente 01_9x16_advertorial-noticia.png`). Eso sale como **NO CONCLUYENTE**, que
  no es lo mismo que "limpia": ahí se juzga a ojo, entera.

Por eso los veredictos son tres: **limpia · revisar · no concluyente**, y el script **sale con código 1
si alguna pieza no es «limpia»** — código 1 significa *hay que mirar esa franja*, no *rechazar la pieza*.

Filtro nuevo (11-09-2026): las filas cuya máscara cubre **más del 60 % del ancho** se descartan. Son
**líneas estructurales y bordes de panel o de foto**, no glifos: ninguna línea de texto, ni un titular
apretado, cubre 1080 px seguidos. Sin este filtro, el borde del split de `Cliente 01_9x16_antes-despues.png`
daba «entra 270 px arriba y 384 abajo» en una pieza aprobada.

Cifras (1080×1920), separando lo que dice Meta de lo que decide la casa — contrastado el 11-09-2026
contra las fuentes reales del NotebookLM «Creativos Meta», porque dos de nuestros números no tenían
fuente:

| | Lo que publica Meta (fuente) | Lo que usa la casa |
|---|---|---|
| Arriba | **269 px (14 %)** | 270 px ✔ coincide |
| Abajo | **672 px (35 %)** — «la zona tapada por el CTA nativo, los subtítulos y los botones» | **384 px (20 %)** — apuesta de la casa para ganar superficie |
| Laterales | **65 px (6 %)** | 107 px — **sin fuente**: es el margen medido en 2 de las 6 piezas aprobadas |
| Área central garantizada | **950×979 px** | — |

Stories y Reels comparten cifras: Meta publica **una sola** zona segura 9:16.

Consecuencia práctica: entre y=1248 y y=1536 la pieza **no invade el valor de la casa pero sí lo que
Meta declara tapado**. Ahí el script avisa en vez de dictaminar, porque lo que decide es *qué* hay:
un CTA, un logo o un claim no pueden estar ahí; un fondo o una foto, sí.

Uso:
  python3 zonas_seguras.py pieza.png                   # una, con medidas
  python3 zonas_seguras.py carpeta/                    # todas
  python3 zonas_seguras.py pieza.png --marcar out.png  # dibuja las franjas encima  ← para decidir
  python3 zonas_seguras.py carpeta/ --json             # salida para otro script
"""
import argparse, glob, json, os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

ARRIBA, ABAJO, LADOS = 270, 384, 65      # 9:16 · arriba y lados = cifras DE FUENTE; abajo = la casa
ABAJO_META = 672                         # 9:16 · la franja inferior QUE PUBLICA META (35 %)
CUADRADO = 54                            # 1:1 · 5 % de margen en los 4 bordes
OBJETIVO_LADOS = 107        # margen de composición de la casa (refs/00_9x16-verticales/LEEME.md).
                            # 65 = mínimo técnico infranqueable; 107 = el que se pide en el prompt.
LUZ_ALTA, LUZ_BAJA, BORDE = 232, 26, 55   # "casi blanco o casi negro con borde duro"
MIN_FILA = 25               # px de máscara en una fila para contarla como contenido
MAX_FILA_FRAC = 0.60        # fila que cubre más de esto = línea/borde estructural, no texto
ANILLO = 6                  # grosor del borde que se mira para saber si la pieza va a sangre
SANGRE_FRAC = 0.0005        # medido: fondo plano da EXACTAMENTE 0,0000; las piezas a sangre,
                            # de 0,0013 a 0,0405. Cualquier contenido en el anillo = llega al borde.
MIN_MASCARA = 5000          # por debajo de esto el detector no ve la paleta → NO CONCLUYENTE
HUECO_FRAC = 0.33           # hueco interior a partir del cual se avisa (ver medir_hueco)


def mascara_texto(img):
    g = np.asarray(img.convert("L"), dtype=np.float32)
    extremo = (g > LUZ_ALTA) | (g < LUZ_BAJA)
    bordes = np.asarray(Image.fromarray(g.astype(np.uint8)).filter(ImageFilter.FIND_EDGES),
                        dtype=np.float32)
    return extremo & (bordes > BORDE)


def _filas_de_contenido(m, w):
    """Filas con contenido, descartando las que son una línea/borde de lado a lado."""
    filas = m.sum(axis=1)
    return np.nonzero((filas > MIN_FILA) & (filas <= MAX_FILA_FRAC * w))[0]


def _cols_de_contenido(m, h):
    """Columnas con contenido, con el MISMO filtro que las filas.

    BUG GRAVE, encontrado por el consejo el 11-09-2026 y corregido aquí. Las columnas se
    calculaban con `cols > MIN_FILA` — el umbral de 25 px pensado para FILAS (que suman 1080
    columnas) aplicado a COLUMNAS (que suman 1920 filas), y **sin el filtro de bordes
    estructurales**. Resultado: cualquier foto a sangre clavaba `izq_x=0` y `der_x=1079`, y como
    en 1:1 los laterales SÍ se dictaminan, **11 de las 12 piezas Cliente 04-APROBADO —el estándar de
    oro de la casa— salían «CAMBIOS»**. Cada pieza habría quemado sus 3-4 iteraciones corrigiendo
    una invasión que no existe, se habría degradado al regenerar, habría acabado en `_PEND`, y
    `armar-campana-meta` no habría subido nada: **una tanda entera sin un solo anuncio publicable,
    y sin que Dirección se entere, porque la auditoría no se le cuenta.**

    El filtro es el mismo razonamiento que en las filas: una columna cuya máscara cubre más del
    60 % del ALTO es un borde de foto o de panel, no una letra. Y el umbral mínimo se escala a la
    longitud del eje, que es lo que estaba mal.
    """
    cols = m.sum(axis=0)
    min_col = MIN_FILA * h / 1080.0          # el 25 estaba calibrado sobre un eje de 1080
    return np.nonzero((cols > min_col) & (cols <= MAX_FILA_FRAC * h))[0]


def va_a_sangre(m):
    """¿La imagen llega al borde (foto/fondo a sangre) o tiene fondo plano?

    Es LA pregunta que decide si este script puede dictaminar o solo informar, y no estaba.
    Una foto a sangre tiene textura de alto contraste pegada a los cuatro bordes, igual que la
    tendría un texto mal colocado: **el detector no puede distinguirlas**. Fingir que sí es lo
    que hacía que 11 de las 12 piezas Cliente 04-APROBADO —el estándar de oro de la casa— salieran
    «CAMBIOS» por una invasión que no existe (consejo, 11-09-2026).

    Con fondo plano, en cambio, lo único que puede tocar el margen es texto, logo o CTA: ahí el
    veredicto sí vale.
    """
    anillo = np.concatenate([m[:ANILLO].ravel(), m[-ANILLO:].ravel(),
                             m[:, :ANILLO].ravel(), m[:, -ANILLO:].ravel()])
    return anillo.mean() > SANGRE_FRAC


def medir_hueco(fy, h):
    """El mayor tramo VACÍO entre la primera y la última fila de contenido.

    Existe porque medir solo el borde miente (11-09-2026): este script daba ✓ y exit 0 a una pieza
    con un tercio del lienzo vacío en el centro — las plantillas HTML están compuestas para 4:5 y su
    `.cta{margin-top:auto}` abre un agujero de 600-840 px cuando el contenido es corto. "Limpia" no
    puede significar "publicable" si nadie mira lo que hay entre la primera fila y la última.

    Calibrado contra las seis verticales aprobadas de Cliente 01: su mayor hueco llega al 27 % (y ahí lo
    que hay es la foto a sangre, que el detector no ve). Las piezas rotas del plan B van del 39 % al
    44 %. El umbral de 33 % los separa sin marcar ninguna aprobada. **Avisa, no dictamina:** un hueco
    grande puede ser aire buscado o una foto que el detector no ve — se mira con --marcar.
    """
    if fy.size < 2: return None
    d = np.diff(fy); i = int(d.argmax()); px = int(d.max())
    if px < HUECO_FRAC * h: return None
    return {"px": px, "pct": round(100 * px / h, 1), "desde": int(fy[i]), "hasta": int(fy[i + 1])}


def medir(ruta):
    img = Image.open(ruta).convert("RGB")
    w, h = img.size
    r = {"fichero": os.path.basename(ruta), "tamano": f"{w}x{h}",
         "veredicto": "no_concluyente", "avisos": [], "contenido": None, "en_franja_px": {},
         "laterales_a_ojo": []}
    if (w, h) == (1080, 1920):
        ratio, arriba, abajo, lados, objetivo = "9:16", ARRIBA, ABAJO, LADOS, OBJETIVO_LADOS
    elif (w, h) == (1080, 1080):
        # En 1:1 no hay franjas muertas de interfaz: es el margen de composición del 5 %,
        # y se dictamina en los CUATRO bordes (sin foto a sangre que dé falsos positivos).
        ratio, arriba, abajo, lados, objetivo = "1:1", CUADRADO, CUADRADO, CUADRADO, CUADRADO
    else:
        # ⚠️ NO se mide nada aquí, y eso NO es lo mismo que «hay que revisarla»: es que no se sabe.
        # Antes el veredicto por defecto era «revisar», así que las 12 piezas Cliente 04-APROBADO (900x900
        # y 900x1600) salían «a revisar» con exit 1 **sin que se hubiera medido un solo píxel** — y eso
        # se leyó como «el medidor las suspende». No las suspendía: no las miraba.
        r["no_medida"] = True
        r["avisos"].append(f"NO MEDIDA: el tamaño ({w}x{h}) no es de la casa. Normaliza ANTES de medir "
                           f"con `normalizar_png.py` (NUNCA con PIL a pelo: se lleva la credencial C2PA "
                           f"y convierte la declaración de IA en manual) y vuelve a pasar el medidor")
        return r
    r["ratio"] = ratio

    m = mascara_texto(img)
    r["a_sangre"] = bool(va_a_sangre(m))
    if m.sum() < MIN_MASCARA:
        r["veredicto"] = "no_concluyente"
        r["avisos"].append("el detector casi no ve nada (¿navy sobre crema, o pieza solo de imagen?) "
                           "— juzgar la pieza a ojo, entera")
        return r

    fy = _filas_de_contenido(m, w)
    if fy.size == 0:
        r["veredicto"] = "no_concluyente"
        r["avisos"].append("solo se detectan líneas de lado a lado, ningún bloque de texto — a ojo")
        return r

    arriba_y, abajo_y = int(fy[0]), int(fy[-1])
    fx = _cols_de_contenido(m, h)
    izq_x, der_x = (int(fx[0]), int(fx[-1])) if fx.size else (None, None)
    if izq_x is None:
        # Puede pasar aunque fy tenga contenido: el umbral se supera sumando 1080 columnas,
        # pero ninguna columna suelta lo supera sumando 1920 filas. Antes petaba con IndexError
        # justo aquí — un traceback en la compuerta es lo peor, porque deja la pieza sin veredicto.
        r["avisos"].append("laterales no medibles (contenido muy fino por columna) — a ojo")
    r["contenido"] = {"primera_fila": arriba_y, "ultima_fila": abajo_y,
                      "primera_col": izq_x, "ultima_col": der_x}

    if arriba_y < arriba:
        r["en_franja_px"]["arriba"] = arriba - arriba_y
    if abajo_y >= h - abajo:
        r["en_franja_px"]["abajo"] = abajo_y - (h - abajo) + 1

    if izq_x is not None:
        if ratio == "1:1":
            # En 1:1 los laterales SÍ se dictaminan: cuentan como invasión, no como aviso.
            if izq_x < lados:  r["en_franja_px"]["izquierda"] = lados - izq_x
            if der_x >= w - lados: r["en_franja_px"]["derecha"] = der_x - (w - lados) + 1
        else:
            if izq_x < lados:
                r["laterales_a_ojo"].append(f"izquierda hasta x={izq_x} (por debajo del mínimo {lados})")
                r["lateral_bajo_minimo"] = True
            elif izq_x < objetivo:
                r["laterales_a_ojo"].append(f"izquierda a x={izq_x} (dentro del mínimo, por debajo "
                                            f"del margen de la casa {objetivo})")
            if der_x >= w - lados:
                r["laterales_a_ojo"].append(f"derecha desde x={der_x} (por debajo del mínimo {lados})")
                r["lateral_bajo_minimo"] = True
            elif der_x > w - objetivo:
                r["laterales_a_ojo"].append(f"derecha a x={der_x} (dentro del mínimo, por debajo "
                                            f"del margen de la casa {objetivo})")

    hueco = medir_hueco(fy, h)
    if hueco: r["hueco"] = hueco
    # Franja de riesgo del 9:16 (11-09-2026, contrastado en NotebookLM con las fuentes reales):
    # **Meta publica 672 px / 35 % como franja inferior**, no 384. Los 384 son una apuesta de la casa
    # para ganar superficie útil. Entre 1248 y 1536 la pieza NO invade el valor de la casa, pero SÍ
    # entra en lo que Meta declara tapado por el CTA nativo, los subtítulos y los botones. Ahí no se
    # dictamina: se avisa, porque lo que decide es QUÉ hay en esa franja.
    if ratio == "9:16" and abajo_y >= h - ABAJO_META and "abajo" not in r["en_franja_px"]:
        r["riesgo_reels"] = {"px": abajo_y - (h - ABAJO_META) + 1, "desde_y": h - ABAJO_META}
    if r["a_sangre"]:
        # No se puede dictaminar: lo que toca el borde puede ser la foto o puede ser el titular.
        r["avisos"].append("la imagen va A SANGRE (llega al borde): el script NO puede distinguir "
                           "la foto del texto, así que aquí solo informa — mira con --marcar y "
                           "decide tú si lo que entra en la franja es fondo o es texto/logo/CTA")
        # ⛔ Con la imagen a sangre el techo es «no concluyente», NUNCA «limpia». Antes decía «limpia»
        # cuando `en_franja_px` venía vacío — y los laterales no entran en `en_franja_px` en 9:16, así
        # que una pieza con texto a x=9 (por debajo del mínimo duro de 65) salía «✓ limpia» con exit 0.
        # Ese era el FALSO NEGATIVO: el único hueco por el que una pieza mala se publicaba sola. Y como
        # el patrón de producción de la casa ES foto a sangre, el hueco estaba abierto casi siempre.
        r["veredicto"] = ("revisar" if (r["en_franja_px"] or hueco or r.get("lateral_bajo_minimo"))
                          else "no_concluyente")
        r["solo_informa"] = True
    else:
        r["veredicto"] = ("limpia" if not r["en_franja_px"] and not hueco
                          and "riesgo_reels" not in r and not r.get("lateral_bajo_minimo")
                          else "revisar")
    return r


def marcar(ruta, salida):
    img = Image.open(ruta).convert("RGB"); w, h = img.size
    if (w, h) not in ((1080, 1080), (1080, 1920)):
        # Las franjas son píxeles absolutos: pintarlas sobre una 900x1600 dibuja zonas que no existen,
        # y `--marcar` es justo la salida que usa el humano para decidir. Mentirle ahí es lo peor.
        raise SystemExit(f"⛔ --marcar necesita 1080x1080 o 1080x1920; esta es {w}x{h}. "
                         f"Normaliza primero con normalizar_png.py.")
    cuadrado = (w, h) == (1080, 1080)
    arriba, abajo, lados = (CUADRADO, CUADRADO, CUADRADO) if cuadrado else (ARRIBA, ABAJO, LADOS)
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(capa)
    rojo = (255, 60, 90, 70)
    d.rectangle([0, 0, w, arriba], fill=rojo)
    d.rectangle([0, h - abajo, w, h], fill=rojo)
    d.rectangle([0, 0, lados, h], fill=rojo)
    d.rectangle([w - lados, 0, w, h], fill=rojo)
    if not cuadrado:                      # franja entre el mínimo (65) y el margen de la casa (107)
        naranja = (255, 170, 40, 45)
        d.rectangle([lados, 0, OBJETIVO_LADOS, h], fill=naranja)
        d.rectangle([w - OBJETIVO_LADOS, 0, w - lados, h], fill=naranja)
    fy = _filas_de_contenido(mascara_texto(img), w)
    if fy.size:
        for y in (int(fy[0]), int(fy[-1])):
            d.line([0, y, w, y], fill=(60, 220, 140, 230), width=4)
    Image.alpha_composite(img.convert("RGBA"), capa).convert("RGB").save(salida)
    return salida


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ruta"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--marcar", default="")
    a = ap.parse_args()

    if a.marcar:
        print("✓", marcar(a.ruta, a.marcar)); return

    rutas = ([a.ruta] if os.path.isfile(a.ruta)
             else sorted(glob.glob(os.path.join(a.ruta, "*.png"))
                         + glob.glob(os.path.join(a.ruta, "*.jpg"))))
    if not rutas: sys.exit(f"✗ No hay imágenes en {a.ruta}")

    res = [medir(p) for p in rutas]
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        sys.exit(1 if any(x["veredicto"] != "limpia" for x in res) else 0)

    icono = {"limpia": "✓", "revisar": "👁", "no_concluyente": "?"}
    for r in res:
        c = r["contenido"]
        rango = f" contenido de y={c['primera_fila']} a y={c['ultima_fila']}" if c else ""
        rt = f"[{r.get('ratio','?')}] "
        print(f"  {icono[r['veredicto']]} {rt}{r['fichero'][:44]:<44}{rango}")
        cuad = r.get("ratio") == "1:1"
        for k, v in r["en_franja_px"].items():
            flecha = "→ MIRAR (va a sangre)" if r.get("solo_informa") else "→ CAMBIOS"
            if cuad:
                print(f"       {k}: entra {v} px en el margen de {CUADRADO} px {flecha}")
            elif k == "arriba":
                print(f"       arriba: entra {v} px en la franja de 270 {flecha} "
                      f"(si es el titular o el logo, caen bajo el perfil)")
            else:
                print(f"       abajo: entra {v} px en la franja de 384 → MIRAR con --marcar: "
                      f"si es la foto a sangre, pasa; si es texto/logo/CTA, CAMBIOS")
        if r.get("hueco"):
            g = r["hueco"]
            print(f"       hueco interior de {g['px']} px ({g['pct']} % del lienzo) entre y={g['desde']} "
                  f"y y={g['hasta']} → MIRAR con --marcar: ¿es aire buscado o la pieza se quedó corta?")
            print(f"       (si viene de una plantilla HTML, es el `.cta{{margin-top:auto}}`: están "
                  f"compuestas para 4:5 y no recomponen)")
        if r.get("riesgo_reels"):
            rr = r["riesgo_reels"]
            print(f"       entra {rr['px']} px en la franja de 672 px que Meta declara tapada "
                  f"(desde y={rr['desde_y']}) → MIRAR: ahí no puede haber CTA, logo ni claim.")
            print(f"       Los 384 px son el valor de la casa, no el de Meta: entre 1248 y 1536 la "
                  f"pieza se ve, pero en Reels el pie nativo se lo come.")
        for x in r["laterales_a_ojo"]:
            print(f"       lateral: {x} — a ojo, suele ser el fondo")
        for x in r["avisos"]:
            print(f"       {x}")

    n = {k: sum(1 for x in res if x["veredicto"] == k) for k in icono}
    print(f"\n  {n['limpia']} limpias · {n['revisar']} a revisar · {n['no_concluyente']} no concluyentes")
    print(f"  1:1 → margen de {CUADRADO} px en los 4 bordes, los cuatro se dictaminan.")
    print("  9:16 → arriba (270) el veredicto vale; abajo (384) hay que MIRAR con --marcar, porque el")
    print("  patrón de la casa es foto a sangre por abajo y eso no es invasión si no es texto/logo/CTA.")
    print(f"  9:16 laterales: {LADOS} px es la cifra DE META (6 %); {OBJETIVO_LADOS} px es una")
    print("  preferencia de composición de la casa, medida en piezas aprobadas, SIN fuente externa.")
    print(f"  9:16 abajo: {ABAJO} px es el valor de la casa; **Meta publica {ABAJO_META} px (35 %)**.")
    print(f"  Hueco interior: se avisa a partir del {int(HUECO_FRAC*100)} % del lienzo. Medir el borde")
    print("  no basta: una pieza con un tercio vacío en el centro pasaba como «limpia».")
    sys.exit(1 if n["limpia"] != len(res) else 0)


if __name__ == "__main__":
    main()
