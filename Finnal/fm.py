'''Map -გადაცემულ ფუნქციას ასრულებს ყოველი იმ ელემენტისთვის, რომელიც გადაცემულ ლისტშია
მაგალითი #'''

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

'''Filter გადაეცემა ფუნქცია რომელიც ან თრუს აბრუნებს ან ფოლსს, და ლისტს ფილტრავს მაგის მიხედვით
მაგალითი #'''

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero) 