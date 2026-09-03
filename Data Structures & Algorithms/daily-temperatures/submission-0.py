class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[0]
        result=[None] * len(temperatures)
        for i in range(1,len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                x=stack.pop()
                result[x]=i-x
            stack.append(i)
        while len(stack)!=0:
            result[stack.pop()] = 0
            

        return result