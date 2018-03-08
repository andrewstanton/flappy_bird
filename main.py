# Flappy Bird Attempt

import pygame as pg
import random
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        self.dir = path.dirname(__file__)
        self.sprite_folder = path.join(self.dir, SPRITE_FOLDER)
        self.font_folder = path.join(self.dir, FONT_FOLDER)
        self.font =  path.join(self.font_folder, 'kenvector_future.ttf')

        #game sprite
        sprite_xml_path = path.join(self.sprite_folder, SPRITESHEET_XML)
        sprite_sheet = path.join(self.sprite_folder, SPRITESHEET)
        self.game_spritesheet = Spritesheet(sprite_sheet, sprite_xml_path)

    def new(self):
        #score
        self.score = 0

        #set up sprite groups
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.pipes = pg.sprite.Group()
        self.grounds = pg.sprite.Group()
        self.player = Player(self)

        # ground
        self.ground = Ground(0, self)
        self.ground_width = self.ground.rect.width
        self.ground2 = Ground(self.ground_width, self)
        
        # sprite groups
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ground)
        self.all_sprites.add(self.ground2)
        self.grounds.add(self.ground)
        self.grounds.add(self.ground2)

        # initial pipes
        PipesGroup(WIDTH + 150, self)
        
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

        # ground collision
        hits = pg.sprite.spritecollide(self.player, self.grounds, False, pg.sprite.collide_mask)
        for hit in hits:
            self.playing = False

        # ground moving
        for ground in self.grounds:
            if ground.rect.right < 0:
                ground.rect.x = self.ground_width

        # remove pipe
        for pipe in self.pipes:
            if pipe.rect.right < -50:
                pipe.kill()
            # add new pipe
            if pipe.group.latest and pipe.rect.right <= (WIDTH - PIPE_SPACE) + (PIPE_WIDTH + PIPE_OFFSCREEN_GAP):
                pipe.group.latest = False
                PipesGroup(WIDTH + PIPE_OFFSCREEN_GAP, self)

        # pipe collison
        hits = pg.sprite.spritecollide(self.player, self.pipes, False)
        for hit in hits:
            self.playing = False


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.running = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def draw(self):
        # Viewing FPS while developing
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))

        # Game Loop - draw
        self.screen.fill(BACKGROUND)
        #bg = self.game_spritesheet.get_image("background.png", None, None, WIDTH, HEIGHT)
        #bg_rect = bg.get_rect()
        #bg_rect.left, bg_rect.top = (0, 0)
        #self.screen.blit(bg, bg_rect)
        
        self.all_sprites.draw(self.screen)

        # Draw Score
        self.draw_text(str(self.score), self.font, 42, BLACK, WIDTH / 2, 40, align="center")

        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        self.screen.fill(WHITE)
        self.draw_text(TITLE, self.font, 45, BLACK, WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Press A Key To Start", self.font, 24, BLACK, WIDTH / 2, HEIGHT / 2 + 50, align="center")
        pg.display.flip()
        self.wait_for_key()
        
    def show_go_screen(self):
        self.screen.fill(WHITE)
        self.draw_text("Game Over", self.font, 45, BLACK, WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Your Score: {!s}".format(self.score), self.font, 24, BLACK, WIDTH / 2, HEIGHT / 2 + 50, align="center")
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
