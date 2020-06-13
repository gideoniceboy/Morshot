import pygame as pg
import sys
from os import path
from settings import *
from player import *
import random

running = True
#score = 0
fps = 64

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption(title)
        self.dt = self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.load()
        self.font_name = pg.font.match_font('arial')
    def load(self):
        self.bg = pg.image.load("back.png")
        self.bh = pg.image.load("back.png")
        mob_img = pg.image.load("m.png")

        self.exploid = pg.mixer.Sound("EXPLODE.wav")
        self.bomb = pg.mixer.Sound("BOMB.wav")

    #new mobs
    def new_mobs(self):
          self.mob = Mob()
          all_sprite.add(self.mob)
          mobs.add(self.mob)

          
    def new(self):
        #mobs
        self.add = 10
        for x in range(self.add):
              self.new_mobs()
        #boss
        for y in range(1):
            self.b = Boss()
            all_sprite.add(self.b)
            bosses.add(self.b) 
        self.player = Player()
        all_sprite.add(self.player)
        #bullets
    def newBulets(self):
        ran = random.randrange(0,width)
        self.bullet = Bullet(ran,height-10)
        all_sprite.add(self.bullet)
        bullets.add(self.bullet)
        for z in range(5):
              self.newBulets()
    #collision detection
    def collide(self):
        hit = pg.sprite.spritecollide(self.player,mobs,True,pg.sprite.collide_circle)
        for h in hit:
              self.player.shied -= 20
              eff = Explosion(h.rect.center,'sm')
              all_sprite.add(eff)
              self.bomb.play()
              self.new_mobs()
              
              
              
              self.plus()
              if self.player.shied <= 0:
                    self.gameOver()
        hits = pg.sprite.groupcollide(bullets,mobs,True,True)
        for hitt in hits:
            self.player.score += 4
            self.new_mobs()
            eff = Explosion(hitt.rect.center,'lg')
            all_sprite.add(eff)
            self.ok = 0
            self.ok += 2
            
            self.draw_texts("+"+str(self.ok),40,yellow,hitt.rect.center)
            pg.display.flip()
            
            
            self.speed = random.randint(5,10)
            self.exploid.play()
            self.plus()
            
    #Boss Collision
    def boss_collide(self):
        die = False
        hitss = pg.sprite.groupcollide(bullets,bosses,True,False)
        if hitss:
            self.b.shied -= 2
            if self.b.shied <=0:
                self.b.kill()
                self.add = 100
                self.won()
        for hitty in hitss:
            self.player.score += 10
            eff = Explosion(hitty.rect.center,'lg')
            all_sprite.add(eff)
            #self.new_mobs()
            self.exploid.play()
            self.plus()

        #End Boss
    def quit(self):
        pg.quit()
        sys.exit()
    def draw_bar(self,surf,x,y,perc):
          if perc <0:
                perc = 0
          bar_length = 150
          bar_height =  20
          fill = (perc/100)* bar_length
          outline_rect = pg.Rect(x,y,bar_length,bar_height)
          fill_rect = pg.Rect(x,y,fill,bar_height)
          pg.draw.rect(surf,(0,255,0),fill_rect)
          pg.draw.rect(surf,(255,255,255),outline_rect,2)
    def draw_enemy_bar(self,surf,x,y,perc):
          if perc <0:
                perc = 0
          bar_length = 150
          bar_height =  20
          fill = (perc/100)* bar_length
          outline_rect = pg.Rect(x,y,bar_length,bar_height)
          fill_rect = pg.Rect(x,y,fill,bar_height)
          pg.draw.rect(surf,(255,0,0),fill_rect)
          pg.draw.rect(surf,(255,255,255),outline_rect,2)
          
    def draw_text(self,text,size,color,x,y):
          font = pg.font.Font(self.font_name,size)
          font_surface = font.render(text,False,color)
          text_rect = font_surface.get_rect()
          text_rect.midtop = (x,y)
          self.screen.blit(font_surface,text_rect)
    def draw_texts(self,text,size,color,center):
          font = pg.font.Font(self.font_name,size)
          font_surface = font.render(text,False,color)
          text_rect = font_surface.get_rect()
          text_rect.center = center
          #self.x = x
          #self.y = y
          #text_rect.x = x
          #text_rect.y = y
          self.screen.blit(font_surface,text_rect)
    def plus(self):
        self.draw_text("+5",25,white,width/1*3,10)
        pg.display.flip()
        self.newBulets()
        

    def perfect(self):
        if self.player.score >= 100 and self.player.score<= 200:
            self.dt = self.clock.tick(20)
            self.draw_text("-40 SLOW",50,white,width/2,height/4)
            self.draw_text("Score 200 to Speed up",40,green,width/2,height *3/4)
            
        elif self.player.score == 300:
            self.dt = self.clock.tick(64)
            self.draw_text("Perfect",70,green,width/2,height *3/4)
            self.draw_text("+120",30,white,width/2,height/4)
            self.player.score + 120
        elif self.player.score >= 500 and self.player.score<= 600:
            self.dt = self.clock.tick(64)
            self.draw_text("Too Slow!",50,white,width/2,height/4)
            self.draw_text("Score 1000+",40,green,width/2,height *3/4)
        elif self.player.score >= 50 and self.player.score <= 70:
            self.speed = random.randrange(12,13)
            
    def draw_grid(self):
        for x in range(0,width,tilesize):
            pg.draw.line(self.screen, green, (x,0),(x,height))
        for y in range(0,height,tilesize):
            pg.draw.line(self.screen, green, (0,y),(width,y))
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(fps) / 1000
            self.event()
            self.update()
            self.collide()
            self.boss_collide()
            self.render()
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                
    def update(self):
        
        all_sprite.update()

        
    def render(self):
        self.bk = pg.transform.scale(self.bg,(width,height))
        self.screen.blit(self.bk,(0,0))
        
        all_sprite.draw(self.screen)
        self.draw_text("Score:"+str(self.player.score),25,white,width/2,8)
        #self.draw_text("+10",25,yellow,width-100,8)

        self.perfect()
        self.draw_text("Player",15,yellow,65,5)
        self.draw_bar(self.screen,5,25,self.player.shied)
        
        self.draw_enemy_bar(self.screen,width-160,25,self.b.shied)
        self.draw_text("Boss",15,yellow,width-100,5)
        pg.display.flip()





        
    def waiting(self):
          self.dt = self.clock.tick(fps)
          play = True
          while play:
                for e in pg.event.get():
                      if e.type == pg.QUIT:
                            self.quit()
                      if e.type == pg.KEYUP:
                            play = False
    def waitings(self):
          self.dt = self.clock.tick(fps)
          play = True
          while play:
                for e in pg.event.get():
                      if e.type == pg.QUIT:
                            self.quit()
                      if e.type == pg.KEYDOWN:
                            if e.key == pg.K_e:
                                  play = False

        
    def starting(self):
        self.bl = pg.transform.scale(self.bh,(width,height))
        self.screen.blit(self.bl,(0,0))
        
        player_img = pg.image.load("player2.png")
        image = pg.transform.scale(player_img,(150,150))
        self.screen.blit(image,(50,height/2))

        rect = image.get_rect()
        rect.y += 10

        player_imgs = pg.image.load("enemy_4.png")
        images = pg.transform.scale(player_imgs,(150,150))
        self.screen.blit(images,(width-200,height/2))

        pg.display.update()
        
        self.draw_text("MORSHOT",80,green,width/2,height/4)
        self.draw_text("Arrow keys to move, Space key to shoot",25,white,width/2,height/2)
        self.draw_text("Press any key to Continue",25,white,width/2,height * 3/4)
        pg.display.flip()
        self.waiting()
    def gameOver(self):
        if (self.playing):
            self.screen.fill(red)
            self.draw_text("Game Over!",150,white,width/2,250)
            self.draw_text("You Scored: "+str(self.player.score),25,white,width/2,height * 2.5/4)
            self.draw_text("Press e key to Continue",25,white,width/2,height * 3/4)
            pg.display.flip()
            self.waitings()
            self.player.shied = 100
            self.player.score = 0
    def won(self):
        self.bl = pg.transform.scale(self.bh,(width,height))
        self.screen.blit(self.bl,(0,0))
        self.draw_text("Congraturations!",80,green,width/2,height/4)
        self.draw_text("You won!",150,white,width/2,250)
        pg.display.flip()
        self.waitings()
        
g = Game()
g.starting()
while running:
    g.new()
    g.run()
    g.won()
    g.gameOver()
pg.quit()
