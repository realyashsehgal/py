from tkinter import *
def drag(event):
    widget = event.widget
    widget.startX = event.x 
    widget.startY = event.y
def loos(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX  + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
Window = Tk()
Label1 = Label(Window,bg="red",height=5,width=10)
Label1.place(x=0,y=0)
Label1.bind("<Button-1>",drag)
Label1.bind("<B1-Motion>",loos)
Window.mainloop()