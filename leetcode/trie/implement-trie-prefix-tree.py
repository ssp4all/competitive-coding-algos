# https://leetcode.com/problems/implement-trie-prefix-tree

from collections import defaultdict

class Node:
    def __init__(self):
        self.letters = defaultdict(Node)
        self.end = 0
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for let in word:
            cur = cur.letters[let]
        cur.end = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for let in word:
            cur = cur.letters.get(let, None)
            if cur == None:
                return 0
        return cur.end
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for let in prefix:
            cur = cur.letters.get(let)
            if cur == None:
                return 0
        return 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)