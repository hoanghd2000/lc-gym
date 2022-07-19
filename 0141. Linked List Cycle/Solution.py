from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if ll is empty
        if not head:
            return False
        
        # if ll has only 1 element
        if not head.next:
            return False
        
        # if ll has at least 2 elements
        ptr1 = head
        ptr2 = head.next
        while ptr1 and ptr2:
            if ptr1 == ptr2:
                return True
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
                if ptr2:
                    ptr2 = ptr2.next
        return False