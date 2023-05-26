import pygame
import sys

from const import * #here * stands for (bau) "all"

class Main:
    
    def __init__(self): #always called when an object is created *¹
        pygame.init() #initializing our pygame module | always necessary
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #here self says about the method its contained in
        pygame.display.set_caption('Chess') #app's caption
        
    def mainloop(self): #to call all other classes
        #while: looping through all the event (as a mouse click or motion, for instance)
        #checking if the user is quitting the app, if yes > follow to sys.exit()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update() #this will update the game's screen
       
main = Main() #main as an instance of the main class
main.mainloop() #*¹ as here