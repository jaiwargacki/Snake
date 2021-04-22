import random
from constants import *

""" Class used to represent the players snake. """
__author__ = "Jai Wargacki"


class Snake:
    __slots__ = 'snake', 'length', 'facing', 'x_bound', 'y_bound'

    def __init__(self):
        self.x_bound, self.y_bound = WINDOW_DIMENSIONS
        self.snake = SnakeChain()
        self.length = 1
        self.facing = EAST

    def __sizeof__(self):
        return self.snake.size

    def get_head(self):
        """
        Gets the current x, y position of the snake's head.
        :return: x, y position of the snake's head.
        """
        return self.snake.head.x_pos, self.snake.head.y_pos

    def get_tail(self):
        """
        Gets the current x, y position of the snake's tail.
        :return: x, y position of the snake's tail.
        """
        return self.snake.tail.x_pos, self.snake.tail.y_pos

    def update_facing(self, update):
        """
        Update the direction the snake is facing.
        :param update: The new direction to be facing.
        :return: None.
        """
        if (self.facing + 2) % 4 != update or self.snake.size == 1:
            self.facing = update

    def move(self):
        """
        Move the snake one move.
        :return: the location of the previous tail piece, None if dead
        """
        x, y = self.get_head()
        if self.facing == NORTH:
            y -= SNAKE_UNIT
        if self.facing == EAST:
            x += SNAKE_UNIT
        if self.facing == SOUTH:
            y += SNAKE_UNIT
        if self.facing == WEST:
            x -= SNAKE_UNIT
        x = x % (DIMENSION * SNAKE_UNIT)
        y = y % (DIMENSION * SNAKE_UNIT)
        if not self.snake.add(SnakeLink(x, y)):
            return None
        prev = self.snake.pop()
        return prev.x_pos, prev.y_pos

    def grow(self):
        """
        Grows the snake by one.
        :return: None.
        """
        self.snake.size += 1
        temp = SnakeLink(self.snake.tail.x_pos, self.snake.tail.y_pos)
        temp.set_next(self.snake.tail)
        self.snake.tail = temp

    def is_valid_food_location(self, x_pos, y_pos):
        """
        Given an x and y pos returns True if valid spot to generate food,
        False otherwise.
        :param x_pos: x position of food.
        :param y_pos: y position of food.
        :return: True if valid, False otherwise.
        """
        return not SnakeLink(x_pos, y_pos) in self.snake.contents


class SnakeChain:
    __slots__ = 'head', 'tail', 'size', 'contents'

    def __init__(self):
        x, y = STARTING_POSITION
        self.head = SnakeLink(x, y)
        self.tail = self.head
        self.size = 1
        self.contents = set()
        self.contents.add(self.head)

    def __sizeof__(self):
        return self.size

    def add(self, link):
        """
        Add to the head of the snake.
        :param link: the new head of the snake.
        :return: None.
        """
        self.head.set_next(link)
        self.head = link
        if self.head in self.contents:
            return False
        else:
            self.contents.add(self.head)
            return True

    def pop(self):
        """
        Pop the tail off of the snake.
        :return: the popped link.
        """
        temp = self.tail
        if temp != temp.next_link:
            self.contents.remove(self.tail)
        self.tail = temp.get_next()
        if self.tail is None:
            self.tail = self.head
        return temp


class SnakeLink:
    __slots__ = 'x_pos', 'y_pos', 'next_link'

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.next_link = None

    def __eq__(self, other):
        return self.x_pos == other.x_pos and self.y_pos == other.y_pos

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return pow(self.x_pos, self.y_pos)

    def __str__(self):
        return "[" + str(self.x_pos) + ":" + str(self.y_pos) + "]"

    def __repr__(self):
        return "[" + str(self.x_pos) + ":" + str(self.y_pos) + "::" + str(self.next_link) + "]"

    def get_next(self):
        """
        Get the link's next.
        :return: the link's next
        """
        return self.next_link

    def set_next(self, link):
        """
        Set the next link in the chain.
        :param link: the next link.
        :return: None.
        """
        self.next_link = link


class Food:
    __slots__ = 'x_pos', 'y_pos'

    def __init__(self, snake):
        while True:
            x = random.randint(1, DIMENSION-1) * 10
            y = random.randint(1, DIMENSION-1) * 10
            if not SnakeLink(x, y) in snake.snake.contents:
                break
        self.x_pos = x
        self.y_pos = y

    def get_location(self):
        """
        Gets the current x, y position of the food piece.
        :return: x, y position of the food piece.
        """
        return self.x_pos, self.y_pos
