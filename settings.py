import pygame as pg
import random
pg.init()
tilesize = 32
width = 1024
height = 700
fps = 60
title = "Morshot"
blue = (0,0,100)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)
speed = 5

all_sprite = pg.sprite.Group()
mobs = pg.sprite.Group()
bullets = pg.sprite.Group()
bosses = pg.sprite.Group()

global score

#loading effect
effects = {}
effects['lg'] = []
effects['sm'] = []
for i in range(10):
    filename = 'effect{}.png'.format(i)
    img = pg.image.load(filename)
    img.set_colorkey(black)
    img_sm = pg.transform.scale(img,(45,45))
    effects['sm'].append(img_sm)

    img_lg = pg.transform.scale(img,(200,200))
    effects['lg'].append(img_lg)
