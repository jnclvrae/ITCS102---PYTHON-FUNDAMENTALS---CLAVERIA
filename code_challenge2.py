deposit = eval(input("Enter the amount to deposit --> "))

print("\nHere is the breakdown, using PH denomination: ")

bill1000 = deposit // 1000
print(bill1000, "\t- 1000")
deposit = deposit % 1000

bill500 = deposit // 500
print(bill500, "\t- 500")
deposit = deposit % 500

bill200 = deposit // 200
print(bill200, "\t- 200")
deposit = deposit % 200

bill100 = deposit // 100
print(bill100, "\t- 100")
deposit = deposit % 100

bill50 = deposit // 50
print(bill50, "\t- 50")
deposit = deposit % 50

bill20 = deposit // 20
print(bill20, "\t- 20")
deposit = deposit % 20

coin10 = deposit // 10
print(coin10, "\t- 10")
deposit = deposit % 10

coin5 = deposit // 5
print(coin5, "\t- 5")
deposit = deposit % 5

coin1 = deposit // 1
print(coin1, "\t- 1")
deposit = deposit % 1