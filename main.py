import pygame
import pygame_gui

import random
from world import *
from tiles import *

def load_map(world, terrain):
    for y in range(45):
        for x in range(WORLDSIZE):
            noisevalue = world.check_noisetile(x,y)
            if noisevalue > 0.01:
                load_image(pygame.transform.scale(terrain.images[1],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
            elif noisevalue < -0.01:
                load_image(pygame.transform.scale(terrain.images[2],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
            else:
                load_image(pygame.transform.scale(terrain.images[3],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
    for y in range(45):
        for x in range(WORLDSIZE):
            height = world.check_heighttile(x,y)
            if height < SEALEVEL:
                load_image(pygame.transform.scale(terrain.images[5],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
            elif height < BEACHLEVEL:
                load_image(pygame.transform.scale(terrain.images[7],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
            elif height > 0.5:
                load_image(pygame.transform.scale(terrain.images[6],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)

def load_image(file, x,y):
    image = file
    rect = image.get_rect()
    #rect[2] = rect[2]/2
    #rect[3] = rect[3]/2
    rect[0] = rect[0] + x
    rect[1] = rect[1] + y
    rect[2] = rect[2] + x
    rect[3] = rect[3] + y
    #print(rect)

    #self.screen = pygame.display.set_mode(rect.size)
    #pygame.display.set_caption(f'size:{rect.size}')
    worldmap.blit(image, rect)
        
def draw_map(gamemap,x,y):
    window_surface.blit(gamemap, (x,y))

pygame.init()

W = 1280
H = 720
SIZE = W, H
TILESIZE = 16
WORLDSIZE = 80
SEALEVEL = -0.008
BEACHLEVEL = 0.002 + SEALEVEL
print("beach height is " + str(BEACHLEVEL))
pygame.display.set_caption("ClanProd")

window_surface = pygame.display.set_mode((1280, 720))

background = pygame.Surface((560, 720))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((560, 720))

regen_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 200), (250, 50)),
                                             text='Regenerate',
                                             manager=manager)
save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 300), (250, 50)),
                                             text='Print Seed',
                                             manager=manager)

clock = pygame.time.Clock()
is_running = True

random.seed()
worldseed = random.randrange(999999)
#print(worldseed) # print world seed
terrain = Tileset('tileset/terrain.tmx', 7, 1) # load tileset for terrain
world = World((WORLDSIZE,WORLDSIZE),worldseed) # init world
worldmap = pygame.Surface((720,720))
load_map(world, terrain)
draw_map(worldmap, 560, 0)

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == regen_button:
                worldseed = random.randrange(999999)
                #print(worldseed) # print world seed
                terrain = Tileset('tileset/terrain.tmx', 7, 1) # load tileset for terrain
                world = World((WORLDSIZE,WORLDSIZE),worldseed) # init world
                worldmap = pygame.Surface((720,720))
                load_map(world, terrain)
                draw_map(worldmap, 560, 0)
            elif event.ui_element == save_button:
                print(worldseed)
        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()