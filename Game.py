#importeer de library pygame
#importeer load_pygame voor de map
# intialiseer pygame dus start het op
import pygame
from pytmx.util_pygame import load_pygame


pygame.init()

#variabelen voor scherm, caption en fps
screen = pygame.display.set_mode((800,432))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
FPS = 60

#maak character aan
char = pygame.image.load('idle.gif').convert_alpha()
#character grootte (x,y)
player_sz = (38,68)
#tranformeer character naar gewenste grootte
char = pygame.transform.scale(char,player_sz)

world_offset = [0,-190]
#maak class aan voor player
class Player(object):
    def __init__(self,x,y,width,height):
        #variabelen voor player
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0
        self.richting = 'rechts'
        self.jumping = False
        self.gravity = 1
        self.velocity_y = 15
        self.jump_strength = self.velocity_y
        self.falling = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    # draw de player op het scherm
    def draw(self,screen):
        screen.blit(char,(self.x,self.y))
        
    def update(self,screen,wereld):
        self.movements()
        self.scroll()
        self.draw(screen)
        self.x += self.vel
        self.vel = 0
        self.handle_gravity()
        self.handle_collisions(wereld)     
    
    def movements(self):
        #player movements 
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.x > 0:
            self.vel = -2
            self.richting = 'links'
        if key[pygame.K_a] and key[pygame.K_LSHIFT] and player.x > 0:
            self.vel = -3
            self.richting = 'links'
        if key[pygame.K_d]:
            self.vel = 2
            self.richting = 'rechts'
        if key[pygame.K_d] and key[pygame.K_LSHIFT]:
            self.vel = 3
            self.richting = 'rechts'
    
        if key[pygame.K_SPACE] and not self.jumping:  # Jumping
            self.jumping = True
            self.velocity_y = -self.jump_strength
        
    def scroll(self):
        global world_offset  # Declare world_offset as global
    
        screen_width = screen.get_width()
        player_width = self.width
        max_scroll_x = screen_width - player_width - 100
    
        if self.x < 100:
            self.x = 100
            world_offset[0] += 5  # Modify the global world_offset
        if self.x > max_scroll_x:
            self.x = max_scroll_x
            world_offset[0] -= 5  # Modify the global world_offset
    
    def handle_gravity(self):
        if self.jumping:
            self.y += self.velocity_y
            self.velocity_y += self.gravity  # Apply gravity

        if self.y >= 320:  # Ground level (adjust this based on your game)
            self.y = 320
            self.jumping = False
            self.velocity_y = 0  # Stop falling    
    
    def handle_collisions(self, world):
        # Check for collisions with tiles (both horizontal and vertical)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        # Check collisions in the horizontal direction
        for tile in world.get_collidable_tiles(self.hitbox):
            if self.hitbox.colliderect(tile):
                if self.vel > 0 and self.richting == 'rechts':  # Moving right
                    self.x = tile.x - self.width  # Push player left to prevent overlap
                elif self.vel < 0 and self.richting == 'links':  # Moving left
                    self.x = tile.x + tile.width  # Push player right to prevent overlap

        # Check collisions in the vertical direction
        for tile in world.get_collidable_tiles(self.hitbox):
            if self.hitbox.colliderect(tile):
                if self.velocity_y > 0:  # Falling down
                    self.y = tile.y - self.height  # Place the player on top of the tile
                    self.velocity_y = 0  # Stop falling
                    self.jumping = False  # Stop jumping
           
player = Player(100,320,38,68)
#map load in
tmxdata = load_pygame('map.tmx')

class World(object):
    def __init__(self, tmxdata):
        self.tmxdata = tmxdata

    def blit_all_tiles(self,screen, tmxdata, world_offset):
        for layer in tmxdata:
            for tile in layer.tiles():
            #tile[0] ... x grid locatie
            #tile[1] ... y grid locatie
            #tile[2] ... image data for blitting
                x_pixel = tile[0] * 32 + world_offset[0]
                y_pixel = tile[1] * 32 + world_offset[1]
                screen.blit(tile[2], (x_pixel, y_pixel))
                
    def get_collidable_tiles(self, hitbox):
        collidable_tiles = []
        for layer in self.tmxdata:
            for tile in layer.tiles():
                x_pixel = tile[0] * 32
                y_pixel = tile[1] * 32
                tile_rect = pygame.Rect(x_pixel, y_pixel, 32, 32)
                
                if tile == '1' or tile == '8':  # Adjust this based on the collidable tile types
                    collidable_tiles.append(tile_rect)

                if tile_rect.colliderect(hitbox):
                    collidable_tiles.append(tile_rect)
        return collidable_tiles
    
wereld = World(tmxdata)

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

# Scroll logic
scroll = 0
def update_scroll():
    global scroll
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and scroll > 0:
        scroll -= 3
    if key[pygame.K_d] and key[pygame.K_LSHIFT] and player.x > 0:
        scroll -= 4 
    if key[pygame.K_d]:
        scroll += 3
    if key[pygame.K_d] and key[pygame.K_LSHIFT]:
        scroll += 4


class GameLoop:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 432))
        self.clock = pygame.time.Clock()
        self.player = Player(100, 320, 38, 68)
        self.world = World(load_pygame('map.tmx'))
        self.world_offset = [0, -190]
        self.scroll = 0

    def update(self):
        # Update game logic (move player, handle collisions, etc.)
        self.player.update(self.screen, self.world)
        update_scroll()
    
    def draw(self, screen):
        draw_bg()
        self.world.blit_all_tiles(screen, self.world.tmxdata, self.world_offset)  # Draw the world
        self.player.draw(screen)  # Draw player
        pygame.display.update()

# Main game loop
def main():
    game_loop = GameLoop()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_loop.update()  # Update game state
        game_loop.draw(screen)  # Draw the screen
        clock.tick(FPS)  # Limit the frame rate to FPS
        
        pygame.display.update()
        
    pygame.quit()

# Run the game

main()