https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

"""
Given a square matrix, turn it by 90 degrees in anti-clockwise direction 
without using any extra space.

Examples :

Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9 
 2  5  8 
 1  4  7 
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#extra space
def RotateMatrix(matrix:'List[List[]]')->None:
    rotated = list(zip(*matrix))[::-1]
    return rotated

#in-place
def RotateMatrix(matrix: 'List[List[]]')->None:
    N = len(matrix)
    for i in range(0, N // 2):
        for j in range(i, N - i - 1):
            temp = matrix[i][j]

            #move right to left
            matrix[i][j] = matrix[j][N - i - 1]

            #move bottom to right up
            matrix[j][N - i - 1] = matrix[N - i - 1][N - j - 1]

            #move left bottom to right bottom
            matrix[N - i - 1][N - j - 1] = matrix[N - j - 1][i]

            matrix[N - j - 1][i] = temp
    print(matrix)

rotated = RotateMatrix(matrix)
print(rotated)