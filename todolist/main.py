from tkinter import *
def addtolist():
    job = input_box.get()
    todolist.insert(todolist.size(),job)
    todolist.config(height=todolist.size())
    input_box.delete(0,END)
def removee():
    todolist.delete(todolist.curselection())
Window = Tk()
Window.config(background='#fbe9e7')
Window.geometry('700x500')
header = Label(Window,
               text="Todo List",
               font=('arial',30,'bold'),
               width=650,
               bg='#fbe9e7')
header.pack()
input_box = Entry(Window,
                 width=50,
                 font=('arial',16),
                 bg='#ffccbc',
                 fg='#000000')
input_box.pack()
add = Button(Window,text="Add",
             font=('arial',15,'bold'),
             command=addtolist,
             bg='#d84315',
             fg='#ffffff')
add.pack(anchor=CENTER,pady=10)

todolist = Listbox(Window,
                   width=50,
                   height=1,
                   font=('arial',13),
                   bg='#ffab91',
                   fg='#000000')
todolist.pack(anchor='w',padx=47)
remove = Button(Window,text="Remove",
                font=('arial',15,'bold'),
                command=removee,
                bg='#d84315',
                fg='#ffffff')
remove.pack(anchor=CENTER,pady=10)
Window.mainloop()