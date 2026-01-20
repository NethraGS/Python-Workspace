class Student:

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.rank = None

    def set_rank(self, rank):
        self.rank = rank

    def display(self):
        print(
            f"ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Marks: {self.marks}, "
            f"Rank: {self.rank}"
        )


class Teacher:

    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.students = []   

    def hello(self):
        print(f"Hi, I am {self.name} (ID: {self.teacher_id})")

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def total_students(self):
        return len(self.students)

    def assign_ranks(self):
        self.students.sort(key=lambda s: s.marks, reverse=True)

        for student in self.students:
            if student.marks >= 60:
                student.set_rank("1st")
            elif 45 <= student.marks < 60:
                student.set_rank("2nd")
            elif 35 <= student.marks < 45:
                student.set_rank("3rd")
            elif 20 <= student.marks < 35:
                student.set_rank("Fail")
            else:
                student.set_rank("Restricted")

    def display_students(self):
        self.students.sort(key=lambda s: s.marks, reverse=True)
        for student in self.students:
            student.display()

    def count_distinction(self):
        return sum(1 for s in self.students if s.marks >= 75)

    def restricted_students(self):
        return [s for s in self.students if s.marks < 20]


if __name__ == "__main__":
    # Students
    s1 = Student(101, "Neo", 95)
    s2 = Student(102, "Trinity", 90)
    s3 = Student(103, "Morpheus", 85)
    s4 = Student(104, "Maichel", 80)

    # Teachers
    python_teacher = Teacher(11, "Upasana")
    ml_teacher = Teacher(2, "Kavita")

    # Association
    python_teacher.add_student(s1)
    python_teacher.add_student(s2)
    python_teacher.add_student(s3)

    ml_teacher.add_student(s2)
    ml_teacher.add_student(s3)
    ml_teacher.add_student(s4)

    # Assign ranks once
    python_teacher.assign_ranks()
    ml_teacher.assign_ranks()

    while True:
        print("\n--- MENU ---")
        print("1. Display number of students under each teacher")
        print("2. Display total strength of students")
        print("3. Display students of a teacher (sorted by marks)")
        print("4. Display rank of students")
        print("5. Count of students with distinction (>=75)")
        print("6. Display restricted students (<20 marks)")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            print(f"{python_teacher.name}: {python_teacher.total_students()}")
            print(f"{ml_teacher.name}: {ml_teacher.total_students()}")

        elif choice == "2":
            total = python_teacher.total_students() + ml_teacher.total_students()
            print("Total student strength:", total)

        elif choice == "3":
            print("\nStudents under Python Teacher:")
            python_teacher.display_students()

        elif choice == "4":
            print("\nStudent Ranks:")
            python_teacher.display_students()

        elif choice == "5":
            print(
                "Distinction count:",
                python_teacher.count_distinction()
            )

        elif choice == "6":
            restricted = python_teacher.restricted_students()
            if not restricted:
                print("No restricted students")
            else:
                print("Restricted students:")
                for s in restricted:
                    s.display()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")
