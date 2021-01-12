https://www.geeksforgeeks.org/quickselect-algorithm/

# quick select 
# O(n)
#find Kth smallest number in the unsorted array 

arr = [10, 50, 20, 30]
k = 2 

def partition(arr, left, right):
    if left == right:   return left 
    pivot = arr[right]     
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i 


def quick_select(arr, left, right, k):
    print("->", arr[left: right + 1], k)
    index = partition(arr, left, right)
    if (k > 0 and k <= right - left + 1): 
        if index == k - 1:
            return arr[index]
        if index - left > k - 1:
            return quick_select(arr, left, index - 1, k)
        else:
            return quick_select(arr, index + 1, right, k - (index - left + 1))
            

ans = quick_select(arr, 0, len(arr) - 1, k)
print(ans)

"""
arr = [10, 50, 20, 30]
k = 4 => ans = 50 
0   1       2   3
[10, 20], [30, 50]

"""