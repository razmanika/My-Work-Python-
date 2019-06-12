import tkinter

class GeeksBro:
    
    def __init__(self, window):

        self.text_btn = tkinter.Button(window, text='Click Me!', command=self.say_hi)
        self.text_btn.pack()

        self.close_btn = tkinter.Button(window, text='Exit', command=self.close)
        self.close_btn.pack()

    def say_hi(self):
        tkinter.Label(window, text='Welcome', font='', fg='green').pack()

    def close(self):
        exit()

window = tkinter.Tk()
window.title("GUI-Classes")
window.geometry('800x600')

we_geek = GeeksBro(window)


window.mainloop()