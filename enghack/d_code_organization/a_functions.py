# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

def average_of_list(some_list):
    return sum(some_list) / len(some_list)


def main():
    average_of_list([1, 23, 44])
    average_of_list([1, 1, 1, 1, 2, 2, 3, 3, 44])


if __name__ == "__main__":
    main()
