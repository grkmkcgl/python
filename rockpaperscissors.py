import random

def user_choice_selector(user_input):
    if user_input == "1":
        user_input = "rock"
    elif user_input == "2":
        user_input = "paper"
    elif user_input == "3":
        user_input = "scissors"
    return user_input


def comparator(user_input, computer_choice):
    if computer_choice == "rock":
        if user_input == "paper":
            print("Your choice: " + user_input)
            print("Computer selected: " + computer_choice)
            print("You win!")
        elif user_input == "scissors":
            print("Your choice: " + user_input)
            print("Computer selected: " + computer_choice)
            print("Computer win!")

    elif computer_choice == "paper":
        if user_input == "rock":
            print("Your choice: " + user_input)
            print("Computer selected: " + computer_choice)
            print("Computer win!")
        elif user_input == "scissors":
            print("Your choice: " + user_input)
            print("Computer selected: " + computer_choice)
            print("You win!")

    else:
        if user_input == "rock":
            print("Your choice: " + user_input)
            print("Computer selected: " + computer_choice)
            print("You win!")
        if user_input == "paper":
            print("Your choice: " + user_input)
            print("Computer selected: " + computer_choice)
            print("Computer win!")


possible_inputs = ["1", "2", "3"]
items = ['rock', 'paper', 'scissors']

# --------------------------------MAIN FUNCTION:
while 1:
    computer_choice = random.choice(items)
    user_input = input("1 for rock 2 for paper 3 for scissors ")

    while user_input not in possible_inputs:
        user_input = input("please enter valid input!")

    user_input = user_choice_selector(user_input)

    while not computer_choice == user_input:
        comparator(user_input, computer_choice)
        break

    while user_input == computer_choice:
        print("Your choice: " + user_input)
        print("Computer selected: " + computer_choice)
        print("TIE! AGAIN!")
        print(" ")

        computer_choice = random.choice(items)
        user_input = input("1 for rock 2 for paper 3 for scissors ")

        while user_input not in possible_inputs:
            user_input = input("please enter valid input!")

        user_input = user_choice_selector(user_input)

        comparator(user_input, computer_choice)
        continue

    print(" ")
    user_input = input("Do you want to play again Y/N? ").lower()
    if user_input == "y" or user_input == "1":
        print(" ")
        continue
    else:
        break
