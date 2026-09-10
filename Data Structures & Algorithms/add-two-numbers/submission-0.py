# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_values = []
        l2_values = []

        curr = l1
        while curr:
            l1_values.append(str(curr.val))
            curr = curr.next
        
        curr = l2
        while curr:
            l2_values.append(str(curr.val))
            curr = curr.next
        
        l1_values = l1_values[::-1]
        l2_values = l2_values[::-1]

        l1_num = int(''.join(l1_values))
        l2_num = int(''.join(l2_values))

        new_digits = str(l1_num+l2_num)[::-1]
        dummy = ListNode()
        curr = dummy
        for d in new_digits:
            curr.next = ListNode(val = int(d))
            curr = curr.next
        
        return dummy.next
    #TC: O(n+m) (add lenght of both words)
    #SC : O(n+m)

    # store in list as string, then rotate list and join list with int type cast
    # add numbers and convert to strong and rotate
    # for each character create node and crave path from


