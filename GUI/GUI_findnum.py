import tkinter, tkinter.messagebox
import random
from tkinter import *

window = tkinter.Tk()
window.title("Find a number GUI")


class GuessNumber:
    def __init__(self, window, rand,click,lists):
        self.input_user = IntVar()
        self.rand = rand
        self.click = click
        self.lists = lists
        
        self.text_label = tkinter.Label(window, text='Guesses the number from 1 to 25', font='Helvetica 10 bold ')
        self.text_label.grid(row=0,column=0)

        self.input_num = tkinter.Entry(window, textvariable=self.input_user, width=20)
        self.input_num.grid(row=1,column=1)

        self.check_btn = tkinter.Button(window, text="Check", command=self.check_num)
        self.check_btn.grid(row=1,column=0)


    def check_num(self):
        #self.click +=1 # ყოველ კლიკზე მატულობს
        print('Answer -',self.rand)
        print("clicks -",self.click)
        try:
            user_input = int(self.input_num.get()) # მოაქვს ინფუთიდან ინფორმაცია როგორც რიცხვი
        except:
            tkinter.messagebox.showinfo("Error", "Please Enter the number!")
            self.click-=1
        if user_input == self.rand:
            tkinter.messagebox.showinfo("Winner",'Happy Winner')
            window.quit()
        elif self.click == 3:
            if 20 <= self.rand <= 25:
                tkinter.messagebox.showinfo("Hint", "Choose From 5-25\n remaining {} try".format(5-self.click))
            elif 1<=self.rand <= 5:
                tkinter.messagebox.showinfo("Hint", "Choose From 1-20\n remaining {} try".format(5-self.click))
            else:
                tkinter.messagebox.showinfo("Hint", "Choose From 5-20\n remaining {} try".format(5-self.click))
            self.click +=1
        elif self.click == 5 and user_input != self.rand:
            tkinter.messagebox.showinfo("Lose",'You Lose Try Again !')
            window.quit()
        elif 1<= user_input <=25 and user_input != self.rand:
            tkinter.messagebox.showwarning('Answer', 'Answer is incorect\n remaining {} try'.format(5 - self.click))
            self.click +=1
        elif user_input > 25 or user_input <= 0:
            tkinter.messagebox.showwarning('Number Not Found', 'You Entered The num  Which is not 1-25')
click=1
lists = range(1,26)
rand = random.choice(lists)
guess = GuessNumber(window,rand,click, lists)
window.mainloop()