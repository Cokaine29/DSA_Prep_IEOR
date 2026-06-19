# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # d = set()

        # nodeA = headA

        # while nodeA :
        #     if nodeA in d :
        #         pass
        #     else :
        #         d.add(nodeA) 
        #     nodeA = nodeA.next 
        
        # nodeB = headB

        # while nodeB :
        #     if nodeB in d :
        #         return nodeB
        #     nodeB = nodeB.next
        
        # return None
        

        d1 = headA
        d2 = headB
        count = 0 
        while d1 != d2 :
            d1 = d1.next
            d2 = d2.next
            if not d1 :
                if count == 2 :
                    return None
                d1 = headB
                count += 1 
            if not d2 :
                if count == 2 :
                    return None
                d2 = headA
                count += 1 

        return d1 