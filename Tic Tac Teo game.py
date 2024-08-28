def sum(a, b, c ):
    return a + b + c

Player1 = input('Enter your Name Player 1')
Player2 = input("Enter your Name Player 2")
print(Player1,'and',Player2,'Enjoy the Game')

def printBoard(P1, P2):
    zero  = 'X' if P1[0] else ('O' if P2[0] else 0)
    one   = 'X' if P1[1] else ('O' if P2[1] else 1)
    two   = 'X' if P1[2] else ('O' if P2[2] else 2)
    three = 'X' if P1[3] else ('O' if P2[3] else 3)
    four  = 'X' if P1[4] else ('O' if P2[4] else 4)
    five  = 'X' if P1[5] else ('O' if P2[5] else 5)
    six   = 'X' if P1[6] else ('O' if P2[6] else 6)
    seven = 'X' if P1[7] else ('O' if P2[7] else 7)
    eight = 'X' if P1[8] else ('O' if P2[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin (P1,P2):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(P1[win[0]], P1[win[1]], P1[win[2]]) == 3):
            print(Player1,"Won the match")
            return 1
        if(sum(P2[win[0]], P2[win[1]], P2[win[2]]) == 3):
            print(Player2,"Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    P1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    P2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe Game")
    while(True):
        printBoard(P1, P2)
        if(turn == 1):
            print("Chance, your 'X' ",Player1)
            value = int(input("Please enter a value: "))
            P1[value] = 1
        else:
            print("Chance, your 'O' ",Player2)
            value = int(input("Please enter a value: "))
            P2[value] = 1
        cwin = checkWin(P1, P2)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn
