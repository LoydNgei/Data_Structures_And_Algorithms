# Create a program that asks the user for a number and then prints out a list of all the divisors of that number

number = int(input('Enter a number: '))

newlist = []

for x in range(1, number+1):
    if number % x == 0:
        newlist.append(x)

print(newlist)




