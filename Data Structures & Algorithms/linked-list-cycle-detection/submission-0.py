# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index=set()
        curr=head
        while curr:
            if curr.next in index:
                return True
            index.add(curr.next)
            curr=curr.next
        return False
            