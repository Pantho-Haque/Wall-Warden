import random

print()
from settings import *


class ball():
    speed = random.randint(3, 6)
    score=[0,0]
    def __init__(self,x,y,radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.speed_x = -1*self.speed
        self.speed_y = self.speed

    def draw(self):
        pygame.draw.circle(screen,white,(self.x,self.y),self.radius)

    def move(self,pp,cp,speed_in=0):
        # self.speed_x-=speed_inc
        # self.speed_y+=speed_inc



        # check for top and bottom 
        if( self.y-self.radius <= margin ) or ( self.y+self.radius > screen_height ):
            self.speed_y *=-1

        # check for collition with python builtin rectangle collition
        # if self.rect.colliderect(pp) or self.rect.colliderect(cp):
        #     self.speed_x *= -1
        
        

        if self.y >= cp.y and self.y < cp.y+cp.height:
            if self.x-self.radius  < cp.x +cp.width :
                self.speed_x *= -1

                middle_y=cp.y + cp.height //2
                diff_y=middle_y-self.y
                reduction_factor = (cp.height//2) // self.speed
                self.speed_y= -1* diff_y // reduction_factor

        
        if self.y >= pp.y and self.y < pp.y+pp.height:
            if self.x + self.radius > pp.x:
                self.speed_x *= -1

                middle_y=pp.y + pp.height //2
                diff_y=middle_y-self.y
                reduction_factor = (pp.height//2) // self.speed
                self.speed_y=-1* diff_y // reduction_factor-1
        
        if self.x<0:
            self.score[0]+=1
            self.reset()
        elif self.x>screen_width:
            self.score[1]+=1
            self.reset()



        # updating the ball position 
        self.x += self.speed_x
        self.y += self.speed_y
        return self.score

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.speed_x =-1*self.speed
        self.speed_y= self.speed
        time.sleep(0.5)


