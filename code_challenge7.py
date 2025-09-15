#code_challenge7.py
#oddnumbersummation

result = 0

for x in range (1, 11):
    number = eval(input("Enter a number --> "))
    if number % 2 == 1:
        result += number
    else:
        result == 0
        
print("The sum of all the ODD numbers is",result)