import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("AlterBox-GUI")

# create a simple alert box (გაფრთხილების ყუთი)
tkinter.messagebox.showinfo("Alert Message", "This is just a alter message!")

# ვქმნით კითხვას რომ მივიღოთ მომხმარებლისგან პასუხი
response = tkinter.messagebox.askquestion("Simple Question", "Do you love Python ?")

if response == 0:
    tkinter.Label(window, text='You Love the python').pack()

elif response == 1:
    tkinter.Label(window, text='You Hate the Python!').pack()
