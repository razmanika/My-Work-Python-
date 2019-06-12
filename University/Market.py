'''
უნდა გავაკეთო პარსერი ორმელიც წამოიგებს პროდუქტებს
საიტებიდან და შესთავაზებს
მომხმარებელს.
'''


def text_save(text, name):
    total = 0
    while total < 1:
        ask = input("gsurt tu ara shenadzenis txt pailshi chawera ? [ki] an [ara] : ")
        if ask == "ki":
            file = open(name + ".txt", "w")
            file.write(" ".join(text))
            return "# paili chawerilia # [{}.txt]".format(name)
            break
        elif ask == "ara":
            return "# sasiamovno dges gisurvebt #"
            break
        else:
            return "dapiqsirda shecdoma"
    

def buy_nikora(nbuy): # Nicora Product list
    nlist = []
    count = 0
    while count <= len(nbuy):
        buy = str(input("chawere dasaxeleba an [stop]shenadzeni: "))
        if buy in nbuy:
            nlist.append(buy)
        if buy == 'stop':
            return 'kalatashi daemata > {}'.format(nlist)
            break
        elif buy == "nikora":
            return nbuy
        elif buy not in nbuy:
            print('aseti produqti ar arsebobs !!!')
        elif len(nlist) == len(nbuy):
            break
    return text_save(nlist, "NikoraP")


def buy_spar(sbuy): # Spar product list
    slist = []
    count = 0
    while count < len(sbuy):
        buy = str(input("chawere dasaxeleba an [stop]shenadzeni: "))
        if buy in sbuy:
            slist.append(buy)
        if buy == 'stop':
            return 'kalatashi daemata > {}'.format(slist)
            break
        elif buy == "spari":
            return sbuy
        elif buy not in sbuy:
            print('aseti produqti ar arsebobs !!!')
        elif len(slist) == len(sbuy):
            break
    return text_save(slist, "SparP")


market = dict(nikora=["rdze", "puri", "kvercxi", "maionezi"], spar=["puri", "wyali", "pamidori", "pilmeni", "naxshiri"])

user_input = input("airchiet marketi : [nikora]--[spar] :")

if user_input == "spar":
    spari = market["spar"]
    in_spar = input("daweret [spar] rom naxot produqti : ")
    if in_spar == "spar":
        print(spari)
        print(buy_spar(spari))

elif user_input == "nikora":
    nikoras = market["nikora"]
    in_nikora = input("daweret [nikora] rom naxot produqti : ")
    if in_nikora == "nikora":
        print(nikoras)
        print(buy_nikora(nikoras))
else:
    print("samwuxarot aseti magazia ar moidzebna !!!")
