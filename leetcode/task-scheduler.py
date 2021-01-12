https://leetcode.com/problems/task-scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks: return -1
        # xx = Counter(tasks)
        map = [0]*26
        for i in tasks:
            map[ord(i) - ord('A')] += 1
        map.sort()
        time = 0
        while map[-1] > 0:
            i = 0
            while i <= n:
                if not map[-1]:
                    break
                if i < 26 and map[25-i] > 0:
                    map[25 - i] -= 1
                time += 1
                i += 1
            map.sort()
        return time

###############################
TC: O(n) n=total tasks
space = O(1)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:   return 0
        task_counts = len(tasks)
        counter  = [0] * 26
        
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
        counter.sort()
        slots = counter.pop() - 1
        total = slots * n
        while total > 0 and counter:
            total -= min(slots, counter.pop())
        total = max(0, total)
        # print(total)
        return task_counts + total