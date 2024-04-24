import pygame
from pygame.locals import *


from paddle import paddle
from ball import ball
from draw import *

cpu_paddle=paddle(10 , screen_height//2 - paddle_height//2,paddle_height,paddle_width)
player_paddle=paddle(screen_width-10-paddle_width , screen_height//2 - paddle_height//2 ,paddle_height,paddle_width)
pong=ball(screen_width//2  -10, screen_height//2 ,7 )

# Running Process
run =True
while run:
    fpsClock.tick(fps)

    if live : 
        draw_board()

        cpu_score_text=font.render(f"CPU: {cpu_score}",1,white)
        screen.blit(cpu_score_text, (screen_width//4 - cpu_score_text.get_width()//2,15))

        player_score_text=font.render(f"Player: {player_score}",1,white)
        screen.blit(player_score_text, (screen_width*(3/4) - player_score_text.get_width()//2,15))

        draw_text("Ball Speed: "+ str(abs(pong.speed_x)) , font , white , screen_width//2-80 ,15)

        # draw_text("CPU: "+ str(cpu_score) , font , white , 20,15)
        # draw_text("Player: "+ str(player_score) , font , white , screen_width-150 ,15)
        
        cpu_paddle.draw()
        player_paddle.draw()

        pong.draw()
        speed_inc+=1
        player_paddle.move()
        cpu_paddle.ai(pong)
        player_score,cpu_score=pong.move(player_paddle,cpu_paddle)

        if cpu_score==3:
            winner="CPU"
            live=False
        elif player_score==3:
            winner="You"
            live=False 
        # if winner==0 :
        #     player_paddle.move()
        #     cpu_paddle.ai(pong)
        #     pong.draw()
        # else:
        #     live_ball=False
        #     if winner==1:
        #         player_score+=1
        #     elif winner==-1:
        #         cpu_score+=1

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

        # if live_ball==False:
        #     if winner==0 :
        #         draw_text("CLICK ANYWHERE TO START", font , white , 100  ,screen_height//2-100)
        #     if winner==1 :
        #         draw_text("YOU SCORED!", font , white , 100  ,screen_height//2-100)
        #         draw_text("CLICK ANYWHERE TO START", font , white , 100  ,screen_height//2-50)
        #     if winner==-1 :
        #         draw_text("CPU SCORED!", font , white , 100  ,screen_height//2-100)
        #         draw_text("CLICK ANYWHERE TO START", font , white , 100  ,screen_height//2-50)
    else :
        if winner == "" :
            initial_screen()
        else:
            speed_inc=0
            winning_screen(winner)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run =False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and live== False:
            live=True
            winner=""
            pong.score=[0,0]
            # player_paddle.reset()
            # cpu_paddle.reset()
            # pong.reset()
            

    

    pygame.display.update()



# Quiting the program
pygame.quit()
