from bge import logic

import random
import game

#Controller und Szene laden
cont = logic.getCurrentController()
scene = logic.getCurrentScene()

#Laden der benötigten Szene-Objekte
ball = scene.objects['ball']
pad1 = scene.objects['pad1']
pad2 = scene.objects['pad2']
scoreTxt1 = scene.objects['score1']
scoreTxt2 = scene.objects['score2']

#Kollisionssensor laden
sensor = cont.sensors['Col_pad1']

hitObject = sensor.hitObject
#Variablen setzen die nicht bei jedem Durchlauf neu initialisiert werden
own = cont.owner
if 'init' not in own:
    if 'restart' not in own:
        #Punktestand initiieren
        own['score1'] = 0
        own['score2'] = 0
        #Steuervariable setzen
        own['restart'] = True
        print('Game started in mode ' + str(game.gameMode))
    #Steuervariable setzen
    own['init'] = True
    #Richtung des Balls
    #dirX = 0 = Ball fliegt nach oben
    #dirX = 1 = Ball fliegt nach unten
    #dirY = 0 = Ball fliegt nach links
    #dirY = 1 = Ball fliegt nach rechts
    own['dirX'] = 0
    own['dirY'] = 0
    #Ball Geschwindigkeit
    own['ballSpeed'] = 1.0
    #x-Bewegung des Balls
    own['ballX'] = 0.1
    #Ball Koordinaten für den Start
    ball.position.x = random.uniform(-14.5, 13.0)
    ball.position.y = -21.8
    ball.position.z = 1.8 
    print('init Done')

#Prüfe ob Menümodu aktiv ist
if game.gameStart == 0:
    #Lösche Steuervariable um beim nächsten Spielstart alles neu zu initialisieren
    del own['init']

#Ausführen wenn der Ball ein Objekt berührt
if hitObject:
    #Name des Objektes was berüht wurde speichern
    hitName = hitObject.name
    #Prüfe ob Pad1 berührt wurde
    if hitName == "pad1":
        print("HIT PAD")
        #ändere y-Ballflugrichtung
        own['dirY'] = 1
        #erhöhe Ballgeschwindigkeit
        own['ballSpeed'] += 0.05
        #ermittle x-Bewegung des Balls anhand der Stelle, an der der Ball das Pad berührt hat
        #je weiter weg von Zentrum des Pads, desto größer die x-Bewegung in die jeweilige Richtung
        own['ballX'] += (ball.position.x - pad1.position.x) / 100
        print(own['ballX'])
    
    #Prüfe ob Pad2 berührt wurde 
    if hitName == "pad2":
        print("HIT PAD2")
        #ändere y-Ballflugrichtung
        own['dirY'] = 0
        #erhöhe Ballgeschwindigkeit
        own['ballSpeed'] += 0.05
        #ermittle x-Bewegung des Balls anhand der Stelle, an der der Ball das Pad berührt hat
        #je weiter weg von Zentrum des Pads, desto größer die x-Bewegung in die jeweilige Richtung
        own['ballX'] += (ball.position.x - pad2.position.x) / 100
        print(own['ballX'])
    
    #Prüfe ob die obere Spielfeldbegrenzung getroffen wurde     
    if hitName == "wand_n":
        print("HIT WAND_N")
        #ändere x-Ballflugrichtung
        own['dirX'] = 1
        #negiere x-Bewegung des Balls
        own['ballX'] -= own['ballX'] * 2
    
    #Prüfe ob die untere Spielfeldbegrenzung getroffen wurde    
    if hitName == "wand_s":
        print("HIT WAND_S")
        #ändere x-Ballflugrichtung
        own['dirX'] = 0
        #negiere x-Bewebung des Balls
        own['ballX'] -= own['ballX'] * 2
    
    #Prüfe ob die linke Spielfeldbegrenzung getroffen wurde    
    if hitName == "wand_w":
        print("HIT WAND_W")
        #erhöhe Punktestand von Spieler 2 / CPU
        own['score2'] += 1
        scoreTxt2.text = str(own['score2'])
        print('Player 2 scored!')
        #lösche Steuervariable um beim nächsten Tick den Ball neu zu initialisieren
        del own['init']
    #Prüfe ob die rechte Spielfeldbegrenzung getroffen wurde    
    if hitName == "wand_o":
        print("HIT WAND_O")
        #erhöhe Punktestand von Spieler 1
        own['score1'] +=  1
        scoreTxt1.text = str(own['score1'])
        print('Player 1 scored!')
        #lösche Steuervariable um beim nächsten Tick den Ball neu zu initialisieren
        del own['init']

#Prüfe ob Spielmodus aktiv ist   
if game.gameStart == 1:
    #je nachdem welche y-Richtungskoordinate aktiv ist -> Bewege Ball in diese Richtung
    if own['dirY'] == 0:  
        ball.position.y += 0.2 * own['ballSpeed']
        ball.position.x += own['ballX'] * own['ballSpeed']
    if own['dirY'] == 1:   
        ball.position.y -= 0.2 * own['ballSpeed']
        ball.position.x += own['ballX'] * own['ballSpeed']
