# Exercise 1 Task: Variables and Types
is_active = False      # bool
attempts = 7           # int
temperature = 19.75    # float
welcome_text = "Hello ISD"  # str

print(type(is_active))
print(type(attempts))
print(type(temperature))
print(type(welcome_text))

# Exercise 1 Task: Casting Variables
count = 12
score = 88.9
is_passed = False
print("count =", count, "score =", score, "is_passed =", is_passed)

count_to_float = float(count)
print("count_to_float =", count_to_float)

score_to_int = int(score)
print("score_to_int =", score_to_int)

passed_to_int = int(is_passed)
print("passed_to_int =", passed_to_int)


# Exercise 2 Arithmetic operators

# Addition
result_addition = 14 + 6
print("Addition:", result_addition)

# Subtraction
result_subtraction = 30 - 11
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = 7 * 5
print("Multiplication:", result_multiplication)

# Division
result_division = 40 / 8
print("Division:", result_division)

# Floor Division
result_floor_division = 29 // 6
print("Floor Division:", result_floor_division)

# Modulus
result_modulus = 29 % 6
print("Modulus:", result_modulus)

# Exponentiation
result_exponentiation = 3 ** 4
print("Exponentiation:", result_exponentiation)


# Task 2: Calculating the Average
mark1 = 64
mark2 = 82
average_mark = (mark1 + mark2) / 2
print("mark1:", mark1)
print("mark2:", mark2)
print("Average:", average_mark)


# Task 3: Calculate the Area of a Rectangle
length = 9
width = 4
area = length * width
print("Rectangle length:", length)
print("Rectangle width:", width)
print("Rectangle area:", area)


# Task 1: Modify Strings
my_string = "Python labs are practical."
print("Original:", my_string)

my_uppercase_string = my_string.upper()
print("Upper:", my_uppercase_string)

my_lowercase_string = my_string.lower()
print("Lower:", my_lowercase_string)

my_new_string = my_string.replace("practical", "important")
print("Replaced:", my_new_string)

my_string_length = len(my_string)
print("Length:", my_string_length)


# Task 2: f-Strings
my_name = "Uttam Pradhan"
my_number_of_classes = 3
my_campus = "Paisley Campus"

my_text = f"I am {my_name}. I study {my_number_of_classes} classes at {my_campus}."
print(my_text)



