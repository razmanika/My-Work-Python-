from tkinter import *

class window(Frame):
    def __init__(self,master =None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('GUI')
        self.pack(fill = BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        self.pack(fill = BOTH , expand =1)
        file = Menu(menu)
        file.add_command(lable = 'Exit', command = self.client_exit)
        menu.add_cascade(lable = 'File', menu = file)
        edit = Menu(menu)
        edit.add_command(lable = 'undo')
        edit.add_command(lable = 'Edit', menu = edit)


        quitButton = Button(self,text = 'Exit', command = self.client_exit)
        quitButton.place(x=200,y=150)
        nameButton = Button(self,text = 'My name', command = self.client_name)
        nameButton.place(x=5,y=5)

    def client_exit(self):
        exit()
    def client_name(self):
        print('nikoloz razmadze')

root = Tk()
root.geometry('400x300')
app = window(root)
root.mainloop()
