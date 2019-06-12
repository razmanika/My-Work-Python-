
# x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# dict1={"luwebi":list(u for u in x if u%2==0),
#       "kentebi":list(a for a in x if a%2!=0)}
# print(dict1)

def funkcia(ricxvi):
  if ricxvi == range:
    return(x)
x=list(range(444,999,2))
a=funkcia(x)


import sys

symbol1 =     [(1,   "I"), (5,   "V"), (10,   "X")]
symbol10 =    [(10,  "X"), (50,  "L"), (100,  "C")]
symbol100 =   [(100, "C"), (500, "D"), (1000, "M")]

symList = [symbol1, symbol10, symbol100]

def change_Romal (digit, symList):
    """ Converts a single digit into its roman symbols """
    one =  symList[0][1]
    five = symList[1][1]
    ten =  symList[2][1]

    switcher = {
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
    return switcher.get(digit, "")

x=change_Romal(5,symbol1)
print(x)