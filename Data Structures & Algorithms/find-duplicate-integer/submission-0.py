class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        visited=set()
        ind=0
        while True:
            val=nums[ind] 
            if val in visited:
                return val
            visited.add(val)
            ind+=1 