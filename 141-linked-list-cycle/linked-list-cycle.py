# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # # Approach 1 

        # d = set()
        # curr = head 

        # while curr :
        #     if curr not in d :
        #         d.add(curr)
        #     else :
        #         return True
        #     curr = curr.next
        # if not curr :
        #     return False 

        ## Approach 2 
        if not head :
            return False
        slow = head 
        fast = head.next
        
        while fast and fast.next and fast.next.next :

            if slow == fast :
                return True
            else :
                slow = slow.next
                fast = fast.next.next
        
        if not fast or not fast.next :
            return False 