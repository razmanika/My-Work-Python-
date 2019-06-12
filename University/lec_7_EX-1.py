man_input = input("sheiyvanet teqsti : ")
write_file = open("User_input" + ".txt","w") # მომხმარებლის ფაილი
write_file.write(man_input)

 # ხმოვნების ფაილი
 # თანხმოვნების ფაილი
def words():      # ამოწმებს ხმოვნებ და დანხმოვნებს + ამატებს ფაილში ცალ-ცალკე
    vow = ['a','e','i','o','u']
    try:
        vowels = [vowel for vowel in write_file if vowel in vow ]
        write_vowel = open("vowel.txt", "w")
        write_vowel.write(vowels)
        write_vowel.close()
    except:
        constant = [constant for constant in write_file if constant != vow]
        write_const = open("costants.txt", "w")
        write_const.write(constant)
        write_const.close()
    return

def numbers():
    try:
        odd_number = [len(write_file) for num in write_file if len(write_file)%2 == 0]
        write_odd = open("odd.txt", "w")
        write_odd.write(odd_number[0])
        write_odd.close()
    
    except:
        even_number = [len(write_file) for num in write_file if len(write_file)%2 != 0]
        write_even = open("even.txt", "w")
        write_even.write(even_number)
        write_even.close()
    return

def other():
    blocked = ",<.>/?;:'[]{}`~!@#$%^&*()_+|\-"
    try:
        other_keyb = [key for key in write_file if key in blocked]
        other_symb = open("other.txt","w")
        other_symb.write(other_symb)
        other_symb.close()
    except:
        pass
    return

words()
numbers()


write_file.close()


