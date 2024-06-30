from tkinter import *
Window = Tk()
food = ["pizza","burger","fried chicken"]
Window.geometry("600x600")
Window.title("ggs i am title")
pizzaa = PhotoImage(file='gui\\pizza.png')
burger = PhotoImage(file='gui\\burger.png')
chicken = PhotoImage(file='gui\\chicken.png')
imges = [pizzaa,burger,chicken]
Window.iconphoto(True,pizzaa)
x = IntVar()
value = IntVar()
value = -1
for i in range(len(food)):
    radio_button = Radiobutton(Window,text=food[i],
                               variable=x,
                               value=i,
                               padx=15,
                               pady=15,
                               font=('Arial',20,'bold'),
                               image=imges[i],
                               compound='left',
                               indicatoron=0,
                               width=375)
    radio_button.pack(anchor=W)
Window.mainloop()