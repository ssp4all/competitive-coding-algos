https://leetcode.com/problems/add-and-search-word-data-structure-design/

from collections import defaultdict

class Node():
    def __init__(self):
        self.child = defaultdict(Node)
        self.end = 0
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if not word:    return 
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.end = 1

    def search(self, word: str) -> bool:
        # print(self.root.child['a'].child['n'].child)
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:    return 0
        cur = self.root
        
        def helper(cur, word):
            if not cur:   return 0
            if not word:
                if cur.end:
                    return 1
                return 0
            st = word[0]
            if st != ".":
                w = cur.child.get(st)
                x = helper(w, word[1:])
                if x:
                    return 1
                return 0
            else:
                for w in cur.child.values():
                    x = helper(w, word[1:])
                    if x:
                        return 1
                    
        x = helper(cur, word)
        return x
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)