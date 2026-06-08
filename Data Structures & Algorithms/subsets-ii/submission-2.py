class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        self.NUMS_LENGTH=len(nums)
        self.RESULT=[]

        def backtrack(start,arr):

            self.RESULT.append(arr.copy())
            for i in range(start,self.NUMS_LENGTH):
                if i!=start and nums[i-1]==nums[i]:
                    continue
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()

        backtrack(0,[])
        return self.RESULT