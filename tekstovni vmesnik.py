from model import Game, Player

#players settings
ime1 = input("Insert Player One: ")
ime2 = input("Insert Player Two: ")
symbol1 = input("{}, choose a Symbol: ".format(ime1))
symbol2 = input("{}, choose a Symbol: ".format(ime2))
print("Hi, {} in {}, welcome in game TIC-TAC-TOE!".format(ime1,ime2))

#initialize classes
igralec1 = Player(ime1, symbol1)
igralec2 = Player(ime2, symbol2)
Game1 = Game(ime1, ime2, symbol1, symbol2)

while(1) :
    Prvi, Drugi = Game1.Turn()
    print("\nGame is about to begin...")
    print("{} starts.".format(Prvi))

    while(1) :
        #first player turn
        if Prvi == ime1 :
            while(1) :
                i = input('Press key, where you want to insert your symbol: ')
                if Game1.CheckBrack(int(i)) :
                    print("Bracket already full! Insert somewhere else.\n")
                    continue
                else :
                    Game1.InsertSymb(symbol1, i)
                    break
        else :
            while(1) :
                i = input('Press key, where you want to insert your symbol: ')
                if Game1.CheckBrack(int(i)) :
                    print("Bracket already full! Insert somewhere else.\n")
                    continue
                else :
                    Game1.InsertSymb(symbol2, i) 
                    break
        Game1.DrawGrid()

        if Game1.CheckWin() : 
            Game1.Win()
            break
        if Game1.CheckDraw() :
            print("Nobody won.")
            break

        #second player turn
        if Drugi == ime1 :
            print("\n{}'s turn.".format(ime1))
            while(1) : 
                i = input('Press key, where you want to insert your symbol: ')
                if Game1.CheckBrack(int(i)) :
                    print("Bracket already full! Insert somewhere else.\n")
                    continue
                else :
                    Game1.InsertSymb(symbol1, i)
                    break 
        else :
            print("\nNa vrsti je {}.".format(ime2))
            while(1) :
                i = input('Press key, where you want to insert your symbol: ')
                if Game1.CheckBrack(int(i)) :
                    print("Bracket already full! Insert somewhere else.\n")
                    continue
                else :
                    Game1.InsertSymb(symbol2, i) 
                    break
        Game1.DrawGrid()
        
        if Game1.CheckWin(): 
            Game1.Win()
            break
        if Game1.CheckDraw() :
            print("Nobody won.")
            break
        
        if Prvi == ime1 :
            print("\n{}'s turn.".format(ime1)) 
        else :
            print("\n{}'s turn.".format(ime2))
    

    Game1.Leader()
    Game1.Score()
    Game1.Restart()
       
    Ans = input("\nDo you want to continue playing? Y/N \n")
    if Game1.PlayAgain(Ans) :
        continue
    else :
        break 


print("\n\nThank you for playing {} and {}. Game Over.".format(ime1,ime2))

