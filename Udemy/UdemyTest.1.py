'''
                                ### 43(lecture) ###
                                *args and **kwargs
'''





'''
                                ### 49(lecture) ###        
                                Map Filter Lambda 
'''

        ##  MAP Function 49(lecture)  ##

# def square(mystring):
#     if len(mystring) % 2 == 0:
#         return 'EVEN'
#     else:
#         return mystring[0]
# name = ['Andy','Eve','Sally']
# print(list(map(square,name) ))

# def square(nums):
#     return nums ** 2

# number = [1,2,3,4,5]
# for i in map(square,number):
#     print(i)
# ##############################



#         # filter Function ##

# def check_even(number):
#     return number % 2 == 0

# my_nums = [1,2,3,4,5,6]
# # print(list(map(check_even,my_nums))) # or # for num in filete(check_even,my_nums):
#                                                 #print(n)


# square = lambda num: num ** 2  #gamoiyeneba martivi operaciebistvis
# print(square(3))
# print(list(map(lambda num:num**2,my_nums)))  # rodesac gvinda cvladis ricxvebi davakavshirot
# print(list(filter(lambda number:number**2,my_nums))) # lambdashi gapiltvra cvladis ricxvebis

# print(list(map(lambda Fname:Fname[0],name)))

'''
                                #### 50 #####

                               NESTED and SCOPE 
'''

# x = 25

# def printer():
#         x = 50
#         return x
# print(x)
# print(printer())

#lambda num:num**2:

#GLOBAL
# name = " THIS IS A GLOBAL STRING "

# def greet():
        
#         #ENCLOSING
#         #name = "Sammy"
#         def Hello():
#                 #LOCAL
#                 #name = "IM A LOCAL"
#                 print("hello " + name)
        
#         Hello()
# greet()

# x = 50

# def func(x):
#         global x
#         print(f"x IS {x}")
#         #LOCAL REASSIGMENT!
#         x = 200
#         print(f"I JUST LOCALLY CHANGED X TO {x}")

# func(x)

# my_list = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20]
# d = {}
# list_key = []
# list_value = []
# for key in my_list:
#         if key % 2 == 0:
#                 list_key.append(key)
#         else:
#                 list_value.append(key)
        
# for i in list_key:
#         d[i]
# for z in list_value:
#         d = z
# print(d)

