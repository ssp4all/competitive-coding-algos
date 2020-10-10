https://leetcode.com/problems/restore-ip-addresses/


"""
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s: return []
        n = len(s)
        res = []
        def helper(s, count, cur):
            if count == 4:
                if not s:   
                    res.append(cur[:-1])
            else:
                for i in range(1, 4):
                    if i > len(s):  continue
                    if i > 1 and s[0] == "0":   continue
                    if i > 2 and int(s[:3]) > 255:  continue
                    
                    helper(s[i:], count + 1, cur + s[:i] + ".")
        helper(s, 0, "")
        return res