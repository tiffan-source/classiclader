import pygame

class Tremie3:
    def __init__(self):
        self.image = pygame.image.load("assets/tremi3.png")
        self.image = pygame.transform.scale(self.image, (150, 130))

    def render(self):
        return self.image
