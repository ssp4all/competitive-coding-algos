def min_plat(arr, dep):
	dep.sort()
	arr.sort()
	n = len(arr)
	i, j, ans, plat = 1, 0, -1, 1
	while i < n and j < n:
		if arr[i] < dep[j]:
			plat += 1
			i += 1
			ans = max(ans, plat)
		else:
			plat -= 1
			j += 1
	return ans
	
arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000]
x = min_plat(arr, dep)
print(x)