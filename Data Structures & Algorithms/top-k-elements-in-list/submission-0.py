class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        max_heap=[]
        ans=[]
        for x in count:
            heapq.heappush(max_heap,((-count[x]),x))
        for i in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        return ans
        
        