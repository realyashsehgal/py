from tkinter import *
def submitted():
    input = text_area.get(1.0,END)
    print(input)
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
text_area = Text(Window)
text_area.pack()
submit = Button(Window,
                text="Submit",
                command=submitted)
submit.pack()
Window.mainloop()