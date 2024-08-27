import random

list  = random.randint(8, 10)  # Кількість елементів у списку від 3 до 10
random_list = [random.randint(1, 10) for _ in range(list)]

first = 0
third = 2
second_from_end = -2

new_list = [random_list[first], random_list[third], random_list[second_from_end]]

print("Вихідний список:", random_list)
print("Новий список:", new_list)

#####

import random

list  = random.randint(3, 5)  # Кількість елементів у списку від 3 до 10
random_list = [random.randint(1, 10) for _ in range(list)]

first = 0
third = 2
second_from_end = -2

new_list = [random_list[first], random_list[third], random_list[second_from_end]]

print("Вихідний список:", random_list)
print("Новий список:", new_list)