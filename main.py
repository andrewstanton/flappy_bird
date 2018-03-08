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
        # start a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.pipes = pg.sprite.Group()
        self.groundG = pg.sprite.Group()
        self.player = Player(self)
        self.ground = Ground(self)
        #self.background = Background(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ground)
        self.groundG.add(self.ground)

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

        # player falls / dies
        hits = pg.sprite.spritecollide(self.player, self.groundG, False, pg.sprite.collide_mask)
        for hit in hits:
            self.playing = False

        for pipe in self.pipes:
            # remove pipe
            if pipe.rect.right < -50:
                pipe.kill()
            # add new pipe
            if pipe.group.latest and pipe.rect.right <= (WIDTH - PIPE_SPACE) + (PIPE_WIDTH + PIPE_OFFSCREEN_GAP):
                pipe.group.latest = False
                PipesGroup(WIDTH + PIPE_OFFSCREEN_GAP, self)

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
        #self.screen.blit(self.background.image, self.background.rect)
        self.all_sprites.draw(self.screen)

        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        self.screen.fill(WHITE)
        self.draw_text("Game Over", self.font, 45, BLACK, WIDTH / 2, HEIGHT / 2, align="center")
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
