import tkinter as tk
from tkinter import ttk
import requests
import json

url = "http://127.0.0.1:8000/student"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

organizations = json.loads(response.text)
organization = organizations['data']
students = json.loads(response.text)
students = students['data']
teachers = json.loads(response.text)
teachers = teachers['data']
masters = json.loads(response.text)
masters = masters['data']
class_rooms = json.loads(response.text)
class_rooms = class_rooms['data']
high_students = json.loads(response.text)
high_students = high_students['data']
college_students = json.loads(response.text)
college_students = college_students['data']
elementaries = json.loads(response.text)
elementaries = elementaries['data']
first_highs = json.loads(response.text)
first_highs = first_highs['data']
second_highs = json.loads(response.text)
second_highs = second_highs['data']
colleges = json.loads(response.text)
colleges= colleges['data']
snacks = json.loads(response.text)
snacks = snacks['data']
vending_machines = json.loads(response.text)
vending_machines = vending_machines['data']
shops = json.loads(response.text)
shops = shops['data']



# مدل‌های فرضی با داده‌های نمونه
# students = [
#     {"first_name": "Alice", "last_name": "Smith", "has_school_bus": True, "grade": "A"},
#     {"first_name": "Bob", "last_name": "Jones", "has_school_bus": False, "grade": "B"},
#     {"first_name": "Charlie", "last_name": "Brown", "has_school_bus": True, "grade": "A"},
# ]

# high_students = [
#     {"first_name": "Dave", "last_name": "Davis", "has_school_bus": False, "grade": "10", "major": "Science"},
#     {"first_name": "Eve", "last_name": "Evans", "has_school_bus": True, "grade": "11", "major": "Arts"},
# ]

# college_students = [
#     {"first_name": "Fay", "last_name": "Johnson", "student_id": 123, "has_dorm": True, "grade": "Sophomore", "education_type": "Full-Time", "major": "CS", "sub_major": "AI"},
# ]

# teachers = [
#     {"first_name": "Grace", "last_name": "Williams", "salary_per_day": 100, "working_days": 20},
# ]

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Model Browser")
root.geometry("500x500")
root.resizable = True, True

# تابع برای باز کردن پنجره جدید با قابلیت جستجو و فیلتر
def open_model_window(model_name, objects, fields):
    new_window = tk.Toplevel(root)
    new_window.title(f"{model_name} List")
    new_window.geometry("600x400")
    
    # فیلد جستجو
    search_label = tk.Label(new_window, text="Search:")
    search_label.pack(pady=5)
    
    search_entry = tk.Entry(new_window)
    search_entry.pack(pady=5)
    
    # جدول برای نمایش object‌ها
    tree = ttk.Treeview(new_window, columns=fields, show="headings")
    for field in fields:
        tree.heading(field, text=field)
    tree.pack(fill="both", expand=True)
    
    # تابع برای بروزرسانی لیست بر اساس جستجو و فیلتر
    def update_list():
        query = search_entry.get().lower()
        tree.delete(*tree.get_children())
        
        for obj in objects:
            values = [str(obj.get(field, "")) for field in fields]
            if any(query in value.lower() for value in values):
                tree.insert("", "end", values=values)
    
    # دکمه فیلتر
    filter_button = tk.Button(new_window, text="Filter", command=update_list)
    filter_button.pack(pady=5)
    
    # نمایش اولیه لیست
    update_list()

# تعریف مدل‌ها و فیلدها برای هر دکمه
models = [
    ("Student", students, ["first_name", "last_name", "grade"]),
    ("HighStudent", high_students, ["first_name", "last_name", "grade", "major"]),
    ("CollegeStudent", college_students, ["first_name", "last_name", "grade", "education_type", "major", "sub_major"]),
    ("Elementary", elementaries, ['grade', 'class_room', 'students', 'teachers']),
    ("FirstHigh", first_highs, ['grade', 'class_room', 'students', 'teachers']),
    ("SecondHigh", second_highs, ['grade', 'class_room', 'students', 'teachers']),
    ("College", colleges, ['semester', 'grade', 'class_rooms', 'students', 'masters', 'major', 'sub_major']),
    ("ClassRoom", class_rooms, ['name', 'students', 'teacher']),
    ("Snack", snacks, ['name', 'cost']),
    ("VendingMachine", vending_machines, ['shopkeeper', 'snacks']),
    ("Shop", shops, ['shopkeeper', 'snacks']),
    ("Teacher", teachers, ["first_name", "last_name"]),
    ("Master", masters, ["first_name", "last_name"]),
    ("EducationOrganization", organizations, ['name', 'gender', 'year_of_foundation', 'school_type', 'education_level']),
]

# ایجاد دکمه‌ها برای هر مدل
for i, (model_name, objects, fields) in enumerate(models):
    button = tk.Button(root, text=model_name, command=lambda m=model_name, o=objects, f=fields: open_model_window(m, o, f))
    button.grid(row=i//2, column=i%2, padx=10, pady=5)

# اجرای برنامه
root.mainloop()
