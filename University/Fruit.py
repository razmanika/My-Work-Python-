import random
class fruit:

    def __init__(self,fruit_info,ripe,price):
        self.fruit_info = fruit_info
        self.ripe = ripe
        self.price = price
    
    def info(self):
        if self.fruit_info == 'ვაშლი':
            return '{} შეიცავს რკინას და ის არის მწვანე !'.format(self.fruit_info)
        elif self.fruit_info == 'ატამი':
            return '{} შეიცავს უამრავ ვიტამინს და არის მოყვითალო !'.format(self.fruit_info)
        elif self.fruit_info == 'ალუბალი':
            return '{} არის ძალიან გემრიელი და პატარა'.format(self.fruit_info)
        else:
            return 'შეყვანილი ხილი არ მოიძებნა სცადეთ ხელახლა'
    
    def mosavali(self):
        if self.ripe == 'მწიფე':
            return '{} მწიფეა'.format(self.fruit_info)
        elif self.ripe == 'მკვახე':
            return '{} მკვახეა'.format(self.fruit_info)
        else:
            return 'სცადეთ ხელახლა !!! :არასწორი პარამეტრი:'


    def pasi(self):
        apple = 2.30
        peach = 3.60
        alpine = 2.00


        if rand_choose == 'გაზაფხული':
            if self.fruit_info == 'ვაშლი':
                return '1კგ {0:.2f} ლარი'.format(apple)
            elif self.fruit_info == 'ატამი':
                return '1კგ {0:.2f} ლარი' .format(peach)
            elif self.fruit_info == 'ალუბალი':
                return '1კგ {0:.2f} ლარი'.format(alpine)


        elif rand_choose == 'ზაფხული':
            if self.fruit_info == 'ვაშლი':
                return'1კგ {0:.2f} ლარი'.format(apple)
            elif self.fruit_info == 'ატამი':
                return'1კგ {0:.2f} ლარი'.format(peach)
            elif self.fruit_info == 'ალუბალი':
                return'1კგ {0:.2f} ლარი'.format(alpine)


        elif rand_choose == 'შემოდგომა':
            if self.fruit_info == 'ვაშლი':
                return '1კგ {0:.2f} ლარი'.format(apple - apple/100*15)
            elif self.fruit_info == 'ატამი':
                return '1კგ {0:.2f} ლარი'.format(peach - peach/100*15)
            elif self.fruit_info == 'ალუბალი':
                return '1კგ {0:.2f} ლარი'.format(alpine - alpine/100*15)


        elif rand_choose == 'ზამთარი':
            if self.fruit_info == 'ვაშლი':
                return '1კგ {0:.2f} ლარი'.format(apple + (apple/100)*15)
            elif self.fruit_info == 'ატამი':
                return '1კგ {0:.2f} ლარი'.format(peach + (peach/100)*15)
            elif self.fruit_info == 'ალუბალი':
                return '1კგ {0:.2f} ლარი'.format(alpine + (alpine/100)*15)

seasons = ['გაზაფხული','ზაფხული','შემოდგომა','ზამთარი']
rand_choose = random.choice(seasons)
#print(rand_choose) #თუ მოგინდება გაიგო სეზონი რანდომად
fruit1 = fruit('ვაშლი','მწიფე',rand_choose)
fruit2 = fruit('ატამი','მკვახე',rand_choose)
fruit3 = fruit('ალუბალი','მკვახე',rand_choose)
print(fruit1.info())
print(fruit1.mosavali())
print(fruit1.pasi())

print(fruit2.info())
print(fruit2.mosavali())
print(fruit2.pasi())

print(fruit3.info())
print(fruit3.mosavali())
print(fruit3.pasi())