# class Grade: 
#     __slot__ = ['grade', 'class_rooms']
#     def __init__(self, grade, class_rooms):
#         self.grade = grade
#         self.classrooms = class_rooms

#     def __repr__(self):
#         return self.grade
    
class ClassRoom:
    __slot__ = ['name', 'students', 'teacher', 'code']
    def __init__(self, name, students, teacher, code):
        self.name = name
        self.students = students
        self.teacher = teacher
        self.code = code

    def __repr__(self):
        return self.name
    
    
class Elementary:
    __slot__ = ['grade', 'class_rooms', 'students', 'teachers']
    def __init__(self, grade, class_rooms, students, teachers):
        self.grade = grade  # 1 - 2 - 3 - 4 - 5 - 6
        self.class_rooms = class_rooms
        self.students = students
        self.teachers = teachers


class FirstHigh:
    __slot__ = ['grade', 'class_rooms', 'students', 'teachers']
    def __init__(self, grade, class_rooms, students, teachers):
        self.grade = grade    # 7 - 8 - 9 
        self.class_rooms = class_rooms
        self.students = students
        self.teachers = teachers


class SecondHigh:
    __slot__ = ['grade', 'class_rooms', 'students', 'teachers', 'major']
    def __init__(self, grade, class_rooms, students, teachers, major):
        self.grade = grade   # 10 - 11 - 12
        self.class_rooms = class_rooms
        self.students = students
        self.teachers = teachers
        self.major = major

class College:
    __slot__ = ['semester', 'grade' , 'class_ids', 'class_rooms', 'students', 'masters', 'major', 'sub_majors']
    def __init__(self, semester, grade, class_rooms, students, masters, major, sub_majors):
        self.semester = semester   # 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 (max=10)
        self.grade = grade      # lisans / fogh lisans / PHD / Fogh doktora
        self.class_rooms = class_rooms
        self.students = students
        self.masters = masters
        self.major = major
        self.sub_majors = sub_majors
