class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            # check=dict()
            # ans=[]
            # for i in range(len(nums)):
            #     check[nums[i]]=i
            # for i in range(len(nums)):
            #     if (target-nums[i]) in check:
            #         ans.append(i)
            #         ans.append(check[nums[i]])
            #         return ans
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        return [i,j]
