# Exercise 1: Comparison Operators

a = 18
b = 12
print("a =", a)
print("b =", b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Exercise 2: Logical Operators

x = 25
print(x > 10 and x < 30)
print(x > 30 or x < 10)
print(not (x == 25))


# Exercise 3: if Conditions

age = 21
age_group = "minor"

if age >= 18:
    age_group = "adult"

print(f"age group: {age_group}")

age = 16
age_group = "minor"

if age >= 18:
    age_group = "adult"

print(f"age group: {age_group}")

# Exercise 4: if-else Conditions

wind_speed = 14
if wind_speed < 10:
    print("Weather status: calm")
else:
    print("Weather status: windy")

wind_speed = 7
if wind_speed < 10:
    print("Weather status: calm")
else:
    print("Weather status: windy")

# Exercise 5: if-elif-else Conditions

grade = 67
if grade < 40:
    print("Result: fail")
elif grade < 60:
    print("Result: pass")
elif grade < 75:
    print("Result: merit")
else:
    print("Result: distinction")

# Exercise 6: Summary Tasks
# compare two temperatures

temperature_1 = 22
temperature_2 = 22
if temperature_1 == temperature_2:
    print("The temperatures are equal.")
else:
    print("The temperatures are not equal.")

# Exercise 1: Creating a list

city_list = ["Paisley", "Glasgow", "Inverness"]
print("City List:", city_list)

# Exercise 2: Accessing List Elements

print("Third city:", city_list[2])
print("Last two cities:", city_list[1:3])

# Exercise 3: Modifying a List

city_list.append("Aberdeen")
print("Updated City List:", city_list)

city_list[1] = "Dundee"
print("Modified City List:", city_list)


# Exercise 4: Summary Tasks

# Task Create, Access and Modify Lists

colours = ["orange", "teal", "navy"]
print("Colours List:", colours)

colours[0] = "gold"
print("Updated Colours List:", colours)

len_colours = len(colours)
print("Number of colours:", len_colours)

if "red" in colours:
    print("Red is in the list.")
else:
    print("Red is not in the list.")

selected_colour = colours[1:3]
print("Selected Colours:", selected_colour)

# Exercise 1: While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Exercise 2: For loop
city_list = ["Paisley", "Dundee", "Inverness"]
for city in city_list:
    print(city)

# Exercise 3: Loop Keywords: Range, Break and Continue

print("For range and break:")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("For range and continue:")
for j in range(1, 11):
    if j == 6:
        continue
    print(j)

# Task - Even Numbers
numbers = list(range(1, 13))
print("Numbers List:", numbers)
print("Even Numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)

# Task - Sum of Squares
sum_of_squares = 0
for num in range(1, 7):
    sum_of_squares += num ** 2
print("The sum of squares from 1 to 6 is:", sum_of_squares)

# Task - Countdown
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")


# Task 1: User Input and Conditional Statements
age = int(input("Please enter your age: "))
if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# Task 2: Temperature Converter
celsius_input = input("Enter a temperature in Celsius: ")
degree_f = (float(celsius_input) * 9/5) + 32
degree_k = float(celsius_input) + 273.15
output = f"Celsius: {celsius_input}°C\nFahrenheit: {degree_f}°F\nKelvin: {degree_k}K"
print(output)