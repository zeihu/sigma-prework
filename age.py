from datetime import datetime


def agecalc(date):
    # converting string to datetime
    birthdate = datetime.strptime(date, "%d-%m-%Y")
    currentdate = datetime.today()

    # calculating age
    age = currentdate.year - birthdate.year

    # accounts for if birthday hasn't occurred yet
    if (currentdate.month, currentdate.day) < (birthdate.month, birthdate.day):
        age -= 1

    # returns final age
    return age


print("Age calculator!")
date = input("Please enter your date of birth (DD-MM-YYYY): ")
print(agecalc(date))
