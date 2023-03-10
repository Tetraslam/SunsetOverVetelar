import time

import pygame

from entity_handler import EntityHandler
from player import Player
from ground import Ground

WIN_WIDTH = 1600
WIN_HEIGHT = 900

FRAMES = 0

# Hello

def game_loop(win, entity_handler):
    last_tick = time.time_ns()
    frame_rate = 0
    timer = time.time_ns() // 1_000_000

    global FRAMES
    run = True
    buffer = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))

    while run:
        now = time.time_ns()
        time_since_last_tick = now - last_tick

        if time_since_last_tick >= 10000:
            tick(entity_handler)
            last_tick = time.time_ns() // 1_000_000
        buffer.fill((0, 0, 0))
        render(entity_handler)
        win.fill((0, 0, 0))  # TODO Create New Window Class
        frame_rate += 1

        if time.time_ns() // 1_000_000 - timer >= 1000:
            timer = time.time_ns() // 1_000_000
            FRAMES = frame_rate
            frame_rate = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def tick(entity_handler):
    entity_handler.tick()


def render(entity_handler):
    entity_handler.render()


def main():
    pygame.init()

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Sunset Over Vetelar")

    entity_handler = EntityHandler()

    entity_handler.add_entity(Ground(win, 0, WIN_HEIGHT - 100, WIN_WIDTH, 100))  # Ground Position: 0
    entity_handler.add_entity(Player(win, 50, 50, 100, 160, 5, entity_handler.entities[0]))  # Player Position: 1

    game_loop(win, entity_handler)

    pygame.quit()


if __name__ == "__main__":
    main()
