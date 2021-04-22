import enum

""" Constants & Enums used in other files. """
__author__ = "Jai Wargacki"

SNAKE_UNIT = 10
STARTING_POSITION = (10, 10)


class Direction(enum.Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


DIMENSION = 60
WINDOW_DIMENSIONS = (DIMENSION * SNAKE_UNIT, DIMENSION * SNAKE_UNIT)
WINDOW_TITLE = "Snake"

# Colors
SNAKE_COLOR = (0, 230, 0)
BACKGROUND_COLOR = (0, 0, 0)
FOOD_COLOR = (230, 0, 0)
