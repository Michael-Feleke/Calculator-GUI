from tkinter import *


def button_pressed(num):
    global equation_text
    equation_text = equation_text+str(num)
    equation_label.set(equation_text)


def equals():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('Arthimetic Error')
        equation_text = ""
    except SyntaxError:
        equation_label.set('Syntax Error')
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


def cancel():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)


window = Tk()
window.config(bg='black')
window.title('Simple Calculator')
window.geometry("550x550")
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label,
              width=44, height=2, bg='black', fg='white', font=('arial', 20))
label.pack()

frame = Frame(window, pady=20, bg='black')
frame.pack()

button1 = Button(frame, text=1, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(1))
button2 = Button(frame, text=2, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(2))
button3 = Button(frame, text=3, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(3))
button4 = Button(frame, text=4, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(4))
button5 = Button(frame, text=5, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(5))
button6 = Button(frame, text=6, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(6))
button7 = Button(frame, text=7, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(7))
button8 = Button(frame, text=8, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(8))
button9 = Button(frame, text=9, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(9))
button0 = Button(frame, text=0, font=15, height=2, width=6, bg='black', fg='green',
                 command=lambda: button_pressed(0))

decimal_button = Button(frame, text='.', font=15, height=2, bg='black', fg='green',
                        width=6, command=lambda: button_pressed('.'))

add_button = Button(frame, text='+', font=15, height=2, bg='black', fg='green',
                    width=6, command=lambda: button_pressed('+'))
subtract_button = Button(frame, text='-', font=15, bg='black', fg='green',
                         height=2, width=6, command=lambda: button_pressed('-'))
multiply_button = Button(frame, text='*', font=15, bg='black', fg='green',
                         height=2, width=6, command=lambda: button_pressed('*'))
divide_button = Button(frame, text='/', font=15, height=2, bg='black', fg='green',
                       width=6, command=lambda: button_pressed('/'))

equals_button = Button(frame, text='=', font=15, bg='black', fg='green',
                       height=2, width=6, command=equals)

clear_button = Button(window, text='Clear', bg='black', fg='green', font=(
    'arial', 15), command=clear)
clear_button.pack()

cancel_image = PhotoImage(file='Reminding\\cancel.png').subsample(16)
cancel_button = Button(frame, image=cancel_image, command=cancel)

button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=1, column=2, padx=5, pady=5)
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
button7.grid(row=3, column=0, padx=5, pady=5)
button8.grid(row=3, column=1, padx=5, pady=5)
button9.grid(row=3, column=2, padx=5, pady=5)
button0.grid(row=4, column=0, padx=5, pady=5)
decimal_button.grid(row=4, column=1, padx=5, pady=5)
equals_button.grid(row=4, column=2, padx=5, pady=5)
add_button.grid(row=1, column=3, padx=5, pady=5)
subtract_button.grid(row=2, column=3, padx=5, pady=5)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=4, column=3, padx=5, pady=5)
cancel_button.grid(row=0, column=3, pady=15)


window.mainloop()
