class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #6/9/26
        cur = 0
        l,r = 0,len(heights)-1
        while l<r:
            temp = min(heights[r],heights[l])*(r-l)
            cur = temp if temp>cur else cur
            if heights[l]>heights[r]:
                r-=1
                continue
            l+=1
        return cur