import heapq
import collections

# prims's algorithm
def solve(N, connections):
    if not connections: return []

    pq = []
    ans = []
    edges = collections.defaultdict(list)

    for t1, t2, cost in connections:
        edges[t1].append((t2, cost))
        edges[t2].append((t1, cost))

    seen = set()
    random_start = connections[0][0]
    seen.add(random_start)

    for outgoing_edge, cost in edges[random_start]:     
        heapq.heappush(pq, (cost, random_start, outgoing_edge))

    while pq and len(seen) < N:
        cost, t1, t2 = heapq.heappop(pq)
    
        if t1 in seen and t2 in seen: 
            continue
        ans += [[t1, t2, cost]]
        if t1 not in seen:
            for outgoing_edge, cost in edges[t1]: 
                heapq.heappush(pq, (cost, t1, outgoing_edge))
            seen.add(t1)
        if t2 not in seen:
            for outgoing_edge, cost in edges[t2]: 
                heapq.heappush(pq, (cost, t2, outgoing_edge))
            seen.add(t2)

    if len(seen) < N: 
        return []
    print(edges, seen)
    # print(ans)
    return ans
connections = [["A", "B", 1], ["B", "C", 4], ["B", "D", 6], ["D", "E", 5], ["C", "E", 1]]
x = solve(5, connections)
print(x) 

--------------------
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


class Solution:
    def __init__(self):
        self.result = []

    def max_avg(self, root: TreeNode):
        if not root or not root.children:
            return None

        self.dfs(root)
        return self.result[1]

    def dfs(self, root: TreeNode):
        if not root.children:
            self.result = [root.val, 1]

        curr_sum, curr_num = root.val, 1
        for child in root.children:
            child_sum, child_num = self.dfs(child)
            curr_sum += child_sum
            curr_num += child_num

        if self.result[1] < curr_sum / curr_num:
            self.result = [root, curr_sum / curr_num]
        
        return [curr_sum, curr_num]
-----------------------
codelist = [["anything", "apple"], ["banana", "anything", "banana"]] 
cart = ["orange", "apple", "apple", "banana", "orange", "banana"]

def helper():
    n1 = len(codelist)
    n2 = len(cart)

    i, j = 0, 0
    while i < n2:
        k = 0
        while (k < len(codelist[j]) and (codelist[j][k] == "anything" or cart[i] == codelist[j][k])):
            print(codelist[j][k], cart[i], k)
            k += 1
            i += 1
            if k == len(codelist[j]):
                j += 1
                if j == len(codelist):
                    return 1
                k = 0
        i += 1
        
    return 0
x = helper()
print(x)

------------------------------
from collections import defaultdict
class graph:  # For Directed edge that shows relations b/w Item1 -> Item 2
  def __init__(self):
    self.graph = defaultdict(list)
  
  def add_edge(self,u,v):
    self.graph[u].append(v)

# Performing depth-first search to get the combined items in a particular group
def dfs(graph,key,visited,lst):
  visited.add(key)
  lst.append(key)
  for nei in graph[key]:
    if nei not in visited:
      dfs(graph,nei,visited,lst)


itemAssociation = [['item1','item2'],['item2','item5'],['item5','item4']]

#Creation of graph
g = graph()
for i in range(len(itemAssociation)):
  g.add_edge(itemAssociation[i][0],itemAssociation[i][1])
print(g.graph)

res = [] # Final list that contains resulted output
visited = set()

for key in list(g.graph):
  intrm = []  #Intermediate list which gives the items belong to single group
  print(key, visited)
  if key not in visited:
    dfs(g.graph,key,visited,intrm)
  print("->", key, visited)
  
  if not res:
    res = intrm
  else:
    if len(intrm) > len(res):
      res = intrm
    elif len(intrm) == len(res):
      if sorted(intrm)[0] < sorted(res)[0]:
        res = intrm

print(res)
------------------------------
from collections import defaultdict

s = "awaglknagawunagwkwagl"
k = 4

def helper():
    wind = defaultdict(int)
    res = set()
    st = 0
    cur = 0
    n = len(s)
    while cur < n:
        wind[s[cur]] += 1
        print(wind, cur)
        while cur < n and st <= cur and wind[s[cur]] > 1:
            wind[s[st]] -= 1
            st += 1
        if cur - st + 1 == k:
            res.add(s[st: cur + 1])
            wind[s[st]] -= 1
            st += 1
        cur += 1
    print(res, len(res))
helper()
#better
def substringk(s, k):
    if not s or k == 0:
        return []
    
    letter, res = {}, set()
    start = 0
    for i in range(len(s)):
        if s[i] in letter and letter[s[i]] >= start:
            start = letter[s[i]]+1
        letter[s[i]] = i
        if i-start+1 == k:
            res.add(s[start:i+1])
            start += 1
    return list(res)
------------------------------------
#Turnstile
arrival_time = [0, 1, 2, 3]
direction = [0, 1, 1, 0]
n = len(arrival_time)
master_clock = 0
i, j = 0, 1
prev = 1 
while j < n:
    if arrival_time[i] == arrival_time[j]:
        if direction[i] == prev:
            arrival_time[i] = max(master_clock, arrival_time[i])
            master_clock = max(master_clock + 1, arrival_time[i])
            i = j
            j += 1
        else:
            arrival_time[j] = max(arrival_time[j], master_clock)
            master_clock = max(master_clock + 1, arrival_time[j])
            j += 1
            prev = 0
        
    else:
        arrival_time[i] = max(arrival_time[i], master_clock)
        master_clock = max(master_clock + 1, arrival_time[i])
        i = j
        j += 1
        prev = direction[i]
arrival_time[i] = max(arrival_time[i], master_clock)
print(arrival_time)

###alternative  turnstile Amazon
def turnstileTimes(numCustomers, arrTime, direction):
    start = arrTime[0]
    exiting  = []
    entering = []

    for i in range(0, numCustomers):
        if direction[i] == 0:
            entering.append((arrTime[i], i))
        else:
            exiting.append((arrTime[i], i))

    res = [-1 for _ in range(numCustomers)]

    enterI = 0
    exitI = 0
    exitPrio = True
    currTime = start
    prevTime = -1

    while enterI < len(entering) and exitI < len(exiting):
        currExitTime = max(exiting[exitI][0], currTime) 
        currEnterTime = max(entering[enterI][0], currTime)
        if currEnterTime < currExitTime:
            res[entering[enterI][1]] = currEnterTime
            prevTime = currEnterTime
            currTime = prevTime + 1
            enterI += 1
            exitPrio = False
        elif currExitTime < currEnterTime:
            res[exiting[exitI][1]] = currExitTime
            prevTime = currExitTime
            currTime = prevTime + 1
            exitI += 1
            exitPrio = True
        else:
            if currTime - prevTime > 1:
                exitPrio = True
            if not exitPrio:
                res[entering[enterI][1]] = currEnterTime
                prevTime = currEnterTime
                currTime = prevTime + 1
                enterI += 1
            else:
                res[exiting[exitI][1]] = currExitTime
                prevTime = currExitTime
                currTime = prevTime + 1
                exitI += 1
                exitPrio = True

    while enterI < len(entering):
        res[entering[enterI][1]] = max(entering[enterI][0], currTime)
        currTime += 1
        enterI += 1

    while exitI < len(exiting):
        res[exiting[exitI][1]] = max(exiting[exitI][0], currTime)
        currTime += 1
        exitI += 1
    return res
x = turnstileTimes(5, arrival_time,direction)
print(x)
-------------------------------
#Amazon | OA 2019 | Optimal Utilization
class Solution:
    def findPairs(self, a, b, target):
        a.sort(key=lambda x: x[1])
        b.sort(key=lambda x: x[1])
        l, r = 0, len(b) - 1
        ans = []
        curDiff = float('inf')
        while l < len(a) and r >= 0:
            id1, i = a[l]
            id2, j = b[r]
            if (target - i - j == curDiff):
                ans.append([id1, id2])
            elif (i + j <= target and target - i - j < curDiff):
                ans.clear()
                ans.append([id1, id2])
                curDiff = target - i - j
            if (target > i + j):
                l += 1
            else:
                r -= 1
        return ans
----------------------------
#packaging 
def findSum(nums, target):
    target -= 30
    map = {}
    maximum = -1
    ans = [-1,-1]
    for i in range(len(nums)):
        if nums[i] not in map:
            map[target - nums[i]] = i
        else:
            if nums[i] > maximum or target - nums[i] > maximum:
                ans[0] = map[nums[i]]
                ans[1] = i
                maximum = max(nums[i],target - nums[i])
    if ans != [-1,-1]:
        return ans
    else:
        return []
---------------------------------
#count of unique pairs
public static int uniquePairs(int[] nums, int target){
        Set<Integer> set = new HashSet<Integer>();
        Set<Integer> seen = new HashSet<Integer>();
        int count = 0;
        for(int num : nums){
            if(set.contains(target-num) && !seen.contains(num)){
                count++;
                seen.add(target-num);
                seen.add(num);
            }
            else if(!set.contains(num)){
                set.add(num);
            }

        }

        return count;
    }

