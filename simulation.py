import pygame

class Simulation:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        self.screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Main game logic here

        return None
