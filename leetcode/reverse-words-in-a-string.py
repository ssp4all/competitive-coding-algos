class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        z = " ".join(x[::-1])
        return z