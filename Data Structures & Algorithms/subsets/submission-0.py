class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def findsets(nums, arr):
            self.res.append(arr.copy())  # ✅ Copy, not reference!

            temp = nums.copy()
            for i in nums:
                temp.remove(i)
                arr.append(i)
                findsets(temp, arr)
                arr.pop()

        findsets(set(nums), [])
        return self.res