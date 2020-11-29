https://brilliant.org/wiki/median-finding-algorithm

def median_of_medians(A, i):
    print(A)
    #divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        #the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)//2)

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high,i-k-1)
    else: #pivot = k
        return pivot
        
A = [1,2,3,4,5,1000,8,9,99]
x = median_of_medians(A, len(A)//2)
print(x)
actual = sorted(A)[len(A)//2]
print(actual)