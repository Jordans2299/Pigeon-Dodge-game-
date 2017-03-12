#pygame template - skeleton for a new pygame project
import pygame as pg
import random
from gamesettings import *
from sprites import *


class Game:
    def __init__(self):
        #initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Pidgeon Dodge")
        self.clock = pg.time.Clock()
        self.running = True
        
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in platform_list:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        #Game loop
      self.playing = True
      while self.playing:
          self.clock.tick(fps)
          self.events()
          self.update()
          self.draw()

    def update(self):
        #Game Loop - Update
        self.all_sprites.update()
        #check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                self.player.pos.y = hits[0].rect.top +1
                self.player.vel.y = 0
        #if player reaches top 1/4 of screen
##        if player.rect.top <= height:
    def events(self):
        #Game Loop - events
        for event in pg.event.get():
            #checks for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.plaing = False
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def draw(self):
        #Game Loop - draw
        self.screen.fill(black)
        self.all_sprites.draw(self.screen)
        #flips display after drawing everything
        pg.display.flip()
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pg.quit()
quit()


