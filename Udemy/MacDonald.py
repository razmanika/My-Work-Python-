def old_macdonald(name):
	first_letter = name.capitalize()
	thered_letter = first_letter[:3] + first_letter[3].upper() + first_letter[4:]

	print(thered_letter)
old_macdonald('macdonalds')