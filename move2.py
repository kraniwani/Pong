from bge import logic
import game

#Controller und Szene laden
cont = logic.getCurrentController()
scene = logic.getCurrentScene()

#Laden der benötigten SZene-Objekte
pad2 = scene.objects['pad2']

#Prüfen ob Spielmodus aktiv ist
if game.gameStart == 1:      
	#Prüfen ob Spielmodus 2 (Spieler gegen Spieler) aktiv ist
    if game.gameMode == 2: 
    	#Prüfe ob Sensor für up oder down des Spieler2-Pads gedrückt wurde und verschiebe Pad entsprechend   
        if cont.sensors['up2'].positive:
            pad2.position.x+=0.15    
        if cont.sensors['down2'].positive:
            pad2.position.x-=0.15
