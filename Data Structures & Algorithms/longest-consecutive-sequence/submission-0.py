class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Handle the empty list edge case
        if not nums:
            return 0
        
        # 2. Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        # 3. Iterate through the unique numbers
        for num in num_set:
            # Check if 'num' is the START of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Count how long this sequence goes
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the global maximum streak found so far
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
