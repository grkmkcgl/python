# it'll ask questions with multiple choices to user
# it'll check answers and will give a point
def game():

    answers = []
    true_answers = 0
    question_num = 1

    for key in questions_and_choices:
        print("****** ****** ****** ******")
        print(key)

        for i in choices[question_num - 1]:
            print(i)

        question_num += 1
        print(" ")

        user_answer = input("Enter A, B, C or D?: ").upper()
        answers.append(user_answer)
        true_answers += check_true(questions_and_choices.get(key), user_answer)

    results(true_answers, answers)


def check_true(true_answer, user_answer):
    if true_answer == user_answer:
        print("True")
        return 1
    else:
        return 0


def results(mark, answers):
    print("-------------RESULTS-------------")
    mark_in_perct = mark * 100 / len(questions_and_choices)
    print("Your score is: " + str(mark_in_perct) + "%")
    # display true answers

    print("True answers were: ", end="")
    for i in questions_and_choices:
        print(questions_and_choices.get(i), end="")
    print()

    print("Your answers were: ", end="")
    for i in answers:
        print(i, end="")
    print()


def restart():
    print()
    while 1:
        answer = input("Do you want to play again? Y/N: ").upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False


print("Welcome to quiz")

questions_and_choices = {'What is the year Turkish Republic is founded?': 'A',
                         'Who is 2021 F1 world champion?': 'C',
                         'What is the meaning of UAV?': 'A',
                         'What does Cacophony mean?': 'D'
                         }

choices = [["A) 1923", "B) 1538", "C) 1881", "D) 1071"],
           ["A) Cem Yılmaz", "B) Sebastian Vettel", "C) Max Verstappen", "D) Lewis Hamilton"],
           ["A) Unmanned Air Vehicle", "B) Ultra Air Vehicle", "C) Unknown Air Vehicle", "D) None Above"],
           ["A) Some answer", "B) Other answer", "C) different answer", "D) A mixture of horrible sounds"]]

game()
while restart():
    game()

print("*****END*****")
