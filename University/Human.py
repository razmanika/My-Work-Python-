'''
ადამიანის ორგანიზმის ურთიერთობა
ტვინი
გული
ფილტვები
თვალები
ყურები

'''

import random
class human:
    def __init__(self,brain,heart,eyes,ears,lungs):
        self.brain = brain
        self.heart = heart
        self.eyes = eyes
        self.ears = ears
        self.lungs = lungs
    
    def tvini(self):
        print('გამარჯობა მე ვარ ტვინი და ვაკონტროლებ ყველაფერს მე თუ ცოცხალი ვარ გულიც ცოცხლობს\n--> ჩემი სიცოცხლეა {}'.format(self.brain))
        if self.brain <=50 : # დამოკიდებული არიან ერთმანეთზე
            return '$$ ჩემი აზროვნება მცირდება და ასევე მახსოვრობაც $$'
        else:
            return '$$ ჩემთვის აზროვნება უკეთესია და ასევე მახსოვრობაც $$'
    
    def guli(self):
        print('მოგესალმებით მე ვარ გული და დამოკიდებული ვარ ტვინზე მე თუ ვცოცხლობ მაშინ ფილტვები სუნთქავს\n--> ჩემი სიცოცხლეა {}:'.format(self.heart))
        if self.lungs <= 80 or self.heart <= 60:   # დამოკიდებული არიან ერთმანეთზე
            return '$$ ჩემთვის რთული ხდება სისხლის მიწოდება სწრაფად $$'
        else:
            return '$$ ჩემთვის შედარებით მარტივია სისხლის მიწოდება სწრაფად $$'
    def tvalebi(self):
        print('მე ვარ თვალები და მე ვეხმარები სხეულს შეიცნოს გარე სამყარო და ამაში ყურები მეხმარება\n --> ჩემი ხედვითი სიცოცხლე {}'.format(self.eyes))
        if self.eyes <=65:
            return '$$ ჩემთვის რთულია საგნების აღქმა შორ მანძილზე $$'
        else:
            return '$$ ჩემთვის მარტივია საგნების აღქმა შორ მანძილზე $$'
    def yurebi(self):
        print('მე ვარ ყურები და მე ტვინს ვაძლევ სმენას რათა იაზროვნოს\n --> ჩემი სმენადობის სიცოცხლეა {}'.format(self.ears))
        if self.ears <=60:
            return '$$ მე მიჩირს გარემოს ხმების სმენა $$'
        else:
            return '$$ მე მიადვილდება გარემოს ხმების მოსმენა $$'
    def piltvebi(self):
        print('მე ვარ ფლტები და ჟანგბადით ვამდიდრებ თითოეულ ორგანოს\n--> ჩემი სიცოცხლე {}'.format(self.lungs))
        if self.lungs <= 80 or self.heart <= 60:     # დამოკიდებული არიან ერთმანეთზე
            return '$$ მე მიჩირს სუნთქვა და შესაძლოა გული გაჩერდეს $$'
        else:
            return '$$ მე მიადვილდება სუნთქვა და გულს ვეხმარები მუშაობაში $$'


age = random.randrange(85)
sex = random.choice(['ქალი','კაცი'])
print("#### {} წლის {} ####".format(age,sex))
if age <= 30:
    heart = random.randrange(83,96)
    mind  = random.randrange(70,95)
    lungs = random.randrange(85,99)
    eyes = random.randrange(1,100)
    ears = random.randrange(1,100)
else:
    heart = random.randrange(50,82)
    mind  = random.randrange(55,70)
    lungs = random.randrange(75,99)
    eyes = random.randrange(1,80)
    ears = random.randrange(1,85)

person = human(mind,heart,eyes,ears,lungs)
print(person.tvini())
print(person.guli())
print(person.tvalebi())
print(person.yurebi())
print(person.piltvebi())