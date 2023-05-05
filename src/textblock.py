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

# run = True 
# while run: 

#     screen.fill("black") 

#     TextBlockPopup.end_text(winner = "Player_1", font = pygame.font.SysFont("arialblack", 40), color = "red", x = 200, y = 200)
#     TextBlockPopup.menu_text(text = "get in", font=pygame.font.SysFont("calibri", 40), color = "green", x = 300, y = 400)

#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT: 
#             run == False 
#     pygame.display.update()

# pygame.quit()

        
