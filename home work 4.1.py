list = [0, 1, 0, 12, 3]
list2 = []
for num in list:
    if num != 0:
        list2.append(num)
for i in range(len(list) - len(list2)):
    list2.append(0)
print(list2)

#####

list = [0]
list2 = []
for num in list:
    if num != 0:
        list2.append(num)
for i in range(len(list) - len(list2)):
    list2.append(0)
print(list2)

#####

list = [1, 0, 13, 0, 0, 0, 5]
list2 = []
for num in list:
    if num != 0:
        list2.append(num)
for i in range(len(list) - len(list2)):
    list2.append(0)
print(list2)

####

list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
list2 = []
for num in list:
    if num != 0:
        list2.append(num)
for i in range(len(list) - len(list2)):
    list2.append(0)
print(list2)
