import pygame
from pytmx.util_pygame import load_pygame

pygame.init()
Clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((800,432))
pygame.display.set_caption('Map')
BG = (50,50,50)

tmxdata = load_pygame('map.tmx')

def blit_all_tiles(screen, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            #tile[0] ... x grid locatie
            #tile[1] ... y grid locatie
            #tile[2] ... image data for blitting
            x_pixel = tile[0] * 32 + world_offset[0]
            y_pixel = tile[1] * 32 + world_offset[1]
            screen.blit( tile[2], (x_pixel, y_pixel))

world_offset = [0,-208]
run = True
while run:
    
    Clock.tick(FPS)
    screen.fill((50,50,50))
    blit_all_tiles(screen, tmxdata, world_offset)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()