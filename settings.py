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
PIPE_GAP = 200
PIPE_SPACE = 250

PIPE_TOP_START = -((HEIGHT / 2 - PIPE_HEIGHT) + (PIPE_GAP / 2))
PIPE_BOTTOM_START = HEIGHT / 2 + (PIPE_GAP / 2)

PIPE_LIST = [(WIDTH + PIPE_SPACE, PIPE_TOP_START),
             (WIDTH + PIPE_SPACE, PIPE_BOTTOM_START),
             (WIDTH + PIPE_SPACE * 2, PIPE_TOP_START + 100),
             (WIDTH + PIPE_SPACE * 2, PIPE_BOTTOM_START + 100),
             (WIDTH + PIPE_SPACE * 3, PIPE_TOP_START - 100),
             (WIDTH + PIPE_SPACE * 3, PIPE_BOTTOM_START - 100)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
