from abc import ABC, abstractmethod

class BasePerson(ABC):
    __slot__ = ['fname', 'lname']
    @abstractmethod
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"{self.fname} {self.lname}"


class Student(BasePerson):
    __slot__ = ['has_school_bus', 'grade']
    def __init__(self, has_school_bus=None, grade=None,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_school_bus = has_school_bus
        self.grade = grade

        # self._budget = budget    # baraye shahriye

class HighStudent(BasePerson):
    __slot__ = ['has_school_bus', 'major', 'grade']
    def __init__(self, major, has_school_bus, grade, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.major = major
        self.grade = grade
        self.has_school_bus = has_school_bus
        

# TODO: add a function to promote a student to a higher grade ( set it to int and +1 it each time)

class CollegeStudent(BasePerson):
    __slot__ = ['student_id', 'has_dorm', 'education_type', 'major', 'sub_major', 'grade']
    def __init__(self, student_id, has_dorm, education_type, major, sub_major, grade, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.student_id = student_id 
        self.has_dorm = has_dorm 
        self.grade = grade    
        self.education_type = education_type   # roozane / shabane / pardis khod gardan / azad
        self.major = major 
        self.sub_major = sub_major 

class Teacher(BasePerson):
    __slot__ = ['salary_per_day', 'workings_days']
    def __init__(self, salary_per_day, working_days, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary_per_day = salary_per_day 
        self.working_days = working_days

    @property
    def weekly_salary(self):
        return (self.working_days * self.salary_per_day) 

# TODO: if a student has school_bus they have to pay more  --> baraye shahriye 
        

class ShopKeeper(BasePerson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Master(Teacher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.degree = degree