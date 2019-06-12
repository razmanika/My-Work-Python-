Mylist = input('sheitanet winadadeba :')

def Myfunc(Mylist):
	list = Mylist.split()
	list_count=list.count(list)
	u = ''
	for i in list:
		i += u
		print(i,':',list_count)
print(Myfunc(Mylist))