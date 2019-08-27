import random

class Player :
        def __init__(self, name, symbol) :
            self.name = name
            self.symbol = symbol
            

class Game : 
    def __init__(self, name1, name2, symbol1, symbol2) :
        self.name1= name1
        self.name2 = name2
        self.symbol1 = symbol1
        self.symbol2 = symbol2
        self.score1 = 0 
        self.score2 = 0
        self.Counter = 0
        self.TTT = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] #10 brackets 
        
   

    def Turn(self) : 
        if random.randint(0,1) == 0 :
            return self.name1, self.name2
        else :
            return self.name2, self.name1


    
    def InsertSymb(self, symbol, index) : 
        self.symbol = symbol
        self.index = int(index)
        self.Counter += 1
        self.TTT[self.index] = symbol
    
    
    def CheckWin(self) :
        #check row
        for k in range(1, 8, 3) :
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.symbol1) :
                self.score1 += 1
                self.Counter = 0
                return True
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.symbol2) :
                self.score2 += 1
                self.Counter = 0
                return True

        #check col
        for l in range(1, 4, 1) :
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.symbol1) :
                self.score1 += 1
                self.Counter = 0
                return True
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.symbol2) :
                self.score2 += 1
                self.Counter = 0
                return True
        
        #check diag
        d = 1
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.symbol1) :
            self.score1 += 1
            self.Counter = 0
            return True
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.symbol2) :
            self.score2 += 1
            self.Counter = 0
            return True
        if (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.symbol1) :
            self.score1 += 1
            self.Counter = 0
            return True
        if (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.symbol2) :
            self.score2 += 1
            self.Counter = 0
            return True 

    def CheckBrack(self, x) :
        self.x = x
        if self.TTT[self.x] == self.symbol1 or self.TTT[self.x] == self.symbol2 :
            return True
        else :
            return False


    def CheckDraw(self) :
        if self.Counter == 9 :
            return True
        else :
            return False


    def DrawGrid(self) : 
        print('---------------\n',
        '| ' + str(self.TTT[7]) + ' | ' + str(self.TTT[8]) + ' | ' + str(self.TTT[9]) + ' | \n',
        '--------------\n',
        '| ' + str(self.TTT[4]) + ' | ' + str(self.TTT[5]) + ' | ' + str(self.TTT[6]) + ' | \n',
            '--------------\n',
        '| ' + str(self.TTT[1]) + ' | ' + str(self.TTT[2]) + ' | ' + str(self.TTT[3]) + ' | \n',
        '--------------')

    def Leader(self) :
        if self.score1 == self.score2 :
            return print("Nobody won.")
        if self.score1 > self.score2 :
            return print("{} lead.".format(self.name1), end=" ")
        else:
            return print("{} lead.".format(self.name2), end=" ")


    def Score(self) :
        return print(" {} : {}".format(str(self.score1),str(self.score2)))  


    def Restart(self) :
        for h in range(10) :
            self.TTT[h] = ' '


    def Win(self) :
        #check rows
        for k in range(1, 8, 3) :
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.symbol1) :
                return print("{} won. HURRAH!".format(self.name1))
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.symbol2) :
                return print("{} won. HURRAH!".format(self.name2))

        #check cols
        for l in range(1, 4, 1) :
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.symbol1) :
                return print("{} won. HURRAH!".format(self.name1))
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.symbol2) :
                return print("{} won. HURRAH!".format(self.name2))
         #check diag
        d = 1
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.symbol1) :
            return print("{} won. HURRAH!".format(self.name1))
        if (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.symbol1) :
            return print("{} won. HURRAH!".format(self.name1))
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.symbol2) :
            return print("{} won. HURRAH!".format(self.name2))
        if (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.symbol2) :
            return print("{} won. HURRAH!".format(self.name2)) 

    def PlayAgain(self, Answer) :
        self.Answer = Answer
        if Answer == 'Y' or Answer == 'y' :
            return True
        else :
            return False


