from tkinter import *
import tkinter.messagebox
import Main


gameBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
playerSymbol = "X"
computerSymbol = "O"
count_round = 0

def btnClick(bottons,x):
    global gameBoard
    if bottons["text"] == " ":
        bottons["text"] = playerSymbol
        gameBoard[x] = X
        btnClick(Main.getComputerMove(gameBoard))
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


tk = Tk()
tk.title("Tic Tac Toe")

buttons = StringVar()
button1 = Button(tk, text=gameBoard[0], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button1, 0))
button1.grid(row=3, column=0)

button2 = Button(tk, text=gameBoard[1], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button2, 1))
button2.grid(row=3, column=1)

button3 = Button(tk, text=gameBoard[2], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button3, 2))
button3.grid(row=3, column=2)

button4 = Button(tk, text=gameBoard[3], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button4, 3))
button4.grid(row=4, column=0)

button5 = Button(tk, text=gameBoard[4], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button5, 4))
button5.grid(row=4, column=1)

button6 = Button(tk, text=gameBoard[5], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button6, 5))
button6.grid(row=4, column=2)

button7 = Button(tk, text=gameBoard[6], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button7, 6))
button7.grid(row=5, column=0)

button8 = Button(tk, text=gameBoard[7], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button8, 7))
button8.grid(row=5, column=1)

button9 = Button(tk, text=gameBoard[8], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button9, 8))
button9.grid(row=5, column=2)


dict_b = {0: button1, 1: button2, 2: button3, 3: button4, 4: button5, 5: button6, 6: button7, 7: button8, 8: button9}


tk.mainloop()
