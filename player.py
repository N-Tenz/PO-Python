import pygame

pygame.init()

Clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((800,432))
pygame.display.set_caption('Player')

char = pygame.image.load('idle.gif').convert_alpha()
player_sz = (38,68)
char = pygame.transform.scale(char,player_sz)

class player(object):
    def __init__(self,x,y,witdh,height):
        self.x = x
        self.y = y
        self.witdh = witdh
        self.height = height
        self.vel = 4
        self.jumping = False
        self.gravity = 1
        self.jumphoogte = 15
        self.snelheid = self.jumphoogte
    
    def draw(self,screen):
        screen.blit(char,(self.x,self.y))

BG = (50,50,50)
world_offset = [0,0]

player = player(100,320,38,68)


run = True
while run:
    
    Clock.tick(FPS)
    screen.fill(BG)
    
    player.draw(screen)
    
    #movements
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and player.x > 0:
        player.x -= 5
    if key[pygame.K_a] and key[pygame.K_LSHIFT] and player.x > 0:
        player.x -= 5
    if key[pygame.K_d]:
        player.x += 5
    if key[pygame.K_d] and key[pygame.K_LSHIFT]:
        player.x += 5
    
    if key[pygame.K_SPACE]:
        player.jumping = True
    if player.jumping:
        player.y -= player.snelheid #jump dus 350 - 15
        player.snelheid -= player.gravity #zet een limiet 
        if player.snelheid < -player.jumphoogte: # als 15 -1 word dan reset
            player.jumping = False #stop met jumpen
            player.snelheid = player.jumphoogte # reset terug naar 15
    
    
    if player.x < 50 :
        player.x = 50
        world_offset[0] += 10
    if player.x >= screen.get_width() - 100:
        player.x = screen.get_width() - 100
        world_offset[0] -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()