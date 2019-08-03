# Grade Book Project _Ryan_C_Pate_
import os

students = []
index = 0
name = ''
grade = ''
filePath = r'ClassNameGrades.txt'
grades = ['aA', 'bB', 'cC', 'dD', 'fF']
count = 0


def writefile(filePath, className, facultyName):
    file = open(filePath, 'a')
    try:
        file.write("Class: %s" % className + '\n')
        file.write("Faculty's Name: %s" % facultyName + '\n')
        file.write(str(students) + '\n')
        file.write("There were %d student(s) who had an A in this class\n" % (students.count('A') + students.count('a')))
        file.write("There were %d student(s) who had a B in this class\n" % (students.count('B') + students.count('b')))
        file.write("There were %d student(s) who had a C in this class\n" % (students.count('C') + students.count('c')))
        file.write("There were %d student(s) who had a D in this class\n" % (students.count('D') + students.count('d')))
        file.write("There were %d student(s) who had an F in this class\n" % (students.count('F') + students.count('f')))
    except Exception as exep:
        print(exep)
    finally:
        if file is not None:
            file.close()


def main(index, name, grade, filePath):
    if os.path.exists(filePath):
        print("File already exists.")
    else:
        className = input("Please input the name of the class: ")
        facultyName = input("Please input the faculty name: ")
        more = 'y'
        while more == 'y':
            name = input("Enter student #%d's name: " % (index+1))
            grade = input("Enter student #%d's letter grade: " % (index+1))
            students.append(name)
            students.append(grade)
            more = input("Do you have more students?\n'y' for yes, anything else is no.\n")
            index += 1
        print(students)
        writefile(filePath, className, facultyName)

main(index, name, grade, filePath)
