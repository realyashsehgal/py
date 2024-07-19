from tkinter import *
#WORKING
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
                    print("Player X wins!")
                else:
                    print("Player O wins!")
            elif turn == 8:  # Check for draw
                print("It's a draw!")
            turn += 1
    else:
            print("It's taken")





#CHECKING WINNING
def checkWind(boardrn):
    #diagnols
    for i in range(3):
        if boardrn[i][0] == boardrn[i][1] == boardrn[i][2] != "*":
            return True
        if boardrn[0][i] == boardrn[1][i] == boardrn[2][i] != "*":
            return True
    # Check diagonals
    if (boardrn[0][0] == boardrn[1][1] == boardrn[2][2] != "*") or (boardrn[0][2] == boardrn[1][1] == boardrn[2][0] != "*"):
        return True
    return False









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
restart = Button(Window,text="Restart",font=('arial',20,'bold'))
restart.pack()

Window.mainloop()