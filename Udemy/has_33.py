def has_33(number):

	for i in range(0,len(number)-1):
		if number[i] == 3 and number[i+1] == 3:
			return True

	return False

print(has_33([3,1,3]))
print(has_33([3,1,3,3]))