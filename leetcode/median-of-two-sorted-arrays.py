https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        m = len(a)
        n = len(b)
        even = 0
        if (m+n) % 2 == 0:
            even = 1
        tar = (m + n - 1) // 2
        op = []
        i, j = 0, 0
        while i < m and j < n:
            if a[i] < b[j]:
                op.append(a[i])
                i += 1
            else:
                op.append(b[j])
                j += 1
            if even == 0 and len(op)-1 == tar:
                return op[tar]
            elif even == 1 and len(op)-1 == tar+1:
                return (op[tar] + op[tar+1]) / 2 
        op += a[i:]
        op += b[j:]
        if even == 0:
            return op[tar]
        else:
            return (op[tar] + op[tar+1]) / 2

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if not a and not b: return 0
        la, lb = len(a), len(b)
        par = (la + lb + 1) // 2
        if la > lb:
            a, b, la, lb = b, a, lb, la
        s, e = 0, la
        # l, r = la //2 , par - (la // 2)
        # print(l, r)
        while s <= e:
            i = (s + e) // 2
            j = par - i
            if i < la and b[j - 1] > a[i]:
                s = i + 1
            elif i > 0 and b[j] < a[i - 1]:
                e = i - 1
            else:
                if i == 0:
                    ml = b[j - 1]
                elif j == 0:
                    ml = a[i - 1]
                else:
                    ml = max(a[i - 1], b[j - 1])
                
                if (la + lb) & 1:
                    return ml
                if i == la:
                    mr = b[j]
                elif j == lb:
                    mr = a[i]
                else:
                    mr = min(a[i], b[j])
                
                return (ml + mr) / 2