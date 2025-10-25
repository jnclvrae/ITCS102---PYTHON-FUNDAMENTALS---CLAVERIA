name = input("Hi! What is your name? --> ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nODD number compiler, type '0' to terminate the loop.\n")

sum = 0
odd = ""
tuloy = True

while tuloy == True:
  num = eval(input("Please input a number --> "))
  
  if num % 2 == 1:
    print("ODD number detected.")
    odd += str(num) + ","
    sum += num
    continue
  elif num == 0:
    print("Loop Terminated.")
    break
  else:
    if num % 2 == 0:
      print("EVEN number, skipping .......")
    else:
      print("Invalid number.")
      continue
    
print(f"\nHi {name}, the sum of all ODD numbers is {sum}.")
print(f"All of the ODD numbers you input is {odd}.")
