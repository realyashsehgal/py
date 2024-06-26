from tkinter import *
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
# img = PhotoImage(file='')
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
Window.config(background="red")
Window.mainloop()