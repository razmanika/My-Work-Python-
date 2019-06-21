'''
დაწერეთ დეკორატორი *args და **kwargs ის 
გამოყენებით რომელიც მიიღებს მომხარებლის
მიერ შემოტანილ მნიშვნელობას და დაადგენს არის
თუ არა ამ მნიშვნელობაში 1 integer (რიცხვი) *
'''

'''
მომხმარებელს აარჩევინეთ რამდენიმე კატეგორია net.adjara.com იდან,
რის შემდეგაც შემთხვევითი პრინციპით ურჩიეთ 10 ფილმი.
ციკლისთვის გამოიყენეთ comprehension ხოლო შემოწმებისთვის 
lambda ფუნქციები. ბონუს ქულა: html/tkinter ვიზუალისთვის. *
'''

'''ააწყვეთ სერვისი flask ის გამოყენებით რომელიც თარგმნის 
ინგლისურ სიტყვებს ქართულად და შეინახეთ .txt ფაილში, 
მნიშვნელობების მოსაძიებლად გამოიყენეთ translate.ge ს *url.
(თუ sqlite ის გამოყენებით დაწერთ დაგეწერებათ ბონუს ქულა)
ასევე აუცილებელია შექმნათ ცალკე კლასი flask ისთვის და ცალკე კლასი
FileManager რომელსაც ექნება მეთოდი ფაილში/db ში შენახვის. 
*url: https://translate.ge/word/georgia *
'''

'''
თქვენი სიტყვებით შეეცადეთ ახსნათ try, except python - ში,
რის შემდეგაც მოიყვანეთ მარტივი მაგალითი რომელიც 
დაადგენს არსებობს თუ არა btu.txt ფაილი.
(IDE - ს გამოყენების უფლებით) *
'''

'''
რა განსხვავებაა map() და filter() ფუნქციებს შორის? მოიყვანეთ მარტივი მაგალითები.
შეგიძლიათ გამოიყენოთ pycharm/python IDE .py
ფაილის შესაქმნელად სადაც ჩაწერთ როგორც მუშა 
კოდს ასევე კომენტარის სახით თოერიულ პასუხს კითხვაზე. *
'''

'''
lambda ოპერატორის დახმარებით დაწერეთ ფუქნცია რომელიც
დაადგენს სიაში მყოფი მათემატიკური მნიშვნელობის საშუალო მაჩვენებელს.
სია შექმენით შემთხვევითი მათემათიკური მაჩვენებლებით
(random ბიბლიოთეკის გამოყენებით) (რაოდენობა იყოს 5 ცალზე მეტი) *
'''

'''
რა არის რეკურსია? განმარტეთ და მოიყვანეთ მარტივი მაგალითი. *
'''


def deco_func(func):
  def inner(*a):
    return func(*a)
  return inner

@deco_func
def user_input(a):
  for i in a.split():
    print(i)

  

user_input(input('შეიყვანე რამე: '))





# def main(func):
#   def wrapper(*args):
#     print(args)
#     func(*args)
#   return wrapper

# @main
# def dec(arg1, arg2):
#   integer_list = []
#   try:
#     arg1.split()
#     arg2.split()
#   except:
#     pass
#   try:
#     for letter in arg1:
#       try:
#         letter=int(letter)
#       except:
#         pass
#       else:
#         integer_list.append(letter)
#   except:
#     pass
#   try:
#     for letter1 in arg2:
#       try:
#         letter1=int(letter1)
#       except:
#         pass
#       else:
#         integer_list.append(letter1)
#   except:
#     pass
#   if arg2==int(arg2):
#     integer_list.append(arg2)
#   print(integer_list)


# dec('asdf98', 9)
