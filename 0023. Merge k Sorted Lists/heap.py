import heapq
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Deleting empty lls
        # lists = [i for i in lists if i is not None]
        
        # If there is no non-empty lls
        if not lists:
            return None
        
        minHeap = []
        for idx, ll in enumerate(lists):
            if ll is not None:
                minHeap.append((ll.val, idx, ll))
        
        if not minHeap:
            return lists[0]
        heapq.heapify(minHeap)
        
        f_idx, res = heapq.heappop(minHeap)[1:]
        if lists[f_idx] != None:
            lists[f_idx] = lists[f_idx].next
        if lists[f_idx] != None:
            heapq.heappush(minHeap, (lists[f_idx].val, f_idx, lists[f_idx]))
        pre = res
        
        while minHeap:
            idx, ll = heapq.heappop(minHeap)[1:]
            pre.next = ll
            pre = ll
            
            if lists[idx] != None:
                lists[idx] = lists[idx].next
            if lists[idx] != None:
                heapq.heappush(minHeap, (lists[idx].val, idx, lists[idx]))
        
        return res