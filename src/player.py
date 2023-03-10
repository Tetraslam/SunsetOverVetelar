import pygame

from base_entity import BaseEntity


class Player(BaseEntity):
    ENTITY_ID = "PLAYER"

    WIN_WIDTH = 1600
    WIN_HEIGHT = 900

    def __init__(self, win, x, y, width, height, vel, ground):
        self.window = win

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.vel = vel
        self.ground = ground

    def render(self):
        self.out_of_screen()
        self.colliding_with_ground()

        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.display.update()

    def tick(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.y += 1

    def get_bounds(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def colliding_with_ground(self):
        if self.get_bounds().colliderect(self.ground.get_bounds()):
            self.y = self.WIN_HEIGHT - self.ground.height - self.height

    def out_of_screen(self):
        if self.y < 0:
            self.y = 0

        elif self.y > self.WIN_HEIGHT - self.height:
            self.y = self.WIN_HEIGHT - self.height

        elif self.x < 0:
            self.x = 0

        elif self.x > self.WIN_WIDTH - self.width:
            self.x = self.WIN_WIDTH - self.width
