from django.shortcuts import render
from django.http import JsonResponse
from school.models import (
    EducationOrganization, Student, Teacher, Master, ClassRoom, HighStudent, CollegeStudent,
    Elementary,
    FirstHigh,
    SecondHigh,
    College,
    Snack,
    Shop,
    VendingMachine,
)

def home(request):
    return render(request, 'home.html')


def api_view(request):  
    return JsonResponse({'text':"hello world"})

def education_organization_view(request):
    organizations_from_db = EducationOrganization.objects.values('name', 'gender', 'year_of_foundation', 'school_type', 'education_level')
    organizations = {
        'data': [item for item in organizations_from_db]
    }
    return JsonResponse(organizations)

def student_view(request):
    students_from_db = Student.objects.values('first_name', 'last_name', 'grade')
    students = {
        'data': [item for item in students_from_db]
    }
    return JsonResponse(students)

def teacher_view(request):
    teachers_from_db = Teacher.objects.values('first_name', 'last_name')
    teachers = {
        'data': [item for item in teachers_from_db]
    }
    return JsonResponse(teachers)

def master_view(request):
    masters_from_db = Master.objects.values('first_name', 'last_name')
    masters = {
        'data': [item for item in masters_from_db]
    }
    return JsonResponse(masters)

def class_room_view(request):
    class_rooms_from_db = ClassRoom.objects.values('name', 'students', 'teacher')
    class_rooms = {
        'data': [item for item in class_rooms_from_db]
    }
    return JsonResponse(class_rooms)

def high_student_view(request):
    high_students_from_db = HighStudent.objects.values('first_name', 'last_name', 'grade', 'major')
    high_students = {
        'data': [item for item in high_students_from_db]
    }
    return JsonResponse(high_students)

def college_student_view(request):
    college_students_from_db = CollegeStudent.objects.values('first_name', 'last_name', 'grade', 'major', 'sub_major')
    college_students = {
        'data': [item for item in college_students_from_db]
    }
    return JsonResponse(college_students)

def elementary_view(request):
    elementaries_from_db = Elementary.objects.values('grade', 'class_room', 'students', 'teachers')
    elementaries = {
        'data': [item for item in elementaries_from_db]
    }
    return JsonResponse(elementaries)

def first_high_view(request):
    first_highs_from_db = FirstHigh.objects.values('grade', 'class_room', 'students', 'teachers')
    first_highs = {
        'data': [item for item in first_highs_from_db]
    }
    return JsonResponse(first_highs)

def second_high_view(request):
    second_highs_from_db = SecondHigh.objects.values('grade', 'class_room', 'students', 'teachers')
    second_highs = {
        'data': [item for item in second_highs_from_db]
    }
    return JsonResponse(second_highs)

def college_view(request):
    colleges_from_db = College.objects.values('semester', 'grade', 'class_rooms', 'students', 'masters', 'major', 'sub_major')
    colleges = {
        'data': [item for item in colleges_from_db]
    }
    return JsonResponse(colleges)

def snack_view(request):
    snacks_from_db = Snack.objects.values('name', 'cost')
    snacks = {
        'data': [item for item in snacks_from_db]
    }
    return JsonResponse(snacks)

def vending_machine_view(request):
    vending_machines_from_db = VendingMachine.objects.values('shopkeeper', 'snacks')
    vending_machines = {
        'data': [item for item in vending_machines_from_db]
    }
    return JsonResponse(vending_machines)

def shop_view(request):
    shops_from_db = Shop.objects.values('shopkeeper', 'snacks')
    shops = {
        'data': [item for item in shops_from_db]
    }
    return JsonResponse(shops)

