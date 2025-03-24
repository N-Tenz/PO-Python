import pygame
from main_menu import *
from Game import *


class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((800,432))
        self.clock = pygame.time.Clock()
        self.run = True
        self.playing = False
        self.game_loop = None  # Will hold the instance of the game loop once the game starts
        
    def new(self):
        #start game
        self.playing = True
        self.game = main()
    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.playing = False
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#input_box":
                self.new()  # Start the game once the username is entered
    def update(self):
        if self.playing == True:
            self.game_loop.update()  # Update game loop if playing
    
    def main(self):
        self.intro()  # Start by showing the intro (main menu)
        while self.run:
            self.event()
            self.update()
            self.draw()
    
    def draw(self):
        if self.playing:
            self.game_loop.draw(self.screen)  # Draw game if playing
        pygame.display.update()

    def intro(self):
        intro = True
        if main_menu(): 
            self.playing = True 
            self.new() 
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.run = False
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#input_box":
                    intro = False  # Exit the intro once the username is entered
                    self.playing = True  # Start the game loop
                    self.new()  # Start the game

game = Game()
game.main()

pygame.quit()