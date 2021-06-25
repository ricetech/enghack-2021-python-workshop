# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

def input_checker(min_range, max_range):
    """
    Written by Eric C (RT)
    This function will continually ask the user for an input until the following conditions are met:
    1. Their input can be converted into a float.
    2. Their float value of their input is in between the min_range and max_range parameters.
    Provided these conditions are met, the user's input will get returned.
    This program can be modified to work with integers by editing line 19.
    :param min_range: A number defining the minimum value of the user's input.
    :param max_range: A number defining the maximum value of the user's input.
    :return: A number between min_range and max_range inputted by the user.
    :rtype: float
    """
    while True:
        try:
            # This also works with int(input())
            user_input = float(input("Enter a number: "))  # Throws an error if input is not a number
            if min_range <= user_input <= max_range:
                # Could put return here, but I prefer to have it at the bottom
                # for code readability
                break
            else:
                print(">> Error: Input out of range. Valid range is " + str(min_range) + " to " + str(max_range) + ". ")
                input("Press Enter to try again.")
        except ValueError:
            input(">> Error: Input was not a number. Press Enter to try again.")
    return user_input


if __name__ == "__main__":
    print(input_checker(1, 10))
