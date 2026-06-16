# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        aage = None 
        curr = head 
        hold = head
        while hold :
            curr = hold
            hold = hold.next
            curr.next = aage
            aage = curr
        
        return aage

            

        