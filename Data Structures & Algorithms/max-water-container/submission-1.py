class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxAreaArr=[]
        first=0
        last=len(heights)-1
        
        def findmax(height):
            maxArea=0
            first=0
            last=len(height)-1
            while(first<last):
                area=min(heights[first],heights[last])*(last-first)
                if (area>maxArea):
                    maxArea=area
                if (heights[first]>heights[last]):
                    last-=1
                elif (heights[last]>heights[first]):
                    first+=1
                else:
                    findmax(height[first:last])
                    findmax(height[first+1:last+1])
                    maxAreaArr.append(maxArea)
                    return
            
            maxAreaArr.append(maxArea)
            return

        findmax(heights)
        
        print(maxAreaArr)
        return max(maxAreaArr)
