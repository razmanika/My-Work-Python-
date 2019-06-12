'''more def then 1 '''

# def p_decorate(func):
#     def in_func(name):
#         return "<p> {} </p>".format(func(name))
#     return in_func

# def strong_decorate(func):
#     def in_func(name):
#         return "<STRONG> {} </STRONG>".format(func(name))
#     return in_func

# def div_decorate(func):
#     def in_func(name):
#         return "<DIV> {} </DIV>".format(func(name))
#     return in_func
    
# @div_decorate
# @strong_decorate
# @p_decorate

# def get_text(name):
#     return "ნამდვილი {} ხარ".format(name)

# print(get_text("ვაჟკაცი"))



def p_decorate(func):
    def func_wrapper(*args,**kwargs):
        return "<P> {0} </P>".format(func(*args,**kwargs))
    return func_wrapper

class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    
    @p_decorate
    def get_full_name(self):
        return self.name + " " +self.surname + " " +self.age

man = Person('ნიკუშა','რაზმაძე',"18")
print(man.get_full_name())


'''TAG example '''
# def tags(tag_name):
#     def tags_decorate(func):
#         def func_wrapper(name):
#             return "<{0}> {1} </{0}>".format(tag_name,func(name))
#         return func_wrapper
#     return tags_decorate

# @tags("P")
# def get_name(name):
#     return "Hello " + name

# print(get_name("Razma"))





''' Easy way '''
# def check(func):
#     def inside(a,b):
#         if b == 0:
#             print("can't divide by 0")
            
#         func(a,b)
#     return inside

# @check
# def div(a,b):
#     return a/b

# print(div(10,0))
