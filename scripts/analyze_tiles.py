from PIL import Image, ImageDraw
import os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

v = Image.open('assets/tileset_village_abandoned.png').convert('RGBA')
TILE = 16

def show_region(src, c0, r0, c1, r1, scale=8, outfile=None):
    w = (c1-c0)*(TILE*scale+1)+1
    h = (r1-r0)*(TILE*scale+1)+1
    out = Image.new('RGBA', (w, h), (10,10,10,255))
    draw = ImageDraw.Draw(out)
    for r in range(r0, r1):
        for c in range(c0, c1):
            tile = src.crop((c*TILE, r*TILE, (c+1)*TILE, (r+1)*TILE))
            tile = tile.resize((TILE*scale, TILE*scale), Image.NEAREST)
            x = (c-c0)*(TILE*scale+1)+1
            y = (r-r0)*(TILE*scale+1)+1
            out.paste(tile, (x, y), tile)
            draw.rectangle([x-1, y-1, x+TILE*scale, y+TILE*scale], outline=(80,80,80))
            draw.text((x+1, y+1), f"{c},{r}", fill=(255,255,0,200))
    if outfile: out.save(outfile); print(f"saved {outfile}")
    return out

show_region(v, 0, 5, 5, 12, outfile='assets/tree_tiles.png')
show_region(v, 16, 7, 20, 12, outfile='assets/small_house.png')
