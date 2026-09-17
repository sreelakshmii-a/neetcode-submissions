class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                idx,height=stack.pop()
                area=height*(i-idx)
                max_area=max(max_area,area)
                start=idx
            stack.append((start,h))
        while stack:
            i,h=stack.pop()
            max_area = max(max_area, h * (len(heights) - i))

        return max_area