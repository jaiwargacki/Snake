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
    paused = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        # Update facing direction
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            snake.update_facing(NORTH)
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            snake.update_facing(SOUTH)
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            snake.update_facing(WEST)
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            snake.update_facing(EAST)
        if pressed[pygame.K_SPACE]:
            paused = not paused
            pygame.time.wait(PAUSE_DELAY)
        if not paused:
            # Update game condition
            try:
                f_x, f_y = food.get_location()
                pygame.draw.rect(screen, FOOD_COLOR,
                                 pygame.Rect(f_x, f_y, SNAKE_UNIT, SNAKE_UNIT))
                x_pos, y_pos = snake.move()
                pygame.draw.rect(screen, BACKGROUND_COLOR,
                                 pygame.Rect(x_pos, y_pos, SNAKE_UNIT, SNAKE_UNIT))
                x_pos, y_pos = snake.get_head()
                pygame.draw.rect(screen, SNAKE_COLOR,
                                 pygame.Rect(x_pos, y_pos, SNAKE_UNIT, SNAKE_UNIT))
                if f_x == x_pos and f_y == y_pos:
                    snake.grow()
                    food = Food(snake)
            except TypeError:
                # Caught if snake.move() returns None indicating game has been lost
                exit(0)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':
    play()
