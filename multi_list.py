def multi_list(suka):
    for i in suka:
        if type(i) == int:
            Mylist.append(i)
        else:
            multi_list(i)
    return Mylist

Mylist =[]


number_of_list = [5,[9,[[[[[2]]]]]],[[[2],[12,[2]],[10]]]]
print(multi_list(number_of_list))

