import pygame

pygame.init()

Clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((800,432))
pygame.display.set_caption('Map')
BG = (50,50,50)

run = True
while run:
    
    Clock.tick(FPS)
    screen.fill(BG)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()