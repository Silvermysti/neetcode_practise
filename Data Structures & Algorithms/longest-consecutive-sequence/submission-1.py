class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0;
        
        maxlen=1
        currlen=1

        nums=sorted(list(set(nums)))

        for ind,val in enumerate(nums):
            if ind==0:
                continue
            if nums[ind-1]==val-1:
                currlen+=1
            else:
                if currlen>maxlen:
                    maxlen=currlen
                currlen=1
        
        if currlen>maxlen:
            maxlen=currlen
        
        return maxlen
