
##For question #1

class Vehicle:
    def __init__(self, brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type

    def getdetails(self):
        print("The Vehicle are manufactured by" + self.brand)
        print("The Vehicle model are " + self.model)
        print("The Vehicle type are " + self.type + "\n")


class SchoolBus(Vehicle):
    def getdetails(self):
        print("The Vehicle are manufactured by " + self.brand)
        print("The Vehicle model are " + self.model)
        print("The Vehicle type are " + self.type + "\n")

class car(Vehicle):
    def getdetails(self):
        print("The Vehicle are manufactured by" + self.brand)
        print("The Vehicle model are " + self.model)
        print("The Vehicle type are " + self.type + "\n")

vehicles = [car("Toyota", "Vios", "Private"), SchoolBus("Yutong", "K6876H", "Public")]


for v in vehicles:
    v.getdetails()


#For question 2

class Employee:
    def __init__(self,name,position,department):
        self.name = name
        self.position = position
        self.department = department

    @classmethod
    def name(cls,name):
        return cls(name, position="N/A", department="N/A")
    @classmethod
    def position(cls,postion):
        return cls(name = "Unknown", position = postion, department="N/A")
    @classmethod
    def department(cls,department):
        return cls(name = "Unknown", position="N/A", department= department)

    def empdetails(self):
        return f"Name: {self.name}, Position: {self.position}, Department: {self.department}"

employee1 = Employee.name("Bryan")
print(employee1.empdetails())

employee2 = Employee.position("Intern")
print(employee2.empdetails())

employee3 = Employee.department("Finance")
print(employee3.empdetails())

employee4 = Employee("Bryan", "Intern", "Finance")
print(employee4.empdetails())


#Question 3

class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def ave_grade(self):
        return sum(self.grades) / len(self.grades)
    def ave_gpa(self):
        avg_grade = self.ave_grade()
        if avg_grade >= 93:
            return 4.0
        elif avg_grade >= 90:
            return 3.7
        elif avg_grade >=87:
            return 3.3
        elif avg_grade >=83:
            return 3.0
        elif avg_grade >=80:
            return 2.7
        elif avg_grade >=77:
            return 2.3
        elif avg_grade >=73:
            return 2.0
        elif avg_grade >=70:
            return 1.7
        elif avg_grade >=67:
            return 1.3
        elif avg_grade >=65:
            return 1.0
        else:
            return 0

    def student_info(self):
        print(f"Student:  {self.name}")
        print(f"Average Grades: {self.ave_grade():.2f}")
        print(f"GPA: {self.ave_gpa():.2f}")


class SchoolOne:
    def __init__(self):
        self.students = []

    def student(self,name,grades):
        self.students.append(Student(name,grades))

    def displaystudents(self):
        print("School One Record")
        for student in self.students:
            student.student_info()
            print()

class SchoolTwo:
    def __init__(self):
        self.students = []

    def student(self,name,grades):
        self.students.append(Student(name,grades))

    def displaystudents(self):
        print("School One Record")
        for student in self.students:
            student.student_info()
            print()

school1=SchoolOne()
school1.student("Julian",[90,78,84])
school1.student("Mark",[67,88,81])
school1.displaystudents()

school2=SchoolTwo()
school2.student("Charlie", [95, 88, 92])
school2.student("Owen",[60, 65, 70])
school2.displaystudents()


#Question 4

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return  Vector(self.x + other.x, self.y + other.y)


    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1,2)
v2 = Vector(3,5)
v3 = v1 + v2

print (v3)


#Question 5
class Author:
    def __init__(self, name, nation):
        self.name = name
        self.nationality = nation
    def details(self):
        return f"{self.name} ({self.nationality})"



class Book:
    def __init__(self, title, pub_year,  author: Author):
        self.title = title
        self.pub_year = pub_year
        self.author = author

    def book(self):
       return f"'{self.title}' ({self.pub_year}) by {self.author.details()}"

    def bookdetails(self):
        return f"{self.book()}"


author1 = Author("Jose Rizal", "Filipino")
book1 = Book ("Noli me Tangere", "1887",author1)

print(book1.bookdetails())


