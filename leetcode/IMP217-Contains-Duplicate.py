class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


'''
Time complexity: O(N) - N is number of elements in nums
Space complexity: O(N)
'''

'''
Improve points:
- Read about Hash collision
'''
