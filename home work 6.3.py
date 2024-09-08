number = int(input("Введіть число: "))

while number > 9:
    digits = str(number)
    product = 1

    for digit in digits:
        product *= int(digit)
    number = product

print(number)