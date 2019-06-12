import sys
import random


choose_num = random.randrange(444,999,2)

def funkcia(ricxvi):
  if ricxvi == range:
    return(choose_num)
a=funkcia(choose_num)
print(a)


symbol_1 =     [(1,   "I"), (5,   "V"), (10,   "X")]
symbol_10 =    [(10,  "X"), (50,  "L"), (100,  "C")]
symbol_100 =   [(100, "C"), (500, "D"), (1000, "M")]

symList = [symbol_1, symbol_10, symbol_100]

def change_Romal (digit, symList):
    one =  symList[0][1]
    five = symList[1][1]
    ten =  symList[2][1]

    switch = {
        1: one,
        2: one + one,
        3: one + one + one,
        4: one + five,
        5: five,
        6: five + one,
        7: five + one + one,
        8: five + one + one + one,
        9: one + ten,
    }
    return switch.get(digit, "")

x=change_Romal(10,symbol_1)
print(x)