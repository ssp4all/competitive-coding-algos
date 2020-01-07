https://leetcode.com/problems/video-stitching/
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        start, end, ans = -1, 0, 0
        for i, j in sorted(clips):
            if end > T or i >= end: break
            elif start < i <= end:
                ans, start = ans + 1, end
            end = max(end, j)
        return ans if end >= T else -1
           
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if not clips: return -1
        ans = 0
        n = len(clips)
        clips.sort()
        # print(clips)
        start = 0
        end = []
        i = 0
        
        #seach for better zero
        while clips[i][0] == 0:
            if i > n-1:  break

            if not end or clips[i][1] > end[-1]:
                end.append(clips[i][1])
                ans = 1
            i += 1
        if not end: return -1
        start = end[-1]
            
        # print(end)
        
        while end[-1] < T:
            if i > n-1:  break
            while clips[i][0] <= start and clips[i][0] <= end[-1]:
                if clips[i][1] > end[-1]:
                    end.append(clips[i][1])
                    # print(end)
                i += 1
                if i > n-1:  break
            i += 1
            ans += 1
            start = end[-1]
            
        return ans if start >= T else -1
                