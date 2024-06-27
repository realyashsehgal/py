from tkinter import *
import os

def submit():
    user_name = userentry.get()
    password = passentry.get()
    print(user_name)
    print(password)
    with open('userdata.txt','w') as file:
        file.write("User name: "+user_name+"\n")
        file.write("Password: "+password)
# Create the main window
Window = Tk()
Window.geometry("600x600")

# Load the image and set it as the icon
image = PhotoImage(file='login_page\\icon.png')
Window.iconphoto(True, image)

# Set the title of the window
Window.title("LOGIN PAGE")

# Create and place the header label
header = Label(Window, text="Login Form", font=('Arial', 20, 'bold'))
header.place(relx=0.40, rely=0.09)

# Create and place the username label
username_label = Label(Window, text="UserName", font=('Arial', 11))
username_label.place(relx=0.27, rely=0.2)

# Create and place the user entry field
userentry = Entry(Window, font=('Arial', 10))
userentry.place(relx=0.27, rely=0.25, height=25, width=300)

# Create and place the password label
password_label = Label(Window, text="Password", font=('Arial', 11))
password_label.place(relx=0.27, rely=0.33)

#Create and place the password entry field
passentry = Entry(Window, font=('arial',10))
passentry.place(relx=0.27,rely=0.38,width=300,height=25)

#making submit button
submitbutton = Button(Window,text="Submit",
                      font=('arial',15),
                      command=submit)
submitbutton.place(relx=0.47,rely=0.55,height=25)
Window.mainloop()
