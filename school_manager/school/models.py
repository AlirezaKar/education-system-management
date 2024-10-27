from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    has_school_bus = models.BooleanField(null=True)
    grade = models.CharField(max_length=2, null=True)
    
    def __str__(self):
        return f"Student- {self.first_name} {self.last_name}"

class HighStudent(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    has_school_bus = models.BooleanField(null=True)
    grade = models.CharField(max_length=2, null=True)
    major = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"Second High- {self.first_name} {self.last_name}"

class CollegeStudent(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    student_id = models.IntegerField(max_length=8, null=True)
    has_dorm = models.BooleanField(null=True)
    grade = models.CharField(max_length=15, null=True)
    education_type = models.CharField(max_length=20, null=True)
    major = models.CharField(max_length=10, null=True)
    sub_major = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"College- {self.first_name} {self.last_name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    salary_per_day = models.IntegerField(null=True) 
    working_days = models.IntegerField(null=True) 

    def __str__(self):
        return f"Teacher- {self.first_name} {self.last_name}"
    
class Master(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    salary_per_day = models.IntegerField(null=True) 
    working_days = models.IntegerField(null=True) 

    def __str__(self):
        return f"master- {self.first_name} {self.last_name}"

class ClassRoom(models.Model):
    name = models.CharField(max_length=50, null=True)
    students = models.ManyToManyField(Student)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

# class Grade(models.Model):
#     name = models.CharField(max_length=10, null=True)
#     class_rooms = models.ManyToManyField(ClassRoom)

#     def __str__(self):
#         return self.name
    
class Elementary(models.Model):
    grade = models.CharField(max_length=2, null=True)
    class_room = models.ManyToManyField(ClassRoom, null=True)
    students = models.ManyToManyField(Student, null=True)
    teachers = models.ManyToManyField(Teacher, null=True)

class FirstHigh(models.Model):
    grade = models.CharField(max_length=2, null=True)
    class_room = models.ManyToManyField(ClassRoom, null=True)
    students = models.ManyToManyField(Student, null=True)
    teachers = models.ManyToManyField(Teacher, null=True)

class SecondHigh(models.Model):
    grade = models.CharField(max_length=2, null=True)
    class_room = models.ManyToManyField(ClassRoom, null=True)
    students = models.ManyToManyField(Student, null=True)
    teachers = models.ManyToManyField(Teacher, null=True)
    major = models.CharField(max_length=15, null=True)

class College(models.Model):
    semester = models.CharField(max_length=20, null=True)
    grade = models.CharField(max_length=20, null=True)
    class_rooms = models.ManyToManyField(ClassRoom, null=True)
    students = models.ManyToManyField(Student, null=True)
    masters = models.ManyToManyField(Master, null=True)
    major = models.CharField(max_length=20, null=True)
    sub_major = models.CharField(max_length=20, null=True)

class EducationOrganization(models.Model):
    name = models.CharField(max_length=70, null=True)
    description = models.TextField(null=True)
    gender = models.CharField(max_length=15, null=True)
    year_of_foundation = models.DateField(auto_now_add=False, null=True)
    school_type = models.CharField(max_length=15, null=True)
    education_level = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name

class Snack(models.Model):
    name = models.CharField(max_length=20, null=True)
    cost = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    shopkeeper = models.ForeignKey(User, on_delete=models.CASCADE)
    snacks = models.ManyToManyField(Snack)

    def __str__(self):
        return str(self.shopkeeper)

class VendingMachine(models.Model):
    shopkeeper = models.ForeignKey(User, on_delete=models.CASCADE)
    snacks = models.ManyToManyField(Snack)

    def __str__(self):
        return str(self.shopkeeper)