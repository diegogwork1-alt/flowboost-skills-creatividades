#!/usr/bin/env python3
"""Compone el LOGO OFICIAL del cliente sobre un estático generado.

⚠️ PLAN B — NO es la regla de la casa.

Lo normal es que el GPT ponga el logo oficial del cliente dentro de la pieza.
Pedir la pieza SIN logo para pegarlo aqui despues es lo que Dirección llamo "error
garrafal": solo se hace si el lo pide expresamente, o si el GPT ya deformo el
logo en esa pieza concreta.

El motivo tecnico por el que existe este script: los modelos de imagen REDIBUJAN
el logo y lo van deformando a lo largo de la cadena de 9 formatos. Cuando pasa,
esto pega el PNG oficial -> fidelidad pixel-perfect.

Uso:
  python3 poner_logo.py <ad.png> <logo.png> <salida.png> \
      [--pos top-left|top-center|top-right|bottom-left|bottom-center|bottom-right] \
      [--ancho 0.22]   # ancho del logo como fraccion del ancho del lienzo
      [--margen 0.05]  # margen como fraccion del lado corto (1:1 -> 5%)
      [--safe-top 0.14] [--safe-bottom 0.20]  # solo 9:16: zonas muertas

Notas:
 - En 9:16 el logo debe quedar POR DEBAJO del 14% superior (safe zone de Stories):
   usar --safe-top 0.14, el script lo baja automaticamente.
 - El logo se pega con transparencia (RGBA). Usar la version del logo que
   contraste con el fondo (navy sobre claro, blanco sobre oscuro).
"""
import argparse
from PIL import Image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ad")
    ap.add_argument("logo")
    ap.add_argument("salida")
    ap.add_argument("--pos", default="top-center")
    ap.add_argument("--ancho", type=float, default=0.22)
    ap.add_argument("--margen", type=float, default=0.05)
    ap.add_argument("--safe-top", type=float, default=0.0)
    ap.add_argument("--safe-bottom", type=float, default=0.0)
    a = ap.parse_args()

    ad = Image.open(a.ad).convert("RGBA")
    logo = Image.open(a.logo).convert("RGBA")
    W, H = ad.size

    # escalar logo
    lw = int(W * a.ancho)
    lh = max(1, int(logo.height * (lw / logo.width)))
    logo = logo.resize((lw, lh), Image.LANCZOS)

    m = int(min(W, H) * a.margen)
    top_limit = int(H * a.safe_top) + m if a.safe_top else m
    bottom_limit = H - (int(H * a.safe_bottom) + m) if a.safe_bottom else H - m

    vert, horiz = a.pos.split("-")
    x = m if horiz == "left" else (W - lw - m if horiz == "right" else (W - lw) // 2)
    y = top_limit if vert == "top" else bottom_limit - lh

    ad.alpha_composite(logo, (x, y))
    ad.convert("RGB").save(a.salida)
    print(f"logo compuesto en {a.pos} -> {a.salida} ({W}x{H}, logo {lw}x{lh} @ {x},{y})")


if __name__ == "__main__":
    main()
