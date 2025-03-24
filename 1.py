#importeer de library pygame
import pygame
import math
#pygame initialeren
pygame.init()
# zet de screen erin met de height en width
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game")
# maak een player aan
player = [[100,500,50,50],0]
#player = pygame.Rect((200,250,50,50))

FPS = pygame.time.Clock()
run = True
#game loop en event handeler
while run:
    FPS.tick(60)
    #geef de scherm een kleur
    screen.fill((0,120,250))
    #draw de player in het scherm
    pygame.draw.rect(screen,(255,0,0),player[0])
    #de toetsen die je gebruikt om te bewegen
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player[0][0] -= 5
    if key[pygame.K_d] == True:
        player[0][0] += 5
    if key[pygame.K_SPACE] == True and player[0][1] == 500:
        player[1] = -5   
    player[0][1] += player[1]
    player[1] += 0.1
    if player[0][1] > 500:
        player[0][1] = 500

    #als je op de x klikt word de window gesloten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    #refresh de scherm om de eerdere dingen in te zetten
    pygame.display.update()

pygame.quit()