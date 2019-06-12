def uxnauri(number):
	return (abs(100 - number) <= 10) or (abs(200 - number) <= 10)
print(uxnauri(90))