import math
from noise import snoise2
import numpy as np

class World:
    def __init__(self, shape, seed):
        self.shape = shape
        self.seed = seed
        self.main_noisemap = self.generate_noisemap(self.seed, 5)
        self.heightmap = self.generate_noisemap(self.seed + self.seed, 20)

    def generate_noisemap(self, seed, scale):
        noisetile = np.zeros(self.shape)
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                noisetile[x][y] = snoise2(x/scale, y/scale, octaves=6, persistence = 0.5, lacunarity = 2.0, base=seed, repeatx=80,repeaty=80)
        world_noise = np.zeros_like(noisetile)
        
        center_x, center_y = self.shape[1] // 2, self.shape[0] // 2
        circle_grad = np.zeros_like(noisetile)

        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                distx = abs(x - center_x)
                disty = abs(y - center_y)
                dist = math.sqrt(distx*distx + disty*disty)
                circle_grad[y][x] = dist

        # get it between -1 and 1
        max_grad = np.max(circle_grad)
        circle_grad = circle_grad / max_grad
        circle_grad -= 0.5
        circle_grad *= 2.0
        circle_grad = -circle_grad
        #toimage(circle_grad).show()

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                world_noise[i][j] = (noisetile[i][j] * circle_grad[i][j])
                if world_noise[i][j] > 0:
                    world_noise[i][j] *= 20

        # get it between 0 and 1
        max_grad = np.max(world_noise)
        world_noise = world_noise / max_grad
        #toimage(noisetile).show()
        #toimage(world_noise).show()
        return world_noise

    def check_noisetile(self, x, y):
        return self.main_noisemap[x][y]
    
    def check_heighttile(self, x, y):
        return self.heightmap[x][y]
    
#world = World((80,80),63)

#noise_array = np.asarray(world.generate_noisemap(0, 20))
#toimage(noise_array).show()