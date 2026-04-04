# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next # store

            # algo
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        rev = self.reverseList(head)        
        curr = rev
        count = 1
        prev = None
        while curr:  
            if count == n:
                if prev is None:
                    rev = curr.next
                else:
                    prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            count += 1
        
        return self.reverseList(rev)