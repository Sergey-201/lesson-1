list = [0, 1, 7, 2, 4, 8]

over = 0
for i in range(0, len(list), 2):
    over += list[i]

last_num = list[-1]
result = over * last_num
print(result)

#####

list = [1, 3, 5]

over = 0
for i in range(0, len(list), 2):
    over += list[i]

last_num = list[-1]
result = over * last_num
print(result)

#####

list = [6]

over = 0
for i in range(0, len(list), 2):
    over += list[i]

last_num = list[-1]
result = over * last_num
print(result)

#####

list = []

over = 0

for i in range(0, len(list), 2):
    over += list[i]
if len(list) > 0:
    last_num = list[-1]
    result = over * last_num
else:
    result = 0
print(result)
