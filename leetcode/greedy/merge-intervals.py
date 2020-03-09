https: // leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, ip: List[List[int]]) -> List[List[int]]:
        if not ip or not ip[0]:
            return ip
        n = len(ip)
        ip.sort()
        r = n - 1
        l = 1
        end = ip[0][1]
        while l <= r:
            if ip[l][0] <= end:

                end = max(ip[l][1], ip[l-1][1])
                ip[l-1][1] = end
                del ip[l]
                r -= 1
            else:
                end = ip[l][1]
                l += 1
        return ip
