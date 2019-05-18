from tkinter import *

def inp():
    global inpt
    number = inpt.get()

    try:
        int(number)
        info.configure(text=number)
    except ValueError:
        info.configure(text = 'Please enter the integer')
    root.update()

root=Tk()
root.geometry("300x100-0+0")
Label(root,text = 'input', height = 1, width = 7 ).grid(row=0)
inpt=Entry(root,width = 35)
inpt.grid(row=0, column = 1)

info = Label(root,text = "", height = 1)
info.grid(row = 3, column = 1)

get = Button(root, text = 'Input', command = inp)
get.grid(row=2,column =1)
mainloop()
