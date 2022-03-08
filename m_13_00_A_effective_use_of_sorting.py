class Student:
    def __init__(self, name: str, grade_point_average: float) -> None:
        self.name = name
        self.grade_point_average = grade_point_average

    def __lt__(self, other: "Student") -> bool:
        return self.name < other.name

    def __repr__(self) -> str:
        return f"<Student(name={self.name}, GPA={self.grade_point_average})>"


def main():
    students = [
        Student("A", 4.0),
        Student("B", 3.0),
        Student("C", 2.0),
        Student("D", 3.5),
    ]

    # Sort according to `Student.__lt__`,
    # in such a way that `students` remains unchanged.
    sorted_students = sorted(students)

    print()
    print(
        sorted_students
    )  # [<Student(name=A, GPA=4.0)>, <Student(name=B, GPA=3.0)>, <Student(name=C, GPA=2.0)>, <Student(name=D, GPA=3.5)>]
    print(
        students
    )  # [<Student(name=A, GPA=4.0)>, <Student(name=B, GPA=3.0)>, <Student(name=C, GPA=2.0)>, <Student(name=D, GPA=3.5)>]

    # Sort by explictly providing a compare function/criterion,
    # in an in-place manner.
    students.sort(key=lambda student: student.grade_point_average)

    print()
    print(
        students
    )  # [<Student(name=C, GPA=2.0)>, <Student(name=B, GPA=3.0)>, <Student(name=D, GPA=3.5)>, <Student(name=A, GPA=4.0)>]


if __name__ == "__main__":
    main()
