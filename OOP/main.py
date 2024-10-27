
from person import CollegeStudent, HighStudent, ShopKeeper, Student, Teacher
from organization import EducationOrganization, Shop, Snack, VendingMachine
from classroom import ClassRoom, Elementary, FirstHigh, SecondHigh, College
from datetime import date
from random import randrange

teacher_1 = Teacher(fname='Alireza', lname='Kalaie', salary_per_day=1, working_days=5)
teacher_2 = Teacher(fname='Hesam', lname='Doosti', salary_per_day=2, working_days=5)
teacher_3 = Teacher(fname='ehsan', lname='gholami', salary_per_day=1, working_days=3)
teacher_4 = Teacher(fname='akbar', lname='fashami', salary_per_day=3, working_days=4)

class_1_students = [ 
    Student(fname = 'hamid', lname = 'goli', has_school_bus=True),
    Student(fname = 'naser', lname = 'hemati', has_school_bus=True),
    Student(fname = 'pejman', lname = 'jamshidi', has_school_bus=False),
    Student(fname = 'naser', lname = 'abdollahi', has_school_bus=True)
]

class_2_students = [
    Student(fname = 'hamid', lname ='goli', has_school_bus=True),
    Student(fname = 'naser', lname = 'hemati', has_school_bus=True),
    Student(fname = 'pejman', lname = 'jamshidi', has_school_bus=False),
    Student(fname = 'naser', lname = 'abdollahi', has_school_bus=True)
]


class_3_students = [
    Student(fname = 'hamid', lname = 'goli', has_school_bus=True),
    Student(fname = 'naser', lname = 'hemati', has_school_bus=True),
    Student(fname = 'pejman', lname = 'jamshidi', has_school_bus=False),
    Student(fname = 'naser', lname = 'abdollahi', has_school_bus=True)
]

class_4_students = [
    Student(fname = 'hamid', lname = 'goli', has_school_bus=True),
    Student(fname = 'naser', lname = 'hemati', has_school_bus=True),
    Student(fname = 'pejman', lname = 'jamshidi', has_school_bus=False),
    Student(fname = 'naser', lname = 'abdollahi', has_school_bus=True)
]

class_5_students = [
    Student(fname = 'hamid', lname = 'goli', has_school_bus=True),
    Student(fname = 'naser', lname = 'hemati', has_school_bus=True),
    Student(fname = 'pejman', lname = 'jamshidi', has_school_bus=False),
    Student(fname = 'naser', lname = 'abdollahi', has_school_bus=True)
]


class_room_1 = ClassRoom(name='kharazi' ,students=class_1_students, teacher=teacher_1, code=1)
class_room_2 = ClassRoom(name='mofateh', students=class_2_students, teacher=teacher_2, code=2)
class_room_3 = ClassRoom(name='backeri', students=class_3_students, teacher=teacher_3, code=3)
class_room_4 = ClassRoom(name='ehsan', students=class_4_students, teacher=teacher_4, code=4)
class_room_5 = ClassRoom(name='tafakor', students=class_5_students, teacher=teacher_4, code=5)


# grade_1th = Grade('1th', class_rooms=[class_room_1, class_room_2]) 
# grade_2th = Grade('2th', class_rooms=[class_room_3]) 
# grade_3th = Grade('3th', class_rooms=[class_room_4, class_room_5]) 



school_1 = EducationOrganization('salam', gender='Boys only', year_of_foundation=date.today(), school_type='private', education_level='high school 1')

pizza = Snack(name='pizza', cost=20)
ice_cream = Snack(name='ice cream', cost=5)
water = Snack(name='water', cost=1)
soda = Snack(name='soda', cost=4)

shopkeeper_1 = ShopKeeper(fname='hasan', lname='kachal')
shopkeeper_2 = ShopKeeper(fname='abdolah', lname='noori')


shop_1 = Shop(shopkeeper=shopkeeper_1, snacks=[pizza, soda, water])

vending_machine_1 = VendingMachine(shopkeeper=shopkeeper_2, snacks=[ice_cream])
####################################DETAILED CLASSING SYSTEM####################################################
e_student_1 = Student(fname='Ramiro', lname='Mercado', has_school_bus=True, grade=1)
e_student_2 = Student(fname='Valentin ', lname='Good', has_school_bus=False, grade=2)
e_student_3 = Student(fname='Justice ', lname='Richards', has_school_bus=True, grade=4)
e_student_4 = Student(fname='Peyton ', lname='Boone', has_school_bus=True, grade=6)
#
fh_student_1 = Student(fname='Asia ', lname='Griffith', has_school_bus=True, grade=7)
fh_student_2 = Student(fname='Kenley  ', lname='GrifMaysfith', has_school_bus=True, grade=8)
fh_student_3 = Student(fname='Tanner  ', lname='Potter', has_school_bus=True, grade=7)
fh_student_4 = Student(fname='Levi  ', lname='Carey', has_school_bus=True, grade=9)
#  TODO: assert for each level grade to be in the correct range 
sh_student_1 = HighStudent(fname='Rayan ', lname='Conner', major='Math', has_school_bus=False, grade=10)
sh_student_2 = HighStudent(fname='Dorian  ', lname='Bates', major='Math', has_school_bus=False, grade=11)
sh_student_3 = HighStudent(fname='Helena  ', lname='Olson', major='tajrobi', has_school_bus=False, grade=12)
sh_student_4 = HighStudent(fname='Kaylie  ', lname='Haley', major='ensani', has_school_bus=False, grade=12)
#
rand_int = randrange(10000000, 99999999)
c_student_1 = CollegeStudent(fname='Antwan ', lname='Werner', student_id=rand_int, has_dorm=True, education_type='shabaneh', grade='lisans', major='Ensani', sub_major='Hoghoogh')
c_student_2 = CollegeStudent(fname='Fernanda  ', lname='Ortega', student_id=rand_int, has_dorm=False, education_type='azad', grade='fogh lisans', major='Math', sub_major='Sanayee')
c_student_3 = CollegeStudent(fname='Cherish  ', lname='Pearson', student_id=rand_int, has_dorm=False, education_type='roozane', grade='PHD', major='Math', sub_major='Software Engineering')
c_student_4 = CollegeStudent(fname='Ismael  ', lname='Chang', student_id=rand_int, has_dorm=True, education_type='pardis khod gardan', grade='fogh doktora', major='tajrobi', sub_major='Medicine')
#
e_teacher_1 = Teacher(fname='Mattie ', lname='Wilson', salary_per_day=6, working_days=4)
e_teacher_2 = Teacher(fname='Jocelyn  ', lname='Grimes', salary_per_day=10, working_days=1)
e_teacher_3 = Teacher(fname='Danny  ', lname='Macdonald', salary_per_day=3, working_days=5)
#
e_classroom_1 = ClassRoom(name='Poetry Palace', students=[e_student_1, e_student_3], teacher=e_teacher_1, code=1)
e_classroom_2 = ClassRoom(name='Imaginarium Inn', students=[e_student_1, e_teacher_2], teacher=e_teacher_2, code=2)
e_classroom_3 = ClassRoom(name='Calculus Cove', students=[e_student_1, e_student_4, e_student_3], teacher=e_teacher_3, code=3)
#
fh_teacher_1 = Teacher(fname='Nash ', lname='Weiss', salary_per_day=8 , working_days=3)
fh_teacher_2 = Teacher(fname='Hudson ', lname='Frank', salary_per_day=12 , working_days=4)
fh_teacher_3 = Teacher(fname='Mohammad ', lname='Eaton', salary_per_day=1 , working_days=5)
#
fh_classroom_1 = ClassRoom(name='Philosophy Forum', students=[sh_student_1, sh_student_3], teacher=fh_teacher_1, code=4)
fh_classroom_2 = ClassRoom(name="Societal Scholars’ Sanctuary", students=[sh_student_1, sh_student_2], teacher=fh_teacher_2, code=5)
fh_classroom_3 = ClassRoom(name='Anthropology Alcove', students=[sh_student_1, sh_student_3, sh_student_4], teacher=fh_teacher_3, code=6)
#
sh_teacher_1 = Teacher(fname='Edwin ', lname='Santana', salary_per_day=20 , working_days=4)
sh_teacher_2 = Teacher(fname='Chanel ', lname='Porter', salary_per_day=5, working_days=3)
sh_teacher_3 = Teacher(fname='Hailey ', lname='Leon', salary_per_day=2 , working_days=2)
#
sh_classroom_1 = ClassRoom(name="Dreamers’ Destiny", students=[sh_student_1, sh_student_3], teacher=sh_teacher_1, code=7)
sh_classroom_2 = ClassRoom(name='Positivity Palace', students=[sh_student_1, sh_student_2], teacher=sh_teacher_2, code=8)
sh_classroom_3 = ClassRoom(name='Visionary Ville', students=[sh_student_1, sh_student_3, sh_student_4], teacher=sh_teacher_3, code=9)
#
c_master_1 = Teacher(fname='Angel ', lname='Rich', salary_per_day=15 , working_days=3)
c_master_2 = Teacher(fname='Zain ', lname='Stevens', salary_per_day=25 , working_days=2)
c_master_3 = Teacher(fname='Mateo ', lname='Hardin', salary_per_day=10 , working_days=1)
#
c_classroom_1 = ClassRoom(name='Success Summit', students=[c_student_1, c_student_3], teacher=c_master_1 , code=10)
c_classroom_2 = ClassRoom(name='Creative Comedy Corner', students=[c_student_1, c_student_2], teacher=c_master_2 , code=11)
c_classroom_3 = ClassRoom(name='Adventure Awaits Arena', students=[c_student_1, c_student_3, c_student_4], teacher=c_master_3 , code=12)
#
elementary_1 = Elementary(class_rooms=[e_classroom_1, e_classroom_2, e_classroom_3], students=[e_student_1, e_student_2, e_student_3, e_student_4], teachers=[e_teacher_1, e_teacher_2, e_teacher_3], grade=[1, 2, 3, 4, 5, 6])
first_high_1 = FirstHigh(class_rooms=[fh_classroom_1, fh_classroom_2, fh_classroom_3], students=[sh_student_1, sh_student_2, sh_student_3, sh_student_4], teachers=[fh_teacher_1, fh_teacher_2, fh_teacher_3], grade=[7, 8, 9])
second_high_1 = SecondHigh(class_rooms=[sh_classroom_1, sh_classroom_2, sh_classroom_3], students=[sh_student_1, sh_student_2, sh_student_3, sh_student_4], teachers=[sh_teacher_1, sh_teacher_2, sh_teacher_3], grade=[10, 11, 12], major=['math', 'tajrobi', 'ensani'])
college_1 = College(major=['math', 'tajrobi', 'ensani'], sub_majors=['Electric', 'Software Engineering', 'Sanayee'], students=[c_student_1, c_student_2, c_student_3, c_student_4], masters=[c_master_1, c_master_2, c_master_3], class_rooms=[c_classroom_1, c_classroom_2, c_classroom_3], grade=['lisans', 'fogh lisans', 'PHD', 'dogh doktora'] ,semester=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],)

if __name__ == '__main__':
    print('school_1', school_1)
    print('school_1.name', school_1.name)
    # print('school_1.grades', school_1.grades)
    print('school_1.gender', school_1.gender)
    print('school_1.year_of_foundation', school_1.year_of_foundation)
    print('school_1.school_type', school_1.school_type)
    print('school_1.education_state', school_1.education_level)
    print(('---------------------------------------'))
    # print('grade_1th.grade', grade_1th.grade)
    # print('grade_1th.classrooms', grade_1th.classrooms)
    # print('grade_2th.grade', grade_2th.grade)
    # print('grade_2th.classrooms', grade_2th.classrooms)
    # print('grade_3th.grade', grade_3th.grade)
    # print('grade_3th.classrooms', grade_3th.classrooms)
    # print(('---------------------------------------'))
    print('class_room_1 ', class_room_1)
    print('class_room_1.name ', class_room_1.name)
    print('class_room_1.code ', class_room_1.code)
    print('class_room_1.students ', class_room_1.students)
    print('class_room_1.teacher ', class_room_1.teacher)
    print(('---------------------------------------'))
    print('class_room_2', class_room_2)
    print('class_room_2.name', class_room_2.name)
    print('class_room_2.code', class_room_2.code)
    print('class_room_2.students', class_room_2.students)
    print('class_room_2.teacher', class_room_2.teacher)
    print(('---------------------------------------'))
    print('class_room_3', class_room_3)
    print('class_room_3.name', class_room_3.name)
    print('class_room_3.code', class_room_3.code)
    print('class_room_3.students', class_room_3.students)
    print('class_room_3.teacher', class_room_3.teacher)
    print(('---------------------------------------'))
    print('class_room_4', class_room_4)
    print('class_room_4.name', class_room_4.name)
    print('class_room_4.code', class_room_4.code)
    print('class_room_4.students', class_room_4.students)
    print('class_room_4.teacher', class_room_4.teacher)
    print(('---------------------------------------'))
    print('class_room_5', class_room_5)
    print('class_room_5.name', class_room_5.name)
    print('class_room_5.code', class_room_5.code)
    print('class_room_5.students', class_room_5.students)
    print('class_room_5.teacher', class_room_5.teacher)
    print(('---------------------------------------')) 
    print('class_room_1.teacher.weekly_salary', class_room_1.teacher.weekly_salary)
    print('class_room_2.teacher.weekly_salary', class_room_2.teacher.weekly_salary)
    print('class_room_3.teacher.weekly_salary', class_room_3.teacher.weekly_salary)
    print('class_room_4.teacher.weekly_salary', class_room_4.teacher.weekly_salary)
    print('class_room_5.teacher.weekly_salary', class_room_5.teacher.weekly_salary)
    print('---------------------------------------')
    snacks = [pizza, water, soda, ice_cream]
    for item in snacks:
        print('snack.name', item.name)
        print('snack.cost', item.cost)
        print()
    print('---------------------------------------')
    print('shopkeeper_1', shopkeeper_1)
    print('shopkeeper_2', shopkeeper_2)
    print('---------------------------------------')
    print('vending_machine_1.shopkeeper', vending_machine_1.shopkeeper)
    print('vending_machine_1.snacks', vending_machine_1.snacks)
    print('---------------------------------------')
    print('shop.shopkeeper', shop_1.shopkeeper)
    print('shop.snacks', shop_1.snacks)
    print('---------------------------------------')
    print()
    print('######## detailed classing system : ########')  
    print('elementary_1.grade', elementary_1.grade)
    print('elementary_1.class_rooms', elementary_1.class_rooms)
    print('elementary_1.students', elementary_1.students)
    print('elementary_1.teachers', elementary_1.teachers)
    print('---------------------------------------')
    print('first_high_1.grade', first_high_1.grade)
    print('first_high_1.class_rooms', first_high_1.class_rooms)
    print('first_high_1.students', first_high_1.students)
    print('first_high_1.teachers', first_high_1.teachers)
    print('---------------------------------------')
    print('second_high_1.grade', second_high_1.grade)
    print('second_high_1.class_rooms', second_high_1.class_rooms)
    print('second_high_1.students', second_high_1.students)
    print('second_high_1.teachers', second_high_1.teachers)
    print('second_high_1.major', second_high_1.major)
    print('---------------------------------------')
    print('college_1.semester', college_1.semester)
    print('college_1.grade', college_1.grade)
    print('college_1.class_rooms', college_1.class_rooms)
    print('college_1.students', college_1.students)
    print('college_1.masters', college_1.masters)
    print('college_1.major', college_1.major)
    print('college_1.sub_majors', college_1.sub_majors)
    print('---------------------------------------')
    for e_student in elementary_1.students:
        print('e_student.fname ', e_student.fname)
        print('e_student.lname ', e_student.lname)
        print('e_student.has_school_bus ', e_student.has_school_bus)
        print('e_student.grade ', e_student.grade)
        print('----------------------')
    print('---------------------------------------')
    for fh_student in first_high_1.students:
        print('fh_student.fname ', fh_student.fname)
        print('fh_student.lname ', fh_student.lname)
        print('fh_student.has_school_bus ', fh_student.has_school_bus)
        print('fh_student.grade ', fh_student.grade)
        print('----------------------')
    print('---------------------------------------')
    for sh_student in second_high_1.students:
        print('sh_student.fname ', sh_student.fname)
        print('sh_student.lname ', sh_student.lname)
        print('sh_student.has_school_bus ', sh_student.has_school_bus)
        print('sh_student.grade ', sh_student.grade)
        print('sh_student.major ', sh_student.major)
        print('----------------------')
    print('---------------------------------------')
    for c_student in college_1.students:
        print('c_student.fname ', c_student.fname)
        print('c_student.lname ', c_student.lname)
        print('c_student.has_school_bus ', c_student.student_id)
        print('c_student.grade ', c_student.grade)
        print('c_student.major ', c_student.major)
        print('c_student.sub_major ', c_student.sub_major)
        print('c_student.has_dorm ', c_student.has_dorm)
        print('c_student.education_type ', c_student.education_type)
        print('----------------------')
    print('---------------------------------------')
    for e_classroom in elementary_1.class_rooms:
        print('e_classroom.name ', e_classroom.name)
        print('e_classroom.students ', e_classroom.students)
        print('e_classroom.teacher ', e_classroom.teacher)
        print('e_classroom.code ', e_classroom.code)
        print('----------------------')
    print('---------------------------------------')
    for fh_classroom in first_high_1.class_rooms:
        print('fh_classroom.name ', fh_classroom.name)
        print('fh_classroom.students ', fh_classroom.students)
        print('fh_classroom.teacher ', fh_classroom.teacher)
        print('fh_classroom.code ', fh_classroom.code)
        print('----------------------')
    print('---------------------------------------')
    for sh_classroom in second_high_1.class_rooms:
        print('sh_classroom.name ', sh_classroom.name)
        print('sh_classroom.students ', sh_classroom.students)
        print('sh_classroom.teacher ', sh_classroom.teacher)
        print('sh_classroom.code ', sh_classroom.code)
        print('----------------------')
    print('---------------------------------------')
    for c_classroom in college_1.class_rooms:
        print('c_classroom.name ', c_classroom.name)
        print('c_classroom.students ', c_classroom.students)
        print('c_classroom.teacher ', c_classroom.teacher)
        print('c_classroom.code ', c_classroom.code)
        print('----------------------')
    print('---------------------------------------')