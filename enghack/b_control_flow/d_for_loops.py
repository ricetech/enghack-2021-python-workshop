# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

# For loop, runs twice
print("range(2)")
for i in range(2):
    print(i)

# For loop, runs twice from 1 to 2
print("range(1, 3)")
for i in range(1, 3):
    print(i)

# For loop, runs 6 times but counts in increments of 10
print("range(0, 51, 10)")
for i in range(0, 51, 10):
    print(i)

# For loop, runs 10 times from 10 to 1 but counts backwards
print("range(10, 0, -1)")
for i in range(10, 0, -1):
    print(i)

# Nested for loops
print("Nested For Loops")
for i in range(2):
    print(f"i: {i}")
    for j in range(2):
        print(f"j: {j}")
        for k in range(2):
            print(f"k: {k}")
