# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ## BruteForce 

        count = 0 
        curr = head 
        while curr :
            count += 1 
            curr = curr.next
        if count == 1 and n == 1 :
            return None
        elif count == n :
            return head.next
        front = head
        for i in range(count - n - 1) :
            front = front.next
        front.next = front.next.next
        return head

        