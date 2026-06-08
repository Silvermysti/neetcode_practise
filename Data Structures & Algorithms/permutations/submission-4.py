class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res=[]
        self.length=len(nums)
        def permutations(visited, arr):

            if len(arr)==self.length:
                self.res.append(arr.copy())
                return
            
            for i in range(self.length):
                if visited[i]==1:
                    continue
                visited[i]=1
                arr.append(nums[i])
                permutations(visited,arr)
                visited[i]=0
                arr.pop()
            
        permutations([0]*self.length,[])
        return self.res
