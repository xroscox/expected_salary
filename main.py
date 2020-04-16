import UserProfile

from datetime import datetime

valid_states = ("FL", "NY", "CA", "TX", "NC")

expected_salaries = {"NY": 70000, "CA": 70000, "FL": 50000, "NC": 50000, "TX": 60000}


def calculate_expected_salary(number_of_experience_years, user_information, number_of_edu_years):
    try:

        expected_salary = expected_salaries[user_information["state"].upper()]
        number_of_education_years = int(number_of_edu_years)

    except KeyError:
        print("****************  Please enter valid State using two letters  ****************")
    except ValueError:
        print("****************  Please enter a valid number for years of learning experience  ****************")

    else:  # this else only gets executed if the exception is not raised/called

        new_expected_salary = 0

        if number_of_experience_years == 1:
            new_expected_salary = expected_salary - 5000  # Deduct $5K due to users 1 year of experience
        elif number_of_experience_years == 2:
            new_expected_salary = expected_salary - 3000  # Deduct $3K due to users 2 years of experience
        elif number_of_experience_years == 3:
            new_expected_salary = expected_salary + 1000  # Add $1K due to users 3 years of experience
        elif number_of_experience_years == 4:
            new_expected_salary = expected_salary + 5000  # Add $5K due to users 4+ years of experience
        else:
            print(5 * "*" + " Sorry, please enter a choice between 1 - 4 " + 5 * "*")

        if len(users_coding_languages) < 3:
            new_expected_salary = new_expected_salary - 10000  # 65,000 - 10,000 = 55,000
            print("Learn some more languages; deduct $10K from the expected salary.")
        elif len(users_coding_languages) > 3:
            new_expected_salary = new_expected_salary + 10000
        else:
            new_expected_salary = new_expected_salary + 5000

        if number_of_education_years > 3:
            new_expected_salary = new_expected_salary + 10000
        else:
            new_expected_salary = new_expected_salary - 5000

        print("Expect $" + str(new_expected_salary) + " for your level of experience")

        for state in expected_salaries:
            salary = expected_salaries[state]
            print("You're starting Salary living in " + state + " could have been $" + str(salary) + ".")


create_a_candidate = True
while create_a_candidate:
    try:

        users_experience = input("How many years experience do you have developing software?\n[1] Less than 1 year"
                         " \n[2] 1 - 3 years of experience \n[3] 3 - 8 years of experience \n[4] "
                         "8+ years of experience \n")

        users_experience = int(users_experience)

        users_coding_languages = input("What languages do you know? (separate each language with a comma)")

        if users_coding_languages == '':
            raise ValueError

        users_coding_languages = users_coding_languages.split(",")

        dob = input("Please enter your Date of Birth (MM/DD/YYYY): \n")

        full_name = input("Please enter your Full Name: \n")

        age = input("Please enter your age: \n")

        country = input("Please enter the country you reside in: \n")

        for state in valid_states:
            print(state)

        state = input("Choose your State (use the two letter abbreviation): \n Choose one of the following:")
        if len(state) > 2:
            raise ValueError

        number_of_education_years = input("Please enter number of years you have been coding: \n")

        is_active = True

        user_info = {
                     "dob": dob, "full_name": full_name, "country": country, "state": state, "is_active": is_active,
                     "numbers_of_education_years": number_of_education_years, "age": int(age)
                }

        # Instatiation an Object aka Create a new instance of the Class
        user_profile = UserProfile.UserProfile(dob, full_name, country, state, number_of_education_years, age)
        # instead of user_profile, call for type of user: Designer or Developer

        user_password = user_profile.get_password() # this will be bad_password
        print("Your Initial Password was", user_password)

        new_password = input("Enter a new password \n")

        user_profile.set_password(new_password)

        user_password = user_profile.get_password()

        print("Your new password is", user_password)

        user_id = user_profile.create_unique_id()
        print("Your confirmation ID is", user_id)

        calculate_expected_salary(users_experience, user_info, number_of_education_years)

        another_candidate = input("Would you like to create another candidate? Y/N \n")

        if another_candidate == "Y":
            create_a_candidate = True
        else:
            create_a_candidate = False
            # break - this would be another way to get out of the loop

    except ValueError:
        print("Please enter all valid values")

print("Thank you for sharing this information. We will be in touch")