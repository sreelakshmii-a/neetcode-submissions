class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            check={}
            for i,num in enumerate(nums):
                num2=target-num
                if num2 in check:
                    return [check[num2],i]
                check[num]=i
            
