from PIL import Image, ImageDraw
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TILE = 16
scale = 5

def labeled_grid(path, outfile):
    src = Image.open(path).convert('RGBA')
    cols = src.width // TILE
    rows = src.height // TILE
    out = Image.new('RGBA', (cols*(TILE*scale+1)+1, rows*(TILE*scale+1)+1), (10,10,10,255))
    draw = ImageDraw.Draw(out)
    for r in range(rows):
        for c in range(cols):
            tile = src.crop((c*TILE, r*TILE, (c+1)*TILE, (r+1)*TILE))
            tile = tile.resize((TILE*scale, TILE*scale), Image.NEAREST)
            x = c*(TILE*scale+1)+1
            y = r*(TILE*scale+1)+1
            out.paste(tile, (x, y), tile)
            draw.rectangle([x-1, y-1, x+TILE*scale, y+TILE*scale], outline=(60,60,60))
            draw.text((x+1, y+1), f"{c},{r}", fill=(255,255,0,200))
    out.save(outfile)
    print(f"saved {outfile}")

labeled_grid('assets/TopDownHouse_FloorsAndWalls.png',   'assets/_grid_floors.png')
labeled_grid('assets/TopDownHouse_FurnitureState1.png',  'assets/_grid_furn1.png')
labeled_grid('assets/TopDownHouse_DoorsAndWindows.png',  'assets/_grid_doors.png')
labeled_grid('assets/TopDownHouse_SmallItems.png',       'assets/_grid_small.png')
