from tkinter import *
def submit():
    username = entry.get()
    print(username)
    entry.config(state='disabled')
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
# img = PhotoImage(file='')
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
Window.config(background="red")
entry = Entry(Window,
              font=('Arial',20,'italic'),
              show="*")
entry.pack(side=LEFT)
button = Button(Window,
                text='Submit',
                font=('Arial',15,'bold'),
                command=submit)
button.pack(side=RIGHT)
button_delete = Button(Window,
                       text='Delete',
                       font=('Arial',15,'bold'),
                       command=delete)
button_delete.pack(side=RIGHT)
button_backspace = Button(Window,
                          text="backSpace",
                          font=('arial',15,'bold'),
                          command=backspace)
button_backspace.pack(side=RIGHT)
Window.mainloop()