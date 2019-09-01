class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"(Initialized member): {self.name}")

    def tell(self):
        '''Tell my details'''
        print(f'Name: "{self.name}", Age: "{self.age}"', end=" ")

# IMPORTING THE SuperClass
# Defining of the values that we want to import in subclass
#
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"(Initialized Teacher: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary: {self.salary}")


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"(Initialized Student: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f'Makrs: "{self.marks}"')

t = Teacher("Mrs. Holmes", 40, 20000)
s = Student("Peter Fox", 21, 80)

print()

members = [t, s]
for member in members:
    member.tell()
