# game options/settings
TITLE = "Flappy Bird"
WIDTH = 480
HEIGHT = 600
FPS = 60

#fonts
FONT_FOLDER = 'font'

#SpriteSheet
SPRITE_FOLDER = 'spritesheet'
SPRITESHEET = 'sheet.png'
SPRITESHEET_XML = 'sheet.xml'

# Player properties
PLAYER_GRAV = 0.4
PLAYER_JUMP = 10
PLAYER_Z = 2

# Window Properties
WINDOW_SPEED = 2

# Pipe properties
PIPE_WIDTH = 80
PIPE_HEIGHT = HEIGHT
PIPE_GAP = 200
PIPE_SPACE = 400
PIPE_OFFSCREEN_GAP = 50
PIPE_Z = 2

PIPE_TOP_START = -((PIPE_HEIGHT - (HEIGHT / 2)) + (PIPE_GAP / 2))
PIPE_BOTTOM_START = HEIGHT / 2 + (PIPE_GAP / 2)

# Ground Properties
GROUND_Z = 3

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUND = (214, 249, 255)
