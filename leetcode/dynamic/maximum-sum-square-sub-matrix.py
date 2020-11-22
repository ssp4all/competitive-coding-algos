#https://www.geeksforgeeks.org/print-maximum-sum-square-sub-matrix-of-given-size/

"""
Given an N x N matrix, find a k x k submatrix where k <= N and k >= 1, 
such that sum of all the elements in submatrix is maximum. 
The input matrix can contain zero, positive and negative numbers.

For example consider below matrix, if k = 3, then output 
should print the sub-matrix enclosed in blue.
"""

def MaxSumSubMatix(matrix, k):
    n = len(matrix)
    preprocess = [[0] * n for _ in range(n)]


    for j in range(n): #col
        sum = 0 
        #calculate for first k rows
        for i in range(k): #row
            sum += matrix[i][j]
        preprocess[0][j] = sum

        #calc for remain. row 
        for i in range(1, n - k + 1):
            sum += matrix[i + k - 1][j] - matrix[i - 1][j]
            preprocess[i][j] = sum
    
    print(preprocess) #done preprocess matrix 

    maxi = 0
    start, end = -1, -1 

    for i in range(n - k + 1): #row wise
        sum = 0
        for j in range(k):
            sum += preprocess[i][j] 
        
        if sum > maxi:
            maxi = sum
            start, end = i, j
        
        #repeat for next columns 
        for j in range(1, n - k + 1):
            sum += preprocess[i][j + k - 1] - preprocess[i][j - 1]
            if sum > maxi:
                maxi = sum 
                start, end = i, j

    print(start, end)
            



matrix = [[ 1, 1, 1, 1, 1 ],  
                [ 2, 2, 2, 2, 2 ],  
                [ 3, 8, 6, 7, 3 ],  
                [ 4, 4, 4, 4, 4 ], 
            [ 5, 5, 5, 5, 5 ]]

MaxSumSubMatix(matrix, 3)
