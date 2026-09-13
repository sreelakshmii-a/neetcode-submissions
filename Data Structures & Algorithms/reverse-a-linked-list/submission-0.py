# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            # 1. Save the next node before breaking the link
            next_node = current.next
            
            # 2. Reverse the current node's pointer
            current.next = prev
            
            # 3. Move the two tracking pointers forward
            prev = current
            current = next_node
            
        # At the end, current is None, and prev points to the new head
        return prev
