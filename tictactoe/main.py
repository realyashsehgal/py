from tkinter import *
#WORKING
def turncount():
    global turnss
    if(turn%2==0):
        turnss.config(text="Player X turn")
    else:
        turnss.config(text="Player O turn")
def placed(row,col,box):

    global turn
    global boardrn
    if boardrn[row][col] == "*":
            if turn % 2 == 0:
                box.config(text="X")
                boardrn[row][col] = "X"
            else:
                box.config(text="O")
                boardrn[row][col] = "O"
            if checkWind(boardrn):
                if turn % 2 == 0:
                    WindWindow = Tk()
                    print("Player X wins!")
                    Winner = Label(WindWindow,text="Player X wins the game",font=('arial',50,'bold')).pack()
                    WindWindow.mainloop()
                else:
                    WindWindow = Tk()
                    print("Player O wins!")
                    Winner = Label(WindWindow,text="Player O wins the game",font=('arial',50,'bold')).pack()
                    WindWindow.mainloop()
            elif turn == 9:  # Check for draw
                WindWindow = Tk()
                print("It's a draw!")
                Winner = Label(WindWindow,text="Its a draw",font=('arial',50,'bold')).pack()
                WindWindow.mainloop()
            turn += 1
    else:
            print("It's taken")
    turncount()


#RESTART
def restart():
     global boardrn
     global turn
     boardrn = [["*","*","*"],
                ["*","*","*"],
                ["*","*","*"]]
     
     for row in range(3):
        for col in range(3):
            box = Button(board, font=('arial', 20), height=2, width=5)
            box.config(command=lambda r=row, c=col, b=box: placed(r, c, b))
            box.grid(row=row, column=col)
     turn = 1




#CHECKING WINNING
def checkWind(boardrn):
    
    for i in range(3):
        if boardrn[i][0] == boardrn[i][1] == boardrn[i][2] != "*":
            return True
        if boardrn[0][i] == boardrn[1][i] == boardrn[2][i] != "*":
            return True
    # Check diagonals
    if (boardrn[0][0] == boardrn[1][1] == boardrn[2][2] != "*") or (boardrn[0][2] == boardrn[1][1] == boardrn[2][0] != "*"):
        return True
    return False









# X = threading.Thread(target=turncount,args=())
# X.start()
turn = 1
boardrn = [["*","*","*"],
           ["*","*","*"],
           ["*","*","*"]]
#LOOKS
Window = Tk()
Window.geometry("600x600")

#HEADING
Heading = Label(Window,text="Tic-Tac-Toe",font=('arial',20,'bold'))
Heading.pack()

#TURN THING
turnss = Label(Window,text="Player O turn",font=('arial',25))
turnss.pack()
#BOARD
board = Frame(Window)
board.pack()
for row in range(3):
    for col in range(3):
        box = Button(board, font=('arial', 20), height=2, width=5)
        box.config(command=lambda r=row, c=col, b=box: placed(r, c, b))
        box.grid(row=row, column=col)

#GAP(JUGAAD)
gap = Label(Window,height=3).pack()


#RESTART
restart = Button(Window,text="Restart",font=('arial',20,'bold'),command=restart)
restart.pack()
# X.join()
Window.mainloop()