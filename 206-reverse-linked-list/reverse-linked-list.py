# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Approach 1 - Iterative

        # if not head :
        #     return None
        # aage = None 
        # curr = head 
        # hold = head
        # while hold :
        #     curr = hold
        #     hold = hold.next
        #     curr.next = aage
        #     aage = curr
        
        # return aage

        ## Approach 2 - Recursion

        if not head or not head.next :
            return head 
        rev = self.reverseList(head.next)
        head.next = None
        
        curr = rev
        while curr.next :
            curr = curr.next 
        curr.next = head

        return rev

            

        