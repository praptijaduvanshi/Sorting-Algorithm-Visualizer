from tkinter import *
from tkinter import ttk
import random 
import pygame
pygame.init()

pygame.font.get_fonts()
#Set up pygame window and global values

class gameInformation:
    BLACK= 0, 0, 0
    WHITE= 255, 255, 255
    GREY= 128, 128, 128
    RED= 255, 0, 0
    GREEN= 0, 255, 0
    BLUE= 0, 0, 255
    BACKGROUND_COLOR= WHITE

    GRADIENTS = [
        (169, 124, 192),
        (203, 178, 216),
        (229, 214, 236)
    ]

    FONT= pygame.font.SysFont("Arial", 30)
    FONT= pygame.font.SysFont("Arial", 40)

    SIDE_PAD=100
    TOP_PAD= 150

    def __init__(self, width, height, list):
        self.width= width
        self.height= height
        
        self.window= pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)

    def set_list(self,list):
        self.list= list
        self.minimum_val= min(list)
        self.maximum_val= max(list)

        self.block_width= round((self.width - self.SIDE_PAD) / len(list))
        self.block_height= round((self.height - self.TOP_PAD) / (self.maximum_val - self.minimum_val))
        self.start_x= self.SIDE_PAD // 2

#Generating starting list
def generate_start_list(n, minimum_val, maximum_val):
    list = []

    for _ in range(n):
        value = random.randint(minimum_val, maximum_val)
        list.append(value)
    
    return list

#General screen
def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    draw_list(draw_info)
    pygame.display.update()
   
#List details screen for sorting
def draw_list(draw_info):
    list= draw_info.list 

    for i, val in enumerate(list):
        x= draw_info.start_x + i * draw_info.block_width
        y= draw_info.height - (val - draw_info.minimum_val) * draw_info.block_height

        color= draw_info.GRADIENTS[i % 3]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

#Render the screen, set up main event loop
def main():
    run = True
    clock=  pygame.time.Clock()

    n= 50
    minimum_val= 0
    maximum_val= 100

    list= generate_start_list(n,minimum_val,maximum_val)
    draw_info= gameInformation(800, 600, list)
    sorting= False
    ascending = True

    while run:
        clock.tick(60)
        draw(draw_info)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                list= generate_start_list(n,minimum_val,maximum_val)
                draw_info.set_list(list)
                sorting= False

            elif event.key == pygame.K_SPACE and sorting== False:
                sorting = True
            
            elif event.key == pygame.K_a and not sorting:
                ascending = True
                
            elif event.key == pygame.K_d and not sorting:
                ascending= False
    

    pygame.quit

if  __name__== "__main__":
    main()


