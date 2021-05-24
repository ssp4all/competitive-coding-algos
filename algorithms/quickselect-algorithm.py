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