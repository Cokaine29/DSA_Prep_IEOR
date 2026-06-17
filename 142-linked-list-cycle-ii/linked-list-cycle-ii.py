# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Approach 1 
        # d = set()

        # curr = head 

        # while curr :
        #     if curr not in d :
        #         d.add(curr)
        #     else :
        #         return curr
        #     curr = curr.next 
        # if not curr :
        #     return None

        ## Approach 2 

        slow = head 
        fast = head 

        while slow and fast :
            if slow.next and fast.next and fast.next.next :
                slow = slow.next 
                fast = fast.next.next
                if slow == fast :
                    break 
            else :
                return None
        
        if not slow or not fast :
            return None
        print(slow.val , fast.val)
        slow = head 

        while slow != fast :
            slow = slow.next
            fast = fast.next
        
        return slow

        
        