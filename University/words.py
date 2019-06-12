def find_my(mylist,secoundlist):
    for i in secoundlist:
        if i in mylist:
            print(mylist)
            print("moidzebna",len(i.split()), "{}".format(i))


mylist = []
secoundlist = ["moon","sun","boy"]

total = 0
while total < 3:
    ask = input("sheiyvane 3 winadadeba :$ ~ ")
    for letter in ask.split():
        mylist.append(letter)
    total += 1

print(mylist)
print(find_my(mylist,secoundlist))