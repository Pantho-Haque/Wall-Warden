from settings import *

def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen,white,(0,margin),(screen_width,margin))

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))