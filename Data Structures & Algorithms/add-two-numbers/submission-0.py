# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy

        carry = 0

        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val
            
            new_node = ListNode(int(sum % 10))
            carry = int(sum / 10)

            curr.next = new_node
            curr = curr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node
        
        return dummy.next


