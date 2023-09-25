class Student:
    def _init_(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa
    def sort_students(student_list):
        sorted_students=sorted(student_list,
                               key=lambda student: student.cgpa,
                               reverse=True)
        return sorted_studnets
    students=[
        student("Raji","A129",7.8),
        student("Ramya","A131",8.9),
        student("Kirthi","A119",7.5),
        student("Kani","A120",7.6)
        ]
    sorted_students= sort_students(students)
    for student in sorted_students:
        print("Name:{},Rolle_Number:{},CGPA:{}",format(student.name,
                                                       student.roll_number,
                                                       student.cgpa))
