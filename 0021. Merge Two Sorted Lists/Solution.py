from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if any of the list is empty
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # if each of the list has at least 1 element
        ## list to be returned is list1
        if list1.val > list2.val:
            list3 = list1
            list1 = list2
            list2 = list3
        
        ## pointer to traverse the lists
        prev1 = None
        cur1 = list1
        cur2 = list2
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                prev1 = cur1
                cur1 = cur1.next
            else:
                prev1.next = cur2
                prev1 = cur2
                temp = cur2.next
                cur2.next = cur1
                cur2 = temp
        
        # if we reach the end of list1, attach the remaining of list2 to list1
        if not cur1:
            prev1.next = cur2
        
        return list1