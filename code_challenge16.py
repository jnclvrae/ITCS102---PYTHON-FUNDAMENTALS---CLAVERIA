import os

os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("---------------------------------------\n")

student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \nA - Add Information\nB - Search a Record\nC - Delete a Record\nD - Modify a Record\nE - Exit")

    choice = input("Your choice        --> ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("-------------------------------")
        search_code = input("Key search for this student --> ")

        first_name = input("Input student's first name --> ").upper()
        last_name = input("Input student's last name --> ").upper()
        course = input("Input student's course --> ").upper()
        email = input("Input student's email address --> ")

        student_records = {search_code : [first_name, last_name, course, email] }
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'b':
        os.system('cls')
        code = input("Input search code ---> ")
        
        for j in student_records.keys():
            code = input("Input search code ---> ")
            if code in student_records.keys():
                print("Record Found")

                print("\nRECORD: ")
                print("----------------------")

                for i in student_records[code].values():
                    print(i,"\n")

            else: 
                    print("NO RECORD FOUND")
        continue


    elif choice == 'c':
        print("EDITING EXISTING RECORD")
        continue

    elif choice == 'd':
        print("System exit")
        break