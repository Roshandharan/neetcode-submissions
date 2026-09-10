# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy

        for _ in range(n+1):
            ahead = ahead.next
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next

        return dummy.next
#tc = O(m)-(lenght of linked list)
#sc = O(1)
# intialize dummy ahead and behing, push ahead n+1 times into the Linked list
# now increment aheah and behing until they end of list
# set behind.next to one up front

        