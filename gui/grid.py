from tkinter import *
Window = Tk()
Window.geometry("600x600")
Window.title("ggs i am title")
icon = PhotoImage(file='gui\\gc.png')
Window.iconphoto(True,icon)
first_name =Label(Window,text="First name",
                  font=('airal',14,'bold'))
first_name.grid(row=0,column=0)
firstname_entry = Entry(Window,
                        font=('arial',15))
firstname_entry.grid(row=0,column=1)
last_name = Label(Window,text="Last name",
                  font=('arial',14,'bold'))
last_name.grid(row=1,column=0)
lastname_entry = Entry(Window,
                       font=('arial',15))
lastname_entry.grid(row=1,column=1)
submit_button = Button(Window,text="submit",
                       font=('arial',15,'bold'))
submit_button.grid(row=2,column=1,columnspan=1)
Window.mainloop(),