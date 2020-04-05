#UserProfile.py

from datetime import datetime

# TODO:

"""
    Create a Subclass for Developer and subclass for Designer
    They both should inherit the UserProfile Class

"""

# TODO:

"""
    Add a variable/property to the Developer subclass: a list of languages

"""

# TODO:
"""
    Add a variable/property to the Designer subclass: a list of software programs
    e.g.) Adobe Illustrator, Adobe Photoshop, Canva, GIMP

"""

# TODO:

"""
    Ask the user (via imput) if this candidate is a designer or developer If a designer - ask for software programs If 
    a developer - ask what languages they know (we already have this code. But only ask it if the candidate is
    a developer)
    
    Based on if the user selected Designer or Developer, create the appropriate object
    for the candidate. So don't call the UserProfile directory from main.py
    
    In calculate_expected_salary function, we need to check if this is a designer or developer so we know if we should
    be counting languages or software programs

"""


class Product:
    def __init__(self):
        self.price = 0.0
        self.description = "some product"
        self.quantity_in_stock = 0
        self.brand = ""

    def get_how_many_left_in_stock(self):
        return self.quantity_in_stock


class CreditCard:
    def __init__(self, full_name, dob, address):
        pass


class CreditCard2:
    def __init__(self, user_profile):
        full_name = user_profile.full_name


class Post:
    def __init__(self, caption, image, user_profile, date_it_was_posted):
        self.number_of_likes = 0

    def update_likes(self):
        self.number_of_likes = self.number_of_likes + 1


class UserProfile:
    def __init__(self, dob, full_name, country, state, number_of_education_years, age):
        self.password = "bad_password"
        self.email = None
        self.is_active = True
        self.date_created = datetime.now()
        self.trial_expiration_date = datetime(2020, 10, 1)
        self.dob = dob
        self.full_name = full_name
        self.country = country
        self.state = state
        self.number_of_education_years = number_of_education_years
        self.age = age

    def get_age(self):
        return self.age

    def set_password(self, new_password):
        self.password = new_password

    def get_password(self):
        return self.password

    def create_unique_id(self):
        random_id = id(self.full_name)
        return random_id

    def get_name(self):
        return self.name


class Developer(UserProfile):
    pass


class Designer(UserProfile):
    pass