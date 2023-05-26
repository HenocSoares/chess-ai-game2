import pygame

from const import *

class Game:
    
    def __init__(self):
        pass
        
    #Show methods.    
        
    def show_bg(self, surface): #this surface will be the self.screen (from main)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                else:
                    color = (119, 154, 88) #dark green
                
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE) #rectangle in py: tuple that has 4 params | x axis, y axis, last 2 are: widht + height
                
                pygame.draw.rect(surface, color, rect)