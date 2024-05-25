import time
import pygame
from pygame.locals import *

pygame.init()

# Defining variables
live = False
margin = 50
fps = 10533  # Set to a more reasonable value for performance
cpu_score = 0
player_score = 0
winner = ""
speed_inc = 0
font = pygame.font.SysFont("Constantia", 30)

# Screen building
fpsClock = pygame.time.Clock()

screen_width, screen_height = 600, 500
paddle_width, paddle_height = 15, 100
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Wall Warden")

# Defining colors in RGB
bg = (50, 25, 50)
white = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def initial_screen():
    screen.fill(bg)
    draw_text("CLICK ANYWHERE TO START", font, white, 100, screen_height // 2 - 50)

def winning_screen(winner):
    screen.fill(bg)
    draw_text(winner + " Win!", font, white, 100, screen_height // 2 - 50)

def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))
    for i in range(10, screen_height, screen_height // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(screen, white, (screen_width // 2 - 5, i + margin, 3, screen_height // 20))


def classify_y(y):
    if y < 50: return 'A'
    elif y < 100: return 'B'
    elif y < 150: return 'C'
    elif y < 200: return 'D'
    elif y < 250: return 'E'
    elif y < 300: return 'F'
    elif y < 350: return 'G'
    elif y < 400: return 'H'
    elif y < 450: return 'I'
    else: return 'J'

def classify_yspeed(ys):
    if ys < -6: return 'a'
    elif ys < -4: return 'b'
    elif ys < -2: return 'c'
    elif ys < -0.5: return 'd'
    elif ys < 2: return 'e'
    elif ys < 4: return 'g'
    elif ys < 6: return 'h'
    else: return 'i'

def classify_xdist(x):
    if x < 100: return 'a'
    elif x < 200: return 'b'
    elif x < 300: return 'c'
    elif x < 400: return 'd'
    elif x < 500: return 'e'
    else: return 'f'

    
ypos = [12, 50, 100, 150, 200, 250, 300, 350, 400,450]
yspeed = [-7.5, -6, -4, -2, -0.5, 0.5, 2, 4, 6, 7.5]
xdist = [550, 500, 400, 300, 200, 100, 40]

ball_positions = [(x, y, ys) for y in ypos for ys in yspeed for x in xdist]
results = []
prevy=12
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and not live:
            live = True
    
    if live:
        
        for pos in ball_positions:
            xi,yi,ysi=x, y, ys = pos
            if(prevy<=y):
                prevy=y
            else:
                live=False
            y+=margin
            while x >= 0:
                draw_board()
                pygame.draw.circle(screen, white, (x, int(y)), 7)
                pygame.display.flip()
                fpsClock.tick(fps)

                # Update ball position
                if (y<=margin) or (y + 7 >screen_height):
                    ys *= -1

                x += -4
                y += ys

                # Check if ball crosses x < 21
                if x < 21:
                    print(yi, ysi, xi , y)
                    results.append([classify_y(yi),classify_yspeed (ysi), classify_xdist(xi) , classify_y(y)])
                    break
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                        live = False
                        break
                if not running or not live:
                    break
            if not running or not live:
                break
        if not running or not live:
            break
    else:
        initial_screen()
        pygame.display.flip()
        fpsClock.tick(fps)

pygame.quit()

# Output the results
print("Results:", results)
rulebook=[]
for index in range(len(results)):
    value = results[index]
    rulebook.append([
        f'rule{index}=min(y_mem["{value[0]}"], speed_mem["{value[1]}"],dist_mem["{value[2]}"])',
        value[3]
    ])

for i in rulebook:
    print(i[0])

# Initialize the degree dictionary
degree = {
    "A": "",
    "B": "",
    "C": "",
    "D": "",
    "E": "",
    "F": "",
    "G": "",
    "H": "",
    "I": "",
    "J": ""
}

# Populate the degree dictionary
for entry in rulebook:
    rule, y_final = entry
    rule_part = rule.split('=')[0]  # Extract the part before the '=' sign
    degree[y_final] += rule_part + ", "  # Concatenate with a comma

# Add "max(" and ")" and remove trailing comma
for key, value in degree.items():
    degree[key] = "max(" + value[:-2] + ")"

# Print the degree dictionary
for key, value in degree.items():
    print(f"{key}= {value}")



