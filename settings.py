import time
import pygame
from pygame.locals import *

pygame.init()

# defining variabls
live=False
margin =50
fps=60
cpu_score =0
player_score =0
winner = ""
speed_inc=0
font=pygame.font.SysFont("Constantia",30)

#  screen building 
fpsClock= pygame.time.Clock()

screen_width,screen_height = 600,500
paddle_width,paddle_height=15,100
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Wall Warden")


# defining colors in RGB
bg=(50,25,50)
white= (255,255,255)


