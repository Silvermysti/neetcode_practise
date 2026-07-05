class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        prereq={c:set() for c in range(numCourses)}
        for i in prerequisites:
            prereq[i[1]].add(i[0])
        #print(prereq)

        def dfs(node,target):
            #print(node,target)
            if node==target:
                return True

            for k in prereq[node]:
                if dfs(k,target):
                    return True
            return False
        

        res=[]
        for i in queries:
            res.append(dfs(i[1],i[0]))
            #print(i, res)
            #print(" ")
        return res
