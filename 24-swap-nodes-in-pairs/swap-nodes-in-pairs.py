# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next  :
            return head
        temp = head 
        final_head = head.next
        source = None
        while temp and temp.next :
            hold = temp.next
            temp.next = temp.next.next
            hold.next = temp
            if source : 
                source.next = hold
            source = temp
            temp = temp.next
        return final_head



        