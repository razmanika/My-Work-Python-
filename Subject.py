class Student:
    def __init__(self, saxeli, gvari, wlovaneba, kreditis_raodenoba):
        self.saxeli = saxeli
        self.gvari = gvari
        self.wlovaneba = wlovaneba
        self.kreditis_raodenoba = kreditis_raodenoba

    def Studname(self):
        print("სტუდენტის სახელი :-> {}".format(self.saxeli))
    
    def Studsurname(self):
        print("სტუდენის გვარი :-> {} ".format(self.gvari))
    

    def credit(self):
        if self.kreditis_raodenoba == 240:
            print("{} ბაკალავრია".format(self.saxeli))
        else:
            print("{} არ არის ბაკალავრი!!!".format(self.saxeli))


class Subject:
    def __init__(self, sagnis_dasaxeleba, sagnis_krediti, jamuri_qula):
        self.sagnis_dasaxeleba = sagnis_dasaxeleba
        self.sagnis_krediti = sagnis_krediti
        self.jamuri_qula = jamuri_qula

    def sub_credit(self):
        print("საგნის კტედიტი :-> {}".format(self.sagnis_krediti))
    def score_equal(self):
        print("ჯამური ქულა -> {}".format(self.jamuri_qula))

    def passed(self):
        if self.jamuri_qula <= 51:
            print("{} შეტენილია".format(self.sagnis_dasaxeleba))
        else:
            print("{} ჩაბარებულია".format(self.sagnis_dasaxeleba))

stud1 = Student("ნიკუშა", "რაზმაძე", "18", 240)
stud2 = Student("გიორიგ", "კოკაშვილი", "19", 236)
stud1.Studname()
stud1.Studsurname()
stud1.credit()
stud2.Studname()
stud2.Studsurname()
stud2.credit()

subj1 = Subject(input("შეიყვანე საგანი : "), "6", 51)
subj2 = Subject(input("შეიყვანე მეორე საგანაი : "), "4", 70)
subj1.sub_credit()
subj1.score_equal()
subj1.passed()
subj2.sub_credit()
subj2.score_equal()
subj2.passed()