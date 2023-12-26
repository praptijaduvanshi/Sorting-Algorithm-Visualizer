from tkinter import *
from tkinter import ttk
import random 
import pygame
pygame.init()

#Set up pygame window and global values

class gameInformation:
    BLACK= 0, 0, 0
    WHITE= 255, 255, 255
    GREY= 128, 128, 128
    RED= 255, 0, 0
    GREEN= 0, 255, 0
    BLUE= 0, 0, 255
    BACKGROUND_COLOR= WHITE

    SIDE_PAD=100
    TOP_PAD= 150



def __init__(self, width, height, list):
    self.width= width
    self.height= height
    
    self.window= pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sorting Algorithm Visualizer")
    self.list(list)


def set_list(self,list):
    self.list= list
    self.minimum_val= min(list)
    self.maximum_val= max(list)

    self.block_width= round((self.width - self.SIDE_PAD) / len(list))
    self.block_heigh= round((self.height - self.TOP_PAD) / (self.maximum_val - self.minimum_val))
    self.start_x= self.SIDE_PAD // 2

#Generating starting list
def generate_start_list(n, minimum_val, maximum_val):
    list = []

    for _ in range(n):
        value = random.randint(minimum_val, maximum_val)
        list.append(value)
    
    return list