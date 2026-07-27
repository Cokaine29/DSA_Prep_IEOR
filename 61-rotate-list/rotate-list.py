# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        H = head
        temp = head 
        hold = head

        f = head
        count = 0 
        while f :
            count += 1
            f = f.next
        k = k % count 

        while k > 0 :
            while temp and temp.next and temp.next.next : 
                temp = temp.next
            

            hold = temp.next
            temp.next = None
            hold.next = H

            H = hold
            temp = hold
            k -= 1

        return hold



        