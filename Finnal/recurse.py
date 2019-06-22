''' რეკურსია არის როდესაც შექმნილი ფუნქცია თავის 
თავს ეძახის თვითონ ფუნქციაში.
'''
def multi_list(num):
    for i in num:
        if type(i) == int:
            Mylist.append(i)
        else:
            return Mylist
multi_list(i)