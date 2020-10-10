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



Java Version

# class Node{
#     public boolean isWord;
#     public Node[] letters = new Node[26];
#     public Node(){};        
# }
# class Trie {
#     private Node root;
#     /** Initialize your data structure here. */
#     public Trie() {
#         root = new Node();
        
#     }
    
#     /** Inserts a word into the trie. */
#     public void insert(String word) {
#         Node cur = root;
#         for (int i = 0; i < word.length(); ++i){
#             char c = word.charAt(i);
#             if (cur.letters[c - 'a'] == null){
#                 cur.letters[c - 'a'] = new Node();
#             }
#             cur = cur.letters[c - 'a'];
#         }
#         cur.isWord = true;
        
#     }
    
#     /** Returns if the word is in the trie. */
#     public boolean search(String word) {
#         Node cur = root;
#         for (int i = 0; i < word.length(); ++i){
#             char c = word.charAt(i);
#             if (cur.letters[c - 'a'] == null)
#                 return false;
#             cur = cur.letters[c - 'a'];
#         }
#         return cur.isWord;
#     }
    
#     /** Returns if there is any word in the trie that starts with the given prefix. */
#     public boolean startsWith(String prefix) {
#         Node cur = root;
#         for (int i = 0; i < prefix.length(); ++i){
#             char c = prefix.charAt(i);
#             if (cur.letters[c - 'a'] == null)
#                 return false;
#             cur = cur.letters[c - 'a'];
#         }
#         return true;
#     }
# }

# /**
#  * Your Trie object will be instantiated and called as such:
#  * Trie obj = new Trie();
#  * obj.insert(word);
#  * boolean param_2 = obj.search(word);
#  * boolean param_3 = obj.startsWith(prefix);
#  */