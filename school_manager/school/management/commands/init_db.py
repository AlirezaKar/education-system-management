from tqdm import tqdm
from random import choice, choices, randint
from faker import Faker
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from school.models import (
    EducationOrganization,
    Elementary,
    FirstHigh,
    HighStudent,
    SecondHigh, 
    College,
    Student,
    CollegeStudent,
    Teacher,
    Master,
    ClassRoom,
    Snack,
    Shop,
    VendingMachine
)


fake=Faker()
PASSWORD = 'asdf@1234'
User = get_user_model()
MAJOR = ['Riazi', 'Ensani', 'tajrobi']
SUB_MAJOR = ['bargh', 'Software Engineering', 'mohandesi polimer', 'Computer Science']
COLLEGE_GRADE = ['lisans', 'fogh lisans', 'doktora', 'fogh doktora']
EDUCATION_TYPE = ['shabane', 'roozane', 'pardis khod gardan']


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        EducationOrganization.objects.all().delete()
        Elementary.objects.all().delete()
        FirstHigh.objects.all().delete()
        SecondHigh.objects.all().delete()
        College.objects.all().delete()
        Student.objects.all().delete()
        HighStudent.objects.all().delete()
        CollegeStudent.objects.all().delete()
        Teacher.objects.all().delete()
        Master.objects.all().delete()
        ClassRoom.objects.all().delete()
        Snack.objects.all().delete()
        Shop.objects.all().delete()
        VendingMachine.objects.all().delete()

        User.objects.create_superuser(username='admin', password=PASSWORD)

        users = []
        for i in tqdm(range(1, 6), 'Creating users'):
            user = User.objects.create_user(
                username=f'user{i}',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password=PASSWORD
            )
            users.append(user)

        teachers = []
        for i in tqdm(range(1, 6), 'Creating Teachers'):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                salary_per_day=randint(1, 50),
                working_days=randint(1, 6)
            )
            teachers.append(teacher)

        masters = []
        for i in tqdm(range(1, 6), 'Creating Masters'):
            master = Master.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                salary_per_day=randint(1, 50),
                working_days=randint(1, 5)
            )
            masters.append(master)

        students = []
        for i in tqdm(range(1, 11), 'Creating Students'):
            student = Student.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                has_school_bus=choice([True, False]),
                grade=randint(1, 9),
            )
            students.append(student)

        high_students = []
        for i in tqdm(range(1, 11), 'Creating HighStudents'):
            high_student = HighStudent.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                has_school_bus=choice([True, False]),
                grade=randint(10, 12),
                major=choice(MAJOR)
            )
            high_students.append(high_student)

        college_studens = []
        for i in tqdm(range(1, 11), 'Creating CollegeStudents'):
            college_student = CollegeStudent.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                student_id=randint(10000000, 99999999),
                has_dorm=choice([True, False]),
                grade=choice(COLLEGE_GRADE),
                education_type=choice(EDUCATION_TYPE),
                major=choice(MAJOR),
                sub_major=choice(SUB_MAJOR),
            )
            college_studens.append(college_student)

        class_rooms = []
        for i in tqdm(range(1, 16), 'Creating ClassRooms'):
            class_room = ClassRoom(
                name = fake.name(),
            )
            class_room.save()
            class_room.students.add(choice(students))
            class_room.teacher.add(choice(teachers))
            class_room.save()
            class_rooms.append(class_room)

        elementaries = []
        for i in tqdm(range(1, 7), 'Creating Elementy'):
            elementary = Elementary(
                grade = randint(1, 6)
            )
            elementary.save()
            elementary.class_room.add(choice(class_rooms))
            elementary.students.add(choice(students))
            elementary.teachers.add(choice(teachers))
            elementary.save()
            elementaries.append(elementary)

        first_highs = []
        for i in tqdm(range(1, 6), 'Creating FirstHigh'):
            first_high = FirstHigh(
                grade=randint(7, 10)
            )
            first_high.save()
            first_high.class_room.add(choice(class_rooms))
            first_high.students.add(choice(students))
            first_high.teachers.add(choice(teachers))
            first_high.save()
            first_highs.append(first_high)

        second_highs = []
        for i in tqdm(range(1, 6), 'Creating SecondHigh'):
            second_high = SecondHigh(
                grade=randint(10, 13),
                major=choices(MAJOR)
            )
            second_high.save()
            second_high.class_room.add(choice(class_rooms))
            second_high.students.add(choice(students))
            second_high.teachers.add(choice(teachers))
            second_high.save()
            second_highs.append(second_high)

        colleges = []
        for i in tqdm(range(1, 6), 'Creating Colleges'):
            college = College(
                semester=randint(1,10),
                grade=choices(COLLEGE_GRADE),
                major=choices(MAJOR),
                sub_major=choices(SUB_MAJOR),
            )
            college.save()
            college.class_rooms.add(choice(class_rooms))    # FIXME: I want to have choices (a list . but error!)
            college.students.add(choice(students))
            college.masters.add(choice(masters))
            college.save()
            colleges.append(college)

        snacks = []
        for i in tqdm(range(1, 9), "Creating Snacks"):
            snack = Snack.objects.create(
                name=fake.name(),
                cost=randint(1, 21)
            )
            snacks.append(snack)

        # shops = []
        # for i in tqdm(range(1, 6), 'Creating Shops'):
        #     shop = Shop(
                
        #     )
        #     shop.save()
        #     shop.shopkeeper.add()
        #     shop.snacks.add(snacks)
        #     shop.save()
        #     shops.append(shop)
            
        # vending_machines = []
        # for i in tqdm(range(1, 6), 'Creating VendingMachine'):
        #     vending_machine = VendingMachine.objects.create(
        #         shopkeeper=choice(User),
        #         snacks=choices(snacks)
        #     )
        #     vending_machines.append(vending_machine)

        education_organizations = []
        for i in tqdm(range(1, 6), 'Creating EducationOrganization'):
            education_organization = EducationOrganization.objects.create(
                name = fake.name(),
                description = fake.text(),
                gender = choice(['Boys Only', 'Girls Only', 'Mixed']),
                year_of_foundation = fake.date_between(start_date='-30y', end_date='today'),
                school_type = choice(['Private', 'Public', 'SAMPAD', 'Heyat omanayee']),
                education_level = choices(['Elementary', 'Junior High', 'Senior High', 'College'])
            )
            education_organizations.append(education_organization)