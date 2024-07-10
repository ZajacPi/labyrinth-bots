import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 50)
        self.buttons = {
            'Map Creator': pygame.Rect(300, 200, 300, 50),
            'Run simulation': pygame.Rect(300, 300, 300, 50),
            'Quit': pygame.Rect(300, 400, 300, 50)
        }


    def run(self):
        self.screen.fill("black")
        clock = pygame.time.Clock()
        while True:
            for text, rect in self.buttons.items():
                pygame.draw.rect(self.screen, 'white', rect)
                label = self.font.render(text, True, (0, 0, 0))
                self.screen.blit(label, (rect.x + 20, rect.y + 10))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    for text, rect in self.buttons.items():
                        if rect.collidepoint(mouse_pos):
                            print("collision")
                            if text == 'Map Creator':
                                print("Clicked map creator")
                                return 'MAP_CREATOR'
                            elif text == 'Run simulation':
                                return 'SIMULATION'
                            elif text == 'Quit':
                                pygame.quit()
                                exit() 
            pygame.display.flip()
            clock.tick(60)