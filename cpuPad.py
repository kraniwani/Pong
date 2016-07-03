from bge import logic
import game

#Controller und Szene laden
cont = logic.getCurrentController()
scene = logic.getCurrentScene()
#Laden der benötigten Szenen-Objekte
pad2 = scene.objects['pad2']
ball = scene.objects['ball']

#Prüfe ob Spiel läuft
if game.gameStart == 1:
	#Prüfe ob gameMode 1 (CPU Spiel) aktiv ist
    if game.gameMode == 1:
    	#Bewege Pad anhand der Position vom Ball
        if ball.position.x > pad2.position.x:
            pad2.position.x+=0.15         
        if ball.position.x < pad2.position.x:
            pad2.position.x-=0.15
