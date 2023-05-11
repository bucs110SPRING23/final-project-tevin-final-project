import pygame 
from detections import Detections

pygame.init() 
class Player():     
    def __init__(self, player, x, y, img):
        """ 
        This initializes all of the variables attributed to a player in the game.
        Args: self, player(int), x, y (ints), img(pygame)
        Returns: none 
        
        """
        self.player = player
        #self.enemy = enemy
        self.pos_flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.jump_vel = 0
        self.jump = False
        self.isattacking = False
        self.attack_type = 0
        self.health = 200
        self.img_w = 160 
        self.img_h = 320
        self.p1img = pygame.image.load("assets/kengood.png").convert_alpha()
        self.p2img = pygame.image.load("assets/ryugood.png").convert_alpha()


    def move(self, screen_w, screen_h, surface, enemy):

        """
        This function controls motion across the screen and keeps both players on the screen. 
        Args: self, screen width and height(ints), surface(screen handled by controller), enemy(int 1 or 2)
        Returns: none
        """
        # standard motion variable
        MOTION_VAR = 10 
        GRAV = 1
        x_pos = 0 
        y_pos = 0 

        #get keypresses 
        key = pygame.key.get_pressed()

        # check if player is attacking 
        if self.isattacking == False:
            if self.player == 1: 
                #self.enemy == 2
                #motion controls
                if key[pygame.K_b]: 
                    x_pos = -MOTION_VAR
                if key[pygame.K_f]: 
                    x_pos = MOTION_VAR

                #jumping controls 
                if key[pygame.K_j] and self.jump == False:
                    self.jump_vel = -25 
                    self.jump = True

                #attack controls
                if key[pygame.K_g] or key[pygame.K_h]:
                    self.attack(enemy)
                    if key[pygame.K_g]:
                        pygame.time.wait(200)
                        self.attack_type = 1
                        self.isattacking = False 
                    if key[pygame.K_h]:
                        pygame.time.wait(200)
                        self.attack_type = 2
                        self.isattacking = False 

            elif self.player == 2:
                #self.enemy == 1 
                #motion controls
                if key[pygame.K_LEFT]: 
                    x_pos = -MOTION_VAR
                if key[pygame.K_RIGHT]: 
                    x_pos = MOTION_VAR
                #jumping controls 
                if key[pygame.K_UP] and self.jump == False:
                    self.jump_vel = -25 
                    self.jump = True
                #attack controls
                if key[pygame.K_RALT] or key[pygame.K_RSHIFT]:
                    self.attack(enemy)
                    if key[pygame.K_RALT]:
                        pygame.time.wait(200)
                        self.attack_type = 1
                        self.isattacking = False 
                    if key[pygame.K_RSHIFT]:
                        pygame.time.wait(200)
                        self.attack_type = 2
                        self.isattacking = False 



        self.jump_vel += GRAV
        y_pos += self.jump_vel

        #keep player on screen 
        if self.rect.left + x_pos < 0: 
            x_pos = 0 - self.rect.left 
        if self.rect.right + x_pos > screen_w: 
            x_pos = screen_w - self.rect.right
        if self.rect.bottom + y_pos > screen_h - 220:
            self.jump_vel = 0 
            y_pos = screen_h - 220 - self.rect.bottom
            self.jump = False

        # players face each other 
        if enemy.rect.centerx > self.rect.centerx: 
            self.pos_flip = False 
        else: 
            self.pos_flip = True 
        
        #update position on screen
        self.rect.x += x_pos 
        self.rect.y += y_pos

    def attack(self, a2impact, enemy):
        """ 
        This controls the attack boundary and the attack and damage states the players utilize.
        args: self, surface(screen handled by controller), attack 2 impact (int from object detection), enemy(int 1 or 2)
        returns: none
        
        """
        # if self.player == 1: 
        #     enemy = fighter_2
        # elif self.player==2: 
        #     enemy = fighter_1
        #a2impact = Detections.object_detection()
        self.isattacking = True 
        attack_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.pos_flip), self.rect.y, 160, 180)
        #pygame.draw.rect(surface, "red", attack_rect)
        if attack_rect.colliderect(enemy.rect) and self.attack_type == 1:
            enemy.health -= 5
        elif attack_rect.colliderect(enemy.rect) and self.attack_type == 2:
            enemy.health -= a2impact


    
    def spawnplayer1(self, surface): 

        """
        This function blits player 1 onto the screen
        Args: self, surface(screen from controller)
        Returns: none

        """
        #p1rect = pygame.draw.rect(surface, 'green', self.rect)
        surface.blit(self.p1img, (self.rect.x, self.rect.y))
        
        
    def spawnplayer2(self, surface): 

        """
        This function blits player 2 onto the screen
        Args: self, surface(screen from controller)
        Returns: none

        """
        #p2rect = pygame.draw.rect(surface, 'green', self.rect)
        surface.blit(self.p2img, (self.rect.x, self.rect.y))
        
        
    
        

