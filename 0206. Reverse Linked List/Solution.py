from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # If the linked list is empty:
        if not head:
            return head
        
        prev = None
        cur = head
        nxt = cur.next
        
        # If the ll has only 1 element
        if not nxt:
            return head
        
        # If the ll has at least 2 elements
        ## Handle the new ll tail
        cur.next = None
        prev = cur
        cur = nxt
        nxt = nxt.next
        
        ## Handle the rest of the nodes
        while cur.next:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next
        
        ## Handle the last element and Point the head of the ll to the last element
        cur.next = prev
        head = cur
        
        return head