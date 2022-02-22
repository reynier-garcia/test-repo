from typing import Dict, Optional


class Student:
    def __init__(self, name: str, age: int, academic_year: int):
        self.name = name
        self.age = age
        self.academic_year = academic_year
        self.notes: Dict[str, float] = dict()

    def add_note(self, subject_name: str, note: float) -> None:
        self.notes[subject_name] = note

    def get_note(self, subject_name: str) -> Optional[float]:
        return self.notes.get(subject_name)
