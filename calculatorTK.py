from tkinter import *


def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        # eval will parse the equation
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Cannot divide by zero")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""


def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
button_height = 3
button_width = 9
button_font_size = 35
window.title("Python Calculator")
window.geometry("400x420")

equation_text = ""

equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('consolas', 20),
              bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button0 = Button(frame, text=0, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(0))
button0.grid(row=3, column=1)

button1 = Button(frame, text=1, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(1))
button1.grid(row=2, column=0)

button2 = Button(frame, text=2, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(2))
button2.grid(row=2, column=1)

button3 = Button(frame, text=3, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(3))
button3.grid(row=2, column=2)

button4 = Button(frame, text=4, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(7))
button7.grid(row=0, column=0)

button8 = Button(frame, text=8, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(8))
button8.grid(row=0, column=1)

button9 = Button(frame, text=9, height=button_height, width=button_width,
                 font=button_font_size,
                 command=lambda: button_press(9))
button9.grid(row=0, column=2)

plus_sign = Button(frame, text='+', height=button_height, width=button_width,
                   font=button_font_size,
                   command=lambda: button_press('+'))
plus_sign.grid(row=3, column=3)

minus_sign = Button(frame, text='-', height=button_height, width=button_width,
                    font=button_font_size,
                    command=lambda: button_press('-'))
minus_sign.grid(row=2, column=3)

multiply_sign = Button(frame, text='*', height=button_height, width=button_width,
                       font=button_font_size,
                       command=lambda: button_press('*'))
multiply_sign.grid(row=1, column=3)

divisor_sign = Button(frame, text='/', height=button_height, width=button_width,
                      font=button_font_size,
                      command=lambda: button_press('/'))
divisor_sign.grid(row=0, column=3)

equal_sign = Button(frame, text='=', height=button_height, width=button_width,
                    font=button_font_size,
                    command=equals)
equal_sign.grid(row=4, column=3)

decimal_sign = Button(frame, text='.', height=button_height, width=button_width,
                      font=button_font_size,
                      command=lambda: button_press('.'))
decimal_sign.grid(row=3, column=2)

clear_sign = Button(frame, text='clear', height=button_height, width=button_width,
                    font=button_font_size,
                    command=clear)
clear_sign.grid(row=3, column=0)

window.mainloop()
