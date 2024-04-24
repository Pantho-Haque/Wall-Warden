import pygame
from pygame.locals import *


from paddle import paddle
from ball import ball
from draw import *

cpu_paddle=paddle(10 , screen_height//2 - paddle_height//2,paddle_width,paddle_height)
player_paddle=paddle(screen_width-10-paddle_width , screen_height//2 - paddle_height//2 ,paddle_width,paddle_height)
pong=ball(screen_width//2  -10, screen_height//2 )

# Running Process
run =True
while run:
    fpsClock.tick(fps)

    draw_board()
    draw_text("CPU: "+ str(cpu_score) , font , white , 20,15)
    draw_text("Ball Speed: "+ str(abs(pong.speed_x)) , font , white , screen_width//2-100 ,15)
    draw_text("Player: "+ str(player_score) , font , white , screen_width-150 ,15)
    
    cpu_paddle.draw()
    player_paddle.draw()


    if live_ball==True:
        speed_inc+=1
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

    if speed_inc>300:
        speed_inc=0
        if pong.speed_x<0:
            pong.speed_x-=1
        if pong.speed_x>0:
            pong.speed_x+=1
        if pong.speed_y<0:
            pong.speed_y-=1
        if pong.speed_y>0:
            pong.speed_y+=1

    if live_ball==False:
        if winner==0 :
            draw_text("CLICK ANYWHERE TO START", font , white , 100  ,screen_height//2-100)
        if winner==1 :
            draw_text("YOU SCORED!", font , white , 100  ,screen_height//2-100)
            draw_text("CLICK ANYWHERE TO START", font , white , 100  ,screen_height//2-50)
        if winner==-1 :
            draw_text("CPU SCORED!", font , white , 100  ,screen_height//2-100)
            draw_text("CLICK ANYWHERE TO START", font , white , 100  ,screen_height//2-50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run =False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball== False:
            live_ball=True
            pong.reset(screen_width-60 , screen_height//2+50)

    pygame.display.update()



# Quiting the program
pygame.quit()
