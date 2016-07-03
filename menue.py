from bge import logic
import game

#Controller und Szene laden
cont = logic.getCurrentController()
scene = logic.getCurrentScene()
#Laden der benütigten Szenen-Objekte
svc = scene.objects['SvC']
svs = scene.objects['SvS']
exit = scene.objects['exit']
menuePlane = scene.objects['MenuePlane']
menue = scene.objects['menue']

#Methode zum Anzeigen / Verbergen des Menüs
#Parameter 1 (Menü anzeigen) oder 0 (Menü verbergen)
def toggleMenue(mode):
   if mode == 0:
        menuePlane.visible = False
        svc.visible = False
        svs.visible = False
        exit.visible = False
        menue.visible = False
   if mode == 1:
        menuePlane.visible = True
        svc.visible = True
        svs.visible = True
        exit.visible = True
        menue.visible = True
   return;

#Variablen definieren, die nicht bei jedem Tick neu definiert werden sollen
own = cont.owner
if 'init' not in own:
    own['init'] = True
    #Zeiger für die Menüeinträge
    own['selected'] = 1

#Prüfe ob spiel noch nicht gestartet ist
if game.gameStart == 0:
    #Wenn Sensor für selectUP/DOWN aktiv ist, veränderer Zeiger für Menüeinträge
    if cont.sensors['selectDown'].positive:
        if own['selected'] < 3:
            own['selected'] += 1      
    if cont.sensors['selectUp'].positive:
        if own['selected'] > 1:
            own['selected'] -= 1
       
    #Ändere gameMode sowie Hervorhebung der Menüeinträge anhand des Menüzeigers    
    if own['selected'] == 1:
        svc.color = [1,0,0,True]
        svs.color = [1,1,1,True]
        exit.color = [1,1,1,True]
        #setze gameMode auf 1 (Spieler gegen CPU)
        game.gameMode = 1
        print(game.gameMode)
        
    if own['selected'] == 2:
        svs.color = [1,0,0,True]
        svc.color = [1,1,1,True]
        exit.color = [1,1,1,True]
        #setze gameMode auf 2 (Spieler gegen Spieler)
        game.gameMode = 2
        print(game.gameMode)
        
    if own['selected'] == 3:
        exit.color = [1,0,0,True]
        svs.color = [1,1,1,True]
        #setze gameMode auf 3 (Spiel beenden)
        game.gameMode = 3
        print(game.gameMode)
    
    #Prüfe ob 'enter' betätigt wurde
    if cont.sensors['enter'].positive:
        #Wenn gameMode 3 (Spiel beenden) ist, beende Spiel
        if game.gameMode == 3:
            print('EXIT')
            logic.endGame()
        #Wenn einer der anderen beíden gameModes, starte Spiel
        else:
            print('gameStartet = true')
            game.gameStart = 1
            #Menü ausblenden
            toggleMenue(0)

 


    