def add_one(some_list):
    number_str = ""
    for digit in some_list:
        number_str += str(digit)

    number = int(number_str)
    number += 1

    number_str = str(number)
    result_list = []

    for char in number_str:
        result_list.append(int(char))

    return result_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")