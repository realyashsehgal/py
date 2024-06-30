from tkinter import *
def submittemp():
    print("The temprature is "+str(temp_scale.get())+" degree celcius")
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
temp_scale = Scale(Window,from_=100,
                   to=0,
                   length=500,
                   orient='vertical',
                   tickinterval=10,
                   troughcolor="red",
                   fg="blue",
                   bg="yellow")
submit = Button(Window,text='sbumit',
                command=submittemp)
submit.pack(side='bottom')
temp_scale.pack()
Window.mainloop()