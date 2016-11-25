# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Build graph
        graph = {}
        for v in range(0, n): 
            graph[v] = set()
            
        # Add edges to graph
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        # DFS on each vertex
        count = 0
        visited = set()
        for vertex in graph:
            if vertex not in visited:
                count += 1
                self.depthFirstSearch(vertex, visited, graph)
        return count
      
    def depthFirstSearch(self, vertex, visited, graph):
        visited.add(vertex)
        for edge in graph[vertex]:
            if edge not in visited:
                self.depthFirstSearch(edge, visited, graph)
            
        
        
        
        
        
           
