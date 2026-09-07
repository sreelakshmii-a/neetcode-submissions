class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        # Initialize two pointers at the ends of the array
        left, right = 0, len(height) - 1
        
        # Track the maximum heights seen so far from both directions
        left_max, right_max = height[left], height[right]
        
        total_water = 0
        
        # Move pointers inward until they meet
        while left < right:
            # We process the side with the smaller maximum boundary
            # because the smaller boundary dictates the trapped water.
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                
        return total_water