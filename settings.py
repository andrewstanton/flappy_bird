# game options/settings
TITLE = "Flappy Bird"
WIDTH = 480
HEIGHT = 600
FPS = 60

# Player properties
PLAYER_GRAV = 0.4
PLAYER_JUMP = 10

# Window Properties
WINDOW_SPEED = 2

# Pipe properties
PIPE_WIDTH = 50
PIPE_HEIGHT = HEIGHT / 2
PIPE_GAP = 250
PIPE_SPACE = 250

PIPE_LIST = [(WIDTH + PIPE_SPACE, -100),
             (WIDTH + PIPE_SPACE, HEIGHT - 200),
             (WIDTH + PIPE_SPACE * 2, -200),
             (WIDTH + PIPE_SPACE * 2, HEIGHT - 300)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
