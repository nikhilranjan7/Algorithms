"""
Sort a linked list using insertion sort.
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(val=float('-inf'), next=head)
        
        curr = dummy.next
        prev_curr = dummy
        while(curr != None):
            travel = dummy.next
            prev_travel = dummy
            while(travel != curr):
                if travel.val <= curr.val:
                    prev_travel, travel = travel, travel.next
                else:
                    prev_curr.next = curr.next
                    prev_travel.next = curr
                    curr.next = travel
                    break
            if travel == curr:
                prev_curr, curr = curr, curr.next
            else:
                curr = prev_curr.next
            
        return dummy.next
        

"""
ToDo:
- Remove if-else from line 37-39
"""

"""
Time complexity: O(n^2) 
Space complexity: O(1) 
"""