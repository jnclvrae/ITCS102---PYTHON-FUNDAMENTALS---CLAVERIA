# ---------------------------------
# MAIN FILE
# ---------------------------------

import os
from compiler import *

# ask for user's name
name = input("What's your name? --> ").title()

# ask if they want to enter the program
enter = input(f"\nHi {name}! Do you want to enter the program? (yes/no)\n--> ").lower()

# main program loop
while True:

    if enter == "yes":
        os.system("cls")

        print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------")
        print(f"          Welcome to the program, {name}! 🌸") 
        print("-----------------------------------------------------")
        print(" ───────────────────── MAIN MENU ────────────────────\n")
        print("                 a. Print Statements                ")
        print("                 b. Variables                       ")
        print("                 c. Operators                       ")
        print("                 d. Conditionals                    ")
        print("                 e. Loops                           ")
        print("                 f. Lists                           ")
        print("                 g. Functions                       ")
        print("                 h. Short Quiz                      ")
        print("                 x. Exit Program                    \n")
        print("--------------------˗⋆｡‧˚ʚ ♡ ɞ˚‧｡⋆-------------------")

        choice = input("\nChoose a letter --> ").lower()

        # EXIT
        if choice == "x":
            print("Thank you for using the program! ❤︎")
            break
        # ------------------------------
        # Print Statements
        # ------------------------------
        elif choice == "a":
            while True:
                os.system('cls')
                print_menu()
                sub = input("\nChoose one subtopic or 'm' for main menu --> ")

                if sub == "m":
                    break
                elif sub == "1":
                    os.system('cls')
                    print_1()
                elif sub == "2":
                    os.system('cls')
                    print_2()
                else:
                    print("\nInvalid choice. Please try again.")

                input("\nPress Enter to continue...")

        # ------------------------------
        # Variables
        # ------------------------------
        elif choice == "b":
            while True:
                os.system('cls')
                variable_menu()
                sub = input("\nChoose a subtopic or 'm' for main menu --> ")

                if sub == "m":
                    break
                elif sub == "1":
                    os.system('cls')
                    variable_1()
                elif sub == "2":
                    os.system('cls')
                    variable_2()
                elif sub == "3":
                    os.system('cls')
                    variable_3()
                else:
                    print("\nInvalid choice. Please try again.")

                input("\nPress Enter to continue...")

        # ------------------------------
        # Operators
        # ------------------------------
        elif choice == "c":
            while True:
                os.system('cls')
                operator_menu()
                sub = input("\nChoose a subtopic or 'm' for main menu --> ")

                if sub == "m":
                    break
                elif sub == "1":
                    os.system('cls')
                    operator_1()
                elif sub == "2":
                    os.system('cls')
                    operator_2()
                elif sub == "3":
                    os.system('cls')
                    operator_3()
                else:
                    print("\nInvalid choice. Please try again.")

                input("\nPress Enter to continue...")

        # ------------------------------
        # Conditionals
        # ------------------------------
        elif choice == "d":
            while True:
                os.system('cls')
                conditional_menu()
                sub = input("\nChoose a subtopic or 'm' for main menu --> ")

                if sub == "m":
                    break
                elif sub == "1":
                    os.system('cls')
                    conditional_1()
                elif sub == "2":
                    os.system('cls')
                    conditional_2()
                else:
                    print("\nInvalid choice. Please try again.")

                input("\nPress Enter to continue...")

        # ------------------------------
        # Loops
        # ------------------------------
        elif choice == "e":
            while True:
                os.system('cls')
                loop_menu()
                sub = input("\nChoose a subtopic or 'm' for main menu --> ")

                if sub == "m":
                    break
                elif sub == "1":
                    os.system('cls')
                    loop_1()
                elif sub == "2":
                    os.system('cls')
                    loop_2()
                else:
                    print("\nInvalid choice. Please try again.")

                input("\nPress Enter to continue...")

        # ------------------------------
        # Lists
        # ------------------------------
        elif choice == "f":
            while True:
                os.system('cls')
                list_menu()
                sub = input("\nChoose a subtopic or 'm' for main menu --> ")

                if sub == "m":
                    break
                elif sub == "1":
                    os.system('cls')
                    list_1()
                elif sub == "2":
                    os.system('cls')
                    list_2()
                elif sub == "3":
                    os.system('cls')
                    list_3()
                else:
                    print("\nInvalid choice. Please try again.")

                input("\nPress Enter to continue...")

        # ------------------------------
        # Functions
        # ------------------------------
        elif choice == "g":
            while True:
                os.system('cls')
                function_menu()
                sub = input("\nChoose a subtopic or 'm' for main menu --> ")

                if sub == "m":
                    break
                elif sub == "1":
                    os.system('cls')
                    function_1()
                elif sub == "2":
                    os.system('cls')
                    function_2()
                else:
                    print("\nInvalid choice. Please try again.")

                input("\nPress Enter to continue...")
        # ------------------------------
        # Short Quiz
        # ------------------------------
        elif choice == "h":
            os.system('cls')
            python_quiz()
            
            input("\nPress Enter to return to the main menu...")


        # ------------------------------
        # Invalid main menu input
        # ------------------------------
        else:
            print("\nInvalid choice. Please select a valid topic.")
            input("\nPress Enter to continue...")

    elif enter == "no":
        print("\nAlright! Maybe next time! ❤︎")
        break