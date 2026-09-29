name=input("Enter your name: ")
age=int(input("Enter your age: "))
major=input("Enter your major: ")
city=input("Enter your city: ")
email=input("Enter your email: ")
number=int(input("Enter your phone number: "))
def age_group(age):
    if age <18 :
        return "You are a minor"
    elif age >=18 and age <65:
        return "You are an adult"
    else:
        return "You are a senior citizen"
def display_info(name, age, major, city, email, number):
    print("Name:", name)
    print("Age:", age)
    print("Major:", major)
    print("City:", city)
    print("Email:", email)
    print("Phone Number:", number)
    print(age_group(age))
birth_year=int(input("Enter your birth year: "))
def calculate_age(birth_year):
    current_year=2027
    age_birth=current_year - birth_year
    return age_birth
print("Your age is:", calculate_age(birth_year))
display_info(name, age, major, city, email, number)