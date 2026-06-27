class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        res=0

        for ind, jump in enumerate(nums):
            if ind>res:
                return False
            res=max(jump+ind, res)
        
        return True

