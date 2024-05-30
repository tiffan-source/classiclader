import pygame

class Rampe:
    def __init__(self):
        self.image = pygame.image.load("assets/rampe.png")
        # self.image = pygame.transform.scale(self.image, (150, 130))

    def render(self):
        return self.image
