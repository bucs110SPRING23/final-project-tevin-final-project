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

#spritesheets

huntress_spritesheet = pygame.image.load("assets/huntressfinalspritesheet.png").convert_alpha
darkwizard_spritesheet = pygame.image.load("assets/wizardfinalspritesheet.png").convert_alpha

#number of steps in each animation row

huntress_phases = [5, 7, 8, 8, 2]
darkwizard_phases = [8, 8, 6, 8, 2]

#player variable 

huntress_size = 162 
huntress_data = [huntress_size]
wizard_size = 200 
wizard_data = [wizard_size]

def health_bar(health, x, y): 
    remaining_health = health / 100 
    pygame.draw.rect(screen, "red", (x, y, 400, 25))
    pygame.draw.rect(screen, "green", (x, y, 400 * remaining_health, 25))

player_1 = Player(200, 300, huntress_data, huntress_spritesheet, huntress_phases)
player_2 = Player(700, 300, wizard_data, darkwizard_spritesheet, darkwizard_phases)

run = True
# class Controller: 
#     def __init__(self): 
#         """
#         add docs string later
#         """
    
while run:
    #load background
    screen.blit(scaled_background, (0,0))

    health_bar(player_1.health, 20, 20)
    health_bar(player_2.health, 580, 20)
    #player motions
    player_1.motion(SCREEN_W, SCREEN_H, screen, enemy = player_2) 
    #player_2.motion

    #spawn players
    player_1.spawn(screen)
    player_2.spawn(screen)

    #COLLISION HANDLING GOES HERE#

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 
    pygame.display.update() 


pygame.quit()