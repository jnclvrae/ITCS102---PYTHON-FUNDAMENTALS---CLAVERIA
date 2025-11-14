print("Adding data to dictionary")
print(" ============================================= ")

tuloy = True

empty_dictionary = {}

def print_anime():
    for anime in empty_dictionary.values():
        print(f"ANIME -- {anime}")
        continue

def pang_search(key):
    print("Searching ...")
    print(f"Results show {empty_dictionary[key]} on our database")

while tuloy == True:
    keys = input("Input keys for this Anime ---> ")
    value = input("Enter Anime Title ---> ")
    
    empty_dictionary[keys] = value

    choice = input("Would you like to continue adding anime?\nY - yes\nN - no\nP - print\nS - search\n--> ").lower()

    if choice == 'y':
        print("Continuing .... ")
        continue
    elif choice == 'n':
        print("Program stops.")
        break
    elif choice == 'p':
        print_anime()
        continue
    elif choice == 's':
        code = input("Please input the code of the anime --> ")
        pang_search(code)
        continue
    else:
        print("INVALID CHOICE.")
        continue
