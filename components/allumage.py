import pygame

class Allumage:
    def __init__(self, x, y, modbus):
        self.x = x
        self.y = y
        self.modbus = modbus
        self.value = self.modbus.getEtatMarcheArret()

        # Load images
        self.image_on = pygame.image.load('assets/power-on.png')
        self.image_off = pygame.image.load('assets/power-off.png')

        # Set the initial image
        self.current_image = self.image_on if self.value else self.image_off

        # Get the rect for positioning and click detection
        self.rect = self.current_image.get_rect(topleft=(self.x, self.y))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.toggle_value()

    def toggle_value(self):
        if self.modbus.getEtatMarcheArret():
            self.modbus.setForceArret(True)
            self.modbus.setForceMarche(False)
            self.current_image = self.image_off
        else:
            self.modbus.setForceArret(False)
            self.modbus.setForceMarche(True)
            self.current_image = self.image_on

    def render(self):
        return self.current_image