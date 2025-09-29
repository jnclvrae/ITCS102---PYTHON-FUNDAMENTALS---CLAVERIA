name = input("Input your name --> ")
isStudent = input("Are you a student? (Yes/No) --> ").lower()
fare = eval(input("Bayad --> ")) 

if isStudent == "yes":
  discount = fare * .2
  new_fare = fare - discount
  print("Hi,",name,"! Good news, you are eligible for the student discount, your new fare is",new_fare,".")
else:
  print("Hi,",name,"! Since you are not eligible for the student discount, your fare is still",fare,".")