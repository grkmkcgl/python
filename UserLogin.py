from tkinter import *
import os


def info_read():
    nameInfo = first_name_entry.get()
    passwordInfo = password_entry.get()
    emailInfo = email_entry.get()
    user_find_flag = 0

    file = open("C:\\Users\\gorke\\Desktop\\login-password-info.txt", "r")
    for line in file.readlines():
        file_infos = line.split()
        if nameInfo == file_infos[0] and emailInfo == file_infos[1] and passwordInfo == file_infos[2]:
            if nameInfo == 'a' and emailInfo == 'a' and passwordInfo == 'a':
                user_find_flag += 1
                print("welcome admin")
                create_admin_frame()
                break
            else:
                user_find_flag += 1
                print("login successful")
                login_success_window_create()
                window.destroy()
                break

    if user_find_flag == 0:
        creadientals_login = Label(submitFrame, text="User couldn't find or credentials are wrong")
        submitButton.grid(row=1,column=0)
        creadientals_login.grid(row=0,column=0)
    file.close()


def login_success_window_create():
    global new_window
    new_window = Tk()
    successMessage = Label(new_window, text="WELCOME SIR", font=("segoe UI", 60))
    successMessage.pack()


def create_admin_frame():
    adminFrame.grid(row=0, column=1)


# playing sounds causes too much error, pydub works but causes problems
# def YEY():
#     song = AudioSegment.from_mp3("notification.mp3")
#     ten_seconds = 10 * 1000
#     first_10_seconds = song[:ten_seconds]
#     print("EVRÜVER VER AY KEN")
#     play(first_10_seconds)
# playsound module didn't work
# playsound('notification.wav')
#


window = Tk()

# Frames are set

topFrame = Frame(window)
topFrame.grid(row=0, column=0)
loginFrame = Frame(window)
loginFrame.grid(row=1, column=0)
submitFrame = Frame(window)
submitFrame.grid(row=2, column=0)

adminFrame = Frame(window, padx=60)

# don't understand below code, analyze later
# window.grid_rowconfigure(2, weight=1)
# window.grid_columnconfigure(2, weight=1)
# use above when resizing


# Left frame is configured

title = Label(topFrame, text="Enter your informations", font=('Segoe UI', 15))
title.grid(row=0, column=0)

first_name_label = Label(loginFrame, text="First name: ", font=('Segoe UI', 20))
first_name_label.grid(row=0, column=0)
first_name_entry = Entry(loginFrame, font=('Segoe UI', 20))
first_name_entry.grid(row=0, column=1)

email_label = Label(loginFrame, text="Email@: ", font=('Segoe UI', 20))
email_label.grid(row=1, column=0)
email_entry = Entry(loginFrame, font=('Segoe UI', 20))
email_entry.grid(row=1, column=1)

password_label = Label(loginFrame, text="Password: ", font=('Segoe UI', 20))
password_label.grid(row=2, column=0)
password_entry = Entry(loginFrame, font=('Segoe UI', 20), show='*')
password_entry.grid(row=2, column=1)

submitButton = Button(submitFrame, text="Submit", font=('Segoe UI', 15),
                      command=info_read, relief=GROOVE, border=3
                      )
submitButton.grid(row=0, column=0)


# Admin frame is configured, only opens when login with 'a' 'a' 'a'

rightFrameTitle = Label(adminFrame, text="Welcome to admin panel", font=("segoe uı", 15))
rightFrameTitle.grid(row=0, column=0)
adminButton = Button(adminFrame, text="Function 1")
adminButton.grid(row=1, column=0)
adminSecondButton = Button(adminFrame, text="Function 2")
adminSecondButton.grid(row=2, column=0)

window.mainloop()
