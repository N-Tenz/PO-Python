import pygame
from pytmx.util_pygame import load_pygame
pygame.init()

screen = pygame.display.set_mode((800,432))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
FPS = 60

char = pygame.image.load('idle.gif').convert_alpha()
player_sz = (38,68)
char = pygame.transform.scale(char,player_sz)

world_offset = [0,-190]

class Player(object):
    def __init__(self,x,y,witdh,height):
        
        self.x = x
        self.y = y
        self.witdh = witdh
        self.height = height
        self.vel = 2
        self.jumping = False
        self.gravity = 1
        self.jumphoogte = 15
        self.snelheid = self.jumphoogte
        self.falling = False
    
    def draw(self,screen):
        screen.blit(char,(self.x,self.y))
        self.hitbox = (self.x,self.y,self.witdh,self.height)
        self.rect = char.get_rect()
        pygame.draw.rect(screen,(255,0,0),self.hitbox,2)
player = Player(100,320,38,68)

#map load in
tmxdata = load_pygame('map.tmx')

class World(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 32
        self.height = 32
    def blit_all_tiles(self,screen, tmxdata, world_offset):
        for layer in tmxdata:
            for tile in layer.tiles():
            #tile[0] ... x grid locatie
            #tile[1] ... y grid locatie
            #tile[2] ... image data for blitting
                x_pixel = tile[0] * 32 + world_offset[0]
                y_pixel = tile[1] * 32 + world_offset[1]
                screen.blit(tile[2], (x_pixel, y_pixel))
                
                
                self.hitbox = (self.x,self.y,self.width,self.height)
                self.rect = pygame.draw.rect(tile[2], (255,0,0),self.hitbox,2)
                

                
                
                
                
wereld = World()

class Border(object):
    def __init__(self,x,y,witdh,height):
        self.x = x
        self.y = y
        self.witdh = witdh
        self.height = height
    
    def draw(self,screen):
        self.hitbox = (self.x,self.y,self.witdh,self.height)
        pygame.draw.rect(screen,(255,0,0),self.hitbox,2)

border = Border(-50,0,50,800)



#background images
Bg1 = pygame.image.load('Layer-1.png').convert_alpha()
Bg2 = pygame.image.load('Layer-2.png').convert_alpha()
Bg3 = pygame.image.load('Layer-3.png').convert_alpha()
Bg4 = pygame.image.load('Layer-4.png').convert_alpha()
Bg5 = pygame.image.load('Layer-5.png').convert_alpha()
#resize background images
img_sz = (768,432)
Bg1 = pygame.transform.scale(Bg1, img_sz)
Bg2 = pygame.transform.scale(Bg2, img_sz)
Bg3 = pygame.transform.scale(Bg3, img_sz)
Bg4 = pygame.transform.scale(Bg4, img_sz)
Bg5 = pygame.transform.scale(Bg5, img_sz)
# Backgroudnd in lijst zetten
Bgs = [Bg1,Bg2,Bg3,Bg4,Bg5]
Bg_width = Bgs[0].get_width()
#eigen functie voor 3d background
def draw_bg():
    for x in range(5):
        speed = 1
        for i in Bgs:
            screen.blit(i , ((x * Bg_width)  - scroll * speed,0))
            speed += 0.2



def get_tile_properties(tmxdata, player_x , player_y ,world_offset):
    world_x = player.x - world_offset[0]
    world_y = player.y - world_offset[1]
    tile_x = world_x // 32
    tile_y = world_y // 32
    properties = tmxdata.get_tile_properties(tile_x, tile_y,0)





















scroll = 0
world_offset = [0,-190]

run = True
#game loop
while run:
    
    clock.tick(FPS)
    
    draw_bg()
    wereld.blit_all_tiles(screen , tmxdata, world_offset)
    player.draw(screen)
    border.draw(screen)
    
    
    
    if player.x < 100 :
        player.x = 100
        world_offset[0] += 10
    if player.x >= screen.get_width() - 200:
        player.x = screen.get_width() - 200
        world_offset[0] -= 10
    
    
    if wereld.rect.colliderect(player.rect.x, player.rect.y + player.y, player.witdh, player.height):
        if player.snelheid < 0:
            player.y = wereld.top - wereld.rect.bottom
            player.snelheid = 0
            
        elif player.snelheid >= 0:
            player.y = wereld.top - wereld.rect.bottom
            player.snelheid = 0
           
    
    
    
    
    
    
    
    
    
    
    #movements player
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and player.x > 0:
        player.x -= player.vel
    if key[pygame.K_a] and key[pygame.K_LSHIFT] and player.x > 0:
        player.x -= player.vel
        
    
    
    if key[pygame.K_d]:
        player.x += player.vel
    if key[pygame.K_d] and key[pygame.K_LSHIFT]:
        player.x += player.vel
    
    if key[pygame.K_SPACE]:
        player.jumping = True
    if player.jumping == True:
        player.y -= player.snelheid #jump dus 350 - 15
        player.snelheid -= player.gravity #zet een limiet
        player.falling = True
        if player.snelheid < -player.jumphoogte: # als 15 -1 word dan reset
            player.jumping = False #stop met jumpen
            player.falling = False
            player.snelheid = player.jumphoogte # reset terug naar 15
    
    #background movement
    if key[pygame.K_a] and scroll > 0:
        scroll -= 3
    if key[pygame.K_d] and key[pygame.K_LSHIFT] and player.x > 0:
        scroll -= 4 
    if key[pygame.K_d]:
        scroll += 3 
    if key[pygame.K_d] and key[pygame.K_LSHIFT]:
        scroll += 4
    
    
        
    
        








   
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
