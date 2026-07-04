class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        nodes={c:set() for c in range(n)}
        for i in edges:
            nodes[i[0]].add(i[1])
        print(nodes)
        noParent=set(range(n))
        visited=set()
        cycle=set()

        def traverse(node):

            if node in cycle:
                return False
            if node in visited:
                return False
            
            cycle.add(node)

            for i in nodes[node]:
                #print(node,noParent,i)
                '''noParent.remove(i)'''
                if traverse(i)==False:
                    return False

            cycle.remove(node)
            visited.add(node)
            return True


        if traverse(0)==False:
            return False
        
        '''if len(noParent)==1:
            return True'''

        return True