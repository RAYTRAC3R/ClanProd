import pygame
from ast import literal_eval
from os import path
import sys
import os
import random
from pygame.locals import *

from world import *
from tiles import *

W = 1280
H = 720
SIZE = W, H
TILESIZE = 16
WORLDSIZE = 80
screen = pygame.display.set_mode(SIZE, pygame.HWSURFACE)
pygame.display.set_caption("ClanProd")

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("ClanProd")
        self.running = True
        random.seed()
        worldseed = random.randrange(10000)
        print(worldseed)
        terrain = Tileset('tileset/terrain.tmx', 7, 1)
        #tiled_map = load_pygame('tileset/terrain.tmx')
        #tileimage = tiled_map.get_tile_image(0, 0, 0)
        world = World((WORLDSIZE,WORLDSIZE),worldseed)
        self.worldmap = pygame.Surface((1280,1280))
        for y in range(45):
            for x in range(WORLDSIZE):
                noisevalue = world.check_noisetile(x,y)
                if noisevalue > 0.01:
                    #buttons.draw_maptile_button((x*TILESIZE,y*TILESIZE),image=(pygame.transform.scale(terrain.images[1],(TILESIZE,TILESIZE))))
                    self.load_image(pygame.transform.scale(terrain.images[1],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                elif noisevalue < -0.01:
                    self.load_image(pygame.transform.scale(terrain.images[2],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                else:
                    self.load_image(pygame.transform.scale(terrain.images[3],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
        for y in range(45):
            for x in range(WORLDSIZE):
                height = world.check_heighttile(x,y)
                if height < 0:
                    self.load_image(pygame.transform.scale(terrain.images[5],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                elif x == 0:
                    self.load_image(pygame.transform.scale(terrain.images[5],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                elif x == 79:
                    self.load_image(pygame.transform.scale(terrain.images[5],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                elif y == 0:
                    self.load_image(pygame.transform.scale(terrain.images[5],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                elif y == 44:
                    self.load_image(pygame.transform.scale(terrain.images[5],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                elif height < 0.03:
                    self.load_image(pygame.transform.scale(terrain.images[7],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
                elif height > 0.5:
                    self.load_image(pygame.transform.scale(terrain.images[6],(TILESIZE,TILESIZE)),x*TILESIZE,y*TILESIZE)
        self.draw_map(self.worldmap, 0, 0)
        

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                #elif event.type == MOUSEWHEEL:
                    

    def load_image(self, file, x,y):
        self.file = file
        self.image = file
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        #self.rect[2] = self.rect[2]/2
        #self.rect[3] = self.rect[3]/2
        self.rect[0] = self.rect[0] + self.x
        self.rect[1] = self.rect[1] + self.y
        self.rect[2] = self.rect[2] + self.x
        self.rect[3] = self.rect[3] + self.y
        #print(self.rect)

        #self.screen = pygame.display.set_mode(self.rect.size)
        #pygame.display.set_caption(f'size:{self.rect.size}')
        self.worldmap.blit(self.image, self.rect)
        
    def draw_map(self,gamemap,x,y):
        self.gamemap = gamemap
        self.x = x
        self.y = y
        self.screen.blit(self.gamemap, (self.x,self.y))
        pygame.display.update()
        
class Mouse(object):
    used_screen = pygame.Surface((1280,1280))

    def __init__(self):
        self.pos = (0, 0)

    def check_pos(self):
        self.pos = pygame.mouse.get_pos()

mouse = Mouse()
        
game = Game()