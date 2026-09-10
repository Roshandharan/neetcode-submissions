# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
        
        return False

    #TC = O(n)
    #SC = O(1)
    # Floyd Two pointer Technique , setup slow and fast pointer; if they meet there is a cycle e
    # else no cycle