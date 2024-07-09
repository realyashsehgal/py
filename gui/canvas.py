from tkinter import *

Window = Tk()


canvas = Canvas(Window,height=500,width=500)

canvas.create_line(0,0,500,500,fill="blue",width=15)
canvas.create_line(0,500,500,0,fill="red",width=15)

rectangle = canvas.create_polygon(250,0,0,500,500,500,fill="green")

canvas.pack()

Window.mainloop()