#!/usr/bin/env python3
"""Los anuncios de los últimos 7 días de cada cliente, de MEJOR a PEOR, con sus métricas → panel.

Sin META_TOKEN: los datos los pide al MCP de Meta el agente de la rutina diaria de las 8 y los deja
en `top-anuncios/entrada/` (junto a este fichero). Este script solo ORDENA y ENVÍA.

  1. top_anuncios.py --cuentas      → qué cuentas pedir y el rango (los 7 días hasta ayer)
  2. (agente) ads_get_ad_entities nivel `ad` por cuenta, con los CAMPOS de abajo → entrada/ads-<cuenta>.json
  3. top_anuncios.py --elegir       → la clasificación de cada cuenta y los creative_id que faltan
  4. (agente) ads_get_creatives + ads_get_ad_videos → entrada/creativos-<cuenta>.json,
     entrada/videos-<cuenta>.json
  4b'. (agente) ads_get_ad_entities nivel `ad`, time_increment 1, 14 días → entrada/diario-<cuenta>.json
       (la evolución diaria de cada anuncio: de ahí sale la FATIGA)
  4b''. (agente) ads_account_get_activity_logs, 30 días → entrada/logs-<cuenta>.json
       (el HISTORIAL DE CAMBIOS: pausas, presupuestos, anuncios nuevos)
  5. top_anuncios.py --enviar       → baja las imágenes y lo manda al panel, con fatiga e historial

CAMPOS que pide el agente (nivel ad, filtro gasto > 0, el rango que da --cuentas):
  id, name, effective_status, campaign_name, creative_id, amount_spent, impressions, reach, frequency, link_click, ctr, cpm,
  cost_per_link_click, outbound_clicks, outbound_clicks_ctr, video_continuous_2_sec_watched_actions,
  video_thruplay_watched_actions, video_p25_watched_actions, video_p50_watched_actions,
  video_p75_watched_actions, video_p100_watched_actions, video_avg_time_watched_actions, results,
  preview_shareable_link (la vista previa del anuncio EXACTO: el botón «Ver anuncio» del panel)

LOS CUATRO SCORES (0-100) comparan cada anuncio con el RESTO de anuncios del mismo cliente esa
semana (percentil), no con una media del sector que nadie ha medido:
  · Gancho     = reproducciones de 2 s seguidos ÷ impresiones  (Meta no da las de 3 s; si
                 deja vacías las de 2 s, se usan las que llegan al 25 % y se marca)
  · Retención  = ThruPlays ÷ impresiones
  · Clic       = CTR saliente
  · Conversión = leads ÷ clics en el enlace
Gancho y retención solo existen en vídeo. Con menos de 3 anuncios comparables no hay score.

CÓMO SE ORDENA (van TODOS los que gastaron, Dirección 24-09-2026): primero los que traen leads, de
más a menos; a igualdad, el de menor coste por lead. Después los que buscan leads y no trajeron
ninguno, de más a menos gasto (los que más queman, arriba). Al final los de otro objetivo
(publicaciones promocionadas que buscan visitas al perfil): no son peores, miden otra cosa.
Solo cuentan los resultados que SON leads (mismas reglas que los reportes). Las campañas que
no gestionamos (`marca_campanas`) quedan fuera, igual que en el reporte.
"""
import base64, datetime, glob, json, os, re, sys, urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from armar_datos import dec, LEAD                  # noqa: el mismo parseo que los reportes
from actualizar_todos import leer_clientes

ENTRADA = os.path.join(AQUI, "top-anuncios", "entrada")
SELECCION = os.path.join(AQUI, "top-anuncios", "seleccion.json")
LEAD_TODOS = LEAD | {"actions:leadgen.other", "actions:lead"}


def semana():
    if "--rango" in sys.argv:                       # para rehacer una semana concreta
        i = sys.argv.index("--rango"); return sys.argv[i + 1], sys.argv[i + 2]
    # Va en la rutina DIARIA de las 8 (Dirección, 24-09-2026): los últimos 7 días completos, hasta ayer.
    ayer = datetime.date.today() - datetime.timedelta(days=1)
    return (ayer - datetime.timedelta(days=6)).isoformat(), ayer.isoformat()


def cargar(p):
    d = json.load(open(p))
    for k in ("ad_entities", "ad_creatives", "ad_videos"):
        if k in d:
            v = d[k]
            return json.loads(v) if isinstance(v, str) else v
    return d if isinstance(d, list) else []


def met(v):
    """Una métrica de Meta: número, cadena, {"value":…} o lista de acciones [{"value":…}]."""
    if isinstance(v, list): return sum(dec(x.get("value")) for x in v if isinstance(x, dict))
    return dec(v)


def percentiles(filas, clave):
    vals = sorted(f[clave] for f in filas if f.get(clave) is not None)
    if len(vals) < 3: return
    for f in filas:
        if f.get(clave) is None: continue
        menores = sum(1 for v in vals if v < f[clave]); iguales = sum(1 for v in vals if v == f[clave])
        f.setdefault("scores", {})[clave] = round(100 * (menores + (iguales - 1) / 2) / (len(vals) - 1))


def leads_de(r, indicador_extra=""):
    res = r.get("results") or {}
    ind = res.get("indicator", "")
    if ind not in LEAD_TODOS and not (indicador_extra and indicador_extra in ind): return 0
    return int(sum(dec(x.get("value")) for x in res.get("values", []) or []))


def elegir():
    d0, d1 = semana(); sel = {}
    for c in leer_clientes():
        p = os.path.join(ENTRADA, f"ads-{c['ad_account_id']}.json")
        if not os.path.exists(p): print(f"· {c['cliente']}: sin volcado de anuncios"); continue
        marca = (c.get("marca_campanas") or "").lower()
        filas = []
        for r in cargar(p):
            camp = str(r.get("campaign_name", ""))
            if marca and marca not in camp.lower(): continue
            gasto = dec(r.get("amount_spent"))
            if gasto <= 0: continue
            n = leads_de(r, c.get("indicador_leads", ""))
            imp = int(met(r.get("impressions"))); clics = int(met(r.get("link_click")))
            v2, thru = met(r.get("video_continuous_2_sec_watched_actions")), met(r.get("video_thruplay_watched_actions"))
            p25, p75, p100 = (met(r.get(f"video_p{x}_watched_actions")) for x in (25, 75, 100))
            es_video = v2 > 0 or thru > 0 or p25 > 0
            salientes = met(r.get("outbound_clicks"))
            filas.append({"ad_id": r["id"], "nombre": r.get("name", ""), "campana": camp,
                          "estado": r.get("effective_status") or None,
                          "creative_id": str(r.get("creative_id", "")), "gasto": round(gasto, 2),
                          "impresiones": imp, "clics": clics, "leads": n,
                          "cpl": round(gasto / n, 2) if n else None,
                          "ctr": clics / imp if imp else None,
                          "ctr_saliente": (salientes / imp) if imp and salientes else (clics / imp if imp else None),
                          "cpc": round(gasto / clics, 2) if clics else None,
                          "cpm": round(gasto / imp * 1000, 2) if imp else None,
                          # Meta a veces deja vacías las de 2 s: entonces, las que llegan al 25 %.
                          "gancho": (v2 or p25) / imp if es_video and imp and (v2 or p25) else None,
                          "gancho_fuente": ("2 s" if v2 else "25 %") if es_video else None,
                          "retencion": thru / imp if es_video and imp else None,
                          "p75": p75 / p25 if es_video and p25 else None,
                          "p100": p100 / p25 if es_video and p25 else None,
                          "tiempo_medio": met(r.get("video_avg_time_watched_actions")) if es_video else None,
                          "conversion": n / clics if clics else None,
                          "frecuencia": round(met(r.get("frequency")), 2) if r.get("frequency") not in (None, "") else None,
                          "busca_leads": (r.get("results") or {}).get("indicator", "") in LEAD_TODOS,
                          # Vista previa del anuncio exacto (Dirección, 25-09-2026). La biblioteca no se
                          # puede filtrar por id de anuncio; esto sí enseña ESE anuncio.
                          "vista_previa": v if (v := str(r.get("preview_shareable_link") or "")).startswith("https://") else None})
        comparables = [f for f in filas if f["gasto"] >= 5]
        for k in ("gancho", "retencion", "ctr_saliente", "conversion"): percentiles(comparables, k)
        con = sorted([f for f in filas if f["leads"]], key=lambda f: (-f["leads"], f["cpl"]))
        # Para completar, solo anuncios que BUSCAN leads (una publicación promocionada que busca
        # visitas al perfil no es un anuncio que «no funcione»: es otro objetivo).
        sin = sorted([f for f in filas if not f["leads"] and f["busca_leads"]], key=lambda f: -f["gasto"])
        otro = sorted([f for f in filas if not f["leads"] and not f["busca_leads"]], key=lambda f: -f["gasto"])
        top = con + sin + otro
        for i, f in enumerate(top, 1): f["puesto"] = i
        sel[c["ad_account_id"]] = {"cliente": c["cliente"], "desde": d0, "hasta": d1, "anuncios": top}
        print(f"{c['cliente']}: {len(top)} anuncios · 1.º {top[0]['nombre'][:45] if top else '—'}"
              + f"\n   creative_ids: {json.dumps([t['creative_id'] for t in top])}")
    os.makedirs(os.path.dirname(SELECCION), exist_ok=True)
    json.dump(sel, open(SELECCION, "w"), ensure_ascii=False, indent=1)


def fatiga(cuenta):
    """Por anuncio: CTR de los últimos 7 días frente a los 7 anteriores, y la serie diaria.
    Fatiga = el CTR cae un 30 % o más (con al menos 500 impresiones en cada tramo) o la
    frecuencia de la semana pasa de 3: la misma gente lo ve demasiado y deja de hacer clic."""
    p = os.path.join(ENTRADA, f"diario-{cuenta}.json")
    if not os.path.exists(p): return {}
    por = {}
    for r in cargar(p):
        por.setdefault(str(r["id"]), []).append((str(r.get("date_start", ""))[:10], met(r.get("impressions")), met(r.get("link_click"))))
    out = {}
    for ad, filas in por.items():
        filas.sort()
        dias = sorted({f[0] for f in filas})
        if len(dias) < 4: continue
        corte = dias[-7] if len(dias) >= 8 else dias[len(dias) // 2]
        ult = [f for f in filas if f[0] >= corte]; ant = [f for f in filas if f[0] < corte]
        iu, cu = sum(f[1] for f in ult), sum(f[2] for f in ult)
        ia, ca = sum(f[1] for f in ant), sum(f[2] for f in ant)
        ctr_u = cu / iu if iu else None; ctr_a = ca / ia if ia else None
        caida = (ctr_a - ctr_u) / ctr_a if ctr_u is not None and ctr_a else None
        out[ad] = {"ctr_ant": ctr_a, "ctr_ult": ctr_u, "caida": caida, "impr_ant": ia, "impr_ult": iu,
                   "serie": [[f[0], round(f[2] / f[1], 5) if f[1] else None] for f in filas]}
    return out


# Del historial de Meta solo interesa lo que cambia resultados: el resto (cobros, estados
# intermedios «Pending Process», revisiones) es ruido.
RUIDO = re.compile(r"billed|after it finishes Ad Review|payment|invoice|funding", re.I)
def historial(cuenta):
    p = os.path.join(ENTRADA, f"logs-{cuenta}.json")
    if not os.path.exists(p): return []
    d = json.load(open(p)); v = d.get("result", d)
    filas = json.loads(v) if isinstance(v, str) else v
    out, vistos = [], set()
    for r in filas or []:
        ev = str(r.get("event_type", ""))
        if RUIDO.search(ev): continue
        try: x = json.loads(r.get("extra_data") or "{}")
        except Exception: x = {}
        antes, despues = x.get("old_value"), x.get("new_value")
        if "Pending Process" in (str(antes), str(despues)): continue
        m = re.match(r"(\d+)/(\d+)/(\d{4}) at (\d+):(\d+)\W*(AM|PM)", str(r.get("datetime", "")).replace("\u202f", " "))
        if not m: continue
        mes, dia, anio, h, mi, ap = m.groups(); h = int(h) % 12 + (12 if ap == "PM" else 0)
        cuando = f"{anio}-{int(mes):02d}-{int(dia):02d}T{h:02d}:{mi}"
        clave = (cuando[:13], r.get("object_id"), ev)
        if clave in vistos: continue
        vistos.add(clave)
        fmt = lambda v: (f"{v / 100:.2f} €".replace(".", ",") if isinstance(v, (int, float)) and "budget" in ev.lower() else str(v)) if v not in (None, "") else ""
        out.append({"cuando": cuando, "quien": r.get("actor_name", ""), "que": ev, "objeto": r.get("object_name", ""),
                    "antes": fmt(antes), "despues": fmt(despues)})
    return out[:300]


def bajar(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 panel-flowboost"})
        r = urllib.request.urlopen(req, timeout=20)
        tipo = r.headers.get("content-type", "image/jpeg").split(";")[0]
        b = r.read()
        return f"data:{tipo};base64," + base64.b64encode(b).decode() if b and tipo.startswith("image/") else None
    except Exception:
        return None


# «Ver en la biblioteca» (Dirección, 25-09-2026): la Biblioteca de anuncios de Meta filtrada por la
# PÁGINA del cliente, no el Administrador de anuncios. Un anuncio suelto no se puede enlazar: la
# biblioteca usa un id propio que no es el del anuncio. La página sale de  del creativo
# (paso 4d); si no viene, del enlace de un vídeo («/<ID_META>/videos/…»); y si tampoco, se
# busca por el nombre del cliente.
BIBLIOTECA = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&media_type=all"
def pagina_de(cre, vid):
    for c in cre.values():
        if str(c.get("actor_id") or "").isdigit(): return str(c["actor_id"])
    for v in vid.values():
        m = re.match(r"/(\d{6,})/videos/", str(v.get("permalink_url", "")))
        if m: return m.group(1)
    return None


def biblioteca(pagina, cliente):
    from urllib.parse import quote
    if pagina: return f"{BIBLIOTECA}&search_type=page&view_all_page_id={pagina}"
    return f"{BIBLIOTECA}&search_type=keyword_unordered&q={quote(cliente)}"


def enviar():
    cfg = json.load(open(os.path.join(AQUI, "panel_sync.json")))
    if not cfg.get("token"):                      # el token vive en el Llavero de macOS
        import subprocess
        cfg["token"] = subprocess.run(["security", "find-generic-password", "-s", "panel-flowboost", "-a", "INGEST_TOKEN", "-w"],
                                      capture_output=True, text=True).stdout.strip()
    sel = json.load(open(SELECCION))
    for cuenta, s in sel.items():
        def leer(n):
            f = os.path.join(ENTRADA, f"{n}-{cuenta}.json")
            return {str(x["id"]): x for x in cargar(f)} if os.path.exists(f) else {}
        cre, vid = leer("creativos"), leer("videos")
        fat = fatiga(cuenta)
        pagina = pagina_de(cre, vid)
        for a in s["anuncios"]:
            f = fat.get(str(a["ad_id"]))
            if f:
                cae = f["caida"] is not None and f["caida"] >= 0.30 and f["impr_ant"] >= 500 and f["impr_ult"] >= 500
                sat = (a.get("frecuencia") or 0) >= 3
                a["fatiga"] = {**f, "nivel": "fatiga" if (cae and sat) or (cae and (f["caida"] or 0) >= 0.5) else "vigilar" if cae or sat else "ok"}
            elif a.get("frecuencia") and a["frecuencia"] >= 3:
                a["fatiga"] = {"nivel": "vigilar", "caida": None, "serie": []}
            c = cre.get(a["creative_id"], {})
            a["tipo"] = "reel" if c.get("object_type") == "VIDEO" or c.get("video_id") else "estatico"
            v = vid.get(str(c.get("video_id", "")), {})
            # La mejor imagen que haya: la del vídeo (160 px), la del estático (completa) o la miniatura (64 px)
            for url in (v.get("picture"), c.get("image_url"), c.get("thumbnail_url")):
                if url and (img := bajar(url)): a["imagen"] = img; break
            a["enlace"] = biblioteca(c.get("actor_id") or pagina, s["cliente"])
        req = urllib.request.Request(cfg["url"].rstrip("/") + "/api/ingest", method="POST",
            data=json.dumps({"cliente": s["cliente"], "top": {"desde": s["desde"], "hasta": s["hasta"],
                                                               "anuncios": s["anuncios"]},
                             "cambios": historial(cuenta)}).encode(),
            headers={"content-type": "application/json", "x-token": cfg["token"], "user-agent": "top_anuncios"})
        try:
            urllib.request.urlopen(req, timeout=60)
            print(f"✓ {s['cliente']}: {len(s['anuncios'])} anuncios, "
                  f"{sum(1 for a in s['anuncios'] if a.get('imagen'))} con imagen")
        except Exception as e:
            print(f"✗ {s['cliente']}: {e}")


if __name__ == "__main__":
    if "--cuentas" in sys.argv:
        d0, d1 = semana(); os.makedirs(ENTRADA, exist_ok=True)
        for f in glob.glob(os.path.join(ENTRADA, "*.json")): os.remove(f)   # nunca mezclar semanas
        print(f"rango: {d0} → {d1}\ncarpeta: {ENTRADA}")
        for c in leer_clientes(): print(f"{c['cliente']}\t{c['ad_account_id']}")
    elif "--elegir" in sys.argv: elegir()
    elif "--enviar" in sys.argv: enviar()
    else: print(__doc__)
