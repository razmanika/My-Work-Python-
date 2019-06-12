def testFunc(func):
    def in_func_wrapper(file,some_text,some_int):
        save = []
        try:
            f = open(file + ".txt","r")
            return f, func(file)
        except:
            return "ასეთი ფაილი არ არსებობს"
        try:
            for i in some_text.split():
                if type(i) == str:
                    return "შემოტანილი ტექსი არის 'STR'",func(some_text)
        except:
            return "ეს ტექსტი არ არის 'STR'"
        try:
            for num in some_int:
                if type(num) == int:
                    return "შემოტანილი იქნა 'INT'",func(some_int)
        except:
            return "შემოტანილი არა არის INT"
    return in_func_wrapper




@testFunc

def user_inputs(file,some_text,some_int):
    return
print(user_inputs(input("შეიყვანეთ რაიმე ჩემიკაააი: ")))
    