from tkinter import *
def button_pressed(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    total = str(eval(equation_text))
    equation_label.set(total)
    equation_text= total
def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)
Window = Tk()
Window.geometry("500x500")

equation_text = ""
equation_label = StringVar()
label =Label(Window,
             textvariable=equation_label,
             font=('arial',20),
             bg="white",
             width=20,
             height=2)
label.pack()
frame = Frame(Window)
frame.pack()

#NUMERIC BUTTONS
button1 = Button(frame,
                 text="1",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(1))
button1.grid(row=0,column=0)


button2 = Button(frame,
                 text="2",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(2))
button2.grid(row=0,column=1)


button3 = Button(frame,
                 text="3",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(3))
button3.grid(row=0,column=2)


button3 = Button(frame,
                 text="3",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(3))
button3.grid(row=0,column=2)


button4 = Button(frame,
                 text="4",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(4))
button4.grid(row=1,column=0)


button5 = Button(frame,
                 text="5",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(5))
button5.grid(row=1,column=1)


button6 = Button(frame,
                 text="6",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(6))
button6.grid(row=1,column=2)


button7 = Button(frame,
                 text="7",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(7))
button7.grid(row=2,column=0)


button8 = Button(frame,
                 text="8",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(8))
button8.grid(row=2,column=1)


button9 = Button(frame,
                 text="9",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(9))
button9.grid(row=2,column=2)


button0 = Button(frame,
                 text="0",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed(0))
button0.grid(row=3,column=0)

#OPERATORS

button_add = Button(frame,
                    text="+",
                    height=1,
                    width=3,
                    font=('arial',20),
                    command=lambda:button_pressed("+"))
button_add.grid(row=0,column=3)

button_sub = Button(frame,
                    text="-",
                    height=1,
                    width=3,
                    font=('arial',20),
                    command=lambda:button_pressed("-"))
button_sub.grid(row=1,column=3)

button_mult = Button(frame,
                    text="X",
                    height=1,
                    width=3,
                    font=('arial',20),
                    command=lambda:button_pressed("*"))
button_mult.grid(row=2,column=3)

button_div = Button(frame,
                    text="/",
                    height=1,
                    width=3,
                    font=('arial',20),
                    command=lambda:button_pressed("/"))
button_div.grid(row=3,column=3)



button_equals = Button(frame,
                 text="=",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= equals)
button_equals.grid(row=3,column=2)


button_dot = Button(frame,
                 text=".",
                 height=1,
                 width=3,
                 font=('arial',20),
                 command= lambda: button_pressed("."))
button_dot.grid(row=3,column=1)



button_clear = Button(Window,
                 text="Clear",
                 height=1,
                 width=6,
                 font=('arial',20),
                 command=  clear)
button_clear.pack()
Window.mainloop()