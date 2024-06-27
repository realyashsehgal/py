from tkinter import *
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
# img = PhotoImage(file='')
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
Window.config(background="red")
Label = Label(Window,text="Hello world!",
              font=('Arial',40,'bold'),
              fg='yellow',#This is for the text color
              bg='black',#this is for the background of the label
              relief='groove',#it the border type 
              bd=10,#it is for the border size
              padx=10,#obv padding 
              pady=10,
              image=icon,#it adds a image in the label
              compound='top')#And this compund sets the position of the image like top bottom right left etc
Label.place(x=0,y=0)
# Label.pack()
Window.mainloop()