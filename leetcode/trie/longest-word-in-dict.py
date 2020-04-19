https://leetcode.com/problems/longest-word-in-dictionary/

class Solution {
    public String longestWord(String[] words) {
        int n = words.length;
        if (n == 0)
            return "";
        String ans = "";
        Set<String> ss = new HashSet<String>();
        for (String s: words)
            ss.add(s);
        for (String w: words){
            if (w.length() > ans.length() || 
                    (w.length() == ans.length() && w.compareTo(ans) < 0)){
                boolean good = true;
                for (int k = 1; k < w.length(); ++k){
                    if (!ss.contains(w.substring(0, k))){
                        good = false;
                        break;
                    }
                }
                if (good)
                    ans = w;
            }
        }
        return ans;
    }
}

class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:   return ""
        words.sort(key = lambda x:(-len(x), x))
        l = 0
        for ind, w in enumerate(words):
            if all([w[:i] in words for i in range(1, len(w))]):
                   return w
        return ""


from collections import defaultdict

class Node:
    def __init__(self):
        self.letters = defaultdict(Node)
        self.end = 0

// Trie
class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:   return ""
        root = Node()
        root.end = 1
        def build_trie():
            for w in words:
                cur = root
                for ch in w:
                    cur = cur.letters[ch]
                cur.end = 1
        build_trie()
        def helper(w):
            if not w and cur.end == 1:
                return 1
            cur = root
            i = 0
            while cur.end == 1 and i < len(w):
                cur = cur.letters[w[i]]
                if not cur:
                    break
                i += 1
            
            if i == len(w):
                return 1
            return 0
        ans = []
        for w in words:
            if w and helper(w):
                ans += [w]
        return min(ans, key = lambda w:(-len(w), w))
        