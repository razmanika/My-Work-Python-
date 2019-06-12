import tkinter

window = tkinter.Tk()
window.title("Canvas-GUI")

# ვქმნიტ canva ს ტერიტორიას სიგრძეზე და სიგანეხე 500px
canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

#'create_line' is used to create a line. Parameters:- (starting x-point, starting y-point, ending x-point, ending y-point)
line1 = canvas.create_line(25,25,250,250)

# parameter:- (fill = color_name)

line2 = canvas.create_line(25,25,250,250, fill='red')

# 'create_rectangle' is used to create rectangle. Parameters:- (starting x-point, starting y-point, width, height, fill)
# starting point the coordinates of top-left point of rectangle
rect = canvas.create_rectangle(500,25,175,75, fill='green') # x დაიწყო 500 იდან y=25 და სიგანე 175 და სიმაღლე 75

canvas.delete(line1,line2)

# you 'delete' all the shapes by passing 'ALL' as parameter to the 'delete' method
# canvas.delete(tkinter.ALL)
window.mainloop()