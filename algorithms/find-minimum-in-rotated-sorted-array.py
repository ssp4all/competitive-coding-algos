def findMin(nums):
    l = 0
    n = len(nums)
    r = n - 1
    while l < r:
        if nums[l] < num[r]:
            return num[l]
        m = (l + r) // 2
        if num[m] >= num[l]:
            l = m + 1
        else:
            r = m
    return num[l]
