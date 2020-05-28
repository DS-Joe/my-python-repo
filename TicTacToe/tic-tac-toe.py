import itertools as it
from colorama import Fore, Back, Style, init
#Back momentan nicht verwendet
init() #Das oder die nächste Zeile jeweils auskommentiert lassen
#init(strip=False) #Farbe in Spyder Konsole

#Übergabe der Parameter und setzen von default-Werten falls diese nicht übergeben werden
def game_board(game_map,player=0,row=0,column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("Die Position ist bereits besetzt, wähle eine andere!")
            return game_map, False
        #Erzeugen der oberen Leiste für Bezeichnung der Spalten
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        
        #Zug ausführen
        if not just_display:
            game_map[row][column]=player
        
        #Spielfeld nach Zug ausgeben, mit Bezeichnung der Spalten links davon
        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count,colored_row) 
        return game_map, True
    
    except IndexError as e:
        print("Ungültige Zeile/Spalte!", e)
        return game_map, False
    
    except Exception as e:
        print("Unerwarteter Fehler!",e)
        return game_map, False
        
        
def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    
    #Horizontal
    for row in current_game:
            if all_same(row):
                print(f"Spieler {row[0]} gewinnt horizontal!") 
                return True
            
    #Vertikal        
    for col in range(len(current_game)):
        check=[]          
        for row in current_game:
            check.append(row[col])            
        if all_same(check):
            print(f"Spieler {check[0]} gewinnt vertikal!") 
            return True
        
    #Diagonal /
    diags=[]        
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])    
    if all_same(diags):
        print(f"Spieler {diags[0]} gewinnt diagonal (/)!")
        return True
    
    #Diagonal \
    diags=[]
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])    
    if all_same(diags):
        print(f"Spieler {diags[0]} gewinnt diagonal (\\)!")
        return True
    
    return False
        
            
play=True
players=[1,2]
while play:
        #Spielfeld erzeugen
        game_size = int(input("Spielfeldgröße wählen: "))
        game = [[0 for i in range(game_size)] for i in range(game_size)]
        
        game_won=False
        game, _ = game_board(game, just_display=True)
        player_choice = it.cycle([1, 2])
        while not game_won:
            current_player = next(player_choice)
            print(f"Spieler am Zug: {current_player}")
            played = False
            
            while not played:
                row_choice = int(input("Waehlen der Zeile: "))
                column_choice = int(input("Waehlen der Spalte: "))
                game, played = game_board(game, current_player, row_choice, column_choice)
        
            if win(game):
                game_won = True
                again = input("Das Spiel ist vorbei. Erneut spielen? (y/n) ")
                if again.lower() == "y":
                    print("Neustart")
                elif again.lower() == "n":
                    print("Auf Wiedersehen.")
                    play = False
                else:
                    print("Keine valide Eingabe. Das Spiel wird beendet.")
                    play = False
                    


#game=game_board(game, just_display=True)