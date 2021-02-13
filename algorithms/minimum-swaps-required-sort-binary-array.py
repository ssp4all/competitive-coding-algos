https://www.geeksforgeeks.org/minimum-swaps-required-sort-binary-array/

"""
Given a binary array, task is to sort this binary array using 
minimum swaps. We are allowed to swap only adjacent elements

Examples: 

Input : [0, 0, 1, 0, 1, 0, 1, 1]
Output : 3
"""

#optimized
def minswaps(arr):
	displacement = 0 #cost to move zeros to the right
	count_of_ones = 0

	for index in range(len(arr) - 1, -1, -1):
		if arr[index] == 1:
			count_of_ones += 1
		else:
			displacement += count_of_ones


		"""
		If asked to calculate cost to move zeroes to the right,
		then ->
		reverse_D = count_of_ones * count_of_zeroes - displacement_of_zeroes
		return min(displacement, reverse_D)
		"""
	return displacement


arr = [1,0,1,0,0,1]
print(minswaps(arr))
