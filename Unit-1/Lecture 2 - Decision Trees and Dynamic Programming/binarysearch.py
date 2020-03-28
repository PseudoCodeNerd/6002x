# code written while reading the book.

def search(arr, e):
    def binary(arr, e, low, high):
        if low == high:
            return arr[low] == e
        mid = (low+high)//2
        if arr[mid] == e:
            return True
        elif arr[mid] > e:
            # search on left side of mid value
            if low == mid:
                # nothing left to search on left side
                return False
            else:
                return binary(arr, e, low, mid - 1)
        else:
            # search on right side of mid value
            return binary(arr, e, mid + 1, high)
    if len(arr) == 0:
        return False
    else:
        return binary(arr, e, 0, len(arr) - 1)

L = [2, 1, 4, 5, 3]

print(search(L, 5)) # True
