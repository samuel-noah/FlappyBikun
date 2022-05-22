import pygame 
from variabel import *

def win():
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bikun With Biskre')
    GAME_SPRITES['OVER'] = pygame.image.load('resources/SPRITES/tamat.png').convert_alpha()
    GAME_SPRITES['RETRY'] = pygame.image.load('resources/SPRITES/retry.png').convert_alpha()
    GAME_SPRITES['HOME'] = pygame.image.load('resources/SPRITES/Home.png').convert_alpha()

    SCREEN.blit(GAME_SPRITES['background'],(0,0))
    SCREEN.blit(GAME_SPRITES['base'],(0,GROUNDY))
    SCREEN.blit(GAME_SPRITES['OVER'], (0,0))
    SCREEN.blit(GAME_SPRITES['RETRY'], (30, 220))
    SCREEN.blit(GAME_SPRITES['HOME'], (30, 280))
    
    pygame.display.update()
           