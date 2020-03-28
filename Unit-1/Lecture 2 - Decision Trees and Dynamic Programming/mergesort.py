# code written while reading the book.

"""
Let’s analyze the complexity of mergeSort . We already know that the time
complexity of merge is O(len(L)) . At each level of recursion the total number of
elements to be merged is len(L) . Therefore, the time complexity of mergeSort is
O(len( L )) multiplied by the number of levels of recursion. Since mergeSort divides
the list in half each time, we know that the number of levels of recursion is
O(log(len( L )) . Therefore, the time complexity of mergeSort is O(n * log(n)) , where n
is len(L) .
"""

L = [2, 1, 4, 5, 3]


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def mergeSort(arr, compare=lambda x, y: x < y):
    # change x < y to x > y to sort in descending order
    if len(arr) < 2:
        return arr[:]
    else:
        mid = len(arr)//2
        left = mergeSort(arr[:mid], compare)
        right = mergeSort(arr[mid:], compare)
        return merge(left, right, compare)


print(mergeSort(L), mergeSort(L, lambda x, y: x > y))
