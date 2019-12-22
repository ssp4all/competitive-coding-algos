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
        left.append(999999999)
        right.append(999999999)
        
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
        for i in range((n/2)-1, -1, -1):
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
            
        # pass

if __name__ == "__main__":
    A = [6, 5, 4, 3, 2, 1]
    s = Solution(A)
    s.merge_sort(0, len(A)-1)