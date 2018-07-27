#Code _- Vidit Shah



#importing The Librart
import statistics

#Create Admins So who all can access The Database-Dictionary
admins ={'Jack':'qwerty','ron':'asdfg'}

#Student-Dictionary with thier Marks
studentDict = {
    'James':[100,100,100],
    'Rahul':[56,45,67],
    'Arjun':[67,88,89]
}

#Fucnction to Add grade
def addGrade():
    student_name = input("Enter Student name")
    if student_name in studentDict:#Check if student is present in our Dictionary
        _grade = input("Enter Grade")
        studentDict[student_name].append(_grade)#Appends Grade
        print(studentDict)
    else:
        print("Student not in Data Base")

#Function to Remove Grade
def removeStudent():
    student_name = input("Enter Student Name")
    if student_name in studentDict:#check if Student is present in our Dictionary
        del studentDict[student_name]#if present Deletes The Student
        print(studentDict)
    else:
        print('Student Not in DataBase')

def calAvg():
    for eachStudent in studentDict:#Loop over Each student in the Dictionary
        gradeList = studentDict[eachStudent]
        avg = statistics.mean(gradeList)
        print(eachStudent,"has Average of ",avg)




def main():

    print("""
    Welcome to the Grade Entry System 
    -Enter a number to perform any of the following operations
    
    [1]-Enter Grades
    [2]-Remove Student
    [3]-Student Average
    [4]-exit
    
    
    
    """)

    choice = int(input("Enter your Choice"))

    if choice==1:
        addGrade()
    elif choice==2:
        removeStudent()
    elif choice==3:
        calAvg()
    elif choice==4:
        exit()
    else:
        print('Invalid Argument Re enter The Data \n')

#Login
username = input("Enter username")
password = input("Enter Pass")

if username in admins and admins[username]==password:
            print("Welcome  ",username)
            while True:

               main()
else:
    print('Invalid Credentials')


