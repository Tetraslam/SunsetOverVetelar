import pygame


class EntityHandler:
    WIN_WIDTH = 1600
    WIN_HEIGHT = 900

    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def render(self):
        for entity in self.entities:
            entity.render()


    def tick(self):
        for entity in self.entities:
            entity.tick()
