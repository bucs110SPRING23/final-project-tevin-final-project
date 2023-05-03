import pygame 


pygame.init() 



class Player(): 
    def __init__(self, x, y, data, spritesheet, animation):
        self.rect = pygame.Rect((x, y, 70, 170))
        self.jump_velocity = 0
        self.flip = False
        self.jump = False
        self.attacking = False
        self.attack_style = 0
        self.health = 100
        self.size = data[0]

    def load_sprites(self, spritesheet, phases): 
        y = 0
        for animation in phases: 
            img_list = []
            for x in range(animation): 
                individual_img = spritesheet.subsurface(x * self.size, 0, self.size, self.size)
                img_list.append(individual_img)
            y += 1

    def motion (self, screen_w, screen_h, surface, enemy): 
        SPEED = 2
        GRAV = 2
        x_pos = 0 
        y_pos = 0

        keypress = pygame.key.get_pressed() 

        #player_1 ctrls = f, b, space for jump 
        #player_2 ctrls = leftarrow, rightarrow, uparrow for jump

        ## KEY CONTROLLED MOTION ##
        if self.attacking == False:
            if keypress[pygame.K_b]: 
                x_pos = -SPEED
            if keypress[pygame.K_f]: 
                x_pos = SPEED
            if keypress[pygame.K_j] and self.jump == False: 
                self.jump_velocity = -20
                self.jump = True #come back to this

            ## ATTACKS - Regular and Special ## p1a = reg, p1s = spec; p2shift = reg, p2enter = spec
            if keypress[pygame.K_a] or keypress[pygame.K_s]: 
                self.attack(surface, enemy) # ** 
                # attack types # 
                if keypress[pygame.K_a]: 
                    self.attack_style = 1 
                if keypress[pygame.K_s]: 
                    self.attack_style = 2
        

        ## COME BACK DOWN AFTER JUMP ##
        self.jump_velocity += GRAV
        y_pos += self.jump_velocity

        ## KEEP PLAYER ON SCREEN ## 

        if self.rect.left + x_pos < 0: 
            x_pos = 0 - self.rect.left 
        if self.rect.right + x_pos > screen_w: 
            x_pos = screen_w - self.rect.right
        if self.rect.bottom + y_pos > (screen_h - 120): 
            self.jump_velocity = 0 
            self.jump = False
            y_pos = (screen_h - 120 - self.rect.bottom)
       
        # keep players facing each other 

        if enemy.rect.centerx > self.rect.centerx:
            self.flip = False 
        else: 
            self.flip = True 
        ## UPDATE PLAYER POSITION ##
        self.rect.x += x_pos
        self.rect.y += y_pos

    def attack(self, surface, enemy): 
        self.attacking = True
        attacker = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        #collision detector
        if attacker.colliderect(enemy.rect):
            enemy.health -= 10
        pygame.draw.rect(surface, (0, 210, 111), attacker)

    def spawn(self, surface): 
        pygame.draw.rect(surface, (225, 100, 0), self.rect)
