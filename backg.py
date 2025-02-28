import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((800,432))
pygame.display.set_caption('Background Layers')

scroll = 0

Bg1 = pygame.image.load('Layer-1.png').convert_alpha()
Bg2 = pygame.image.load('Layer-2.png').convert_alpha()
Bg3 = pygame.image.load('Layer-3.png').convert_alpha()
Bg4 = pygame.image.load('Layer-4.png').convert_alpha()
Bg5 = pygame.image.load('Layer-5.png').convert_alpha()

img_sz = (768,432)
Bg1 = pygame.transform.scale(Bg1, img_sz)
Bg2 = pygame.transform.scale(Bg2, img_sz)
Bg3 = pygame.transform.scale(Bg3, img_sz)
Bg4 = pygame.transform.scale(Bg4, img_sz)
Bg5 = pygame.transform.scale(Bg5, img_sz)

Bgs = [Bg1,Bg2,Bg3,Bg4,Bg5]
Bg_width = Bgs[0].get_width()

def draw_bg():
    for x in range(5):
        speed = 1
        for i in Bgs:
            screen.blit(i , ((x * Bg_width)  - scroll * speed,0))
            speed += 0.2

run = True

while run:
    
    clock.tick(FPS)
    
    draw_bg()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and scroll > 0:
        scroll -= 5
    if key[pygame.K_a] and key[pygame.K_LSHIFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_d]:
        scroll += 5
    if key[pygame.K_d] and key[pygame.K_LSHIFT]:
        scroll += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()