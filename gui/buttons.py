from tkinter import *
count = 0
def click():
    global count
    count+=1
    print(count)
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
# img = PhotoImage(file='')
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
Window.config(background="red")
Button = Button(Window,text="are you a gc",
                font=('Arial',40,'bold'),
                command=click,
                fg='#ffae00',
                bg='#0d2275',
                activebackground='#0d2275',
                activeforeground='#ffae00',
                state='active',
                image=icon,
                compound='right')
Button.pack()
Window.mainloop()