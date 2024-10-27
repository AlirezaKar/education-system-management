from django.shortcuts import render
# from .models import School, Student, Teacher, ClassRoom


# def school_homepage(request):
    # school_obj = School.objects.all()
    # return render(request, 'homepage.html', {'school_obj':school_obj})

# def grades_view(request):
#     grades = Grade.objects.all()
#     return render(request, 'parent/grades.html', {'grades':grades})

# def teachers_view(request, pk):
#     teachers = Teacher.objects.all()
#     return render(request, 'parent/teachers.html', {'teachers':teachers})

# def students_view(request, pk):
#     students = Student.objects.all()
#     return render(request, 'parent/students.html', {'students':students})

# FIXME: students_view / teachers_view --> it must get those objects with the appropriate grade

