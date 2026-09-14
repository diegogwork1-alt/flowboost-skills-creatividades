#!/usr/bin/env python3
"""
Render de estáticos Flowboost: rellena una plantilla HTML con los tokens de la
hoja de especificación, ENFORZA las safe zones de Meta y exporta a PNG.

Uso:
  python3 render.py <plantilla.html> <datos.json> <salida.png> [--size cuadrado|story|WxH] [--guides]
                    [--permitir-vacios TOKEN1,TOKEN2]

TOKENS: **ausente = error (sale con código 1); cadena vacía = decisión tomada.** Antes un JSON
incompleto renderizaba la pieza con los huecos en blanco y decía OK: una tanda podía subirse al
Drive sin titular y con el botón vacío. Si un hueco tiene que ir vacío, va en el JSON como "".

Los DOS tamaños de la casa (se suben a TODAS las ubicaciones):
- cuadrado = 1080x1080 (1:1)  → safe: 5% margen en los 4 lados (54px)
- story    = 1080x1920 (9:16) → safe: 270px arriba (14%), 384px abajo (20%), 107px lados
             (107 = margen de composición de la casa; 65px es el mínimo técnico, no el objetivo)
- story35  = igual pero 672px abajo (35%) — solo Reels-safe extremo
- Tokens en la plantilla: {{CLAVE}}; datos.json es {"CLAVE":"valor", ...}.
- --guides dibuja las zonas muertas y el área segura para revisión visual (QA).
- Requiere Google Chrome / Chromium (headless). Foto de fondo: pasar {{PHOTO_BG}}
  como ruta file:// o data URI para fiabilidad offline.
"""
import json, sys, subprocess, tempfile, os, shutil, re

# (w, h, safe_top, safe_bottom, safe_x) — safe zones de los informes de Dirección
SIZES = {
    "cuadrado": (1080, 1080, 54,  54,  54),
    "1x1":      (1080, 1080, 54,  54,  54),
    # 9:16 zona de trabajo Stories (Meta mar-2026: 14% arriba / 20% abajo / 6% lados).
    # El CTA debe quedar por encima del 20%. Para cobertura Reels extrema usar bottom=672 (35%).
    # Laterales a 107, NO a 65: 107 es el margen de composición de la casa (medido en las
    # piezas aprobadas, refs/00_9x16-verticales/LEEME.md) y 65 es solo el mínimo técnico que no
    # se puede cruzar. Inyectar 65 hacía que el plan B saliera siempre apretado y "legal".
    "story":    (1080, 1920, 270, 384, 107),
    "9x16":     (1080, 1920, 270, 384, 107),
    "story35":  (1080, 1920, 270, 672, 107),
}

def find_chrome():
    for c in [
        "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]:
        if shutil.which(c) or os.path.exists(c):
            return c
    sys.exit("No se encontró Chrome/Chromium para renderizar.")

def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    tpl, data_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    guides = "--guides" in sys.argv
    size = "cuadrado"
    if "--size" in sys.argv:
        size = sys.argv[sys.argv.index("--size") + 1]

    if size in SIZES:
        w, h, st, sb, sx = SIZES[size]
    else:  # WxH custom → safe 5%
        w, h = (int(x) for x in size.lower().split("x"))
        st = sb = round(h * 0.05); sx = round(w * 0.05)

    html = open(tpl, encoding="utf-8").read()
    data = json.load(open(data_path, encoding="utf-8"))

    # Las plantillas cargan Anton/Oswald/Playfair de Google Fonts por red. Sin red, Chrome
    # cae al fallback y la pieza sale con OTRA tipografía — sin un solo aviso, con exit 0.
    # Fidelidad de marca es el check 7 del audit: esto no puede pasar callado.
    if "fonts.googleapis.com" in html:
        import socket
        try:
            socket.create_connection(("fonts.googleapis.com", 443), timeout=4).close()
        except OSError:
            print("⚠️  SIN RED: no se pueden cargar las tipografías de Google Fonts "
                  "(Anton/Oswald/Playfair). La pieza saldrá con la tipografía de reserva, "
                  "que NO es la de la marca → NO la apruebes por fidelidad de marca.",
                  file=sys.stderr)

    # dimensiones del canvas (robusto ante cualquier alto por defecto en la plantilla)
    html = re.sub(r"width:1080px;height:\d+px", f"width:{w}px;height:{h}px", html)
    # Inyectar safe zones (sobrescribe el default de la plantilla).
    # Por REGEX y no por literal: antes se sustituía la cadena exacta
    # "--safe-top: 67px; --safe-bottom: 67px; --safe-x: 54px;" y cualquier plantilla que las
    # escribiera con otro espaciado u otros valores (antes-despues.html: "--safe-top:54px;…")
    # se quedaba SIN sustituir y renderizaba con sus defaults. En 9:16 eso saca la pieza con
    # 54/54/54 en vez de 270/384/65: texto dentro de la zona muerta de Stories, que es
    # justamente la restricción DURA de la casa. Y fallaba en silencio.
    html, n_top = re.subn(r"--safe-top:\s*\d+px", f"--safe-top: {st}px", html)
    html, n_bot = re.subn(r"--safe-bottom:\s*\d+px", f"--safe-bottom: {sb}px", html)
    html, n_x = re.subn(r"--safe-x:\s*\d+px", f"--safe-x: {sx}px", html)
    if not (n_top and n_bot and n_x):
        sys.exit(f"⛔ {os.path.basename(tpl)} no declara las tres safe zones "
                 f"(--safe-top/{n_top}, --safe-bottom/{n_bot}, --safe-x/{n_x}). "
                 f"Sin ellas la pieza sale con el texto en la zona muerta. "
                 f"Añádelas al :root de la plantilla.")

    # Clase de tamaño en el <body>: es lo que permite a la plantilla RECOMPONER según el ratio
    # en vez de estirar la misma composición. Sin esto, una maqueta pensada para 4:5 puesta en
    # 1080x1920 deja el contenido arriba y abre un agujero de 600-840 px antes del CTA
    # (`.cta{margin-top:auto}`), que es lo que el medidor cazaba como «hueco interior».
    clase = {"cuadrado": "size-cuadrado", "1x1": "size-cuadrado",
             "story": "size-story", "9x16": "size-story", "story35": "size-story"}.get(size, "size-libre")
    # El patrón 9:16 de la casa es «texto arriba, FOTO A SANGRE abajo». Si no hay foto, la mitad
    # inferior se queda muerta: entonces el contenido se reparte por toda la altura en vez de
    # apelotonarse arriba. Los formatos sin foto existen (8 Prueba social va sobre fondo sobrio).
    if clase == "size-story" and not str(data.get("PHOTO_BG", "")).strip():
        clase += " sin-foto"
        print("ℹ️  9:16 sin PHOTO_BG: el contenido se reparte por toda la altura (el patrón de la "
              "casa lleva foto a sangre abajo; sin ella, apelotonar arriba deja el tercio inferior "
              "muerto).", file=sys.stderr)
    html = html.replace("<body", f"<body class='{clase}'", 1)

    # guías de QA
    if guides:
        html = html.replace(f"<body class='{clase}'", f"<body class='{clase} show-guides'", 1)
        zones = (f"<div class='z' style='top:0;height:{st}px'></div>"
                 f"<div class='z' style='bottom:0;height:{sb}px'></div>")
        data.setdefault("GUIDE_ZONES", zones)
    else:
        data.setdefault("GUIDE_ZONES", "")

    # ---- VALIDACIÓN DE TOKENS (11-09-2026) ----
    # Antes se rellenaba lo que hubiera y el resto se borraba en silencio: con un JSON
    # incompleto salía la pieza SIN titular y con el botón vacío, imprimiendo "OK" y
    # saliendo con código 0. Una tanda podía subirse al Drive mutilada sin un solo aviso.
    # Semántica nueva: **token ausente = error; token con cadena vacía = decisión tomada.**
    INTERNOS = {"GUIDE_ZONES"}
    declarados = set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", html)) - INTERNOS
    dados = set(data) - INTERNOS
    faltan = sorted(declarados - dados)
    sobran = sorted(dados - declarados)
    permitidos = set()
    if "--permitir-vacios" in sys.argv:
        permitidos = {x.strip() for x in sys.argv[sys.argv.index("--permitir-vacios") + 1].split(",")}
    faltan = [f for f in faltan if f not in permitidos]
    if sobran:
        print(f"⚠️  {os.path.basename(data_path)} trae claves que la plantilla NO usa "
              f"(¿nombre equivocado?): {', '.join(sobran)}", file=sys.stderr)
    if faltan:
        sys.exit(f"⛔ Faltan {len(faltan)} token(s) de {os.path.basename(tpl)} en "
                 f"{os.path.basename(data_path)}: {', '.join(faltan)}\n"
                 f"   La pieza saldría con esos huecos VACÍOS y antes se guardaba igual, con un OK.\n"
                 f"   Si alguno tiene que ir vacío a propósito, ponlo en el JSON con \"\" "
                 f"o pásalo en --permitir-vacios {','.join(faltan)}")

    # El logo va como IMAGEN. Recomponer la marca con tipografía es un error que Dirección ya
    # corrigió dos veces: el modelo/la plantilla "dibuja" el nombre y deja de ser el logo.
    if "{{LOGO_SRC}}" in html and not str(data.get("LOGO_SRC", "")).strip():
        if "--sin-logo" not in sys.argv:
            sys.exit("⛔ LOGO_SRC vacío: la pieza saldría con el nombre de la marca escrito en la "
                     "tipografía de la plantilla — eso NO es el logo, y es el error que Dirección ya "
                     "corrigió dos veces.\n"
                     "   Pasa la ruta del PNG oficial (`Insumos/logo/Logotipo-*.png`), o compón el "
                     "logo después con `templates/poner_logo.py`.\n"
                     "   Si la pieza va SIN logo a propósito (advertorial: el masthead sustituye al "
                     "logo, que baja a firma de pie), pásalo explícito con --sin-logo.")
        print("ℹ️  --sin-logo: pieza sin logo a propósito (¿advertorial?).", file=sys.stderr)

    for k, v in data.items():
        html = html.replace("{{" + k + "}}", str(v))
    html = re.sub(r"\{\{[A-Z0-9_]+\}\}", "", html)  # solo quedan los ya validados

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html); filled = f.name

    # Se delega en el renderizador común, que SIEMPRE cierra Chrome (07-09-2026).
    # Antes se hacía subprocess.run(...) sin timeout ni perfil propio: Chrome headless
    # genera el fichero y NO sale, así que cada render dejaba procesos vivos (45 procesos
    # y 2,9 GB en una tanda de pruebas) y el run se quedaba colgado esperándolo.
    import importlib.util
    _rc = os.path.expanduser("~/Desktop/FLOWBOOST-BACKUP-MAC/Documentos-Flowboost/Estandar-carpetas/render_chrome.py")
    if os.path.exists(_rc):
        _sp = importlib.util.spec_from_file_location("render_chrome", _rc)
        _m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
        _m.render(filled, out, size=f"{w},{h}")
    else:  # fallback: mismo comportamiento, con perfil propio y timeout
        import shutil as _sh, signal as _sg, tempfile as _tf, time as _t
        perfil = _tf.mkdtemp(prefix="chrome-render-")
        pr = subprocess.Popen([find_chrome(), "--headless=old", "--disable-gpu", "--hide-scrollbars",
                               f"--user-data-dir={perfil}", "--force-device-scale-factor=1",
                               f"--window-size={w},{h}", f"--screenshot={out}", "file://" + filled],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        try:
            t0 = _t.time()
            while _t.time() - t0 < 45 and not (os.path.exists(out) and os.path.getsize(out) > 0):
                _t.sleep(0.3)
            _t.sleep(0.5)
        finally:
            try:
                os.killpg(os.getpgid(pr.pid), _sg.SIGKILL)
            except Exception:
                pass
            _sh.rmtree(perfil, ignore_errors=True)
    os.unlink(filled)
    print(f"OK → {out} ({w}x{h}){' [con guías]' if guides else ''}")

if __name__ == "__main__":
    main()
