from fuzzywuzzy import fuzz
import numpy as np
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
 
    # def ai(self,pong):
    #     if self.y+(self.height//2) < pong.y and self.y+self.height < screen_height:
    #         self.y += self.speed
        
    #     if self.y+(self.height//2) > pong.y+ 2*pong.radius and self.y > margin:
    #         self.y -= self.speed
    def ai(self, pong):
        # Define position categories and thresholds (change these to adjust sensitivity)
        position_categories = ["very_low", "low", "medium", "high", "very_high"]
        thresholds = [60, 75, 90]  # Adjust thresholds for desired responsiveness

        # Calculate ball position string based on relative position to paddle
        ball_position_y = pong.y - (self.y + self.height / 2)
        ball_position_str = "medium"  # Default

        if ball_position_y < -self.height / 3:
            ball_position_str = "very_low"
        elif ball_position_y < 0:
            ball_position_str = "low"
        elif ball_position_y > self.height / 3:
            ball_position_str = "very_high"
        elif ball_position_y > 0:
            ball_position_str = "high"

        # Evaluate similarity scores for each category
        similarities = {}
        for category in position_categories:
            similarities[category] = fuzz.partial_ratio(ball_position_str, category)

        # Choose action with highest similarity score (adjust logic for more complex behavior)
        chosen_action = max(similarities, key=similarities.get)
        movement = "none"

        if chosen_action in ["very_low", "low"] and similarities[chosen_action] > thresholds[0]:
            movement = "up"
        elif chosen_action in ["very_high", "high"] and similarities[chosen_action] > thresholds[1]:
            movement = "down"

        if movement == "up":
            self.y -= self.speed
        elif movement == "down":
            self.y += self.speed
            # Ensure paddle stays within screen boundaries
            self.y = max(margin, min(self.y, screen_height - self.height))

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y





