import pygame

from base_entity import BaseEntity


class Ground(BaseEntity):
    WIN_WIDTH = 1600
    WIN_HEIGHT = 900

    def __init__(self, sprite_x, win, sprite_y, sprite_vel, sprite_width, sprite_height):
        self.window = win


    def render(self):
        # TODO Unhardcode The Values
        pygame.draw.rect(self.win, (50, 50, 200), (0, self.WIN_HEIGHT - 100, self.WIN_WIDTH, 100)) #ground


    def tick(self):
        pass
