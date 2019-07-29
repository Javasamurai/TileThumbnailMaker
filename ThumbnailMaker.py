from PIL import Image
import json

img = [None] * 5

# Offset to put thumbnails x and y pos
offset = (30, 13)

# final_img = Image.new("RGB", size, (255,255,255))
final_img = Image.open("Tiles/bg_green.png")

base_img = Image.open("Tiles/base.png")
base_img.thumbnail((40, 40))


def create_thumbnail(data):
        level = data["LevelData"].split(",")
        name = data["Id"]
        level_img = final_img.copy()
        thumbnail_size = 19

        for r in range(0, 26):
                for c in range(0, 26):
                        pointer = int(level[r * 26 + c] )
                        if (pointer!= 0) :
                                level_img.paste( img[pointer], ((c * thumbnail_size) + offset[0], (r * thumbnail_size) + offset[1]))
                        if (r == 24 and c == 12):
                                level_img.paste( base_img, ( (c * thumbnail_size) + offset[0], (r * thumbnail_size) + offset[1]) )

        level_img.save('thumbnail' + name +'.png')
        level_img.show()


with open('Data.json') as json_data:
        thumbnail_size = 19
        for i in range(1, 5):
                img[i] = Image.open("Tiles/" + str(i) + ".png")
                img[i].thumbnail( (thumbnail_size, thumbnail_size) )
        pass
        json_data = json.load(json_data)
        level_data = json_data["TankLevels"]

        
        for data in level_data:
                create_thumbnail(data)
        pass
