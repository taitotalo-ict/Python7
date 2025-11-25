class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self) -> str:
        return f'Person({self.first_name}, {self.last_name})'
    
    def __str__(self) -> str:
        return f'<Person {self.first_name} {self.last_name}>'

class Student(Person):
    _count = 0
    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        Student._count += 1
        self.student_id = Student._count
        self.email = f'{first_name[0].lower()}{last_name[0].lower()}{self.student_id:06}@edu.taitotalo.fi'

    def __str__(self) -> str:
        return f'<Student {self.first_name} {self.last_name} ({self.student_id})>'

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, subject: str) -> None:
        super().__init__(first_name, last_name)
        self.subject = subject
        self.email = f'{first_name.lower()}.{last_name.lower()}@taitotalo.fi'

    def __str__(self) -> str:
        return f'<Teacher {self.first_name} {self.last_name}>'

mika = Person('Mika', 'Suomalainen')
print(mika)

seppo = Student('Seppo', 'Suomalainen')
print(f'{seppo} - Email: {seppo.email}')

chrisu = Teacher('Christian', 'Finnberg', 'Python')
print(f'{chrisu} - Email: {chrisu.email}')

teijo = Student('Teijo', 'Tehokas')
print(f'{teijo} - Email: {teijo.email}')