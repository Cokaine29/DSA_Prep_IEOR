# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def rev(head) :
            if not head or not head.next :
                return head 

            r = rev(head.next)
            front = head.next
            front.next = head 
            head.next = None 

            return r 
        if not head or not head.next:
            return True
        
        slow = head 
        fast = head.next
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        reverse = rev(slow.next)
        curr = head
        temp = reverse
        while temp :
            if temp.val != curr.val :
                return False
            temp = temp.next
            curr = curr.next 
        return True