class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[nums[0]]
        K=1

        for i in nums[1:]:
            ind=K-1
            while heap[ind]<i:
                    ind-=1
                    if ind<0:
                        break
            heap.insert(ind+1,i)
            if K<k:
                K+=1
        return heap[k-1]