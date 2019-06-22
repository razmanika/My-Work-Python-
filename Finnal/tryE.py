'''try except თითქმის if else_ს წააგავს უბრალოდ try და except ვამოწმებთ
 რაიმე მოქმედებას მაგალითად #'''
try:
    with open('btu.txt', 'r') as f:
        print("წარმატებით მოიძებნა")

except FileNotFoundError:
    print("ასეთი ფაილი არ არსებობს")