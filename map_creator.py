import pygame
import numpy as np

class MapCreator:
    def __init__(self, screen, screen_size):
        self.screen_width, self.screen_height = screen_size
        self.screen = screen
        self.grid = np.full((10, 10), 0)
        self.width = 20
        self.height = 20
        self.margin = 5

        self.map_height = 10
        self.map_width = 10

        self.left_margin = (self.screen_width-self.map_width*(self.width+self.margin))//2
        self.top_margin = 5
        self.empty_color = 'white'
        self.wall_color = 'blue'
        self.make_walls = False

        self.button_color = 'grey'
        self.button_text_color = 'black'
        self.button_rect = pygame.Rect(500, 260, 150, 50)
        self.font = pygame.font.SysFont(None, 24)
        
        buttons_margin = 20
        interval = (self.screen_width-2*buttons_margin)//4
        buttons_height = (self.map_height + self.margin)*self.height + buttons_margin
        self.buttons = {
            'Create Walls': pygame.Rect(buttons_margin, buttons_height, interval-50, 50),
            'Place Bot': pygame.Rect(interval*1, buttons_height, interval-buttons_margin, 50),
            'Place Exit': pygame.Rect(interval*2, buttons_height, interval-buttons_margin, 50),
            'Quit': pygame.Rect(interval*3, buttons_height, interval-buttons_margin, 50)
        }
    def run(self):
        self.screen.fill('black')
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    for text in self.buttons:
                        if rect.collidepoint(mouse):
                            print("collision")
                            if text == 'Create Walls':
                                self.buttons['Create Walls'] = "Stop creating walls"
                            elif text == 'Place Bot':
                                pass
                            elif text == 'Place Exit':
                                pass
                            elif text == 'Quit':
                                pygame.quit()
                                exit() 
                    if self.button_rect.collidepoint(mouse):
                        self.make_walls = not self.make_walls
                        self.button_text = 'Make Walls' if not self.make_walls else 'Stop Making Walls'
                    else:
                        mouse = ((mouse[0] - self.left_margin) // (self.width + self.margin), (mouse[1] - self.top_margin) // (self.height + self.margin))
                        if 0 <= mouse[0] < 10 and 0 <= mouse[1] < 10:
                            self.grid[mouse[1], mouse[0]] = 1 #if self.make_walls else 0
                            
            for row in range(self.map_height):
                for col in range(self.map_width):
                    color = self.wall_color if self.grid[row][col] == 1 else self.empty_color
                    pygame.draw.rect(self.screen, color, (col * (self.width + self.margin) + self.left_margin, row * (self.height + self.margin) + self.top_margin, self.width, self.height))
            # for i, text in enumerate(self.buttons):
            #     rect = pygame.Rect(i*(self.screen_width//len(self.buttons)), self.map_height*(self.height+self.margin) + 20, 150, 50)
            #     pygame.draw.rect(self.screen, self.button_color, rect)
            #     label = self.font.render(text, True, "black")
            #     self.screen.blit(label, (rect.x + 20, rect.y + 10))
            for text, rect in self.buttons.items():
                pygame.draw.rect(self.screen, 'white', rect)
                label = self.font.render(text, True, (0, 0, 0))
                self.screen.blit(label, (rect.x + 20, rect.y + 10))
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600)) 
    mapcreator = MapCreator(screen)
    mapcreator.run()