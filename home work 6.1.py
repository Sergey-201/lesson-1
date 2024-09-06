import string
string_input = input("Введіть дві літери через дефіс:")
first_letter, second_letter = string_input.split("-")

letters = string.ascii_letters
start = letters.index(first_letter)
end = letters.index(second_letter) + 1

print(letters[start:end])

