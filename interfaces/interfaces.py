import pygame
from components.panel import Panel
from components.tremie1 import Tremie1
from components.tremie2 import Tremie2
from components.tremie3 import Tremie3
from components.rampe import Rampe
from components.allumage import Allumage
from components.cycle import Cycle
from components.debit1 import Debit1
from components.level import Level
from components.debit2 import Debit2
from components.debit3 import Debit3
from components.plus import Plus
from components.minus import Minus

class ApplicationInterface:
    def __init__(self, modubusConnexion):
        self.width = 800
        self.height = 600
        self.title = "Supervision de tremie"
        self.running = False
        self.modubusConnexion = modubusConnexion

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        
        # Define some colors
        self.background_color = (255, 255, 255)
        self.text_color = (255, 255, 255)
        
        # Initialize font
        self.font = pygame.font.SysFont(None, 48)
        
        # Initialize components
        
        self.panel = Panel(0, 0, 800, 60, (155, 155, 155))
        
        self.tremie1 = Tremie1()
        self.debit1 = Debit1(self.modubusConnexion)
        self.plus1 = Plus(75, 177, self.debit1Increase)
        self.minus1 = Minus(145, 177, self.debit1Decrease)
        self.level1 = Level(self.getPercentFillTremie1)
        
        self.tremie2 = Tremie2()
        self.debit2 = Debit2(self.modubusConnexion)
        self.plus2 = Plus(445, 177, self.debit2Increase)
        self.minus2 = Minus(515, 177, self.debit2Decrease)
        self.level2 = Level(self.getPercentFillTremie2)
        
        self.tremie3 = Tremie3()
        self.debit3 = Debit3(self.modubusConnexion)
        self.plus3 = Plus(245, 377, self.debit3Increase)
        self.minus3 = Minus(315, 377, self.debit3Decrease)
        self.level3 = Level(self.getPercentFillTremie3)

        self.rampe1 = Rampe()
        self.rampe2 = Rampe()
        self.rampe3 = Rampe()
        
        self.allumage = Allumage(700, 10, self.modubusConnexion)
        
        self.cycle = Cycle(self.modubusConnexion)
        
    def debit1Increase(self):
        self.modubusConnexion.setDebitTremie1(self.modubusConnexion.getDebitTremie1() + 1)

    def debit1Decrease(self):
        self.modubusConnexion.setDebitTremie1(self.modubusConnexion.getDebitTremie1() - 1)

    def debit2Increase(self):
        self.modubusConnexion.setDebitTremie2(self.modubusConnexion.getDebitTremie2() + 1)
        
    def debit2Decrease(self):
        self.modubusConnexion.setDebitTremie2(self.modubusConnexion.getDebitTremie2() - 1)

    def debit3Increase(self):
        self.modubusConnexion.setDebitTremie3(self.modubusConnexion.getDebitTremie3() + 1)
        
    def debit3Decrease(self):
        self.modubusConnexion.setDebitTremie3(self.modubusConnexion.getDebitTremie3() - 1)

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(60)  # Limit to 60 frames per second

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            self.handle_components_events(event)
                    
    def handle_components_events(self, event):
        self.allumage.handle_events(event)
        self.plus1.handle_events(event)
        self.minus1.handle_events(event)
        self.plus2.handle_events(event)
        self.minus2.handle_events(event)
        self.plus3.handle_events(event)
        self.minus3.handle_events(event)
        
    def getPercentFillTremie1(self):
        mc = self.modubusConnexion
        print((5100 - mc.getDebitTremie1() * mc.getNiveauTremie3() / (mc.getDebitTremie1() + mc.getDebitTremie2() + mc.getDebitTremie3()))/5100)
        return (5100 - mc.getDebitTremie1() * mc.getNiveauTremie3() / (mc.getDebitTremie1() + mc.getDebitTremie2() + mc.getDebitTremie3()))/5100
    
    def getPercentFillTremie2(self):
        mc = self.modubusConnexion
        return (5100 - mc.getDebitTremie2() * mc.getNiveauTremie3() / (mc.getDebitTremie1() + mc.getDebitTremie2() + mc.getDebitTremie3()))/5100    
    
    def getPercentFillTremie3(self):
        if self.modubusConnexion.getNiveauTremie3() >= 10000:
            return 1
        return self.modubusConnexion.getNiveauTremie3() / 10000

    def render(self):
        self.screen.fill(self.background_color)
        
        self.screen.blit(self.panel.render(), (0, 0))
        
        self.screen.blit(self.tremie1.render(), (150, 120))
        self.screen.blit(self.debit1.render(), (100, 180))
        self.screen.blit(self.plus1.render(), (75, 177))
        self.screen.blit(self.minus1.render(), (145, 177))
        surfaceLevel1, y1 = self.level1.getSurfaceAndXY(240)
        self.screen.blit(surfaceLevel1, (217, y1))
        
        self.screen.blit(self.tremie2.render(), (500, 120))
        self.screen.blit(self.debit2.render(), (470, 180))
        self.screen.blit(self.plus2.render(), (445, 177))
        self.screen.blit(self.minus2.render(), (515, 177))
        surfaceLevel2, y2 = self.level2.getSurfaceAndXY(240)
        self.screen.blit(surfaceLevel2, (567, y2))
        
        self.screen.blit(self.tremie3.render(), (315, 320))
        self.screen.blit(self.debit3.render(), (270, 380))
        self.screen.blit(self.plus3.render(), (245, 377))
        self.screen.blit(self.minus3.render(), (315, 377))
        surfaceLevel3, y3 = self.level3.getSurfaceAndXY(440)
        self.screen.blit(surfaceLevel3, (382, y3))
        
        
        self.screen.blit(self.rampe1.render(), (120, 260))
        self.screen.blit(self.rampe2.render(), (470, 260))
        self.screen.blit(self.rampe3.render(), (285, 460))
        
        self.screen.blit(self.allumage.render(), (700, 10))
        
        self.screen.blit(self.cycle.render(), (50, 10))
        
        pygame.display.flip()

    def close(self):
        pygame.quit()
