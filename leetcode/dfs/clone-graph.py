https://leetcode.com/problems/clone-graph/


"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:    return node
        # cur = Node()
        seen = dict()
        
        def helper(node):
            if node.val in seen:
                return seen[node.val]
            cur = Node()
            seen[node.val] = cur
            cur.val = node.val
            for i in node.neighbors:
                # nn = Node()
                cur.neighbors += [helper(i)]
            return cur
        
        cur = helper(node)
        # print(cur)
        return cur
        
        
        