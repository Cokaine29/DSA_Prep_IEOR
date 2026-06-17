# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        d = set()

        curr = head 

        while curr :
            if curr not in d :
                d.add(curr)
            else :
                return curr
            curr = curr.next 
        if not curr :
            return None

        
        