https://leetcode.com/problems/number-of-matching-subsequences/

"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
"""
import collections
import copy
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if not S or not words:  return 0
        ans = 0
        count = collections.defaultdict(collections.deque)
        
        for ind, s in enumerate(S):
            if s in count:
                count[s] += [ind]
            else:
                count[s] = deque([ind])
        for word in words:
            prev = -1
            count_copy = copy.deepcopy(count)
            i = 0
            for ind, w in enumerate(word):
                if w in count_copy and count_copy[w]:
                    cur_ind = count_copy[w].popleft()
                    
                    while count_copy[w] and cur_ind < prev:
                        cur_ind = count_copy[w].popleft()
                    if prev > cur_ind:
                        break 
                    prev = cur_ind
                else:
                    break
                i = ind
            if i == len(word) - 1: 
                ans += 1
        return ans

import collections
import copy
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if not S or not words:  return 0
        waiting = collections.defaultdict(list)
        for word in words:
            waiting[word[0]] += [word]
        ans = 0
        for s in S:
            if s in waiting:
                temp = waiting[s]
                waiting[s] = []
                for word in temp:
                    if len(word) > 1:
                        waiting[word[1]] += [word[1:]]
                    else:
                        ans += 1
        return ans 