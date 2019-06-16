import tkinter , tkinter.messagebox
from tkinter import *

subject = {
    'math':4,
    'python':6,
    'startup':5,
    'architecture':3,
    'english':5,
    'managment':4
}


class GpaCalculator:
    def __init__(self, window,subject):
        self.subject = subject
        self.input_subj = StringVar()
        self.input_point = IntVar()

        # იქმნება სათაური subject 
        self.text_subj = tkinter.Label(window, text='Subject', fg='#00A786')
        self.text_subj.grid(row=0,column=1)

        # იქმნება სათაური subject
        self.text_point = tkinter.Label(window, text='Point', fg='#00A786')
        self.text_point.grid(row=0,column=3)

        # იქმნება Input ველი საგნისთვის
        self.subj_input = tkinter.Entry(window, textvariable=self.input_subj, width=20)
        self.subj_input.grid(row=1,column=1)

        # იქმნება Input ველი ქულისთვის
        self.point_input = tkinter.Entry(window, textvariable=self.input_point, width=20)
        self.point_input.grid(row=1,column=3)

        # GPA კალკულატორის ღილაკი
        self.gpa_btn = tkinter.Button(window, text='GPA', fg='#FC00A0', command=self.calculator)
        self.gpa_btn.grid(row=3,column=2)


    def calculator(self):
        for k,v in self.subject.items():
            try:
                self.subj_input == any(k)
            except ValueError:
                tkinter.messagebox.showerror("Value Error", "Please Enter Your correct Subject")
        





window = tkinter.Tk()
window.title("GUI-GPA")
gpa = GpaCalculator(window,subject)



window.mainloop()
