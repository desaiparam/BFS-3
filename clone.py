# Time Complexity : O(V+E) where V is the number of vertices and E is the number of edges in the graph
# Space Complexity : O(V) for storing the cloned nodes
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using BFS to traverse the graph and clone each node along with its neighbors.
# I maintain a mapping of original nodes to their cloned counterparts to avoid duplications.
# I use a queue to facilitate the BFS traversal. For each node, I clone it if it hasn't been cloned yet,
# and then I iterate through its neighbors, cloning them as well and adding them to the neighbors list of the cloned node.
# Finally, I return the cloned node corresponding to the input node.
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapy = {}
        q = deque([node])
        def clone(node):
            if not node:
                return None
            if node in mapy:
                return mapy[node]
            mapy[node] = Node(node.val)
            return mapy[node]
        while q:
            curr = q.popleft()
            copy = clone(curr)
            for n in curr.neighbors:
                if n not in mapy:
                    q.append(n)
                copy.neighbors.append(clone(n))
        return mapy[node]
