#code_challenge6.py
#factorialprogram

number = eval(input("Enter a number --> "))
result = 1

for x in range(number, 0, -1):
    result*= x
    
print("The factorial of",number,"is",result)