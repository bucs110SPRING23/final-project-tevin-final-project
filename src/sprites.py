import pygame 

import spriteclass

pygame.init()

SCREEN_WIDTH = 1000 
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

greendinosprite = pygame.image.load("assets/greendinosprite.png").convert_alpha()
sprite_sheet = spriteclass.Sprite(greendinosprite)

BG = (50, 50, 50)

#animation list

animation_list = []
animation_steps = [4, 6, 3, 4]
action = 1  
last_update = pygame.time.get_ticks()
cooldown = 200
frame = 0 
step_counter = 0 

for animation in animation_steps:
    img_list = []
    for _ in range(animation): 
        img_list.append(sprite_sheet.get_image (step_counter, 24, 24, 3, "black"))
        step_counter += 1
    animation_list.append(img_list)

run = True 
while run: 

    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= cooldown: 
        frame += 1
        last_update = current_time 
        if frame >= len(animation_list[action]): 
            frame = 0

    
    screen.blit(animation_list[action][frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a and action < len(animation_list) - 1:
                action -= 1
                frame = 0 
            if event.key == pygame.K_f or event.key == pygame.K_b and action > 0:
                action += 1
                frame = 0 
    pygame.display.update()
pygame.quit()