import pygame 

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 495
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'resources\SPRITES\\bikun3.png'
BACKGROUND = 'resources\SPRITES\\GerbangUI.png'
PIPE = 'resources\SPRITES\Pipe3.png '
DELAY = 5
FPSCLOCK = pygame.time.Clock() #for controlling the FPS