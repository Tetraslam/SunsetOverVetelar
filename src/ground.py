import pygame

from base_entity import BaseEntity


class Ground(BaseEntity):
    ENTITY_ID = "GROUND"

    WIN_WIDTH = 1600
    WIN_HEIGHT = 900

    def __init__(self, win, x, y, width, height):
        self.window = win

        self.x = x
        self.y = y

        self.width = width
        self.height = height

    def render(self):
        pygame.draw.rect(self.window, (50, 50, 200), (self.x, self.y, self.width, self.height))
        pygame.display.update()

    def tick(self):
        pass

    def get_bounds(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
