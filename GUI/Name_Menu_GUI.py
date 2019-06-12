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
        file = Menu(menu)
        file.add_command(label = 'Exit', command = self.client_exit)
        menu.add_cascade(label = 'File', menu = file)
        edit = Menu(menu)
        edit.add_command(label = 'Undo')
        menu.add_cascade(label = 'Edit', menu = edit)


        quitButton = Button(self,text = 'Exit', command = self.client_exit)
        quitButton.place(x=700,y=500)
        nameButton = Button(self,text = 'My name', command = self.client_name)
        nameButton.place(x=40,y=1)
        AgeButton = Button(self,text = 'AGE', command = self.client_Age)
        AgeButton.place(x = 1,y= 1)

    def client_exit(self):
        exit()
    def client_name(self):
        print('nikoloz razmadze')
    def client_Age(self):
        print('18')

root = Tk()
root.geometry('800x600')
app = window(root)
root.mainloop()