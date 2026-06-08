class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        self.length=len(nums)
        self.res=[]

        def backtrack(start,arr):

            self.res.append(arr.copy())
            for i in range(start,self.length):
                if i!=start and nums[i-1]==nums[i]:
                    continue
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()

        backtrack(0,[])
        return self.res