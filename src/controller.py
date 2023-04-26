import pygame 
from player import Player 


pygame.init() 

SCREEN_W = 1000 
SCREEN_H = 600
screensize = (SCREEN_W, SCREEN_H)

screen = pygame.display.set_mode(screensize) 
pygame.display.set_caption("Object Detection Fighter Game")

background = pygame.image.load("assets\wildwestbackground.jpg")
scaled_background = pygame.transform.scale(background, screensize) 

player_1 = Player(200, 300)
player_2 = Player(700, 300)

run_game = True 
while run_game:
    #load background
    screen.blit(scaled_background, (0,0))

    #player motions
    player_1.motion(SCREEN_W, SCREEN_H) 
    #player_2.motion()

    #spawn players
    player_1.spawn(screen)
    player_2.spawn(screen)

    #COLLISION HANDLING GOES HERE#

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run_game = False 
    pygame.display.update() 

pygame.quit()