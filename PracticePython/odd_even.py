# User: number
# even = remainder 0 (%) 74 % 2 == 0 -> This number is even. (0 & Negative) -> You can't have zero or negative
# odd = else condition


number = int(input("Enter a number: "))

if (number % 2 == 0):
    print(number, "is an even number")
else:
    print(number, "is an odd number")