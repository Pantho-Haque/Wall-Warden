import pygame
from pygame.locals import *


from paddle import paddle
from ball import ball
from draw import *

player_paddle=paddle(screen_width-40 , screen_height//2)
cpu_paddle=paddle(20 , screen_height//2)
pong=ball(screen_width-60 , screen_height//2+50)

# Running Process
run =True
while run:
    fpsClock.tick(fps)

    draw_board()
    draw_text(cmd, font , white , 20,15)
    draw_text("CPU: "+ str(cpu_score) , font , white , 20,65)
    draw_text("Player: "+ str(player_score) , font , white , screen_width-150 ,65)
    
    cpu_paddle.draw()
    player_paddle.draw()
    


    if live_ball==True:
        winner = pong.move(player_paddle,cpu_paddle)
        if winner==0 :
            player_paddle.move()
            cpu_paddle.ai(pong)
            pong.draw()
            cmd="use arrow to play"
        else:
            live_ball=False
            if winner==1:
                player_score+=1
            elif winner==-1:
                cpu_score+=1
            cmd="Click to Begin"


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run =False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball== False:
            live_ball=True
            pong.reset(screen_width-60 , screen_height//2+50)

    pygame.display.update()



# Quiting the program
pygame.quit()
