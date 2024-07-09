import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((255, 255))
clock = pygame.time.Clock()
running = True
width = 20
height = 20
margin = 5
empty_color = 'white'
wall_color = 'blue'
# a array we can work on for coding
grid = np.full((10,10), 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse = pygame.mouse.get_pos()
            mouse = (mouse[0] // (width + margin), mouse[1] // (height + margin))
            if 0 <= mouse[0] < 10 and 0 <= mouse[1] < 10: 
                grid[mouse[1], mouse[0]] = 1 if grid[mouse[1], mouse[0]] == 0 else 0

    # creating an empty map
    for row in range(10):
        for col in range(10):
            if grid[row][col] == 1:
                color = wall_color
            else:
                color = empty_color
            pygame.draw.rect(screen, color, (col*(width + margin)+margin, row*(height + margin)+margin, width, height))
   
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()