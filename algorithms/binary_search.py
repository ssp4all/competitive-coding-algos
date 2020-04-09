
def bsearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left if arr[left] == target else -1
    # x = float('inf')


a = list(range(10))
x = bsearch(a, 4)
print(x)

""" Gives left start """
def bsearch(arr, tar):
    l, r = 0, len(arr)
    while l < r:
        m = l + (r - l) // 2
        if arr[m] < tar:
            l = m + 1
        else:
            r = m
    return l
ip = ["a", "b", "e", "f"]
x = bsearch(ip, "c")
print(x)

""" Gives right start """
def bsearch(arr, tar):
    l, r = 0, len(arr)
    while l < r:
        m = l + (r - l) // 2
        if arr[m] > tar:
            r = m - 1
        else:
            l = m 
    return l