class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res=[]
        def permutations(remain,arr):

            if len(remain)==0:
                self.res.append(arr.copy())
                return
            
            for i in remain:
                temp=remain.copy()
                temp.remove(i)
                arr.append(i)
                permutations(temp,arr)
                arr.pop()
            
        permutations(set(nums),[])
        return self.res
