https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:  return folder
        folder.sort()
        l, r = 1, len(folder) - 1
        st = folder[0]
        while l <= r:
            stl = len(st)
            if folder[l][:stl + 1] == st+"/" :
                del folder[l]
                r -= 1
                continue
            else:
                st = folder[l]
            l += 1
        return folder
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []
        for f in folder:
            if not ans or f[: 1 + len(ans[-1])] != ans[-1] + '/':   # need '/' to ensure a parent.
                ans.append(f)
        return ans