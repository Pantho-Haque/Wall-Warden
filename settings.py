import pygame
from pygame.locals import *

pygame.init()

# defining variabls
live_ball=False
margin =50
fps=60
cpu_score =0
player_score =0
winner =0 
font=pygame.font.SysFont("Constantia",30)
cmd="Click to begin"

#  screen building 
fpsClock= pygame.time.Clock()
screen_height=500
screen_width=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")


# defining colors in RGB
bg=(50,25,50)
white= (255,255,255)


