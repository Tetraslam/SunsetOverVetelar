import pygame

from entity_handler import EntityHandler
from player import Player
from ground import Ground

WIN_WIDTH = 1600
WIN_HEIGHT = 900


def game_loop(win, entity_handler):
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.time.delay(10)

        tick(entity_handler)
        render(entity_handler)

        win.fill((0, 0, 0))  # TODO Create New Window Class


def tick(entity_handler):
    entity_handler.tick()


def render(entity_handler):
    entity_handler.render()


def main():
    pygame.init()

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Sunset Over Vetelar")

    entity_handler = EntityHandler()

    entity_handler.add_entity(Player(win, 50, 50, 10, 400, 600))
    entity_handler.add_entity(Ground(win))

    game_loop(win, entity_handler)

    pygame.quit()


if __name__ == "__main__":
    main()
