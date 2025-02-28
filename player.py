import pygame

pygame.init()

Clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((800,432))
pygame.display.set_caption('Player')

player = pygame.image.load('idle.gif').convert_alpha()

player_sz = (38,68)
player = pygame.transform.scale(player,player_sz)

jumping = False
gravity = 1
jumphoogte = 15
snelheid = jumphoogte
BG = (50,50,50)
x = 50
y = 350
world_offset = [0,0]

run = True
while run:
    
    Clock.tick(FPS)
    screen.fill(BG)
    
    screen.blit(player,(x,y))
    
    #movements
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and x > 0:
        x -= 5
    if key[pygame.K_a] and key[pygame.K_LSHIFT] and x > 0:
        x -= 5
    if key[pygame.K_d]:
        x += 5
    if key[pygame.K_d] and key[pygame.K_LSHIFT]:
        x += 5
    
    if key[pygame.K_SPACE]:
        jumping = True
    if jumping:
        y -= snelheid #jump dus 350 - 15
        snelheid -= gravity #zet een limiet 
        if snelheid < -jumphoogte: # als 15 -1 word dan reset
            jumping = False #stop met jumpen
            snelheid = jumphoogte # reset terug naar 15
    
    
    if x < 50 :
        x = 50
        world_offset[0] += 10
    if x >= screen.get_width() - 100:
        x = screen.get_width() - 100
        world_offset[0] -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()