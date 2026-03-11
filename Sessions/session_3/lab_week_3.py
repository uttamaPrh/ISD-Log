# Task 1: Greeting message

participant_list = ["Uttam", "Aarav", "Sita"]


def greet(person_name):
    print(f"Hello {person_name}")


for person in participant_list:
    greet(person)


# Task 2: Tax calculation

def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax


calculated_tax = calculate_tax(72000, 0.22)
print("Calculated Tax:", calculated_tax, "pounds")


# Task 3: Compound interest calculator

def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None

    for year in range(1, duration + 1):
        total_for_year = principal * (1 + interest_rate) ** year
        print(f"Year {year}: {total_for_year:.2f} pounds")

    final_amount = principal * (1 + interest_rate) ** duration
    return int(final_amount)


result = compound_interest(1500, 4, 0.06)
print("Final amount:", result)


# Exercise 2 Task 2: Variable Scope

counter = 0


def increment_local():
    counter = 5
    print("Inside function, counter =", counter)


increment_local()
print("Outside function, counter =", counter)


# Exercise 1 Task 1: Assertions

assert len("ISD") == 3, "Length check should pass."
assert 10 < 5, "This assertion is intentionally false."


# Exercise 1 Task 2: Identifying and Fixing Common Errors

# Syntax error example (fixed)
print("Hello, Python!")

# Name error example (fixed)
message = "Ready to run"
print(message)

# Value/type conversion example (fixed)
number_text = "12"
number_value = 8
result_sum = int(number_text) + number_value
print("The sum is:", result_sum)

# Index error example (kept as comment)
sample_list = [1, 2, 3]
# print(sample_list[5])


def fixed_indent_function():
    print("Indentation is correct.")