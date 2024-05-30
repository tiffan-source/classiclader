from interfaces.interfaces import ApplicationInterface
from data.connexionModbus import ConnexionModbus

newModbus = ConnexionModbus()
app = ApplicationInterface(newModbus)

app.run()
