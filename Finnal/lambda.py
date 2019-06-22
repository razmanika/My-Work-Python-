from random import randint

mylist = []
for i in range(6):
    value = randint(0,30)
    mylist.append(value)
sums = sum(mylist)
func = lambda x: round(x/6,2) 
print(func(sums))
