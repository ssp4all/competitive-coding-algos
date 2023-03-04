# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

"""
Given two strings needle and haystack, return the index of the first occurrence of needle in 
haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

#TC: O(M+N), SC:O(M)
def boyer_moore_search(string, substring):
    n = len(string)
    m = len(substring)

    # Create a bad character table
    bad_char = {}
    for i in range(m):
        bad_char[substring[i]] = i

    # Initialize variables
    i = m - 1
    j = m - 1

    # Search for the substring in the string
    while i < n and j >= 0:
        if string[i] == substring[j]:
            i -= 1
            j -= 1
        else:
            if string[i] in bad_char:
                i += m - min(j, 1 + bad_char[string[i]])
            else:
                i += m
            j = m - 1

    # Return the index of the substring in the string, or -1 if it is not found
    if j < 0:
        return i + 1
    else:
        return -1


# TC: O(M*N), SC:O(1)
public int strStr(String haystack, String needle) {
  for (int i = 0; ; i++) {
    for (int j = 0; ; j++) {
      if (j == needle.length()) return i;
      if (i + j == haystack.length()) return -1;
      if (needle.charAt(j) != haystack.charAt(i + j)) break;
    }
  }
}