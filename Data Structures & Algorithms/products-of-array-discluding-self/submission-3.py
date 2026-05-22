class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeroCount=0
        zeroInd=-1
        product=1

        for ind,i in enumerate(nums):
            if (i==0):
                if (zeroCount==0):
                    zeroCount=1
                    zeroInd=ind
                    continue
                else:
                    return [0]*len(nums)
            else:
                product *= i
        
        res=[0]*len(nums)

        if (zeroCount==1):
            res[zeroInd]=product
            return res         
        else:
            for ind,val in enumerate(nums):
                res[ind]=int(product/val)
            return res
        