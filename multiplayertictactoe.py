from tkinter import *

window =Tk()
window.title("Tic tac Toe")
window.config(padx=80, pady=50, bg="black")
turn = "X"
game = True
moves = {1: " ", 2: " ", 3:" ",
         4: " ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}

def check(player):
    if moves[1] == moves[2] and moves[2] == moves[3] and moves[3] == player:
        button1.config(bg="Orange")
        button2.config(bg="Orange")
        button3.config(bg="Orange")
        return True
    elif moves[7] == moves[8] and moves[8] == moves[9] and moves[7] == player:
        button7.config(bg="Orange")
        button8.config(bg="Orange")
        button9.config(bg="Orange")
        return True
    elif moves[4] == moves[5] and moves[5] == moves[6] and moves[6] == player:
        button4.config(bg="Orange")
        button5.config(bg="Orange")
        button6.config(bg="Orange")
        return True
    elif moves[1] == moves[4] and moves[4] == moves[7] and moves[1] == player:
        button1.config(bg="Orange")
        button4.config(bg="Orange")
        button7.config(bg="Orange")
        return True
    elif moves[2] == moves[5] and moves[5] == moves[8] and moves[2] == player:
        button2.config(bg="Orange")
        button5.config(bg="Orange")
        button8.config(bg="Orange")
        return True
    elif moves[3] == moves[6] and moves[6] == moves[9] and moves[9] == player:
        button3.config(bg="Orange")
        button6.config(bg="Orange")
        button9.config(bg="Orange")
        return True
    elif moves[1] == moves[5] and moves[5] == moves[9] and moves[1] == player:
        button1.config(bg="Orange")
        button5.config(bg="Orange")
        button9.config(bg="Orange")
        return True
    elif moves[3] == moves[5] and moves[5] == moves[7] and moves[7] == player:
        button3.config(bg="Orange")
        button5.config(bg="Orange")
        button7.config(bg="Orange")
        return True

def draw():

    for key in moves.keys():
        if moves[key] == " ":
            return False
    return True

def play(event):
    global game
    if game == False:
        return
    global turn
    button = event.widget
    button.config(state= DISABLED)
    last_value = str(button)
    bv = last_value[-1]
    if(bv=="n"):
        bv = "1"

    if button["text"] == " ":
        if turn == "O":
            button["text"] = "O"
            moves[int(bv)] = turn

            if check(turn) == True:
                label.config(text=f"{turn} wins", font=("Arial", 20))


                game = False
                return

            turn = "X"
        else:
            button["text"] = "X"
            moves[int(bv)] = turn


            if check(turn) == True:

                label.config(text=f"{turn} wins", font=("Arial", 20))

                game = False
                return

            turn = "O"

        if draw() == True:
            label.config(text=f"Game Draw", font=("Arial", 20))
        print(moves)

def restart_play():
    global game
    game = True
    for button in buttons:
        button["text"] = " "
        button.config(bg="Black")
    for keys in moves.keys():
        moves[keys] = " "
    label.config(text = "Tic Tac Toe")


button1 = Button(text=" ", font=("Arial", 27), bg = "black", fg= "white", width =4, height=2, borderwidth=3)

button1.grid(row = 0, column =0)
button1.bind("<Button-1>", play)
button2 = Button(text=" ", font=("Arial", 27), bg = "black", fg= "white",width =4, height = 2,borderwidth=3)
button2.grid(row = 0, column =1)
button2.bind("<Button-1>", play)
button3 = Button(text=" ", font=("Arial", 27), bg = "black", fg= "white",width =4, height = 2,borderwidth=3)
button3.grid(row = 0, column =2)
button3.bind("<Button-1> ", play)
button4 = Button(text=" ",  font=("Arial", 27),bg = "black", fg= "white", width =4, height = 2,borderwidth=3)
button4.grid(row = 1, column =0)
button4.bind("<Button-1>", play)
button5 = Button(text=" ",  font=("Arial", 27),bg = "black", fg= "white", width =4, height = 2,borderwidth=3)
button5.grid(row = 1, column =1)
button5.bind("<Button-1>", play)
button6 = Button(text=" ", font=("Arial", 27), bg = "black", fg= "white",width =4, height = 2,borderwidth=3)
button6.grid(row = 1, column =2)
button6.bind("<Button-1>", play)
button7 = Button(text=" ",  font=("Arial", 27),bg = "black", fg= "white", width =4, height = 2,borderwidth=3)
button7.grid(row = 2, column =0)
button7.bind("<Button-1>", play)
button8 = Button(text=" ",  font=("Arial", 27),bg = "black", fg= "white", width =4, height = 2,borderwidth=3)
button8.grid(row = 2, column =1)
button8.bind("<Button-1>", play)

button9 = Button(text=" ",  font=("Arial", 27),bg = "black", fg= "white", width =4, height = 2,borderwidth=3)
button9.grid(row = 2, column =2)
button9.bind("<Button-1>", play)
'''label1 = Label(text="Tic Tac Toe", width=15, bg="black", fg="white")
label1.grid(row=0, column =0, columnspan =3)'''
label = Label(text="Tic Tac Toe", width=15, bg="black", fg="white",font=("Arial", 20))
label.grid(row=3, column =0, columnspan =3)
restart = Button(text="Restart", width=10, font=("Arial", 10), bg = "Yellow", fg = "Black", command=restart_play)
restart.grid(row=4, column =0, columnspan =3)
buttons = [button1, button2, button3, button4,button5, button6, button7, button8, button9]
window.mainloop()
