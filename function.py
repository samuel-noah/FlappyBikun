from variabel import *
import pygame
import random
from pygame.locals import *
import sys
import pygame_textinput




def welcomeScreen():

    #IT WIll Show Welcome Screen TO user to make the game more interactive and interesting
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2
    messagex = int(SCREENWIDTH - GAME_SPRITES['message'].get_width())/2
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0
    FONT = pygame.font.SysFont('monospace', 32)
    text_input = pygame_textinput.TextInputVisualizer()
    events = pygame.event.get()

    
    
    
    
    # Drawing Rectangle for playbutton
    playbutton = pygame.Rect(108,222,68,65)

    while True:
        text_input.update(events)
        SCREEN.blit(text_input.surface,(30,50))
        
        for event in events:
            
             #If user clicks on Cross or presses the Escape button Close the Game
            if event.type== QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if pygame.mouse.get_pos()[0] > playbutton[0]  and pygame.mouse.get_pos()[0] < playbutton[0] + playbutton[2]:
                if pygame.mouse.get_pos()[1] > playbutton[1]  and pygame.mouse.get_pos()[1] < playbutton[1] + playbutton[3]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            if playbutton.collidepoint(pygame.mouse.get_pos()): #checking if mouse is collided with the play button
            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #checking if mouse has been clicked
                    mainGame()
                    

            else :

                # SCREEN.blit(GAME_SPRITES['background'],(0,0))
                
                
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                #Adding INRO Music
                pygame.mixer.music.load('resources/AUDIO/INTROMUSIC.mp3')
                pygame.mixer.music.play()
                pygame.display.update()
                FPSCLOCK.tick(FPS)


playerScore = []

def maxScore():
    maxScore = 0
    playerScore.append(score)
    for i in playerScore:
        if i > maxScore:
            maxScore = i
    return maxScore

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        pygame.mixer.music.stop()
        print('Max Score',maxScore())
        gameOver()
        
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()-20):
            GAME_SOUNDS['hit'].play()
            print(playerx, pipe['x'],)
            pygame.mixer.music.stop()
            print('Max Score',maxScore())
            gameOver()
            

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()-20:
            GAME_SOUNDS['hit'].play()
            pygame.mixer.music.stop()
            print('Max Score',maxScore())
            gameOver()

    return False




def gameOver():
    FONT = pygame.font.SysFont('monospace', 32)
    display = FONT.render('Best Score: ' + str(maxScore()), True, (255,255,255))
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bikun With Biskre')
    GAME_SPRITES['OVER'] = pygame.image.load('resources/SPRITES/gameover2.png').convert_alpha()
    GAME_SPRITES['RETRY'] = pygame.image.load('resources/SPRITES/retry.png').convert_alpha()
    GAME_SPRITES['HOME'] = pygame.image.load('resources/SPRITES/Home.png').convert_alpha()
    SCREEN.blit(display, (30,50))
    # SCREEN.blit(GAME_SPRITES['background'],(0,0))
    SCREEN.blit(GAME_SPRITES['base'],(0,GROUNDY))
    SCREEN.blit(GAME_SPRITES['OVER'], (0,0))
    SCREEN.blit(GAME_SPRITES['RETRY'], (30, 220))
    SCREEN.blit(GAME_SPRITES['HOME'], (30, 280))
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
 
            if event.type == KEYDOWN and event.key == K_SPACE:
                mainGame()
  
            ### RETRY BUTTON
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if pygame.mouse.get_pos()[0]>30 and pygame.mouse.get_pos()[0]< 30+GAME_SPRITES['RETRY'].get_width():
                if pygame.mouse.get_pos()[1]>220 and pygame.mouse.get_pos()[1]< 220+GAME_SPRITES['RETRY'].get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        
                        mainGame()
                      
            ### HOME BUTTON
            if pygame.mouse.get_pos()[0]>30 and pygame.mouse.get_pos()[0]< 30+GAME_SPRITES['HOME'].get_width():
                if pygame.mouse.get_pos()[1]>280 and pygame.mouse.get_pos()[1]< 280+GAME_SPRITES['HOME'].get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        welcomeScreen()
           

def getRandomPipe():
    """
    generating positions of the two pipes one upper pipe and other lower pipe 
    To blit on the Screen
    """
                
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/4.5
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 *offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [ 
        {'x': pipeX, 'y': -y1}, #Upper Pipes
        {'x': pipeX, 'y': y2}   #Lower Pipes
    ]
    return pipe 

def mainGame():
    
    #ADDING THE BACKGROUND MUSIC
    pygame.mixer.music.stop()
    pygame.mixer.music.load('resources/AUDIO/BGMUSIC.mp3')
    pygame.mixer.music.play()
    global score
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int (SCREENHEIGHT/2)
    basex = 0

    
    #Creating upper and Lower Pipes for the game
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    
    # Upper pipe List
    upperPipes = [
        {'x':SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x':SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[0]['y']}
    ]

    #lists of Lower Pipe
    lowerPipes = [
        {'x':SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x':SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[1]['y']}
    ]

    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10  
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping
    

    while True:

        for event in pygame.event.get():
           
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            return     

        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()
            if score == 0:
                GAME_SPRITES['background'] = pygame.image.load('resources/SPRITES/GerbangUI.png')
            if score == 2:
                GAME_SPRITES['background'] = pygame.image.load('resources/SPRITES/GerbangUI.png')
            if score == 3:
                GAME_SPRITES['background'] = pygame.image.load('resources/SPRITES/DanauUI.png')
            if score == 4:
                GAME_SPRITES['background'] = pygame.image.load('resources/SPRITES/JembatanTexas.png')
            if score == 5:
                GAME_SPRITES['background'] = pygame.image.load('resources/SPRITES/PerpustakaanNasional.png')
            if score == 6:
                GAME_SPRITES['background'] = pygame.image.load('resources/SPRITES/RektoratUI.png')
        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))


        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)