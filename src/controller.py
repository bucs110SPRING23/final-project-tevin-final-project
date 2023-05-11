import pygame 
from player import Player

pygame.init() 

SCREEN_W = 1000 
SCREEN_H = 600 
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
background = pygame.image.load("assets/wildwestbackground.jpg").convert_alpha()
f1_img = pygame.image.load("assets/kengood.png").convert_alpha()
f2_img = pygame.image.load("assets/ryugood.png").convert_alpha()
fighter_1 = Player(1, 200, 200, f1_img) 
fighter_2 = Player(2, 700, 200, f2_img)
windowcap = pygame.display.set_caption("Object Detection Street Fighter Clone")


class Controller(): 

    def __init__(self):
        pass
    def introloop(): 
        """
        This function runs a temporary intro screen. The user presses the space bar to exit the screen and begin the game. It does not work properly. 
        Args:None 
        Returns: None
        
        """
        intro_img = pygame.image.load("assets/introscreen.png").convert_alpha()
        screen.blit(intro_img, (0, 0))
        key = pygame.key.get_pressed() 
        if key[pygame.K_SPACE]: 
            pygame.time.wait(10000)
            pygame.display.update() 
        else: 
            screen.blit(intro_img, (0,0))

    def draw_screen(): 
        """
        This function sets up the screen for the game. 
        Args: none 
        Returns: none 
        
        """
        scaled_bg = pygame.transform.scale(background, (SCREEN_W, SCREEN_H))
        screen.blit(scaled_bg, (0,0))

    def healthbars(health, x, y):
        """ 
        This function constructs and updates the health bars. When either player's health bar reaches zero, the KO image blits to the screen.
        Args: health, x, y (all from player class) 
        Returns: none
        """
        health_loss = health / 200
        pygame.draw.rect(screen, "red", (x, y, 400, 30))
        pygame.draw.rect(screen, "green", (x, y, 400 * health_loss, 30))
        if health == 0: 
            koimage = pygame.image.load("assets/ko.png")
            screen.blit(koimage, (500, 300))
            pygame.time.wait(5000)
        
    


    




    ## GAMELOOP ## 
    run = True 
    while run: 

        introloop()
        draw_screen()
        healthbars(fighter_1.health, 20, 20)
        healthbars(fighter_2.health, 580, 20)
        fighter_1.spawnplayer1(screen)
        fighter_1.move(SCREEN_W, SCREEN_H, screen, fighter_2)
        #fighter_1.attack(enemy = fighter_2, a2impact = 10)
        fighter_2.spawnplayer2(screen) 
        fighter_2.move(SCREEN_W, SCREEN_H, screen, fighter_1)
        #fighter_1.attack(enemy = fighter_2, a2impact = 10)

        ## EVENT HANDLER ##
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False 
        pygame.display.update()
    pygame.quit()