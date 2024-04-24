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