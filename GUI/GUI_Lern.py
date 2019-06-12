'''
widgets_ი ჰგავს ელემენტს HTML_ში. შეგვხვდება სხვადასხვა ტიპის ვიჯეტები ელემენტების განსხვავებული დასახელებით Tkinter-ში.
განვიხილოთ ისინი მცირედით : >
1) Button : Button მოწყობილობა გამოიყენება რომ განათავსო ღილაკი გარკვეულ ადგილას ტკინტერში. parameters text(Value of the button), fg(color of the text)
2) Canvas: Canvas გამოიყენება GUI- ში ფორმების შესაქმნელად.
3) Checkbutton : Checkbutton გამოიყენება რომ შექმნა შემოწმების ღილაკი შენს აპლიკაციაში. თქვენ შეგიძლიათ აირჩიოთ ერთზე მეტი პარამეტრი.
4) Entry : Entry-ის ვიჯეტი გამოიყენება რომ შექმნა შესავსები ველი ( input field ).
5) Frame : Frame გამოიყენება როგორც ჩარჩო თუ სად გინდა ჩასვა ვიჯეტი ტკინტერში.
6) Lable : Lable გამოიყენება რომ შექმნა ერთ ხაზზე მოწყობილობა როგორიცაა 'ტექსტი, სურათი და ა.შ.'
7) Menu : Menu გამოიყენება რომ შექმნა მენიუ GUI_ში.

Geometry Management [ყველა ვიჯეტს ტკინტერში აქვს გეომეტრიული მდებარეობა ისინი კი გვეხმარებიან ორგანიზებაში მათი ფანჯრის ჩარჩოსა და ა.შ]
მას აქვს სამი გეომეტრიული დაგეგმარების კლასი.
1) Pack() : მოწყობილობის(widget) ზომის მიხედვით გამოიტანოს ტექსტის გამოსახულება და იკავებს მთელ სიგანეს.
            ეს არის სტანდარტული მეთოდი რომ ვიჯეტი გამოჩნდეს ფანჯარაში.
2) Grid() : ის ორგანიზება უკეთებს ვიჯეთს როგორც სტრუქტურულს
3) Place() : ეს გამოიყენება რომ მოათავსო ვიჯეტი შენთვის მოსახერხებელ პოზიციაზე სადაც გინდა.

Row = Y
Column = X
'''
import tkinter

window = tkinter.Tk() # ინიციალიზაცია ხდება გამოსაჩენი ფანჯრის.
window.title('Bar_name_GUI') # ამ ფანჯარის სახელი.

#სახელის ინფუთ ველი
tkinter.Label(window, text='usename').grid(row=0)
tkinter.Entry(window).grid(row=0, column=1)

#Entry რომ გავაკეთოთ ინფუთ ველი
tkinter.Label(window, text='password').grid(row=1)
tkinter.Entry(window).grid(row=1, column=1)

# ვაკეთებთ submit ღილაკს
label3 = tkinter.Frame(window).grid(row=3, column=1)
button1 = tkinter.Button(label3, text='Submit', fg='#FF2D2D').grid(row=2, column=1)

# შესამოწმებელი
tkinter.Checkbutton(window,text = "Keep Me Logged In").grid(columnspan = 2) # columnspan პირველ ორ სიგანეს(X) იკავებს შეგვიძლია rowspan_ის გამოყენებაც (Y)-ისთვის

# # პირველი არგუმენტი არის სადაც გამოდის ხოლო მეორე რაც უნდა გამოვიდეს
# label = tkinter.Label(window, text='Hello World!').pack() # მოწყობილობის(widget) ზომის მიხედვით გამოიტანოს ტექსტის გამოსახულება

# # საფუძვლიანი ვიჯეტი
# tkinter.Label(window, text='Suf. width', fg='white', bg='purple').pack()

# # სიგანე X_ის
# tkinter.Label(window, text='Taking all available X width', fg='white', bg='green').pack(fill= 'x')

# #სიგრძე Y_ის
# tkinter.Label(window, text='Taking all available Y height', fg='white', bg='black').pack(side='left', fill='y')
# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side='bottom')

# btn1 = tkinter.Button(top_frame, text='Button1', fg='red').pack()
# btn2 = tkinter.Button(top_frame, text='Button2', fg='green').pack()
# btn3 = tkinter.Button(bottom_frame, text='Button3', fg='purple').pack(side='left')
# btn4 = tkinter.Button(bottom_frame, text='Button3', fg='orange').pack(side='left')



window.geometry('800x600')
window.mainloop() # ლუპავს ფანჯარას და ამიშავებს იქამდე სანამ არ გავთიშავ.

