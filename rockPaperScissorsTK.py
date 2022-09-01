from tkinter import *
import random

# this is the best I can do until I learn frames


items = ["rock", "paper", "scissors"]


def restart():
    global computer_selection
    computer_selection = random.choice(items)
    situation_restart.config(text="computer changed hand")
    startGameButton.config(bg="green", activebackground="green", activeforeground="black")


def user_selected_hand():
    if (selected_button.get() == 0):  # user selected rock
        if computer_selection == "rock":
            situation.config(text="computer also selected rock, tie.")
        elif computer_selection == "paper":
            situation.config(text="computer selected paper, computer win.")
        else:
            situation.config(text="you win.")
    if (selected_button.get() == 1):  # user selected paper
        if computer_selection == "rock":
            situation.config(text="you win.")
        elif computer_selection == "paper":
            situation.config(text="computer also selected paper, tie")
        else:
            situation.config(text="computer selected scissors, computer win.")
    if (selected_button.get() == 2):  # user selected scissors
        if computer_selection == "rock":
            situation.config(text="computer selected rock, computer win.")
        elif computer_selection == "paper":
            situation.config(text="you win.")
        else:
            situation.config(text="computer also selected scissors, tie")
    startGameButton.config(state=ACTIVE)
    situation_restart.config(text="")


def start_game():
    global computer_selection
    computer_selection = random.choice(items)
    situation_restart.config(text="")

    startGameButton.config(state=DISABLED, bg="black", activebackground="black",
                           activeforeground="gray")
    user_rock_select.config(state=ACTIVE,
                            activebackground="light blue",
                            bg="light blue",
                            activeforeground="red")
    user_paper_select.config(state=ACTIVE,
                             activebackground="light blue",
                             bg="light blue",
                             activeforeground="red")
    user_scissors_select.config(state=ACTIVE,
                                activebackground="light blue",
                                bg="light blue",
                                activeforeground="red")

    replayButton.config(state=ACTIVE, activebackground="green")


if __name__ == '__main__':
    window = Tk()
    # window.geometry("550x300")

    startGameButton = Button(window, text="click to start game", font=('ariel', 30), command=start_game,
                             bg="green")
    startGameButton.grid(row=0, column=0, padx=30)

    selected_button = IntVar()
    user_rock_select = Radiobutton(window, text=items[0], variable=selected_button,
                                   value=0,
                                   indicatoron=False,
                                   command=user_selected_hand,
                                   state=DISABLED,
                                   pady=5,
                                   font=("ariel", 20),
                                   bg="black"
                                   )
    user_rock_select.grid(row=0, column=1)
    user_paper_select = Radiobutton(window, text=items[1], variable=selected_button,
                                    value=1,
                                    indicatoron=False,
                                    command=user_selected_hand,
                                    state=DISABLED,
                                    pady=5,
                                    font=("ariel", 20),
                                    bg="black"
                                    )
    user_paper_select.grid(row=1, column=1)
    user_scissors_select = Radiobutton(window, text=items[2], variable=selected_button,
                                       value=2,
                                       indicatoron=False,
                                       command=user_selected_hand,
                                       state=DISABLED,
                                       pady=5,
                                       font=("ariel", 20),
                                       bg="black"
                                       )
    user_scissors_select.grid(row=2, column=1)

    replayButton = Button(window, text="YES", state=DISABLED, font=('ariel', 30),
                          bg="red", compound=BOTTOM, command=restart)
    replayButton.grid(row=1, column=0, pady=20, padx=30)

    situation = Label(window, font=('ariel', 15))
    situation.grid(row=2, column=0)

    situation_restart = Label(window, font=('ink free', 10))
    situation_restart.grid(row=3, column=0)

    window.mainloop()
