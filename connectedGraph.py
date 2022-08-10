from collections import defaultdict,deque
class Solution:
    
    def countComponents(self,n, edges):
            graph = defaultdict(list)
            for i,v in edges:
                graph[i].append(v)
            
            
            def dfs(graph,key):
                visited = []
                stack = deque([key])
                while stack:
                    vertex = stack.pop()
                    visited.append(vertex)
                    for neighbor in graph[vertex]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                
                return visited
            visited  = []
            counter = 0
            for key in list(graph.keys()):
                if key not in visited:
                    counter += 1
                    visited += dfs(graph,key)
         
            return counter
        
s = Solution()
print(s.countComponents(5,[[0,1],[1,2],[3,4]]))