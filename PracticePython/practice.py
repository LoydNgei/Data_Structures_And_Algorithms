from datetime import date

name = input("Enter your name: ")
age = input("Enter your age: ")

current_year = date.today().year
target_age = 100


yearsTo_target = (current_year + target_age) - age

print(name + "you will be 100 years old in " + str(yearsTo_target))


number = int(input("Enter a number: "))

if (number % 2 == 0):
    print(number, 'is an even number')
else:
    print(number, 'is an odd number')