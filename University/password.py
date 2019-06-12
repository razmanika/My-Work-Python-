def number_in_pas(password):
    num = 0
    for number in password:
        if number.isdigit():
            num += 1
    if num > 1:
        return True
    else:
        return False


def big_letter(password):
    for letters in password:
        if letters.isupper():
            return True
    else:
        return False


def errors(password):
    for error in akrdzaluli:
        if error in password:
            return False
    else:
        return True


def all(password):
    if len(password) < 6:
        return "!!! paroli unda sheicavdes 6 ze met simbolos !!!"

    if not number_in_pas(password):
        return "!!! parolshi aucilebelia 1_ze meti ricxvi !!!"

    elif not big_letter(password):
        return "!!! paroli unda sheicavdes ert did asos mainc !!!"

    elif not errors(password):
        return "!!! parolshi ar sheidzleba [~!@#$%^&*()_-+=}{|[]\?/:;'<>,.] am simboloebi gamoyeneba !!!"

    else:
        return "** paroli sheyvanilia ** [tqveni parolia -{}]".format(passw)


akrdzaluli = "~!@#$%^&*()_-+=}{|[]\?/:;'<>,."

passw = input("sheiyvanet paroli ~:$ an sheiyvanet [txt]: ")
if passw == "txt":
    file = input('sheiyvanet pailis dasaxeleba :')
    txt = open(file + ".txt", "r")
    for txt_line in txt:
        print(all(txt_line))
else:
    print(all(passw))
