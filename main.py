import pygame

pygame.init()
win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Sunset Over Veletar")

x = 50
y = 50
vel = 10

width = 400
height = 600

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
        
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    

pygame.quit()
