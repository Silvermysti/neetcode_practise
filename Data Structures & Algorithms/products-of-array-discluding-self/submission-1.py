class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero=False
        zeroInd=-1
        product=1

        for ind,i in enumerate(nums):
            if (i==0):
                zero=True
                zeroInd=ind
                continue
            else:
                product *= i
        
        res=[0]*len(nums)

        if (zero==True):
            res[zeroInd]=product
            return res
        
        else:
            for ind,val in enumerate(nums):
                res[ind]=int(product/val)
            return res
        