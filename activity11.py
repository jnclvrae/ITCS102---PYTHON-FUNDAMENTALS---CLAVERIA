#activity11
#temperatureconditions

temp = eval(input("Enter temperature --> "))

if temp >= 1 and temp <= 20:
    print("Temperature is cold.")
elif temp >= 21 and temp <= 30:
    print("Temperature is lukewarm.")
elif temp >= 31 and temp <= 40:
    print("Temperature is warm.")
elif temp >= 41 and temp <= 50:
    print("Temperature is hot.")
elif temp >= 51:
    print("Temperature is scorching hot.")
else:
    print("Invalid temperature.")