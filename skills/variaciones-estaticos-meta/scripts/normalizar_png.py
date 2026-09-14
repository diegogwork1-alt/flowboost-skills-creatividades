#!/usr/bin/env python3
"""Lleva el PNG del GPT al tamaño de la casa SIN perder las Content Credentials (C2PA).

Por qué existe (11-09-2026). El GPT devuelve tamaños raros (941×1672 y parecidos) y el paso 8 del
protocolo los escalaba con PIL. Pero `Image.resize(...).save(destino)` **reescribe el PNG y se lleva
por delante todos los chunks de metadatos**: comprobado, un PNG con `c2pa.manifest` entra con la
credencial y sale sin ella.

Eso importa porque **Meta detecta sola** las Content Credentials que los generadores grandes (OpenAI
entre ellos) incrustan, y etiqueta el anuncio como IA sin que nadie haga nada. Si se pierden, la
declaración pasa a ser **manual** en el Administrador de Anuncios — y omitirla es desaprobación del
anuncio más penalización acumulada en la cuenta. O sea: nuestro propio paso de escalado convertía un
trámite automático en una obligación manual que nadie sabía que existía.

Este script escala **preservando los metadatos** y **dice si la credencial sobrevivió**, que es el
dato que va a `specs_Tanda<N>.md` y que lee `armar-campana-meta` para activar (o no) el control de
divulgación de IA al subir el anuncio.

Uso:
  python3 normalizar_png.py entrada.png                 # in situ, deduce el ratio por su forma
  python3 normalizar_png.py entrada.png salida.png --size 1080x1920
  python3 normalizar_png.py carpeta/ --json             # toda la tanda; salida para el specs
"""
import argparse, glob, json, os, struct, sys, zlib
from PIL import Image, PngImagePlugin

CASA = {(1, 1): (1080, 1080), (9, 16): (1080, 1920)}
# Marcas de C2PA / procedencia que dejan los generadores. Se busca por subcadena, en minúsculas:
# cada herramienta lo escribe a su manera y no hay una clave única estándar en PNG.
PISTAS_C2PA = ("c2pa", "content credential", "contentcredential", "cai", "jumbf",
               "provenance", "dall-e", "openai", "generated with")


# C2PA no viaja en el texto del PNG: viaja en un chunk auxiliar propio, `caBX` (JUMBF).
# **PIL no lo expone en `.info` NUNCA** (comprobado el 11-09-2026: un PNG con `caBX` da
# `.info == {}`), así que buscarlo ahí — como se hacía — no podía funcionar. Peor: al guardar,
# PIL reescribe el fichero y **se lleva el chunk por delante**. El script decía «C2PA presente»
# leyendo un XMP que mencionaba «openai» mientras destruía el manifiesto de verdad.
# Se trabaja a nivel de BYTES: se leen los chunks, se conservan los auxiliares y se detecta el
# manifiesto por su firma binaria.
CHUNKS_A_CONSERVAR = (b"caBX", b"iTXt", b"tEXt", b"zTXt", b"eXIf")
FIRMAS_C2PA = (b"caBX", b"jumb", b"c2pa")


def _chunks(raw):
    """Itera los chunks de un PNG: (tipo, bytes completos del chunk)."""
    i = 8
    while i < len(raw) - 8:
        ln = struct.unpack(">I", raw[i:i + 4])[0]
        tipo = raw[i + 4:i + 8]
        yield tipo, raw[i:i + 12 + ln]
        i += 12 + ln
        if tipo == b"IEND":
            break


def credencial_en_bytes(raw):
    """¿Lleva este PNG un manifiesto de procedencia que Meta pueda leer?"""
    for firma in FIRMAS_C2PA:
        if firma in raw:
            return firma.decode("ascii", "replace")
    bajo = raw[:200000].lower()
    for pista in (b"content credential", b"contentcredential", b"provenance"):
        if pista in bajo:
            return pista.decode()
    return None


def reinyectar(origen_raw, destino):
    """Vuelve a meter en el PNG de salida los chunks auxiliares que PIL se comió."""
    salida = open(destino, "rb").read()
    ya = {t for t, _ in _chunks(salida)}
    extra = b"".join(c for t, c in _chunks(origen_raw)
                     if t in CHUNKS_A_CONSERVAR and t not in ya)
    if not extra:
        return False
    i = salida.index(b"IDAT") - 4           # los auxiliares van antes del primer IDAT
    open(destino, "wb").write(salida[:i] + extra + salida[i:])
    return True


def credencial(info):
    """Compatibilidad: detección por texto. La buena es `credencial_en_bytes`."""
    for k, v in info.items():
        s = f"{k} {v}".lower()
        if any(p in s for p in PISTAS_C2PA):
            return f"{k}"
    return None


def destino_casa(w, h):
    r = 1 if w == h else (9 / 16)
    return CASA[(1, 1)] if w == h else CASA[(9, 16)]


def veredicto_ia(credencial, reescalado):
    """Qué se pone en `IA declarada`, y por qué NO basta con que el chunk siga ahí.

    Un manifiesto C2PA no es una etiqueta: es una firma que incluye una **aserción de hash sobre los
    bytes de la imagen**. Reinyectar el chunk `caBX` en un PNG reescalado conserva el chunk pero
    **rompe ese hash**: el validador (Meta) lee un manifiesto que no corresponde a los píxeles y lo
    trata como no válido — no como válido. O sea que decir «automática» porque el `caBX` está presente
    es declarar de MENOS, que es justo lo que cuesta la desaprobación del anuncio.

    Por eso el veredicto mira las DOS cosas, y ante la duda manda declarar a mano (el Reglamento de IA
    europeo pide lo mismo: ante la duda, se declara).
    """
    if not credencial:
        return "MANUAL PENDIENTE (sin C2PA)"
    if reescalado:
        return ("MANUAL PENDIENTE (C2PA reinyectada pero la pieza se REESCALÓ: "
                "el manifiesto ya no cuadra con los píxeles y Meta no lo valida)")
    return "automática (C2PA intacta, sin reescalar)"


def normalizar(origen, salida=None, size=None):
    origen_raw = open(origen, "rb").read()
    src = Image.open(origen)
    w, h = src.size
    antes = credencial_en_bytes(origen_raw) or credencial(src.info)
    destino = tuple(int(x) for x in size.lower().split("x")) if size else destino_casa(w, h)

    # Los metadatos se copian a mano: PIL no los arrastra al guardar.
    info = PngImagePlugin.PngInfo()
    for k, v in src.info.items():
        if isinstance(v, str):
            info.add_itxt(k, v)

    # NUNCA se sobrescribe el original sin dejar copia: si el escalado sale mal, la credencial
    # original es irrecuperable.
    out = salida or origen
    if out == origen:
        copia = origen + ".orig"
        if not os.path.exists(copia):
            open(copia, "wb").write(origen_raw)
    img = src if (w, h) == destino else src.convert("RGB").resize(destino, Image.LANCZOS)
    img.save(out, pnginfo=info)
    reinyectar(origen_raw, out)             # devolver los chunks que PIL se llevó

    despues = credencial_en_bytes(open(out, "rb").read())
    return {"fichero": os.path.basename(out),
            "de": f"{w}x{h}", "a": f"{destino[0]}x{destino[1]}",
            "reescalado": (w, h) != destino,
            "c2pa_antes": antes, "c2pa_despues": despues,
            "ia_declarada": veredicto_ia(despues, (w, h) != destino),
            # «perdida» = hay que mirarlo antes de subir. Dos casos, no uno:
            #   · la credencial se fue del todo, o
            #   · sobrevivió el chunk pero la pieza se reescaló → el manifiesto ya no valida.
            "perdida": (bool(antes) and not despues) or (bool(despues) and (w, h) != destino)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ruta"); ap.add_argument("salida", nargs="?")
    ap.add_argument("--size"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    rutas = [a.ruta] if os.path.isfile(a.ruta) else sorted(glob.glob(os.path.join(a.ruta, "*.png")))
    if not rutas: sys.exit(f"✗ No hay PNG en {a.ruta}")
    res = [normalizar(p, a.salida if len(rutas) == 1 else None, a.size) for p in rutas]

    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1)); return

    perdidas = 0
    for r in res:
        print(f"  {r['fichero'][:46]:<46} {r['de']} → {r['a']}   IA declarada: {r['ia_declarada']}")
        if r["c2pa_antes"] and not r["c2pa_despues"]:
            perdidas += 1
            print("       ⛔ la credencial se ha PERDIDO al guardar — no debería pasar, revisar")
        elif r["c2pa_despues"] and r["reescalado"]:
            perdidas += 1
            print(f"       ⚠️  reescalada {r['de']} → {r['a']}: el chunk C2PA sigue ahí pero su hash ya "
                  "no cuadra con los píxeles, así que Meta NO la etiquetará sola → DIVULGACIÓN MANUAL")
    a_mano = sum(1 for r in res if r["ia_declarada"].startswith("MANUAL"))
    if a_mano:
        print(f"\n  {len(res)} pieza(s) · **{a_mano} piden declaración MANUAL de IA** en el "
              f"Administrador de Anuncios al crear el anuncio (casilla de divulgación)")
    else:
        print(f"\n  {len(res)} pieza(s) · todas con la credencial intacta y sin reescalar → "
              f"**Meta las etiqueta sola**, no hay que tocar nada al subirlas")
    print("  Este dato va al specs de la tanda por pieza (`specs_Tanda<N>.md` o `specs_VAR_<fecha>.md`):")
    print("  lo lee armar-campana-meta al subir el anuncio. Sin el campo se asume MANUAL PENDIENTE.")
    sys.exit(1 if perdidas else 0)


if __name__ == "__main__":
    main()
