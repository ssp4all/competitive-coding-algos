
def bsearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right if arr[right] == target else -1
    # x = float('inf')


a = list(range(10))
x = bsearch(a, 4)
print(x)
