import pygame

class Cycle:
    def __init__(self, modbus):
        self.modbus = modbus
        self.value = modbus.getEtatCycleRemplissage() == True and modbus.getEtatCycleVidange() == False
        self.font = pygame.font.SysFont(None, 26)
        self.text_color = (255, 255, 255)
        self.fill_color = (0, 200, 0)
        self.drain_color = (200, 0, 0)

    # def handle_events(self, event):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if self.rect.collidepoint(event.pos):
    #             self.value = not self.value

    def render(self):
        self.value = self.modbus.getEtatCycleRemplissage() == True and self.modbus.getEtatCycleVidange() == False
        if self.modbus.getEtatMarcheArret() == True:
            cycle_text = "Remplissage" if self.value else "Vidange"
        else:
            cycle_text = "L'automate est à l'arrêt"

        text_surface = self.font.render("Cycle: " + cycle_text, True, self.text_color)
        return text_surface
