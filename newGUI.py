from tkinter import *
import tkinter.messagebox
import Main
from Main import step
from Main import gameBoard

playerSymbol = "X"
computerSymbol = "O"


def computerClick():
    move = Main.getComputerMove(gameBoard)
    gameBoard[move] = computerSymbol
    print(move)
    dict_b[move]["text"] = "O"

def btnClick(x):
    if dict_b[x]["text"] == " ":
        dict_b[x]["text"] = playerSymbol
        gameBoard[x] = 'X'
        computerClick()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


tk = Tk()
tk.title("Tic Tac Toe")

buttons = StringVar()

# button_confirm = Button(tk, text='确定', font='Times 20 bold', bg='gray', fg='white', height=1, width=5,)
# button_confirm.grid(row=0, column=0)

button1 = Button(tk, text=gameBoard[0], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(0))
button1.grid(row=3, column=0)

button2 = Button(tk, text=gameBoard[1], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(1))
button2.grid(row=3, column=1)

button3 = Button(tk, text=gameBoard[2], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(2))
button3.grid(row=3, column=2)

button4 = Button(tk, text=gameBoard[3], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(3))
button4.grid(row=4, column=0)

button5 = Button(tk, text=gameBoard[4], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(4))
button5.grid(row=4, column=1)

button6 = Button(tk, text=gameBoard[5], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(5))
button6.grid(row=4, column=2)

button7 = Button(tk, text=gameBoard[6], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(6))
button7.grid(row=5, column=0)

button8 = Button(tk, text=gameBoard[7], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(7))
button8.grid(row=5, column=1)

button9 = Button(tk, text=gameBoard[8], font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(8))
button9.grid(row=5, column=2)


dict_b = {0: button1, 1: button2, 2: button3, 3: button4, 4: button5, 5: button6, 6: button7, 7: button8, 8: button9}

if __name__ == '__main__':
    tk.mainloop()
