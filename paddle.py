from settings import *

class paddle():
    def __init__(self,x,y,height,width):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.height=height
        self.width=width
        self.speed=5
    
    def draw(self):
        pygame.draw.rect(screen,white,(self.x, self.y, self.width, self.height))

    def move(self):
        key=pygame.key.get_pressed()
        if(key[pygame.K_UP] and self.y>margin):
            self.y -= self.speed
        if(key[pygame.K_DOWN] and (self.y + self.height) <screen_height):
            self.y += self.speed
 
    def ai(self,pong):
        if self.y+(self.height//2) < pong.y and self.y+self.height < screen_height:
            self.y += self.speed
        
        if self.y+(self.height//2) > pong.y+ 2*pong.radius and self.y > margin:
            self.y -= self.speed

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y





