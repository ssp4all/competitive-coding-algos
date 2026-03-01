https://www.geeksforgeeks.org/quickselect-algorithm/

# quick select 
# O(n) Avg case but O(n^2) for worst case
#find Kth smallest number in the unsorted array 

arr = [10, 50, 20, 30]
k = 2 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, arr, left, right, k_index):
        if left == right:
            return arr[left]
        # Partition and get pivot position
        pivot_index = self.partition(arr, left, right)
        # If pivot is at the target position, we found the answer
        if k_index == pivot_index:
            return arr[k_index]
        # If target is on the left side, search left
        elif k_index < pivot_index:
            return self.quickSelect(arr, left, pivot_index - 1, k_index)
        # If target is on the right side, search right
        else:
            return self.quickSelect(arr, pivot_index + 1, right, k_index)

    def partition(self, arr, left, right):
        pivot = arr[right]
        i = left
        # Move all elements smaller than pivot to the left
        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # Place pivot in its correct position
        arr[i], arr[right] = arr[right], arr[i]
        return i


"""
arr = [10, 50, 20, 30]
k = 4 => ans = 50 
0   1       2   3
[10, 20], [30, 50]

"""
