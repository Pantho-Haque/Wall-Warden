from settings import *


class ball():
    def __init__(self,x,y):
        self.reset(x,y)

    def draw(self):
        center_x=self.rect.x+self.ball_rad
        center_y=self.rect.y+self.ball_rad
        pygame.draw.circle(screen,white,(center_x,center_y),self.ball_rad)

    def move(self,pp,cp,speed_in=0):
        # self.speed_x-=speed_inc
        # self.speed_y+=speed_inc

        # check for top and bottom 
        if( self.rect.top < margin ):
            self.speed_y *=-1
        if( self.rect.bottom > screen_height ):
            self.speed_y *=-1

        # check for collition with python builtin rectangle collition
        if self.rect.colliderect(pp) or self.rect.colliderect(cp):
            self.speed_x *= -1

        # check for winner

        if( self.rect.left < 0 ):
            self.winner=1
        if( self.rect.right > screen_width ):
            self.winner=-1

        # updating the ball position 

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner

    def reset(self,x,y):
        self.x=x
        self.y=y
        self.ball_rad=8
        self.rect=Rect(self.x,self.y,self.ball_rad*2,self.ball_rad*2)
        self.speed_x=-4
        self.speed_y= 4
        self.winner=0   
        """
            winner =  1 -> player has scored
                   = -1 -> cpu has scored
        """


