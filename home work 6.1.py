import string
string_input = "a-c"
first_letter, second_letter = string_input.split("-")

letters = string.ascii_letters
start = letters.index(first_letter)
end = letters.index(second_letter) + 1

print(letters[start:end])

######

import string
string_input = "s-H"
first_letter, second_letter = string_input.split("-")

letters = string.ascii_letters
start = letters.index(first_letter)
end = letters.index(second_letter) + 1

print(letters[start:end])