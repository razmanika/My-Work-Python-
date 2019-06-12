class Pangram:
    def __init__(self,sentence):
        self.sentence = sentence.lower()
        

    def check_pangram(self):
        if len(set(self.sentence.lower())) == 27: # 26 ასო და +1 "space"
            return 'This is a Pangram'
        else:
            return 'This is not a Pangram !!'



panaga = Pangram('The quick brown fox jumps over the lazy dog')
print(panaga.check_pangram())

"""
ესე მქონდა დაწერილი ადრე 

"""

# import string
# class Pangram:
#     def __init__(self,str1):
#         self.str1 = str1


#     def ispangram(self, alphabet=string.ascii_lowercase):
#         mylist = []
#         for letter in alphabet:
#             if letter in self.str1:
#                 mylist.append(letter)
#         if len(mylist) == 26:
#             return True
#         else:
#             return False

# text = Pangram('The quick brown fox jumps over the lazy dog')
# print(text.ispangram())