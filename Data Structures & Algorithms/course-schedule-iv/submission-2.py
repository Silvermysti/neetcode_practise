class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        prereq={c:set() for c in range(numCourses)}
        for i in prerequisites:
            prereq[i[1]].add(i[0])
        visited=set()
        #print(prereq)

        def dfs(node):

            for k in prereq[node]:
                if k not in visited:
                    dfs(k)
                prereq[node]=prereq[node] | prereq[k] 
            visited.add(node)
            return 
        

        for i in range(numCourses):
            if i not in visited:
                dfs(i)
        #print(prereq)

        res=[]
        for query in queries:
            if query[0] in prereq[query[1]]:
                res.append(True)
            else:
                res.append(False)
        

        return res
