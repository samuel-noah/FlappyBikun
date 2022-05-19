
import pygame
from pygame.locals import * #Basic Pygame Imports
from variabel import *
from function import *
  
if __name__ == "__main__":

    pygame.init() #Initializing the Modules of Pygame 

    pygame.display.set_caption('Flappy Bikun With Biskre')
     #Setting the Caption of The Game

    #### LOADING THE SPRITES ####

    GAME_SPRITES['numbers'] = (
        pygame.image.load('resources\SPRITES\\0.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\1.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\2.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\3.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\4.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\5.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\6.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\7.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\8.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\9.png').convert_alpha(),
    
    ) 
    
    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['message'] = pygame.image.load('resources\SPRITES\message3.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('resources\SPRITES\\base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        
        
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), #### UPPER PIPES, WE JUST ROTATED THE PIPE BY 180deg
    pygame.image.load(PIPE).convert_alpha()   #### LOWER PIPES  
    )



    #Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('resources\AUDIO\die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('resources\AUDIO\hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('resources\AUDIO\point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('resources\AUDIO\swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('resources\AUDIO\wing.wav')
    while True:
        welcomeScreen() #Shows a welcomescreen to the user until they starts the game
        mainGame() #This is our main game funtion
