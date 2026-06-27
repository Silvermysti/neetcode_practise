class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        res=nums[0]
        currsum=nums[0]

        for i in range(1,len(nums)):
            if nums[i]>currsum:
                res=max(currsum,res)
                currsum=nums[i]
            else:
                currsum+=nums[i]

        res=max(res,currsum)
        
        return res