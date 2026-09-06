class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stores indices
        max_area = 0
        
        # Append a 0 to the end to flush out all elements remaining in stack at the end
        heights.append(0)
        
        for i in range(len(heights)):
            # While the current bar is shorter than the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                
                # If stack is empty, it means this popped bar was the shortest seen so far.
                # The width extends from index 0 all the way to i.
                if not stack:
                    width = i
                else:
                    # Otherwise, width is bounded by the current index and the new top of the stack
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        # Restore the original array array modification (optional good practice)
        heights.pop()
        
        return max_area
