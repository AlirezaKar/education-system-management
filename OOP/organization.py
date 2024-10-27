
class EducationOrganization:
    __slot__ = ['name', 'gender', 'year_of_foundation', 'school_type', 'education_level']
    def __init__(self, name, gender, year_of_foundation, school_type, education_level):
        self.name = name
        # self.grades = grades     
        self.gender = gender   # boys only / girls only / mixed   * can be only one
        self.year_of_foundation = year_of_foundation
        self.school_type = school_type  # private  / public / SAMPAD / heyat omanayee /    *TODO: can be only one
        self.education_level = education_level  # elementary / high school 1 /high school 2 / college   *TODO: can have many

        
        # self.__bank = bank   # baraye shahriye
        # description   

    def __repr__(self):
        return self.name
        
    
class Snack:
    __slot__ = ['name', 'cost']
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return self.name

class Shop:
    __slot__ = ['shopkeeper', 'cost']
    def __init__(self, shopkeeper, snacks):
        self.shopkeeper = shopkeeper
        self.snacks = snacks

    def __repr__(self):
        return self.shopkeeper

class VendingMachine:
    __slot__ = ['shopkeeper', 'cost']
    def __init__(self, shopkeeper, snacks):
        self.shopkeeper = shopkeeper
        self.snacks = snacks

    def __repr__(self):
        return self.shopkeeper