# Sprite classes for platform game
import pygame as pg
from settings import *
import random
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.jumping = False
        self.game = game
        self.image = pg.Surface((40, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        self.jumping = True
        self.vel.y = -PLAYER_JUMP

    def update(self):
        # player grav
        self.acc = vec(0, PLAYER_GRAV)
        
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.2 * self.acc
        
        # wrap around the sides of the screen
        if self.pos.y >= HEIGHT:
            self.game.playing = False
        
        self.rect.midbottom = self.pos

class Pipe(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    def update(self):
        self.rect.x -= WINDOW_SPEED

class PipesGroup():
    def __init__(self, x, game):
        offset = random.choice([-150, -100, -50, 0, 50, 100, 150])
        self.game = game
        self.top = Pipe(x, PIPE_TOP_START + offset)
        self.bottom = Pipe(x, PIPE_BOTTOM_START + offset)
        game.pipes.add(self.top)
        game.pipes.add(self.bottom)
        game.all_sprites.add(self.top)
        game.all_sprites.add(self.bottom)