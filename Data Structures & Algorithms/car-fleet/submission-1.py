class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack=[]
        for p,s in pairs:
            rtime=(target-p)/s
            if not stack or stack[-1]<rtime:
                stack.append(rtime)
        return len(stack)