class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        graph=defaultdict(set)
        visited=set()
        cycle=set()
        cyclesets=set()
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        def dfs(node, prev):
            if node in cycle:
                cycle.add(node)
                cyclesets.add((node,prev))
                return True
            if node in visited:
                return False
            
            cycle.add(node)
            cyclesets.add((node,prev))
            for i in graph[node]:
                if i!=prev and dfs(i,node):
                    return True
                    break
            cyclesets.remove((node,prev))
            cycle.remove(node)
            visited.add(node)
            return False

        dfs(1,None)
        
        for i,j in edges[::-1]:
            if (i,j) in cyclesets or (j,i) in cyclesets:
                return [i,j]


            
