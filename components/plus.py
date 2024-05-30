import pygame

class Plus:
    def __init__(self, x, y, callback):
        self.image = pygame.image.load('assets/plus.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.callback = callback

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def render(self):
        return self.image
