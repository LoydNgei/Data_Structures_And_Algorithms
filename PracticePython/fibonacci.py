# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.


# def fibonnaci(n):
#     if n <= 0:
#         print("Please enter a positive int")
#         return
#     a, b = 1, 1

#     for _ in range(n):
#         print(a, end=",")
#         a, b = b, a + b

    
# num = int(input("How many Fibonacci numbers do you want to generate? "))

# fibonnaci(num)



def fib_num(n):

    if n <= 0:
        print("Enter a positive integer")
        return

    # The first 2 fibonacci numbers
    a, b = 1, 1 


    for _ in range(n):
        print(a, end=", ")
        a, b = b, a + b


num = int(input("How many fibonacci numbers do you want? "))

fib_num(num)
