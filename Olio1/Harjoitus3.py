class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

        self._completed_courses = []
    
    def _full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def add_course(self, course_name: str) -> None:
        self._completed_courses.append(course_name)

    def add_courses(self, course_list: list|tuple) -> None:
        self._completed_courses.extend(course_list)
        
    def print_courses(self) -> None:
        if self._completed_courses:
            print(f'Student {self._full_name()} has completed following courses:')
            for course_name in self._completed_courses:
                print(f'- {course_name}')
        else:
            print(f'Student {self._full_name()} has not completed any courses yet.')
            

christian = Student('Christian', 'Finnberg')
# christian.add_course('Python')
# christian.add_course('Linux')
#christian.add_courses(['Python', 'Linux'])
#christian.add_courses('Python', 'Linux')
christian.print_courses()
