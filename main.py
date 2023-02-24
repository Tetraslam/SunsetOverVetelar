import pygame

pygame.init()

WIN_WIDTH = 1600
WIN_HEIGHT = 900

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sunset Over Veletar")

sprite_x = 50
sprite_y = 50
sprite_vel = 10

sprite_width = 400
sprite_height = 600

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sprite_x -= sprite_vel

    if keys[pygame.K_RIGHT]:
        sprite_x += sprite_vel

    if keys[pygame.K_UP]:
        sprite_y -= sprite_vel

    if keys[pygame.K_DOWN]:
        sprite_y += sprite_vel

    win.fill((0, 0, 0))  # Set Background Color

    pygame.draw.rect(win, (255, 0, 0), (sprite_x, sprite_y, sprite_width, sprite_height))
    pygame.draw.rect(win, (50, 50, 200), (0, WIN_HEIGHT-100, WIN_WIDTH, 100))

    pygame.display.update()


pygame.quit()
