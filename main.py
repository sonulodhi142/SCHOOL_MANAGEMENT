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


# fuction for display all studentData
def displayData():
    print("\n All student Data is given below:-\n")
    count = 0
    for data in studentData:
        count = count + 1
        print(f"\n The data of student {count}: \n")
        print(f"name      : {data['name']}")
        print(f"roll NO.  : {data['rollno']}")
        print(f"class     : {data['class']}")
        print(f"age       : {data['age']}")
        print(f"phone no. : {data['phone']}\n\n")

# fuction to update studentData
def updateData():
    print("\n Here you Update-Date to Search student with their rollno:- ")
    search = input("Enter roll NO.::")
    for data in studentData:
        if data['rollno']==search:
            print("\n Here are student prev. Data:-\n")
            print(f"name      : {data['name']}")
            print(f"roll NO.  : {data['rollno']}")
            print(f"class     : {data['class']}")
            print(f"age       : {data['age']}")
            print(f"phone no. : {data['phone']}\n\n")
            # here updata the StudentData
            print("\n Here are student prev. Data:-\n")
            data['name'] = input("Update Name::")
            data['rollno'] = input("Update roll No.::")
            data['class'] = input("Update class::")
            data['age'] = input("Update age::")
            data['phone'] = input("Update phone No.::")
            print(f"\n The {data['name']}'s data succesfully Updated:-\n\n")

# function for remove studentData
def removeData():
    print("\n Here you Remove student Data by Search with their rollno:- ")
    search = input("Enter roll NO.::")
    for data in studentData:
        if data['rollno']==search:
            print(f"\n The {data['name']}'s data succesfully Deleted:-\n")
            studentData.remove(data)

# fuction to display specific studentData
def searchData():
    print("\n Here you Search student with their rollno:- ")
    search = input("Enter roll NO.::")
    for data in studentData:
        if data['rollno']==search:
            print("\n Here are student prev. Data:-\n")
            print(f"name      : {data['name']}")
            print(f"roll NO.  : {data['rollno']}")
            print(f"class     : {data['class']}")
            print(f"age       : {data['age']}")
            print(f"phone no. : {data['phone']}\n\n")
        

while True:

    print("\n\n<--WEL-COME TO THE SCHOOL MANAGEMENT PROGRAM---->\n")
    print("Click 1 to add student data ")
    print("Click 2 to update student data ")
    print("Click 3 to remove student data ")
    print("Click 4 to display all student data  ")
    print("Click 5 to display specific student data ")
    choice = int(input("Enter any one choice::"))

    if choice == 1:
        addStudent()
    elif choice == 2:
        updateData()
    elif choice == 3:
        removeData()
    elif choice == 4:
        displayData()
    elif choice == 5:
        searchData()
    else:
        print("\n Please Enter vailed Choice:-\n")
    
    check = input("Do you want to perform more operation ? (y/n):")
    if check == 'n':
        break





