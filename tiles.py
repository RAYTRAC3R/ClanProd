from pytmx.util_pygame import load_pygame

class Tileset:
    def __init__(self, file, xnum, ynum):
        self.file = file
        self.xnum = xnum
        self.ynum = ynum
        self.images = {}
        self.get_images()
        
    def get_images(self):
        tiled_map = load_pygame(self.file)
        z = 1
        for x in range(self.xnum):
            for y in range(self.ynum):
                self.save_image(tiled_map.get_tile_image(x, y, 0), z)
                z = z + 1
                
    def save_image(self, image, name):
        self.images[name] = image