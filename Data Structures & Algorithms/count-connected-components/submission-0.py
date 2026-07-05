class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph={c:set() for c in range(n)}
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        visited=set()

        def dfs(node,prev):
            
            visited.add(node)

            for k in graph[node]:
                if k!=prev and k not in visited:
                    dfs(k,node)
            return
        
        count=0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i,None)

        return count