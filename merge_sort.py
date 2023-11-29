def merge_sort(list):

    """
    Sorts a list in ascending order
    Returns a new sorted list

    STEPS
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous steps
    Combine: Merge the sorted sublists created in previous steps


    tAKES 0 n(log n) time
    """


    if len(list) <= 1:
        return list

    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):

    """Divide the unsorted list at midpoint into sublists
    Returns two sublists (left and right)

    TAKES 0(log n) TIME
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):

    """
    Merges 2 lists(arrays), sorting them in the process
    Returns a new merged list

    Takes overrall 0(n) TIME
    """

    l= []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1

        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 63, 67, 34, 98, 22, 45, 29, 14]
l = merge_sort(alist)
print(l)
print(verify_sorted(alist))
print(verify_sorted(l))