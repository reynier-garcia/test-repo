from typing import List

from .student import Student
from .subject import Subject


class School:
    def __init__(self, name: str):
        self.name = name
        self.subjects: List[Subject] = []
        self.students: List[Student] = []

    def add_subject(self, name: str, description: str):
        self.subjects.append(Subject(name, description))

    def add_student(self, name: str, age: int, academic_year: int):
        self.students.append(Student(name, age, academic_year))

    def get_students_names(self) -> List[str]:
        return [s.name for s in self.students]
