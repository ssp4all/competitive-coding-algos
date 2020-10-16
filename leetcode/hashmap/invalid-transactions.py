https://leetcode.com/problems/invalid-transactions/

"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing 
the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within
 a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
"""

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:    return []
        
        n = len(transactions)
        
        seen = collections.defaultdict(list)
        fraud = []
        
        for tran in transactions:
            name, time, amount, city = tran.split(",")
            seen[name] += [tran]
        
        for tran in transactions:
            name, time, amount, city = tran.split(",")
            if int(amount) > 1000:
                fraud += [tran]
                continue 
            
            for index, other_tran in enumerate(seen[name]):
                name2, time2, amount2, city2 = other_tran.split(",")
                if abs(int(time2) - int(time)) <= 60 and city2 != city:
                    fraud += [(tran)]
                    break
        return fraud