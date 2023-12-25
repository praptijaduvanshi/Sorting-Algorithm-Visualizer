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

def __init__(self, width, height, list):
    self.width= width
    self.height= height
    
    self.window= pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sorting Algorithm Visualizer")
    self.list(list)


def set_list(self,list):
    pass