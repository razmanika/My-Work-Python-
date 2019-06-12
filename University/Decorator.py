def xmovnebi(args):
    def wrapper(func):
        XM = ['a','e','i','o','u']
        listxm = []
        for i in XM:
            if i in func:
                listxm.append(i)
            else:
                pass
        print(len(listxm),"ხმოვანია სიტყვაში")
        return args(func)
    return wrapper

def censorship(func):
    def infunc(args):
        not_allow = 'i hate python'
        if func == not_allow:
            return "ასეთი სიტყვის გამოყენება აკრძალულია!!!"
        else:
            return args
    return infunc

@xmovnebi
@censorship

def input_something(func):
    return 

input_something(input("შეიყვანეთ სიტყვა : "))