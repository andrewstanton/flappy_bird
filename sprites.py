# Sprite classes for platform game
import pygame as pg
from settings import *
import random
vec = pg.math.Vector2
from xml.dom import minidom

class Spritesheet():
    def __init__(self, sprite, xml):
        self.spritesheet = pg.image.load(sprite).convert_alpha()
        self.xml = minidom.parse(xml)

    def get_image(self, name, width=None, height=None):
        # get image data
        images = self.xml.getElementsByTagName('SubTexture')
        x = 0
        y = 0
        w = 0
        h = 0

        # get data
        for img in images:
            if img.attributes['name'].value == name:
                x = int(img.attributes['x'].value)
                y = int(img.attributes['y'].value)
                w = int(img.attributes['width'].value)
                h = int(img.attributes['height'].value)

        image = pg.Surface((w, h), pg.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))
        if not (width is None) and not (height is None):
            image = pg.transform.scale(image, (int(w * width), int(h * height)))
        else:
            image = pg.transform.scale(image, (int(w * 3 / 4), int(h * 3 / 4) ))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = PLAYER_Z
        pg.sprite.Sprite.__init__(self)
        self.jumping = False
        self.game = game
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = game.game_spritesheet.get_image("planeBlue1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (PLAYER_X, HEIGHT / 2)
        self.pos = vec(PLAYER_X, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.animation_frames = [self.game.game_spritesheet.get_image("planeBlue1.png"), self.game.game_spritesheet.get_image("planeBlue2.png"), self.game.game_spritesheet.get_image("planeBlue3.png")]


    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        self.jumping = True
        self.vel.y = -PLAYER_JUMP

    def update(self):
        self.animate()
        # player grav
        self.acc = vec(0, PLAYER_GRAV)
        
        self.mask = pg.mask.from_surface(self.image)

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.2 * self.acc
        
        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.current_frame]

class Pipe(pg.sprite.Sprite):
    def __init__(self, x, y, group):
        self._layer = PIPE_Z
        pg.sprite.Sprite.__init__(self)
        self.group = group
        self.image = pg.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    def update(self):
        self.rect.x -= WINDOW_SPEED

        if self.rect.x < PLAYER_X - self.group.game.player.rect.width / 2 and not self.group.scored:
            self.group.game.score += 1
            self.group.scored = True

class PipesGroup():
    def __init__(self, x, game):
        offset = random.choice([-150, -100, -50, 0, 50, 100, 150])
        self.game = game
        self.scored = False
        self.top = Pipe(x, PIPE_TOP_START + offset, self)
        self.bottom = Pipe(x, PIPE_BOTTOM_START + offset, self)
        self.latest = True
        game.pipes.add(self.top)
        game.pipes.add(self.bottom)
        game.all_sprites.add(self.top)
        game.all_sprites.add(self.bottom)

class Ground(pg.sprite.Sprite):
    def __init__(self, x, game):
        self._layer = GROUND_Z
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = game.game_spritesheet.get_image("groundGrass.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, GROUND_HEIGHT)

    def update(self):
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x -= WINDOW_SPEED
        
class Background(pg.sprite.Sprite):
    def __init__(self, x, game):
        self._layer = BACKGROUND_Z
        pg.sprite.Sprite.__init__(self)  
        self.image = game.game_spritesheet.get_image("background.png", 1.3, 1.3)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, 0)
    
    def update(self):
        self.rect.x -= WINDOW_SPEED / 2