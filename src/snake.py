import pygame
from player import *

""" Main file for the snake program. """
__author__ = "Jai Wargacki"


def play():
    """
    Begins the game of snake.
    :return: None
    """
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
    pygame.display.set_caption(WINDOW_TITLE)
    screen.fill(BACKGROUND_COLOR)

    snake = Snake()
    food = Food(snake)
    paused = True
    first = True

    # Display start screen
    font_1 = pygame.font.SysFont(MENU_FONT, LARGE_FONT_SIZE)
    text_1 = font_1.render(WINDOW_TITLE, True, SNAKE_COLOR)
    text_rect_1 = text_1.get_rect(center=LARGE_TEXT_LOC)
    screen.blit(text_1, text_rect_1)
    font_2 = pygame.font.SysFont(MENU_FONT, SMALL_FONT_SIZE)
    text_2 = font_2.render(START_TEXT, True, FOOD_COLOR)
    text_rect_2 = text_2.get_rect(center=SMALL_TEXT_LOC)
    screen.blit(text_2, text_rect_2)
    pygame.display.update()

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
            if first:
                first = False
                screen.fill(BACKGROUND_COLOR)
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
                screen.fill(BACKGROUND_COLOR)
                font = pygame.font.SysFont(MENU_FONT, SMALL_FONT_SIZE)
                text = font.render(SCORE_TEXT % snake.__sizeof__(), True, FOOD_COLOR)
                text_rect = text.get_rect(center=SMALL_TEXT_LOC)
                screen.blit(text, text_rect)
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit(0)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':
    play()
