class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        numdict={}

        for i,j in enumerate(numbers):
            numdict[j]=i
        
        for key in numdict.keys():
            if (target-key in numdict and target!=2*key):
                return [numdict[key]+1, numdict[target-key]+1]
        
        