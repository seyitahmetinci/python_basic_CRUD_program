
class Student:

    def __init__(example, fName, lName, age, sex, country, number):
        example.fName = fName
        example.lName = lName
        example.age = age
        example.sex = sex
        example.country = country
        example.number = number

#getters
    def getFName(example):
        return example.fName
    def getLName(example):
        return example.lName
    def getAge(example):
        return example.age
    def getSex(example):
        return example.sex
    def getCountry(example):
        return example.country
    def getNumber(example):
        return example.number

#setters
    def setFName(example, firstName):
        example.fName = firstName
    def setLName(example, lastName):
        example.lName = lastName
    def setAge(example, age):
        example.age = age
    def setSex(example, sex):
        example.sex = sex
    def setCountry(example, country):
        example.country = country
    def setNumber(example, number):
        example.number = number

#adding student method
def addStudent(studentsdata, filename):
    addFName = input("Enter student first name: ")
    addLName = input("Enter student last name: ")
    addAge = int(input("Enter student age: "))
    addSex = input("Enter student sex: ")
    addCountry = input("Enter student country: ")
    addNumber = input("Enter student number: ")
    studentsdata.append(Student(addFName, addLName, addAge, addSex, addCountry, addNumber))
    writeFile(filename, studentsdata)

#find student method by number
def findByName(studentsdata):
    found = []
    findNumber = (input("Enter Student Number to find details. "))
    for student in studentsdata:
        if student.getNumber() == findNumber:
            found.append(student)
            break
    if (len(found) == 0):
        print("No student found")
        return
    showAll(found)


#show all student record method
def showAll(studentsdata):
    for student in studentsdata:
        print("Student Name: ", student.getFName(), student.getLName())
        print("Student Age: ", student.getAge())
        print("Student Sex: ", student.getSex())
        print("Student Country: ", student.getCountry())
        print("Student Number: ", student.getNumber())
        print()

#find student by age range method
def findByAgeRange(studentsdata):
    lower = int(input("Enter Lower Age Range: "))
    upper = int(input("Enter Upper Age Range: \n"))
    found = []

    for student in studentsdata:
        if student.getAge() >= lower and upper >= student.getAge():
            found.append(student)
    if (len(found) == 0):
        print("No student found")
        return
    showAll(found)

#modify student method by number
def modifyStudent(studentsdata, filename):
    findNumber = (input("Enter Student Number to find details. "))
    flag = True

    for student in studentsdata:
        if student.getNumber() == findNumber:
            flag = False
            print("Choose field to modify:\n1. First Name\n2. Last Name\n3. Age\n4. Sex\n5. Country\n6. Number")
            x = int(input())

            if x == 1:
                tempFName = input("Enter new first name: ")
                student.setFName(tempFName)
            elif x == 2:
                tempLName = input("Enter new last name: ")
                student.setLName(tempLName)
            elif x == 3:
                tempAge = input("Enter new Age: ")
                student.setAge(tempAge)
            elif x == 4:
                tempSex = input("Enter new sex: ")
                student.setSex(tempSex)
            elif x == 5:
                tempCountry = input("Enter new country: ")
                student.setCountry(tempCountry)
            elif x == 6:
                tempNumber = input("Enter new number: ")
                student.setNumber(tempNumber)
            break

    if (flag):
        print("Student record not founded!")

    else:
        print("\n Record updated succesfully! \n")
        writeFile(filename, studentsdata)

#delete student method by number
def deleteStudent(studentsdata, filename):
    findNumber = (input("Enter Student Number to find details. "))
    flag = True

    for student in studentsdata:
        if student.getNumber() == findNumber:
            flag = False
            studentsdata.remove(student)
            break

    if (flag):
        print("Student record not found.")
    else:

        print("\n Record deleted. \n")
        writeFile(filename, studentsdata)

#read student info method
def readFile(filename, studentsdata):
    f = open(filename, mode="r")
    print(f.read())

    for x in f.readlines():
        str1 = x.split(", ")

        n = str1[0]
        l = str1[1]
        a = str1[2]
        s = str1[3]
        c = str1[4]
        num = str1[5].strip()

        st = Student(n, l, int(a), s, c, num)

        studentsdata.append(st)

    f.close()
    print("\n Operation is done succesfully !!! \n")
    return studentsdata

#write student to txt file method
def writeFile(filename, studentsdata):

    try:
        f = open(filename, mode='w')
        for student in studentsdata:
            f.write(str(student.fName + ", " + student.lName + ", " + str(
                student.age) + ", " + student.sex + ", " + student.country + ", " + str(student.number) + "\n"))
    finally:
        f.close()
        print("\n Operation is done succesfully \n")

#find student method
def findStudent(studentsdata):
    print("Select search criterion:\n1. First Name\n2. Last Name\n3. Age\n4. Sex\n5. Country\n6. Number")
    choice = int(input())

    if choice == 1:
        found = []
        tempdata = (input("Enter First Name: "))
        for student in studentsdata:
            if student.getFName() == tempdata:
                found.append(student)
        if (len(found) == 0):
            print("No student found with specified First Name")
            return
        showAll(found)

    if choice == 2:
        found = []
        tempdata = (input("Enter Last Name: "))
        for student in studentsdata:
            if student.getLName() == tempdata:
                found.append(student)
        if (len(found) == 0):
            print("No student found with specified Last Name")
            return
        showAll(found)

    if choice == 3:
        found = []
        tempdata = int(input("Enter Age: "))
        for student in studentsdata:
            if student.getAge() == tempdata:
                found.append(student)
        if (len(found) == 0):
            print("Didn't find student with the given age...")
            return
        showAll(found)

    if choice == 4:
        found = []
        tempdata = (input("Enter Sex: "))
        for student in studentsdata:
            if student.getSex() == tempdata:
                found.append(student)
        if (len(found) == 0):
            print("Didn't find student with the given sex...")
            return
        showAll(found)

    if choice == 5:
        found = []
        tempdata = (input("Enter Country: "))
        for student in studentsdata:
            if student.getCountry() == tempdata:
                found.append(student)
        if (len(found) == 0):
            print("Didn't find student with the given country...")
            return
        showAll(found)

    if choice == 6:
        found = []
        tempdata = (input("Enter Number: "))
        for student in studentsdata:
            if student.getNumber() == tempdata:
                found.append(student)
        if (len(found) == 0):
            print("Didn't find student with the given number...")
            return
        showAll(found)


if __name__ == '__main__':
    studentsdata = [100],

    studentsdata = [Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplenam9e", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123"),
                    Student("examplename", "example", "age", "sex", "country", "123123")]

    action = None

    while action != 0:
        print(" Select an action from the menu below: \n "
              "1- Add new student\n"
              "2- Find student by Student Number\n"
              "3- Show all student informations\n"
              "4- Find Students in a Certain Age Range\n"
              "5- Modify Student record by student number\n"
              "6- Delete a student with a specific student number\n"
              "7- Export all student data to file\n"
              "8- Import students data from file\n"
              "9- Exit program\n"
              "0- (Bonus) To search any criterion\n")
        action = int(input("Enter action number what you want to do:"))

        if action == 1:
            addStudent(studentsdata, "students.txt")
        elif action == 2:
            findByName(studentsdata)
        elif action == 3:
            showAll(studentsdata)
        elif action == 4:
            findByAgeRange(studentsdata)
        elif action == 5:
            modifyStudent(studentsdata, "students.txt")
        elif action == 6:
            deleteStudent(studentsdata, "students.txt")
        elif action == 7:
            writeFile("students.txt", studentsdata)
        elif action == 8:
            studentsdata = readFile("students.txt", studentsdata)
        elif action == 9:
            exit()

        elif action == 0:
            findStudent(studentsdata)
        else:
            continue


