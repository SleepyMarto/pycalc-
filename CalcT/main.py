import tkinter as tk
from tkinter import *
from func import Functions

window = tk.Tk()
window.title("Calculator")
window.geometry('255x375')
window.resizable(False, False)


equation_label = StringVar()

func = Functions(equation_label)

label = Label(window, textvariable=equation_label, font=('sans-serif', 20), background="white", width=16, height=1).pack()

# 1 do 9 chislata
frame = Frame()
frame.pack()

# +, 0, -
frame_below = Frame()
frame_below.pack()

# enter i C
frame_below2 = Frame()
frame_below2.pack()


button9 = Button(frame, text=9, height=3, width=6, font=25, command=lambda: func.button_press(9))
button9.grid(row=0, column=2)

button8 = Button(frame, text=8, height=3, width=6, font=25, command=lambda: func.button_press(8))
button8.grid(row=0, column=1)

button7 = Button(frame, text=7, height=3, width=6, font=25, command=lambda: func.button_press(7))
button7.grid(row=0, column=0)

divide = Button(frame, text="/", height=3, width=6, font=25, command=lambda: func.button_press("/"))
divide.grid(row=0, column=3)

button6 = Button(frame, text=6, height=3, width=6, font=25, command=lambda: func.button_press(6))
button6.grid(row=1, column=2)

button5 = Button(frame, text=5, height=3, width=6, font=25, command=lambda: func.button_press(5))
button5.grid(row=1, column=1)

button4 = Button(frame, text=4, height=3, width=6, font=25, command=lambda: func.button_press(4))
button4.grid(row=1, column=0)

multiply = Button(frame, text="*", height=3, width=6, font=25, command=lambda: func.button_press("*"))
multiply.grid(row=1, column=3)

button3 = Button(frame, text=3, height=3, width=6, font=25, command=lambda: func.button_press(3))
button3.grid(row=2, column=2)

button2 = Button(frame, text=2, height=3, width=6, font=25, command=lambda: func.button_press(2))
button2.grid(row=2, column=1)

button1 = Button(frame, text=1, height=3, width=6, font=25, command=lambda: func.button_press(1))
button1.grid(row=2, column=0)

minus = Button(frame, text="-", height=3, width=6, font=25, command=lambda: func.button_press("-"))
minus.grid(row=2, column=3)


decimal = Button(frame_below, text=".", height=3, width=6, font=25, command=lambda: func.button_press("."))
decimal.grid(row=0, column=0)

button0 = Button(frame_below, text=0, height=3, width=13, font=25, command=lambda: func.button_press(0))
button0.grid(row=0, column=1)

plus = Button(frame_below, text="+", height=3, width=6, font=25, command=lambda: func.button_press("+"))
plus.grid(row=0, column=3)


delete = Button(frame_below2, text="C", height=3, width=13, font=25, command=func.clear)
delete.grid(row=1, column=0)

enter = Button(frame_below2, text="enter", height=3, width=13, font=25, command=func.equals)
enter.grid(row=1, column=1)


window.mainloop()