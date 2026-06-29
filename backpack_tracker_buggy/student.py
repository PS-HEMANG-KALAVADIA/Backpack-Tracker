from person import Person

class Student(Person):
    def __init__(self, name, student_id, course):
        super().__init__(name, student_id)
        self.__course = course

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course
