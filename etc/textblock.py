import pygame 
pygame.init()

screen = pygame.display.set_mode((1000, 600))

class TextBlock(): 
    def __init__(self): 
        self.font = pygame.font.SysFont("arialblack", 40)
        self.color = "red" 
    def menu_text(text, font, color, x, y): 
        text = "menu text"
        textblock = font.render(text, True, color) 
        screen.blit(textblock, (x, y))
    def end_text(winner, font, color, x, y): 
        winner = str(winner)
        textblock = font.render(winner + " IS THE WINNER!", True, color) 
        screen.blit(textblock, (x, y))

        
