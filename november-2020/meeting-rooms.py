"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals.length == 2
0 <= starti < endi <= 106
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        
        if len(intervals) <= 1:
            return True
        
        for i in range(len(intervals)-1):
            prev_start, prev_end = intervals[i][0], intervals[i][1]
            curr_start, curr_end = intervals[i+1][0], intervals[i+1][1]
            
            if curr_start < prev_end:
                return False
            
            
        return True

"""
Time complexity: O(nlogn) 
Space complexity: O(1) (As python sorting is in-place) Source: https://blog.usejournal.com/list-sort-vs-sorted-list-aab92c00e17
"""