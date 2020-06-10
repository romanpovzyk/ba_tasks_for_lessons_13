class Person:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school


class Student(Person):
    def __init__(self, name, age, school, group):
        super().__init__(name, age, school)
        self.group = group


class Teacher(Person):
    def __init__(self, name, age, school, subject, salary):
        super().__init__(name, age, school)
        self.subject = subject
        self.salary = salary


s1 = Student("Roma", 29, "Beetroot", "Python101")
t1 = Teacher("Kate", 27, "Beetroot", "Marketing", 20000)
