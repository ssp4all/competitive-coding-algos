https://leetcode.com/problems/making-file-names-unique/

"""
Given an array of strings names of size n. You will create n 
folders in your file system such that, at the ith minute, you will 
create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder 
name which is previously used, the system will have a suffix addition 
to its name in the form of (k), where, k is the smallest positive 
integer such that the obtained name remains unique.

Return an array of strings of length n where ans[i] is the actual 
name the system will assign to the ith folder when you create it.

 

Example 1:

Input: names = ["pes","fifa","gta","pes(2019)"]
Output: ["pes","fifa","gta","pes(2019)"]
"""

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        uniques = []
        
        used = {}
        
        for name in names:
            if name in used:
                suff = used[name]
                tmp = f"{name}({suff})"
                while tmp in used:
                    suff += 1
                    tmp = f"{name}({suff})"
                used[tmp] = 1
                used[name] = used.get(name, 0) + 1 
                uniques += [tmp]
            else:
                used[name] = 1 
                uniques += [name]
            
        return uniques
            