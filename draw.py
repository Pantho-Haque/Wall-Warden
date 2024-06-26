from settings import *

def initial_screen():
    screen.fill(bg)
    draw_text("CLICK ANYWHERE TO START", font , white , 100  ,screen_height//2-50)

def winning_screen(winner):
    screen.fill(bg)
    draw_text(winner + " Win !", font , white , 100  ,screen_height//2-50)


def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen,white,(0,margin),(screen_width,margin))
    for i in range(10,screen_height,screen_height//20):
        if i%2 ==1:
            continue
        pygame.draw.rect(screen,white,(screen_width//2 -5,i+margin,3,screen_height//20))

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))