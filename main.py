
import pygame 
from player import Player
from detections import Detections
from controller import Controller

def main(): 
    pygame.init() 

    SCREEN_W = 1000 
    SCREEN_H = 600 
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    background = pygame.image.load("assets/wildwestbackground.jpg").convert_alpha()
    f1_img = pygame.image.load("assets/kengood.png").convert_alpha()
    f2_img = pygame.image.load("assets/ryugood.png").convert_alpha()
    fighter_1 = Player(1, 200, 200, f1_img, 2) 
    fighter_2 = Player(2, 700, 200, f2_img, 1)
    windowcap = pygame.display.set_caption("Object Detection Street Fighter Clone")
    Controller()

if __name__ == '__main__':
    main()