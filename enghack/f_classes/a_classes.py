# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

from enghack.d_code_organization.a_functions import average_of_list


class Student:
    def __init__(self, name, student_number, birth_year, graduated):
        self.name = name
        self.student_number = student_number
        self.birth_year = birth_year
        self.age = 2021 - birth_year
        self.graduated = graduated
        self.course_marks = []

    def calculate_average(self):
        return average_of_list(self.course_marks)


def main():
    bob = Student("bob", 1, 2002, True)
    jane = Student("jane", 2, 2006, False)
    bob.course_marks.append(100)
    bob.course_marks.append(96)
    bob.course_marks.append(90)
    jane.course_marks.append(100)
    jane.course_marks.append(99)
    jane.course_marks.append(99)

    bob_average = bob.calculate_average()
    jane_average = jane.calculate_average()

    if bob_average > jane_average:
        print(f"Bob's average is {(bob_average - jane_average)}% higher than Jane's average")
    else:
        print(f"Jane's average is {(jane_average - bob_average)}% higher than Bob's average")


if __name__ == "__main__":
    main()
