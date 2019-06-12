import tkinter

window = tkinter.Tk()
window.title("GUI-Menu")

def func():
    pass

def new_file():
    pass


# ვქმნით მენიუს როოთს რომ შევიტანოთ ყოლიფერი
root_menu = tkinter.Menu(window) # სად გვინდა რომ გამოჩნდეს მენიუს ბარი
window.config(menu = root_menu)

# შევქმნათ sub menu როოთ მენიუში
file_menu = tkinter.Menu(root_menu) # ინიციალიზაციას უკეთებს ახალ სუბ მენიუს რუთში
root_menu.add_cascade(label = "File", menu = file_menu) # sub menus-ს დასახელება მოკლედ მაინ სახელი
file_menu.add_command(label = "New file.....", command = new_file)
file_menu.add_command(label = "Open files", command = func)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = window.quit)


# შევქმნათ ახალი საბ მენიუ
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = func)
edit_menu.add_command(label = "Redo", command = func) 


window.mainloop()