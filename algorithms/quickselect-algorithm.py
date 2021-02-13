https://www.geeksforgeeks.org/quickselect-algorithm/

# quick select 
# O(n) Avg case but O(n^2) for worst case
#find Kth smallest number in the unsorted array 

arr = [10, 50, 20, 30]
k = 2 

def partition(nums, l, r):
    pivot = nums[r]
    j = l
    for i in range(l, r):
        if nums[i] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    nums[j], nums[r] = nums[r], nums[j]
    return j

def quick_select(nums, l, r, k):
    if l > r or k - 1 > r - l:  return 
    pivot = partition(nums, l, r)
    if pivot - l == k - 1:
        return nums[pivot]
    if k - 1 < pivot - l:
        return quick_select(nums, l, pivot - 1, k)
    else:
        return quick_select(nums, pivot + 1, r, k - (pivot - l + 1))

return quick_select(nums, 0, len(nums) - 1, len(nums) - k + 1)

"""
arr = [10, 50, 20, 30]
k = 4 => ans = 50 
0   1       2   3
[10, 20], [30, 50]

"""

# With extra space but easy to code
def partition(A):
    n = len(A)
    pivot = A[n - 1]
    j = 0 
    for i in range(n - 1):
        if A[i] < pivot:
            A[j], A[i] = A[i], A[j]
            j += 1
        i += 1 
    A[j], A[n - 1] = A[n - 1], A[j]
    return j 

def quick_select(A, k):
    if not A or k >= len(A):   return
    pivot = partition(A)
    if k == pivot:
        return A[k]
    elif k < pivot:
        return quick_select(A[:pivot], k)
    return quick_select(A[pivot + 1:], k - pivot - 1)
    
A = [1,2,3,4,5,99,8,1000, 7]
k = 3
idx = quick_select(A, k - 1)
print(idx)