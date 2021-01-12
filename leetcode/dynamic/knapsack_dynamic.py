def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W+1)] for x in range(n+1)] 
	# print(K)
	for i in range(n+1): 
		for w in range(W+1): 
			# print(wt[i-1])
			if i==0 or w==0: 
				K[i][w] = 0
			
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 
	print(K)

	return K[n][W] 

def ks(w, wt, val, n):
    k = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif j >= wt[i - 1]:
                k[i][j] = max(val[i - 1] + k[i - 1][w - wt[i - 1]],
                              k[i - 1][j])
            else:
                k[i][j] = k[i - 1][j]
    return k[n][w]
	# return 
				

w = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = 3
x = ks(w, wt, val, n)
print(x)

# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) 