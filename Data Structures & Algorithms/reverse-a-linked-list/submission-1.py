
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
            stack.append(curr.val)
            curr=curr.next

        
        curr=head
        while len(stack)!=0:
            curr.val=stack[-1]
            stack.pop()
            curr=curr.next
        
        return head

            