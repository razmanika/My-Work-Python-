from tkinter import *

def inp():
    global inpt
    global inpt1
    string = inpt.get()

    try:
        global user_name
        global user_surname
        user_name = str(name)
        user_surname = str(surname)
        info.configure(text = name)
        info1.configure(text = surname)
        f = open('data.txt','w+')
        f.write(user_name)
        f.close()
    except:
        info.configure(text = 'Please enter your name and Surname')
    else:
        info.configure(text = 'Info Successfully added')
        
    root.update()


root=Tk()
root.geometry("600x300-0+0")
Label(root,text = 'Name', height = 1, width = 7 ).grid(row=0)
Label(root, text = 'Surname', height = 2, width = 8).grid(row=1)
inpt=Entry(root,width = 35)
inpt1 = Entry(root,width = 35)

inpt.grid(row=0, column = 1)
inpt1.grid(row = 1, column = 1)

info = Label(root,text = "", height = 1)
info.grid(row = 3, column = 1)
info1= Label(root, text ='', height= 2)
info1.grid(row= 4, column = 1)

get = Button(root, text = 'Save', command = inp)
get.grid(row=2,column =1)
mainloop()

