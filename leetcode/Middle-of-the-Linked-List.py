# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

'''
Time complexity: O(N) - N is number of nodes starting from head
Space complexity: O(1)
'''

'''
Improve points:
-
'''
