from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev1 = None
        ptr1 = head
        ptr2 = head
        
        # ptr2 is n nodes ahead of ptr1
        for i in range(n):
            ptr2 = ptr2.next
        
        # Incrementally traverse the linked list with both ptr1 and ptr2, until ptr2 reaches the end of the linked list
        while ptr2:
            prev1 = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        # If the nth node from the end of the list is the head node
        if not prev1:
            head = ptr1.next
        else:
            prev1.next = ptr1.next
        
        return head