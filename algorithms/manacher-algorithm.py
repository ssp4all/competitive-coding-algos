class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"
        p = [0] * len(t)

        center = 0
        right = 0

        for i in range(1, len(t) - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        max_len = max(p)
        center_index = p.index(max_len)

        start = (center_index - max_len) // 2
        return s[start:start + max_len]

  ## Complexity

  # Let n be the length of the original string.

  # Time:  O(n)
  # Space: O(n)
