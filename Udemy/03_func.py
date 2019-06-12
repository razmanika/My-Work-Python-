def makes_twenty(n1,n2):
	if n1 == 20 or n2 == 20:
		return True
	elif n1 + n2 == 20:
		return True
	else:
		return False
n1 = 3
n2 = 4
print(makes_twenty(n1,n2))