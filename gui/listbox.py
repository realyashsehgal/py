from tkinter import *
def submitt():
    print(list_box.get(list_box.curselection()))
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
list_box = Listbox(Window,
                   width=50,
                   bg='black',
                   fg='yellow',
                   font=('Arial',30))
list_box.insert(1,"Pizza")
list_box.insert(2,"burger")
list_box.insert(3,"chicken")
list_box.insert(4,"cake")
submit = Button(Window,text="submit",
                font=('arial',20,'bold'),
                command=submitt)
submit.pack(side='bottom')
list_box.pack()
Window.mainloop()