import pygame

class Tremie1:
    def __init__(self):
        self.image = pygame.image.load("assets/tremi1.png")
        self.image = pygame.transform.scale(self.image, (150, 130))

    def render(self):
        return self.image
