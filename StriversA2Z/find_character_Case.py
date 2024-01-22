# Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.



# 1, if the character is an uppercase alphabet (A - Z).
# 0, if the character is a lowercase alphabet (a - z).
# -1, if the character is not an alphabet.


x = input("The character is: ");

if x.isupper():
    result = 1
elif x.islower():
    result = 0
else:
    result = -1

print(result);