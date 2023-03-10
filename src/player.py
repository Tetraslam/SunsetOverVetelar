import pygame

from base_entity import BaseEntity


class Player(BaseEntity):
    def __init__(self, win, sprite_x, sprite_y, sprite_vel, sprite_width, sprite_height):
        self.window = win
        self.sprite_x = sprite_x;
        self.sprite_y = sprite_y;
        self.sprite_vel = sprite_vel;
        self.sprite_width = sprite_width;
        self.sprite_height = sprite_height;


    def render(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.sprite_x, self.sprite_y, self.sprite_width, self.sprite_height))

        pygame.display.update()



    def tick(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.sprite_x -= self.sprite_vel

        if keys[pygame.K_RIGHT]:
            self.sprite_x += self.sprite_vel

        if keys[pygame.K_UP]:
            self.sprite_y -= self.sprite_vel

        if keys[pygame.K_DOWN]:
            self.sprite_y += self.sprite_vel
