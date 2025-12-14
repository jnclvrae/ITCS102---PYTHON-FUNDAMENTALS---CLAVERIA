# ---------------------------------
# COMPILER FILE
# ---------------------------------


# ================= PRINT =================
def print_menu():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------\n")
    print("PRINT STATEMENTS")
    print("\t⤷ Print statements are used to display \n\t  information on the screen. You can show \n\t  text, numbers, or the result of calculations.\n")
    
    print("1. Basic print")
    print("2. Print with variables\n")
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------")

def print_1():
    print("---------------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------\n")
    print("🌸 1. Basic print: Show text or numbers directly on the screen")
    print("\nInput:")
    print('print("Hello, Python!")')
    print('print(123)')
    print("\nOutput:")
    print("Hello, Python!")
    print("123")

def print_2():
    print("-----------------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆------------------------------\n")
    print("🌸 2. Print with variables: Store values in variables and print them")
    print("\nInput:")
    print('name = "Alice"')
    print('age = 12')
    print('print(name)')
    print('print(age)')
    print("\nOutput:")
    print("Alice")
    print("12")


# ================= VARIABLES =================
def variable_menu():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------------------\n")
    print("VARIABLES")
    print("\t⤷ Variables are like boxes where you \n\t  can store information. You can give the \n\t  box a name and put numbers, text, or other values inside.\n")

    print("1. Creating a variable")
    print("2. Different data types")
    print("3. Checking data type\n")
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------------------")

def variable_1():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------\n")
    print("🌸 1. Creating a variable: Store data in a variable")
    print("\nInput:")
    print('name = "Alice"')
    print('age = 12')
    print("\nOutput:")
    print("Variables 'name' and 'age' are created and hold values")

def variable_2():
    print("-------------------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------------------\n")
    print("🌸 2. Different data types: Variables can store text, numbers, decimals")
    print("\nInput:")
    print('text = "Hello"')
    print('num = 5')
    print('decimal = 3.14')
    print("\nOutput:")
    print("text:", "Hello")
    print("num:", 5)
    print("decimal:", 3.14)

def variable_3():
    print("------------------------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------------------------------\n")
    print("🌸 3. Checking data type: You can use type() to see what kind of value a variable stores\n")
    user_input = input("Type anything to check its data type (use quotes for words) \n--> ")
    value = eval(user_input) 

    print("\nThe type of your input is", type(value))



# ================= OPERATORS =================
def operator_menu():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------\n")
    print("OPERATORS")
    print("\t⤷ Operators are symbols that perform \n\t  operations on values. They can do math, \n\t  compare values, and combine conditions.\n")

    print("1. Arithmetic")
    print("2. Comparison")
    print("3. Logical\n")
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------")

def operator_1():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------\n")
    print("🌸 1. Arithmetic operators: Perform math +, -, *, /")
    print("\nInput:")
    print('print(5 + 3)')
    print('print(5 * 2)')
    print("\nOutput:")
    print("8")
    print("10")

def operator_2():
    print("-------------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------\n")
    print("🌸 2. Comparison operators: Compare values, return True/False")
    print("\nInput:")
    print('print(5 == 3)')
    print('print(5 > 3)')
    print("\nOutput:")
    print("False")
    print("True")

def operator_3():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆---------------------------\n")
    print("🌸 3. Logical operators: Combine True/False conditions")
    print("\nInput:")
    print('print(True and False)')
    print('print(True or False)')
    print("\nOutput:")
    print("False")
    print("True")


# ================= CONDITIONALS =================
def conditional_menu():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------\n")
    print("CONDITIONALS")
    print("\t⤷ Conditionals help your program \n\t  make decisions. They let you run \n\t  different code based on whether \n\t  something is true or false.\n")

    print("1. If")
    print("2. If-else\n")
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------")

def conditional_1():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------\n")
    print("🌸 1. If statement: Run code only if condition is True")
    print("\nInput:")
    print('age = 15')
    print('if age >= 18:')
    print('    print("You can vote!")')
    print("\nOutput:")
    print("Nothing (condition is False)")

def conditional_2():
    print("---------------------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------------------\n")
    print("🌸 2. If-else statement: Run code if condition is True, else run alternative")
    print("\nInput:")
    print('age = 15')
    print('if age >= 18:')
    print('    print("You can vote!")')
    print('else:')
    print('    print("Too young")')
    print("\nOutput:")
    print("Too young")


# ================= LOOPS =================
def loop_menu():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------\n")
    print("LOOPS")
    print("\t⤷ Loops let you repeat code \n\t  multiple times. You can use loops \n\t  to go through items in a list or \n\t  repeat actions until a condition is met.\n")
    
    print("1. For loop")
    print("2. While loop\n")
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------")

def loop_1():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------------------\n")
    print("🌸 1. For loop: Repeat code a fixed number of times")
    print("\nInput:")
    print('for i in range(3):')
    print('    print("Python is fun!")')
    print("\nOutput:")
    print("Python is fun!")
    print("Python is fun!")
    print("Python is fun!")

def loop_2():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------------------\n")
    print("🌸 2. While loop: Repeat code while a condition is True")
    print("\nInput:")
    print('count = 1')
    print('while count <= 3:')
    print('    print("Hello", count)')
    print('    count += 1')
    print("\nOutput:")
    print("Hello 1")
    print("Hello 2")
    print("Hello 3")


# ================= LISTS =================
def list_menu():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆----------------------------\n")
    print("LISTS")
    print("\t⤷ Lists are like containers that \n\t  can hold multiple items. You can \n\t  store numbers, text, or other values \n\t  in a list and access them using their position.\n")
    
    print("1. Create list")
    print("2. Access list")
    print("3. Remove item from list\n")
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆----------------------------")

def list_1():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆--------------------------\n")
    print("🌸 1. Create list: Store multiple items in one variable")
    print("\nInput:")
    print('fruits = ["apple", "banana", "cherry"]')
    print('print(fruits)')
    print("\nOutput:")
    print("['apple', 'banana', 'cherry']")

def list_2():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------------------\n")
    print("🌸 2. Access list: Get an item from the list using its index")
    print("\nInput:")
    print('fruits = ["apple", "banana", "cherry"]')
    print('print(fruits[1])')
    print("\nOutput:")
    print("banana")

def list_3():
    print("---------------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------------------\n")
    print("🌸 3. Remove item from list: Delete an item using remove() or pop()")
    print("\nInput:")
    print('fruits = ["apple", "banana", "cherry"]')
    print('fruits.remove("banana")')
    print('print(fruits)')
    print("\nOutput:")
    print("['apple', 'cherry']")

# ================= FUNCTIONS =================
def function_menu():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆------------------------\n")
    print("FUNCTIONS")
    print("\t⤷ Functions are like mini-programs \n\t  within your code. They let you group \n\t  related code together and run it \n\t  whenever you need to.\n")

    print("1. Simple function")
    print("2. Function with parameter\n")
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆------------------------")

def function_1():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------------------\n")
    print("🌸 1. Simple function: A reusable block of code")
    print("\nInput:")
    print('def greet():')
    print('    print("Hello!")')
    print('greet()')
    print("\nOutput:")
    print("Hello!")

def function_2():
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------------------------\n")
    print("🌸 2. Function with parameter: Accept input to use inside the function")
    print("\nInput:")
    print('def greet(name):')
    print('    print("Hi", name)')
    print('greet("Alice")')
    print("\nOutput:")
    print("Hi Alice")


# ================= SHORT QUIZ =================
def python_quiz():
    import random
    print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-----------------------")
    print("             TIME FOR A SHORT PYTHON QUIZ!\n")

    score = 0

    # Question 1
    q1 = input("1) Which of these will print 'Hello, Python!'?\n   a. input('Hello, Python!')\n   b. print('Hello, Python!')\n   c. 'Hello, Python!'\n--> ").lower()
    if q1 == "b":
        print("Correct! ✮")
        score += 1
    else:
        print("Incorrect! The correct answer is b. print('Hello, Python!')")

    # Question 2
    q2 = input("\n2) How do you print the value stored in a variable 'name'?\n   a. print(name)\n   b. name.print()\n   c. show(name)\n--> ").lower()
    if q2 == "a":
        print("Correct! ✮")
        score += 1
    else:
        print("Incorrect! The correct answer is a. print(name)")

    # Question 3
    q3 = input("\n3) What is the output of True or False?\n   a. False\n   b. True\n   c. None\n--> ").lower()
    if q3 == "b":
        print("Correct! ✮")
        score += 1
    else:
        print("Incorrect! The correct answer is b. True")

    # Question 4
    q4 = input("\n4) How do you access the second item in a list called fruits?\n   a. fruits[1]\n   b. fruits[2]\n   c. fruits.get(2)\n--> ").lower()
    if q4 == "a":
        print("Correct! ✮")
        score += 1
    else:
        print("Incorrect! The correct answer is a. fruits[1]")

    # Question 5
    q5 = input("\n5) How do you define a function named greet that prints 'Hello'?\n   a. def greet(): print('Hello')\n   b. function greet() print('Hello')\n   c. greet() = def print('Hello')\n--> ").lower()
    if q5 == "a":
        print("Correct! ✮")
        score += 1
    else:
        print("Incorrect! The correct answer is a. def greet(): print('Hello')")

    print(f"\nYour total score: {score}/5")
    if score == 5:
        print("\nExcellent! You really know Python basics! ❤︎")
    elif score >= 3:
        print("\nGood job! Just a little more practice. ❤︎")
    else:
        print("\nKeep learning! Practice makes perfect. ❤︎")