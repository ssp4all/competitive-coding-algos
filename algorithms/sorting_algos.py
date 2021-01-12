class Solution:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0
    
    def merge(self, p, q, r):
        """Merge two arrays into one"""
        # n1 = q-p+1
        # n2 = r-q
        # left = [0]*n1
        # right = [0]*n2
        
        left = self.sorting_array[p:q+1]
        right = self.sorting_array[q+1:r+1]
        
        # for i in range(n1):
        #     left[i] = self.sorting_array[p+i]
                    
        # for j in range(n2):
        #     right[j] = self.sorting_array[q+j+1]
        # print(left, right)
        left.append(float('inf'))
        right.append(float('inf'))
        
        i, j = 0, 0
        for k in range(p, r+1):
            self.comparison_count += 1
            if left[i] <= right[j]:
                self.sorting_array[k] = left[i]
                i += 1
            else:
                self.sorting_array[k] = right[j]
                j += 1
        print(self.sorting_array)
        
    def merge_sort(self, p, r):
        """Sort an array using merge sort"""
        if p < r:
            q = (p+r) // 2
            self.merge_sort(p, q)
            self.merge_sort(q+1, r)
            print("p q r", p, q, r)
            self.merge(p, q, r)
            
    def heapify(self, n, i):
        """Heapify the given array"""
        lar = i
        left = 2*i + 1
        right = 2*i + 2
        
        #if left child is large than root
        if (left < n):
            self.comparison_count += 1
            if (self.sorting_array[left] > self.sorting_array[lar]):
                lar = left    
        
        #if right child is large than root
        if (right < n):
            self.comparison_count += 1
            if (self.sorting_array[right] > self.sorting_array[lar]):
                lar = right 
        
        if lar != i:
            self.sorting_array[lar], self.sorting_array[i] = self.sorting_array[i], self.sorting_array[lar]
            self.heapify(n, lar)
    
    
    def heap_sort(self):
        """Sort given array using HEAP sort """
        n = len(self.sorting_array)
        for i in range((n//2)-1, -1, -1):
            self.heapify(n, i)
            
        for i in range(n-1, -1, -1):
            self.sorting_array[0], self.sorting_array[i] = self.sorting_array[i], self.sorting_array[0]
            self.heapify(i, 0) 
        
        
    def insertion_sort(self):
        """Sort input array using Insertion Sort """
        # print(self.sorting_array)
        self.comparison_count = 0

        n = len(self.sorting_array)

        for j in range(1, n):
            key = self.sorting_array[j]
            i = j-1
            
            while True:                                
                if i>-1:
                    self.comparison_count += 1
                    if self.sorting_array[i] > key:
                        self.sorting_array[i+1] = self.sorting_array[i]
                        i -= 1   
                    else:
                        break
                else:
                    break                            
            self.sorting_array[i+1] = key


    def heappush(heap, val):
        heap.insert(0, val)
        n = len(heap)
        heapify(heap, n, 0)

    def heappop(heap):
        if not heap: return -1
        heap[0], heap[-1] = heap[-1], heap[0]
        x = heap.pop()
        n = len(heap)
        heapify(heap, n, 0)
        return x
    
    def heapsort(ip):
        heap = []
        for i in ip:
            heappush(heap, i)
            print(i, heap)
        while heap:
            x = heappop(heap)
            print(x, end=" ")




if __name__ == "__main__":
    A = [6, 5, 4, 3, 2, 1]
    s = Solution(A)
    s.merge_sort(0, len(A)-1)


----------------------------------
# Iterative merge sort

from collections import deque

def atomize(l):
    return deque(
        map(
            lambda x: deque([x]),
            l if l else []
        )
    )

def merge(l, r):
    res = deque()
    while (len(l) + len(r)) > 0:
        if len(l) < 1:
            res += r
            r = deque()
        elif len(r) < 1:
            res += l
            l = deque()
        else:
            if l[0] <= r[0]:
                res.append(l.popleft())
            else:
                res.append(r.popleft())
    return res

def iter_merge_sort(l):
    atoms = atomize(l) # O(n)
    print(atoms)
    while len(atoms) > 1: # O(n - 1)
        atoms.append(merge(atoms.popleft(), atoms.popleft()))
    return list(atoms[0])

def counting_sort(ip):
    n = len(ip)
    c = [0] * (5)

    # Count no of occurence
    for i in ip:
        c[i] += 1
    print(c)

    # Take cummulative sum
    for i in range(1, 5):
        c[i] += c[i - 1]
    print(c)
    # Here index is the element with position as values in C list
    op = [0] * (n)
    for i in range(n):
        op[c[ip[i]] - 1] = ip[i]
        c[ip[i]] -= 1
    print(op)
    

ip = list(map(int, "01222222221101"))
counting_sort(ip)

"""
Radix sort
"""
def radix_sort():
    maxi = max(ip) #find max no of digits in a number
    i = 1
    while maxi // i > 0: #for each digit
        counting_sort(i)
        i *= 10


def counting_sort(exp):
    print(exp)
    c = [0] * 10    #count each occurence
    op = [0] * n    #output list

    for i in range(n):
        ind = ip[i] // exp
        c[ind % 10] += 1
    print(c)

    for i in range(1, 10):
        c[i] += c[i - 1]
    
    for i in range(n - 1, -1, -1):  #make sure to do reverse iteration
        ind = ip[i] // exp
        op[c[ind % 10] - 1] = ip[i]
        c[ind % 10] -= 1

    ip[:] = op
    print(exp, op)


ip = [ 170, 45, 75, 90, 802, 24, 2, 66]
n = len(ip)
print("input - >", ip)
radix_sort()
print("0>", ip)


x = iter_merge_sort([4,3,2,1,17,8])
print(x)

################################################
# quick sort 
# TC: O(nlgn)

arr = [40, 20, 10, 30]

def partition(arr, left, right):
    if left == right:   return left 
    pivot = arr[right] 
    
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
    i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i 
    

def quick_sort(arr, left, right):
    if left >= right:   return
    index = partition(arr, left, right)
    quick_sort(arr, left, index - 1)
    quick_sort(arr, index + 1, right)

quick_sort(arr, 0, len(arr) - 1)
