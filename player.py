import pygame as pg
from settings import *
import random

#player speed

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        player_img = pg.image.load("ship1.png")
        
        self.img = pg.transform.scale(player_img,(42,42))
        self.image = self.img
        self.shied = 100

        self.score = 0
        self.laser = pg.mixer.Sound("LASER.wav")

        self.speedx = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height - 10
        self.last_shot = pg.time.get_ticks()
        self.shoot_rate = 250
    def shoot(self):
          now = pg.time.get_ticks()
          if now - self.last_shot > self.shoot_rate:
              self.last_shot = now
              self.bullet = Bullet(self.rect.centerx,self.rect.bottom)
              all_sprite.add(self.bullet)
              bullets.add(self.bullet)
    def keys(self,x=0,y=0):
        speedx = 0 
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT or pg.K_a]:
            self.speedx = 8
            self.rect.x -= self.speedx
            
        if keys[pg.K_RIGHT or pg.K_d]:
            self.speedx = 8
            self.rect.x += self.speedx

        if keys[pg.K_SPACE]:
            self.shoot()
            self.laser.play()

    def update(self):
        self.keys()
        if self.rect.right > width:
              self.rect.right = width
        if self.rect.left < 0:
              self.rect.left = 0
              
              
class Mob(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        mob_img = pg.image.load("ship6.png")
        mob_img.set_colorkey(white)
        back = ((32,32),(64,64),(16,16))
        ran = random.choice(back)
        self.image = pg.transform.scale(mob_img,(ran))
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speed = random.randrange(3,8)
        #self.speed = random.randint(2,8)
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height + 10:
              self.rect.centerx = random.randrange(width - self.rect.width)
              self.rect.y = random.randrange(-100,-40)
              self.speed = random.randrange(3,8)
              #self.speed = random.randint(1,6)
             
              
              
class Bullet(pg.sprite.Sprite):
      def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        bullet_img = pg.image.load("bullet.png")
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
      def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                  self.kill()
class Explosion(pg.sprite.Sprite):
      def __init__(self,center,size):
        pg.sprite.Sprite.__init__(self)
        self.size = size 
        self.image = effects[self.size][0]
        
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last = pg.time.get_ticks()
        self.rate = 50
      def update(self):
          now = pg.time.get_ticks()
          if now - self.last > self.rate:
              self.last = now
              self.frame += 1
              if self.frame == len(effects[self.size]):
                  self.kill()
              else:
                  center = self.rect.center
                  self.image = effects[self.size][self.frame]
                  self.rect = self.image.get_rect()
                  self.rect.center = center
class Boss(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        mob_img = pg.image.load("enemyShip.png")
        mobk = pg.transform.scale(mob_img,(80,32))
        self.image = mobk
        mob_img.set_colorkey(black)
        self.shied = 100
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-12000,-10000)
        self.speed = 4
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height-600:
            self.speed = 0
            #self.rect.x += 4
        self.rect.x += 4
        rand = random.randint(0,width)
        if self.rect.x > width-100:
            self.rect.x = rand
            self.speed = 4
        if self.rect.x <0:
            self.rect.x = rand
            
        if self.rect.top > height + 10:
              self.rect.centerx = random.randrange(width - self.rect.width)
              self.rect.y = random.randrange(-100,-40)
              self.speed = 4
class Bullets(pg.sprite.Sprite):
      def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        sbullet_img = pg.image.load("shoot.png")
        self.image = sbullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
      def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                  self.kill()
