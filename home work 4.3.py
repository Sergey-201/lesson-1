import random

list  = random.randint(3, 10)
random_list = [random.randint(1, 10) for i in range(list)]

first = 0
third = 2
second_from_end = -2

new_list = [random_list[first], random_list[third], random_list[second_from_end]]

print(random_list)
print(new_list)


#####

import random

list  = random.randint(3, 5)
random_list = [random.randint(1, 10) for i in range(list)]

first = 0
third = 2
second_from_end = -2

new_list = [random_list[first], random_list[third], random_list[second_from_end]]

print(random_list)
print(new_list)