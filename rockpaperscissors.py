import random

# will add functions in future to simplify code

possible_inputs = ["1" , "2", "3"]
items = ['rock', 'paper', 'scissors']

while 1:
    computer_choice = random.choice(items)
    user_input = input("what is your hand? Write 1 for rock 2 for paper 3 for scissors ")

    while user_input not in possible_inputs:
        user_input = input("please enter valid input!")
    if user_input == "1":
        user_input = "rock"
    elif user_input == "2":
        user_input = "paper"
    elif user_input == "3":
        user_input = "scissors"

    while not computer_choice == user_input:
        if computer_choice == "rock":
            if user_input == "paper":
                print("player wins!")
                break
            elif user_input == "scissors":
                print("computer wins!")
                break

        if computer_choice == "paper":
            if user_input == "rock":
                print("computer wins!")
                break
            elif user_input == "scissors":
                print("player wins!")
                break

        if computer_choice == "scissors":
            if user_input == "rock":
                print("player wins!")
                break
            if user_input == "paper":
                print("computer wins!")
                break


    while user_input == computer_choice:
        print("WITHDRAW AGAIN!")
        computer_choice = random.choice(items)
        user_input = input("what is your hand? Write 1 for rock 2 for paper 3 for scissors ")
        while user_input not in possible_inputs:
            user_input = input("please enter valid input!")
        if user_input == "1":
            user_input = "rock"
        elif user_input == "2":
            user_input = "paper"
        elif user_input == "3":
            user_input = "scissors"

        if computer_choice == "rock":
            if user_input == "paper":
                print("player wins!")
                break
            elif user_input == "scissors":
                print("computer wins!")
                break

        if computer_choice == "paper":
            if user_input == "rock":
                print("computer wins!")
                break
            elif user_input == "scissors":
                print("player wins!")
                break

        if computer_choice == "scissors":
            if user_input == "rock":
                print("player wins!")
                break
            if user_input == "paper":
                print("computer wins!")
                break
        continue


    user_input = input("Do you want to play again Y/N? ")
    if user_input == "Y" or user_input == "y" or user_input == "1":
        continue
    else:
        break

