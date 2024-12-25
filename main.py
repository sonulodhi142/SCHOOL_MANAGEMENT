# List to store all data
studentData = []

# function to add student

def addStudent():
    name = input("Enter the student name:")
    
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





