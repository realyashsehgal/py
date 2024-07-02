from tkinter import *
from tkinter import filedialog
def opening():
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\yashs\\OneDrive\\]Desktop\\coding\\py',
                                          title="Open text file only",
                                          filetypes=(('text files','*.txt'),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()
Window = Tk()
file_open = Button(Window,
                   text="Click me to open file dialog thingie",
                   command=opening)
file_open.pack()
Window.mainloop()
