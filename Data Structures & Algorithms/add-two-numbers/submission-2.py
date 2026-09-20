# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        result=ListNode(0)
        curr1=l1
        curr2=l2
        curr3=result
        while curr1 or curr2 or carry:
            val1=curr1.val if curr1 else 0
            val2=curr2.val if curr2 else 0

            summ=val1+val2+carry
            if summ<10:
                carry=0
                curr3.next=ListNode(summ)
            else:
                carry=1
                curr3.next=ListNode(summ-10)
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
            curr3=curr3.next
        
        


        return result.next