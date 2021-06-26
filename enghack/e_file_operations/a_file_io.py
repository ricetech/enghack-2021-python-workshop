# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

from enghack.d_code_organization.a_functions import average_of_list

numbers_list = []

# We use with open so we don't have to remember to close the file
# Without with open, we would have to close the file to avoid a memory leak
with open("numbers.txt") as number_file:
    # Dot notation calls a function using the value to the left of the dot
    # readlines() returns all of the lines of number_file
    for line in number_file.readlines():
        # strip() removes all whitespace from a string - we need it because each line contains a new line character
        # \n by default
        line_float = float(line.strip())
        numbers_list.append(line_float)

print(numbers_list)
