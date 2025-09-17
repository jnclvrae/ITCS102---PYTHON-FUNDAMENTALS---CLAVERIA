#codechallenge8
#multiplicationtablemaker

print("MULTIPLICATION TABLE MAKER")

number = eval(input("Enter a number: "))

print(f"\nMultiplication table for {number}:")

for x in range(1,11):
    result = number * x
    print(number,"x",x,"=",result)