import csv, glob, os, sys

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "playlists")
ok = True
for f in sorted(glob.glob(os.path.join(base, "*.csv"))):
    with open(f, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    keys = [(r["Title"].lower(), r["Artist"].lower()) for r in rows]
    dups = {k for k in keys if keys.count(k) > 1}
    bad = [r for r in rows if not 1990 <= int(r["Year"]) <= 1999]
    name = os.path.basename(f)
    print(f"{name}: {len(rows)} Songs, Duplikate={sorted(dups)}, ausserhalb 1990-1999={[(r['Title'], r['Year']) for r in bad]}")
    if len(rows) != 50 or dups or bad:
        ok = False
    md = os.path.splitext(f)[0] + ".md"
    title = os.path.splitext(name)[0][3:].replace("-", " ").title()
    with open(md, "w", encoding="utf-8") as out:
        out.write(f"# 90er: {title}\n\n| # | Titel | Interpret | Jahr |\n|---|-------|-----------|------|\n")
        for i, r in enumerate(rows, 1):
            out.write(f"| {i} | {r['Title']} | {r['Artist']} | {r['Year']} |\n")
sys.exit(0 if ok else 1)
