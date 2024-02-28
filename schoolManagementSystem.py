# School Management System


class Person():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def display_info(self):
        pass

class Students(Person):
    def __init__(self, name, age,roll,classs) -> None:
        super().__init__(name, age)
        self.roll = roll
        self.classs = classs

    def __str__(self) -> str:
        return f"{self.name} of {self.age} years old of {self.roll} reads in class {self.classs}"

class Teacher(Person):
    def __init__(self, name, age,employee_id, subject) -> None:
        super().__init__(name, age)
        self.id = employee_id
        self.sub = subject

    def __str__(self) -> str:
        return f"Mr. {self.name} is {self.age} years old and his ID is {self.id} and he is good for {self.sub}"

s1 = Students("Akkas", 23, 1212, 8)
s2 = Students("Moyna", 22, 1243, 8)

t1 = Teacher("Luthfor", 43, 12344, "Bangla")
t2 = Teacher("Saiful", 45, 12335, "English")

print(t1)
print(t2)
print(s1)
print(s2)