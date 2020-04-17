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