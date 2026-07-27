# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0 :
            return head
        # H = head
        # temp = head 
        # hold = head

        # f = head
        # count = 0 
        # while f :
        #     count += 1
        #     f = f.next
        # k = k % count 

        # while k > 0 :
        #     while temp and temp.next and temp.next.next : 
        #         temp = temp.next
            

        #     hold = temp.next
        #     temp.next = None
        #     hold.next = H

        #     H = hold
        #     temp = hold
        #     k -= 1

        # return hold


        count = 0
        F = head
        hold = head
        temp = head
        while temp :
            count += 1 
            temp = temp.next
        k = k % count
        if k == 0 :
            return head
        for i in range(count-k-1) : 
            hold = hold.next 
        H = hold.next
        ans = hold.next
        hold.next = None
        while H and H.next :
            H = H.next
        if H :
            H.next = F 

        return ans






        