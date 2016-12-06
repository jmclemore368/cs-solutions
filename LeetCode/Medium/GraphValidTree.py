# https://leetcode.com/problems/graph-valid-tree/


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        # Initialize subsets 
        parent = [-1] * n
        
        # Iterate through all edges of graph & find subset of both vertices of every edge.
        for edge in edges:
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])
            
            # If they are the same, then there is a cycle. Since trees do not have cycles, return false.
            if x == y:
                return False
            self.union(parent, x, y)
        
        # Trees are not disjoint. Specifically, they have exactly 1 root node.
        count = parent.count(-1)
        return count == 1
        
        
    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[y_set] = x_set
    
    
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])
