# Session 2: Introduction to Python Programming II
- [Session 2: Introduction to Python Programming II](#session-2-introduction-to-python-programming-ii)
  - [Section 1 Comparisons and Conditionals](#section-1-comparisons-and-conditionals)
    - [Exercise 1 Task 1 : Comparison Operators](#exercise-1-task-1--comparison-operators)
    - [Exercise 1 Task 2 : Logical Operators](#exercise-1-task-2--logical-operators)
    - [Exercise 1 Task 3 : if Conditions](#exercise-1-task-3--if-conditions)
    - [Exercise 1 Task 4 : if-else Conditions](#exercise-1-task-4--if-else-conditions)
    - [Exercise 1 Task 5 : if-elif-else Conditions](#exercise-1-task-5--if-elif-else-conditions)
    - [Exercise 1 Task 6 : Summary Tasks](#exercise-1-task-6--summary-tasks)
  - [Section 2 Python Lists](#section-2-python-lists)
    - [Exercise 2 Task 1 : Creating a list](#exercise-2-task-1--creating-a-list)
    - [Exercise 2 Task 2 : Accessing List Elements](#exercise-2-task-2--accessing-list-elements)
    - [Exercise 2 Task 3 : Modifying a list](#exercise-2-task-3--modifying-a-list)
    - [Exercise 2 Task 4 : Summary Task](#exercise-2-task-4--summary-task)
  - [Section 3 Python Loops](#section-3-python-loops)
    - [Exercise 3 Task 1 : While Loop](#exercise-3-task-1--while-loop)
    - [Exercise 3 Task 2 : For Loop](#exercise-3-task-2--for-loop)
    - [Exercise 3 Task 3 : Loop Keywords: Range, Break and Continue](#exercise-3-task-3--loop-keywords-range-break-and-continue)
    - [Exercise 3 Task 4 : Summary Tasks](#exercise-3-task-4--summary-tasks)
  - [Section 4 Obtaining User Input](#section-4-obtaining-user-input)
    - [Exercise 4 Task 1 : User Input and Conditional Statements](#exercise-4-task-1--user-input-and-conditional-statements)
    - [Exercise 4 Task 2 : Temperature Converter](#exercise-4-task-2--temperature-converter)

## Section 1 Comparisons and Conditionals

### Exercise 1 Task 1 : Comparison Operators

```python
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
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
a = 18
b = 12
a == b: False
a != b: True
a > b: True
a < b: False
a >= b: True
a <= b: False
```

### Exercise 1 Task 2 : Logical Operators

```python
# Exercise 2: Logical Operators

x = 25
print(x > 10 and x < 30)
print(x > 30 or x < 10)
print(not (x == 25))
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
True
False
False
```

### Exercise 1 Task 3 : if Conditions

```python
# Exercise 3: if Conditions

age = 21
age_group = "minor"

if age >= 18:
    age_group = "adult"

print(f"age group: {age_group}")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
age group: adult
```

```python
# Exercise 3: if Conditions

age = 16
age_group = "minor"

if age >= 18:
    age_group = "adult"

print(f"age group: {age_group}")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
age group: minor
```

### Exercise 1 Task 4 : if-else Conditions

```python
# Exercise 4: if-else Conditions

wind_speed = 14
if wind_speed < 10:
    print("Weather status: calm")
else:
    print("Weather status: windy")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Weather status: windy
```

```python
# Exercise 4: if-else Conditions

wind_speed = 7
if wind_speed < 10:
    print("Weather status: calm")
else:
    print("Weather status: windy")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Weather status: calm
```

### Exercise 1 Task 5 : if-elif-else Conditions

```python
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
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Result: merit
```

### Exercise 1 Task 6 : Summary Tasks

```python
# Exercise 6: Summary Tasks
# compare two temperatures

temperature_1 = 22
temperature_2 = 22
if temperature_1 == temperature_2:
    print("The temperatures are equal.")
else:
    print("The temperatures are not equal.")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
The temperatures are equal.
```

## Section 2 Python Lists

### Exercise 2 Task 1 : Creating a list

```python
# Exercise 1: Creating a list

city_list = ["Paisley", "Glasgow", "Inverness"]
print("City List:", city_list)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
City List: ['Paisley', 'Glasgow', 'Inverness']
```

### Exercise 2 Task 2 : Accessing List Elements

```python
# Exercise 2: Accessing List Elements

city_list = ["Paisley", "Glasgow", "Inverness"]
print("City List:", city_list)
print("Third city:", city_list[2])
print("Last two cities:", city_list[1:3])
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
City List: ['Paisley', 'Glasgow', 'Inverness']
Third city: Inverness
Last two cities: ['Glasgow', 'Inverness']
```

### Exercise 2 Task 3 : Modifying a list

```python
# Exercise 3: Modifying a List

city_list = ["Paisley", "Glasgow", "Inverness"]
print("City List:", city_list)

city_list.append("Aberdeen")
print("Updated City List:", city_list)

city_list[1] = "Dundee"
print("Modified City List:", city_list)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
City List: ['Paisley', 'Glasgow', 'Inverness']
Updated City List: ['Paisley', 'Glasgow', 'Inverness', 'Aberdeen']
Modified City List: ['Paisley', 'Dundee', 'Inverness', 'Aberdeen']
```

### Exercise 2 Task 4 : Summary Task

```python
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
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Colours List: ['orange', 'teal', 'navy']
Updated Colours List: ['gold', 'teal', 'navy']
Number of colours: 3
Red is not in the list.
Selected Colours: ['teal', 'navy']
```

## Section 3 Python Loops

### Exercise 3 Task 1 : While Loop

```python
# Exercise 1: While loop

i = 1
while i <= 5:
    print(i)
    i += 1
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
1
2
3
4
5
```

### Exercise 3 Task 2 : For Loop

```python
# Exercise 2: For loop

city_list = ["Paisley", "Dundee", "Inverness"]
for city in city_list:
    print(city)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Paisley
Dundee
Inverness
```

### Exercise 3 Task 3 : Loop Keywords: Range, Break and Continue

```python
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
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
For range and break:
1
2
3
4
5
For range and continue:
1
2
3
4
5
7
8
9
10
```

### Exercise 3 Task 4 : Summary Tasks

```python
# Task - Even Numbers

numbers = list(range(1, 13))
print("Numbers List:", numbers)
print("Even Numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Numbers List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Even Numbers:
2
4
6
8
10
12
```

```python
# Task - Sum of Squares

sum_of_squares = 0
for num in range(1, 7):
    sum_of_squares += num ** 2
print("The sum of squares from 1 to 6 is:", sum_of_squares)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
The sum of squares from 1 to 6 is: 91
```

```python
# Task - Countdown

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
5
4
3
2
1
Liftoff!
```

## Section 4 Obtaining User Input

### Exercise 4 Task 1 : User Input and Conditional Statements

```python
# Task 1: User Input and Conditional Statements

age = int(input("Please enter your age: "))
if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Please enter your age: 30
You are an adult.
```

### Exercise 4 Task 2 : Temperature Converter

```python
# Task 2: Temperature Converter

celsius_input = input("Enter a temperature in Celsius: ")
degree_f = (float(celsius_input) * 9/5) + 32
degree_k = float(celsius_input) + 273.15
output = f"Celsius: {celsius_input}°C\nFahrenheit: {degree_f}°F\nKelvin: {degree_k}K"
print(output)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_2/lab_week_2.py"
Enter a temperature in Celsius: 18
Celsius: 18°C
Fahrenheit: 64.4°F
Kelvin: 291.15K
```
