# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

# Here are the basic primitive types in Python:
some_str = "hello world!"
some_boolean = False
some_float = 1.23456
some_other_float = 4 / 2  # Floats can also hold whole numbers!
some_int = 42
sneaky_string = "42"  # This is a string, not an integer!

# Not sure what type a variable is?
print(type(some_boolean))
print(type(some_float))
print(type(some_other_float))
print(type(some_int))
print(type(sneaky_string))

# You can also tell the difference between strings and int/floats - strings will have quotation marks when printed
print(some_int)  # No quotes because the type is int
print(sneaky_string)  # Has quotes because type is str

# Convert between types using type casting
print(int("2"))
print(str(17))

# You can use type casting to get numbers from the user
# Remember - user input is type "str" by default
user_input = int(input("Enter a whole number: "))  # Add a space or new line (\n) after the colon to make it look nice
print(user_input)
