class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        lastind=len(nums)-1
        nums=sorted(nums)
        res=[]

        for ind,target in enumerate(nums):
            last=lastind
            first=0
            while (ind>first and last>ind):
                if (nums[first]+nums[last]+target==0):
                    triplet=[target, nums[first], nums[last]]
                    if triplet not in res:
                        res.append(triplet)
                    break
                elif (nums[first]+nums[last]+target>0):
                    last-=1
                else:
                    first+=1
        
        return res

