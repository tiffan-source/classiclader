import pygame

class Level:
    def __init__(self, callback=None):
        self.callback = callback
        self.rect = pygame.Rect(20, 20, 16, 200)
        self.color = (0, 0, 0)

    def render(self):
        self.rect.height = 200 * self.callback()
        surface = pygame.Surface((self.rect.width, self.rect.height))
        surface.fill(self.color)
        return surface
    
    def getSurfaceAndXY(self, y):
        self.rect.height = 200 * self.callback()
        surface = pygame.Surface((self.rect.width, self.rect.height))
        surface.fill(self.color)
        return surface, y - self.rect.height