from PIL import Image, ImageDraw
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TILE = 16

def zoom(path, c0, r0, c1, r1, scale=7, out=None):
    src = Image.open(path).convert('RGBA')
    w = (c1-c0)*(TILE*scale+1)+1
    h = (r1-r0)*(TILE*scale+1)+1
    img = Image.new('RGBA', (w, h), (10,10,10,255))
    d = ImageDraw.Draw(img)
    for r in range(r0, r1):
        for c in range(c0, c1):
            t = src.crop((c*TILE, r*TILE, (c+1)*TILE, (r+1)*TILE))
            t = t.resize((TILE*scale, TILE*scale), Image.NEAREST)
            x, y = (c-c0)*(TILE*scale+1)+1, (r-r0)*(TILE*scale+1)+1
            img.paste(t, (x,y), t)
            d.rectangle([x-1,y-1,x+TILE*scale,y+TILE*scale], outline=(70,70,70))
            d.text((x+2,y+2), f"{c},{r}", fill=(255,255,0,220))
    if out: img.save(out); print(f"saved {out}")

fw = 'assets/TopDownHouse_FloorsAndWalls.png'
f1 = 'assets/TopDownHouse_FurnitureState1.png'
dw = 'assets/TopDownHouse_DoorsAndWindows.png'

zoom(fw, 0, 0, 18, 9, out='assets/_z_floors_full.png')   # full floors sheet
zoom(f1, 0, 0, 13, 4, out='assets/_z_tables_chairs.png') # top of furniture (tables/chairs)
zoom(f1, 0, 10, 13, 16, out='assets/_z_kitchen.png')     # kitchen area
zoom(dw, 6, 0, 18, 10, out='assets/_z_doors.png')        # doors + windows
