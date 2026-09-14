
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack=[]
        
        curr=head
        while curr:
            stack.append(curr)
            curr=curr.next

        
        ncurr=stack[-1]
        while len(stack)>1:
            node=stack.pop()
            node.next=stack[-1]
            
        stack[-1].next=None
        return ncurr

            