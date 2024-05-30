import pygame

class Debit1:
    def __init__(self, modbus):
        self.modbus = modbus
        self.value = modbus.getEtatCycleRemplissage() == True and modbus.getEtatCycleVidange() == False
        self.font = pygame.font.SysFont(None, 24)
        self.text_color = (0, 0, 0)

    def render(self):
        self.value = self.modbus.getDebitTremie1()
        
        cycle_text = str(self.value) + "/s"

        text_surface = self.font.render(cycle_text, True, self.text_color)
        return text_surface
