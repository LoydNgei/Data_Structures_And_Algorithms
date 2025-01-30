# Loyd
# 25 yrs - 2024

# return year( 20..)

# 75 years away

# 2124


from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = date.today().year
target_age = 100
# print(current_year)

yearsTo_target = (current_year + target_age) - age

print(name + " you will be 100 years old in " + str(yearsTo_target))



