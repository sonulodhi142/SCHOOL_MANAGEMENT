# List to store all data
studentData = []

# function to add student

def addStudent():
    print("\nFill the student data to add new student:-\n ")
    name = input("Enter the student name:")
    rollno = input("Enter the student roll NO.:")
    age = input("Enter the student age:")
    clas = input("Enter the student clas:")
    phone = input("Enter the student phone:")

    values = {
        "name":name,
        "rollno":rollno,
        "age" : age,
        "class": clas,
        "phone" : phone
    }
    studentData.append(values)
    print(f"\n The {name}'s data succesfully added:-\n\n")
    

while True:

    print("<--WEL-COME TO THE SCHOOL MANAGEMENT PROGRAM---->\n")
    print("Click 1 to add student data ")
    print("Click 2 to update student data ")
    print("Click 3 to remove student data ")
    print("Click 4 to display all student data  ")
    print("Click 5 to display specific student data ")
    choice = int(input("Enter any one choice::"))

    if choice == 1:
        addStudent
    
    check = input("Do you want to perform more operation ? (y/n):")
    if check == 'y':
        break





