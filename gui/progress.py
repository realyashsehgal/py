from tkinter import *
from tkinter.ttk import *
import time
Window = Tk()
Window.geometry("300x300")
def progresss():
    end = 10
    i = 1
    while(i<=end):
        time.sleep(1)
        i+=1
        loading['value'] += 10
        Window.update_idletasks()
        percentage.set(str((i/10)*100) + "%")
percentage = StringVar()
loading = Progressbar(Window,orient=HORIZONTAL,length=150)
loading.pack()
progress = Label(Window,font=('ariral',12,'bold'),
                 textvariable=percentage)
progress.pack()
submit = Button(Window,text="Submit",
                command=progresss)
submit.pack()
Window.mainloop()