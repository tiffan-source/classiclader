import pygame

class Panel:
    def __init__(self, x, y, width, height, background_color=(100, 100, 100)):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color

    def render(self):
        surface = pygame.Surface((self.rect.width, self.rect.height))
        surface.fill(self.background_color)
        return surface
