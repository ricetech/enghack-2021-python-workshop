# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

some_str = "Hello"
some_num = 2
some_list = [2, 3, 63]

# We use the boolean expressions from before in If statements
if some_num in some_list:
    print("some_num is in some_list")  # You would replace this with your own logic
# If statements can act alone

user_input = int(input("Enter a whole number: "))
if user_input < 2:
    print("Number is less than 2")
else:
    print("Number is greater than 2")

fav_color = input("What's my favourite colour?\n")  # \n means new line
if fav_color.lower() == "blue":
    print("Blue is close, but it's not my favourite colour!")
elif fav_color.upper() == "green":
    print("Correct!")
else:
    print("That's not my favourite colour!")
