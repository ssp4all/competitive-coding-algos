https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # if not customers and not grumpy: return 0
        n = len(customers)
        sat = 0
        win = 0
        i = 0
        l = 0
        ans = float('-inf')
        for a, b in zip(customers, grumpy):
            sat += (a if b == 0 else 0)
            if i-l >= X:
                win -= (customers[l] if grumpy[l] == 1 else 0)
                l += 1
            win += (customers[i] if grumpy[i] == 1 else 0)
            ans = max(win, ans)
            
            
            i += 1
        return sat + ans        
        