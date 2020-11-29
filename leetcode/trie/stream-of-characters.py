from collections import defaultdict
class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.end = 0
        
class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.root = Node()
        self.letters = []
        maxi = max(words, key=lambda x:len(x))
        self.ml = len(maxi)
        for word in words:
            cur = self.root
            for ch in word[::-1]:
                cur = cur.child[ch]
            cur.end = 1
    
        
    def query(self, letter: str) -> bool:
        if not letter:  return 0
        
        cur = self.root
        self.letters += [letter]
        # print(self.letters, self.ml)
        ptr = len(self.letters) - 1
        st = max(0, len(self.letters) - self.ml)
        while cur.end == 0 and ptr >= st:
            # print(self.letters[ptr])
            cur = cur.child[self.letters[ptr]]
            ptr -= 1
        # print("#")
        return cur.end
  
import collections

        
class StreamChecker:

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
        self.S = ""
        self.W = max(map(len, words))

    def query(self, letter):
        self.S = (letter + self.S)[:self.W]
        cur = self.trie
        for c in self.S:
            if c in cur:
                cur = cur[c]
                if cur['#'] == True:
                    return True
            else:
                break
        return False
          

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
