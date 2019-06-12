# import tkinter

# window = tkinter.Tk()
# window.title('Say_Hi')

# def say_hi(event):
#     tkinter.Label(window,text='Hello my Friend').pack()

# but_lable_button = tkinter.Button(window, text='Cilck Me', fg='black', bg='yellow')
# but_lable_button.bind("<Button-1>", say_hi) # bind განსაზღვრავს თუ რომელ მაუსის წკაპუნზე გამოიძახოს ფუნქცია
# but_lable_button.pack()

# window.mainloop()


import tkinter

window = tkinter.Tk()
window.title('Say_Hi')

def left_click(event):
    tkinter.Label(window,text='left Click', fg='red').pack()

def middle_click(event):
    tkinter.Label(window,text='middle Click', fg='green').pack()

def right_click(event):
    tkinter.Label(window,text='right Click', fg='purple').pack()


window.bind("<Button-1>", left_click) # bind განსაზღვრავს თუ რომელ მაუსის წკაპუნზე გამოიძახოს ფუნქცია
window.bind("<Button-2>", middle_click) # ნებისმიერ ადგილას დაწკაპუნებაზე იძახებს შესაბამის ფუნქციას
window.bind("<Button-3>", right_click)

window.geometry('800x600')
window.mainloop()