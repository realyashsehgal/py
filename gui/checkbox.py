from tkinter import *
def display():
    if (x.get() == 1):
        print("you have my respect")
    else:
        print("stupid feminist")
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
Window.config(background="red")
x= IntVar()
check_box = Checkbutton(Window,
                        text="eren was right ??",
                        font=('arial',10,'bold'),
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=display)
check_box.pack()

Window.mainloop()