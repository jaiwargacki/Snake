import pygame
from player import *

""" Main file for the snake program. """
__author__ = "Jai Wargacki"


def play():
    """
    Begins the game of snake.
    :return: None
    """
    screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
    pygame.display.set_caption(WINDOW_TITLE)
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

    snake = Snake()
    food = Food(snake)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        # Update facing direction
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            snake.update_facing(Direction.NORTH)
        if pressed[pygame.K_DOWN]:
            snake.update_facing(Direction.SOUTH)
        if pressed[pygame.K_LEFT]:
            snake.update_facing(Direction.WEST)
        if pressed[pygame.K_RIGHT]:
            snake.update_facing(Direction.EAST)
        if pressed[pygame.K_SPACE]:
            snake.grow()

        # Update game condition
        try:
            f_x, f_y = food.get_location()
            pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(f_x, f_y, 10, 10))
            x_pos, y_pos = snake.move()
            pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(x_pos, y_pos, 10, 10))
            x_pos, y_pos = snake.get_head()
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(x_pos, y_pos, 10, 10))
            if f_x == x_pos and f_y == y_pos:
                snake.grow()
                food = Food(snake)
        except TypeError:
            exit(0)

        pygame.display.update()
        pygame.time.Clock().tick(15)


if __name__ == '__main__':
    play()
