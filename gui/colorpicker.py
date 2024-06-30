from tkinter import *
from tkinter import colorchooser
def clicked():
    color = colorchooser.askcolor()
    colorhex = color[1]
    Window.config(background=colorhex)
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
click = Button(Window,text="Click me",
               command=clicked)
click.pack()
Window.mainloop()