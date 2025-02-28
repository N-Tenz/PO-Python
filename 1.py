#importeer de library pygame
import pygame
#pygame initialeren
pygame.init()
# zet de screen erin met de height en width
screen = pygame.display.set_mode((800,600))
# maak een player aan
player = [[100,500,50,50],0]
#player = pygame.Rect((200,250,50,50))

clock = pygame.time.Clock()
#game loop
run = True
while run:
    clock.tick(60)
    #event handeler
    #geef de scherm een kleur
    screen.fill((0,120,250))
    #draw de player in het scherm
    pygame.draw.rect(screen,(255,0,0),player[0])
    #de toetsen die je gebruikt om te bewegen
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player[0][0] -= 2
    elif key[pygame.K_d] == True:
        player[0][0] += 2
    elif key[pygame.K_SPACE] == True and player[0][1] == 500:
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
#sluit de window af
pygame.quit()