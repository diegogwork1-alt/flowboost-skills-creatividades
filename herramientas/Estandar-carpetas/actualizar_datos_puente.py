#!/usr/bin/env python3
"""Actualiza la pestaña `datos` de la hoja de un cliente SIN regenerar el libro.

CÓMO ESCRIBE (desde el 24-09-2026): por el PUENTE de Apps Script del panel (acciones `leerDatos`
y `escribirDatos`), fila a fila y solo las filas que cambian. Antes bajaba la hoja como .xlsx y la
volvía a subir ENTERA a Drive: lo que Equipo apuntara mientras tanto se perdía. Eso ya no pasa.
URL y secreto del puente: Llavero de macOS, servicio «panel-flowboost» (APPS_SCRIPT_URL,
APPS_SCRIPT_SECRET). Copia del código anterior: actualizar_datos.py.bak-antes-puente.

POR QUÉ EXISTE: `montar_hoja_reportes.py` rehace el libro entero, así que sobre una hoja en
uso borra los cierres, los importes a mano y `datos-google`. Esto hace lo que hace n8n cada
mañana —escribir filas en `datos` y corregir las que ya estaban— pero desde aquí, con los
datos que trae el MCP de Meta. No hace falta META_TOKEN.

QUÉ TOCA Y QUÉ NO: escribe **solo** las celdas de la pestaña `datos`. Las pestañas de
reporte son fórmulas que leen de ahí, así que se recalculan solas. `ventas`, `datos-google`
y todo lo escrito a mano se quedan como estaban.

La clave es `id` = «fecha|campaña», igual que en el flujo: un día que ya estaba se CORRIGE
en su sitio, no se duplica. Por eso se puede reescribir la misma ventana todos los días.

Uso:  actualizar_datos.py <sheet_id> <datos.json> [--dry]
"""
import json, os, subprocess, sys, tempfile, time, urllib.error, urllib.parse, urllib.request
sys.path.insert(0, os.path.expanduser(
    "~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas"))
from subir_a_drive import token
from montar_hoja_reportes import DATOS, EUR, ENT, PCT, DEC2, SUAVE, GRIS, NEGRO

XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
FMTS = [None, None, None, None, EUR, ENT, ENT, DEC2, EUR, ENT, ENT, PCT, ENT, ENT, None]


def bajar(sheet_id, destino):
    u = (f"https://www.googleapis.com/drive/v3/files/{sheet_id}/export?"
         + urllib.parse.urlencode({"mimeType": XLSX}))
    for i in range(6):
        try:
            r = urllib.request.urlopen(urllib.request.Request(
                u, headers={"Authorization": "Bearer " + token(refrescar=(i > 0))}))
            open(destino, "wb").write(r.read()); return
        except Exception as e:
            err = e; time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"no se pudo exportar la hoja: {err}")


def filas_del_json(p):
    """El mismo formato que come `montar_hoja_reportes.py --datos`."""
    d = json.load(open(p)); camps = d["campanas"]
    out = []
    for f in sorted(d["filas"], key=lambda x: (x[0], x[1])):
        nom = camps[f[1]]["nombre"]
        out.append([f"{f[0]}|{nom}", f[0], d["cliente"], nom, f[2], f[3], f[7], f[8],
                    f[9], f[4], f[5], f[10] / 100, f[6], f[11], "MCP " +
                    time.strftime("%Y-%m-%d %H:%M")])
    return out



def _igual(a, b):
    """¿El mismo valor, venga como venga de la hoja?"""
    if a is None: a = 0 if isinstance(b, (int, float)) else ""
    if isinstance(b, (int, float)):
        try: return abs(float(a) - float(b)) < 5e-5
        except (TypeError, ValueError): return False
    return str(a).strip() == str(b).strip()


def _distintas(a, b):
    return any(not _igual(x, y) for x, y in zip(a, b))


def _detalle(antes, fila):
    return "; ".join(f"{DATOS[i]}: {antes[i]}→{fila[i]}"
                     for i in range(len(DATOS) - 1) if not _igual(antes[i], fila[i]))



def _secreto(nombre):
    r = subprocess.run(["security", "find-generic-password", "-s", "panel-flowboost", "-a", nombre, "-w"],
                       capture_output=True, text=True)
    if not r.stdout.strip(): sys.exit(f"✗ no encuentro {nombre} en el Llavero (servicio panel-flowboost)")
    return r.stdout.strip()


def puente(accion, **cuerpo):
    """Llama al Apps Script «Puente panel Flowboost». Nunca imprime el secreto."""
    url, secreto = _secreto("APPS_SCRIPT_URL"), _secreto("APPS_SCRIPT_SECRET")
    datos = json.dumps({**cuerpo, "accion": accion, "secreto": secreto}).encode()
    err = None
    for i in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, data=datos, method="POST",
                headers={"content-type": "text/plain"}), timeout=300)
            d = json.load(r)
            if d.get("error"): sys.exit(f"✗ el puente de hojas dice: {d['error']}")
            return d
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            err = e; time.sleep(3 * (i + 1))
    sys.exit(f"✗ el puente de hojas no responde: {err}")


def _mismo_cliente(existentes, filas, cols):
    """⛔ Impide escribir los datos de un cliente en la hoja de OTRO.

    `armar_datos.py` lee todos los volcados que encuentre, y en una pasada de varios
    clientes todos caen en la misma carpeta: sin esto, el segundo cliente arrastraría las
    campañas del primero y acabarían en la hoja equivocada, sin un solo error. Dos
    comprobaciones contra lo que YA hay escrito en la hoja:
      · el nombre de cliente tiene que ser el mismo;
      · y alguna campaña nueva tiene que existir ya ahí (una hoja viva nunca cambia de
        campañas de un día para otro). Si no se parecen en nada, es otro cliente.
    """
    ic, icam = cols["cliente"] - 1, cols["campana"] - 1
    clientes_hoja = {str(f[ic]).strip() for f in existentes if f[ic]}
    camp_hoja = {str(f[icam]).strip() for f in existentes if f[icam]}
    if not clientes_hoja:
        return []                                  # hoja vacía: nada que contrastar
    nuevos = {str(f[ic]).strip() for f in filas}
    camp_nuevas = {str(f[icam]).strip() for f in filas}
    fallos = []
    if nuevos - clientes_hoja:
        fallos.append(f"la hoja es de «{'», «'.join(sorted(clientes_hoja))}» y los datos "
                      f"traen «{'», «'.join(sorted(nuevos))}»")
    if camp_hoja and not (camp_nuevas & camp_hoja):
        fallos.append(f"ninguna de las {len(camp_nuevas)} campañas de los datos está en esta "
                      f"hoja (que tiene {len(camp_hoja)}): parecen de otra cuenta")
    return fallos


def main():
    sheet_id, datos_json = sys.argv[1], sys.argv[2]
    dry = "--dry" in sys.argv
    hoja = puente("leerDatos", sheet=sheet_id)      # el puente ya comprueba la pestaña y el orden de columnas
    if hoja.get("cabecera") != DATOS:
        sys.exit(f"✗ el orden de columnas de `datos` no es el esperado.\n"
                 f"  puente: {hoja.get('cabecera')}\n  script: {DATOS}")
    existentes = [[None if v == "" else v for v in f] for f in hoja["filas"]]

    filas_nuevas = filas_del_json(datos_json)
    cols = {n: i + 1 for i, n in enumerate(DATOS)}
    fallos = _mismo_cliente(existentes, filas_nuevas, cols)
    if fallos:
        sys.exit("✗ NO se escribe nada: estos datos no son de esta hoja.\n"
                 + "".join(f"   · {f}\n" for f in fallos))

    # índice de lo que ya hay, por `id` (fila 2 = la primera de datos)
    donde = {str(f[0]): i + 2 for i, f in enumerate(existentes) if f[0]}

    cambios, nuevas, iguales, detalle = [], [], 0, []
    for fila in filas_nuevas:
        r = donde.get(fila[0])
        if r:
            antes = existentes[r - 2]
            # Se compara sin la marca de tiempo (última columna), que siempre cambia, y
            # NUMÉRICAMENTE: lo que vuelve de la hoja es float («1855.0») y lo nuevo int («1855»).
            if not _distintas(antes[:-1], fila[:-1]):
                iguales += 1; continue
            cambios.append({"fila": r, "id": fila[0], "valores": fila})
            detalle.append((fila[0], _detalle(antes, fila)))
        elif fila[0] not in {n[0] for n in nuevas}:
            nuevas.append(fila)

    print(f"  filas nuevas: {len(nuevas)} · corregidas: {len(cambios)} · sin cambios: {iguales}")
    for id_, det in detalle[:12]:
        print(f"    · {id_}  {det}")
    if len(detalle) > 12: print(f"    … y {len(detalle)-12} más")
    if dry:
        print("  (--dry: no se ha escrito nada)"); return
    if not nuevas and not cambios:
        print("  ya estaba al día: no se escribe nada"); return

    # '@' = texto: la fecha y el id TIENEN que seguir siendo texto (los reportes comparan
    # datos!B con «>="2026-09-01"»; si Sheets la convirtiera en fecha, los totales darían 0).
    formatos = [f or "@" for f in FMTS]
    r = puente("escribirDatos", sheet=sheet_id, cambios=cambios, nuevas=nuevas, formatos=formatos)
    print(f"  ✓ escrito por el puente: {r['nuevas']} nuevas, {r['corregidas']} corregidas "
          f"(solo la pestaña `datos`) · https://docs.google.com/spreadsheets/d/{sheet_id}/edit")


if __name__ == "__main__":
    main()
