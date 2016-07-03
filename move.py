from bge import logic
import game
from ball import own['score1']  

#Controller und Szene laden
cont = logic.getCurrentController()
scene = logic.getCurrentScene()

#Laden der benötigten Szenen-Objekte
pad1 = scene.objects['pad1']
pad2 = scene.objects['pad2']

#Variablen definieren, die nicht bei jedem Tick neu definiert werden sollen
own = cont.owner
if 'init' not in own:
    own['init'] = True
    #setzen der Startpositionen der beiden Pads
    pad1.position.x = 0.023
    pad2.position.x = 0.023

#Prüfen ob ESC gedrückt wurde
if cont.sensors['esc'].positive:
    print('gameStartet = false')
    #alle Variablen neu definieren beim nächsten Tick
    del own['init']
    #Methode zum Ein/Ausblenden des Menüs importerien
    from menue import toggleMenue
    #gameStart = 0 = Menümodus
    game.gameStart = 0
    #Menü einblenden
    toggleMenue(1)

#Prüfen ob Spielmodus aktiv ist
if game.gameStart == 1:
    #Prüfe ob Sensor für up oder down des Spieler-Pads gedrückt wurde und verschiebe Pad entsprechend.
    if cont.sensors['up'].positive:
        pad1.position.x+=0.15      
    if cont.sensors['down'].positive:
        pad1.position.x-=0.15
        
