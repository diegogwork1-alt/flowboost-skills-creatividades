#!/usr/bin/env python3
"""Reescribe la sección de recuento del README de refs/ con lo que hay DE VERDAD.

El README decía 74 piezas cuando había 94, y su tabla por carpeta no cuadraba en 7 de 11 filas.
Se corre después de añadir o quitar referencias:  python3 contar_refs.py
"""
import os, re, collections

AQUI = os.path.dirname(os.path.abspath(__file__))
EXT = (".png", ".jpg", ".jpeg", ".webp")
NOTAS = {"00_9x16-verticales": "verticales de referencia para medir la deriva del 9:16",
         "10_tres-pasos": "formato maestro de la casa, fuera de la secuencia de 9"}

def main():
    por_carpeta, por_cliente = {}, collections.Counter()
    for d in sorted(os.listdir(AQUI)):
        if not os.path.isdir(os.path.join(AQUI, d)): continue
        fs = [f for f in os.listdir(os.path.join(AQUI, d)) if f.lower().endswith(EXT)]
        por_carpeta[d] = len(fs)
        for f in fs:
            por_cliente[f.split("_")[0]] += 1
    total = sum(por_carpeta.values())
    aprob = sum(n for c, n in por_cliente.items() if "APROBADO" in c)
    dubai = sum(n for c, n in por_cliente.items() if "Dubai" in c or "Dubái" in c)

    filas = "\n".join(f"| `{d}` | {n}" + (f" ({NOTAS[d]})" if d in NOTAS else "") + " |"
                      for d, n in por_carpeta.items())
    bloque = (f"## Contenido ({total} piezas)\n"
              f"- **{total - aprob - dubai} estáticos REALES ya publicados** de clientes de Flowboost, "
              f"sacados de sus Drives y revisados uno a uno.\n"
              f"- **{aprob} piezas APROBADAS por Dirección** (`*-APROBADO_<formato>_<1x1|9x16>.jpg`) → son el "
              f"estándar visual al que hay que parecerse.\n"
              + (f"- **{dubai} piezas de Flowboost Dubái**, la tanda más reciente.\n" if dubai else "")
              + f"\n| Carpeta | Piezas |\n|---|---|\n{filas}\n\n"
              f"*Recuento regenerado con `contar_refs.py`. Si editás la carpeta, volvé a correrlo.*\n")

    p = os.path.join(AQUI, "README.md")
    t = open(p, encoding="utf-8").read()
    ini = t.index("## Contenido")
    fin = t.find("\n## ", ini + 5)
    t = t[:ini] + bloque + (t[fin + 1:] if fin != -1 else "")
    open(p, "w", encoding="utf-8").write(t)
    print(f"README actualizado: {total} piezas en {len(por_carpeta)} carpetas")
    print("  clientes:", ", ".join(f"{c} ({n})" for c, n in por_cliente.most_common(6)))

if __name__ == "__main__":
    main()
