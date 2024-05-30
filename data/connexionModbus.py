from data.modbus import Modbus

class ConnexionModbus:
    def __init__(self):
        self.modbus = Modbus()

    def setForceMarche(self, valeur):
        self.modbus.ecrireBit(201, valeur)

    def setForceArret(self, valeur):
        self.modbus.ecrireBit(202, valeur)

    def getForceMarche(self):
        return self.modbus.lireBit(201)
    
    def getForceArret(self):
        return self.modbus.lireBit(202)    
    
    def getEtatCycleRemplissage(self):
        return self.modbus.lireBit(300)
    
    def getEtatCycleVidange(self):
        return self.modbus.lireBit(301)
    
    def getEtatMarcheArret(self):
        return self.modbus.lireBit(302)
    
    def getEtatConvoyeur1(self):
        return self.modbus.lireBit(303)
    
    def getEtatConvoyeur2(self):
        return self.modbus.lireBit(304)
    
    def getEtatConvoyeur3(self):
        return self.modbus.lireBit(305)
    
    def getAutorisationPilotageDistance(self):
        return self.modbus.lireBit(306)
    
    def getDebitTremie1(self):
        return self.modbus.lireRegistre(11)
    
    def setDebitTremie1(self, valeur):
        self.modbus.ecrireRegistre(11, valeur)
    
    def getDebitTremie2(self):
        return self.modbus.lireRegistre(12)
    
    def setDebitTremie2(self, valeur):
        self.modbus.ecrireRegistre(12, valeur)
    
    def getDebitTremie3(self):
        return self.modbus.lireRegistre(13)
    
    def setDebitTremie3(self, valeur):
        self.modbus.ecrireRegistre(13, valeur)
    
    def getNiveauTremie3(self):
        return self.modbus.lireRegistre(30)

    def closeConnexion(self):
        self.modbus.close()
