import pygame, sys, pygame_gui #importeert de benodigde modules
pygame.init() 

pygame.display.set_caption("Main Menu") #zet de titel van het venster
clock = pygame.time.Clock() #creëert de klok voor de framerate
screen = pygame.display.set_mode((800, 600)) 
font = pygame.font.SysFont(None, 100)

# afbeeldingen van de knoppen
play_image = pygame.image.load("play_button.png").convert_alpha()
exit_image = pygame.image.load("exit_button.png").convert_alpha() #laadt de afbeeldingen vanuit de bestanden en convert_alpha() zorgt voor transparantie

play_image = pygame.transform.scale(play_image, (300, 100))
exit_image = pygame.transform.scale(exit_image, (300, 100))


#nodig voor meerdere vensters
def draw_text(text, font, color, surface, x, y): #functie 1 voldoet
    textobj = font.render(text, 1, color) #maakt van de tekst een afbeelding
    textrect = textobj.get_rect() #zorgt ervoor dat de tekst een rechthoekige afbeelding wordt
    textrect.topleft = (x, y) 
    surface.blit(textobj, textrect) #blit() zorgt ervoor dat de afbeelding op het scherm wordt gezet


#functie voor het hoofd menu
def main_menu(): #functie 2 voldoet
    while True: #While loop voldoet
        screen.fill((70, 130, 180)) #kleurt de achtergrond staalblauw
        draw_text('main menu', font, (0, 0, 0), screen, 220, 50) 
        
        play_rect = play_image.get_rect(topleft=(250, 200)) 
        exit_rect = exit_image.get_rect(topleft=(250, 350))
        
        screen.blit(play_image, play_rect.topleft)
        screen.blit(exit_image, exit_rect.topleft)
        
        mx, my = pygame.mouse.get_pos() #haalt de muispositie op
        
        for event in pygame.event.get(): #loop door alle gebeurtenissen
            if event.type == pygame.QUIT: #als er op het kruisje wordt geclicked ga je uit het spel
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #als een toets wordt ingedrukt
                if event.key == pygame.K_ESCAPE:
                    are_you_sure() #er komt een are you sure venster als je probeert om weg te gaan, dit helpt als je perongeluk iets klikt
            if event.type == pygame.MOUSEBUTTONDOWN: #als er met de muis wordt geklikt
                if event.button == 1:
                    if exit_rect.collidepoint((mx, my)):
                        are_you_sure()
                    if play_rect.collidepoint((mx, my)):
                        username() #als je op start drukt word je eerst naar een andere venster gestuurd
                        
        pygame.display.update() #is nodig om veranderingen zichtbaar te maken
        clock.tick(60) #de framerate is 60


second_font = pygame.font.SysFont(None, 40) #de eerste font is een beetje te groot

yes_image = pygame.image.load("yes_button.png").convert_alpha()
no_image = pygame.image.load("no_button.png").convert_alpha()
yes_image = pygame.transform.scale(yes_image, (75, 75))
no_image = pygame.transform.scale(no_image, (75, 75))

#kleine pop up screen om zeker te maken dat je wil verlaten
def are_you_sure(): #derde functie, dus alle functies voldoen
    global screen #zorgt ervoor dat je de scherm grootte kan veranderen
    screen = pygame.display.set_mode((200, 200)) 
    
    running = True
    while running:
        screen.fill((255, 255, 255))
        draw_text('Are you sure?', second_font, (0, 0, 0), screen, 5, 40)
        
        yes_rect = yes_image.get_rect(topleft=(15, 80))
        no_rect = no_image.get_rect(topleft=(110, 80))

        screen.blit(yes_image, yes_rect.topleft)
        screen.blit(no_image, no_rect.topleft)
        
        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get(): #for loop voldoet
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((800, 600)) #als je dit niet deed dan zou de venster nog steeds zo klein blijven
                    running = False #zorgt ervoor dat het weer terug gaat naar de main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yes_rect.collidepoint((mx, my)):
                        pygame.quit()
                        sys.exit()
                    if no_rect.collidepoint((mx, my)):
                        screen = pygame.display.set_mode((800, 600))
                        running = False
                        
        pygame.display.update()
        clock.tick(60)


#pygame gui manager aanmaken
pymanager = pygame_gui.UIManager((800, 600))

#deze code maakt de tekst invoer veld
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 275), (400, 50)), manager=pymanager, object_id="#input_box")


#gebruikersnaam venster voordat je de game echt kan spelen
def username():
    running = True
    while running:
        screen.fill((70, 130, 180))
        draw_text('Fill in your username', font, (0, 0, 0), screen, 50, 100)
    
        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#input_box":
                # after this you should enter the actual game
                pygame.quit()
                sys.exit()
        
            pymanager.process_events(event) #laat de gui manager de gebeurtenissen afhandelen
        
        pymanager.update(clock.tick(60)/1000) #update de GUI anders, het moest wel gedeeld door duizend zijn anders gebeurde het te vaak
        
        pymanager.draw_ui(screen) #tekent de gui op het scherm
                        
        pygame.display.update()
        clock.tick(60)



main_menu() #the main menu start meteen na het runnen van het script