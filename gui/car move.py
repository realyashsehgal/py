from tkinter import *
def moveup(event):
    car.place(x=car.winfo_x(),y=car.winfo_y()-10)
def movedn(event):
    car.place(x=car.winfo_x(),y=car.winfo_y()+10)
def moveleft(event):
    car.place(x=car.winfo_x()-10,y=car.winfo_y())
def moveright(event):
    car.place(x=car.winfo_x()+10,y=car.winfo_y())
Window = Tk()
Window.geometry("600x600")

gaddi = PhotoImage(file='C:\\Users\\yashs\\OneDrive\\Desktop\\coding\\py\\gui\\mater.png')
car = Label(Window,image=gaddi)
car.place(x=0,y=200)

Window.bind("<w>",moveup)
Window.bind("<s>",movedn)
Window.bind("<a>",moveleft)
Window.bind("<d>",moveright)

Window.bind("<Up>",moveup)
Window.bind("<Down>",movedn)
Window.bind("<Left>",moveleft)
Window.bind("<Right>",moveright)

Window.mainloop()