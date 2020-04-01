class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count_dict = {}

        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        for i in count_dict:
            if count_dict[i] == 1:
                return i

'''
Time complexity: O(N) - N is number of elements in nums
Space complexity: O(N) # Can be converted to O(1) as if slow and fast pointer approach is used
'''

'''
Improve points:
-
'''
