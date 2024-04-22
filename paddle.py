from settings import *

class paddle():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rect=Rect(self.x,self.y,20,100)
        self.speed=5
    
    def draw(self):
        pygame.draw.rect(screen,white,self.rect)

    def move(self):
        key=pygame.key.get_pressed()
        if(key[pygame.K_UP] and self.rect.top>margin):
            self.rect.move_ip(0, -1*self.speed)
        if(key[pygame.K_DOWN] and self.rect.bottom<screen_height):
            self.rect.move_ip(0, 1*self.speed)

    def ai(self,pong):
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0,self.speed)
        
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0,-1*self.speed)






