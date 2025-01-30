# write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []

for i in a:
    if i in b and i not in common:
        common.append(i)
print(common)



# Using a function now

def append_two_lists(list1, list2):

    common_list = []

    for item in list1:
        if item in list2:
            common_list.append(item)
    return common_list


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = append_two_lists(a, b)
print(result)