class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        graph=defaultdict(set)
        visited=set()
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
            if i in visited and j in visited:
                return[i,j]
            visited.add(i)
            visited.add(j)
        

            
