class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        nodes={c:set() for c in range(n)}
        for i in edges:
            nodes[i[0]].add(i[1])
            nodes[i[1]].add(i[0])
        #print(nodes)
        visited=set()
        cycle=set()

        def traverse(node,prev):
            if node in visited:
                return False

            visited.add(node)

            for i in nodes[node]:
                if i!=prev:
                    if traverse(i,node)==False:
                        #print(node,i,visited)
                        return False
            return True
            
        if traverse(0,None)==False or len(visited)!=n:
            return False

        return True