
class Isogram:

    def __init__(self,file_txt):
        self.file_txt = file_txt

    def check_file(self):
        try:
            global read
            f = open(self.file_txt,'r')
            read = f.read()
        except:
            print('No such file name')
        else:
            print('Your file was successfully found')
        finally:
            print('This Is a Filename Checker !!!')
            print('Word is :',read)

    def check_word(self):
        if len(set(read)) == len(read):
            return 'no repeated letter'
        else:
            return 'letters were repeated !!! '


isogram = Isogram('SparP.txt')
isogram.check_file()
print(isogram.check_word())