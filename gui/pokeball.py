from tkinter import *
Windows = Tk()

canvas = Canvas(Windows,height=500,width=500)

canvas.create_arc(5,5,495,495,fill="red",extent=180,width=4)
canvas.create_arc(5,5,495,495,fill="white",start=180,extent=180,width=4)
canvas.create_oval(190,190,310,310,fill="white",width=4)
canvas.pack()
Windows.mainloop()