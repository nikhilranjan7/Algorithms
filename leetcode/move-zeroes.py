class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nz = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nz] = nums[nz], nums[i]
                nz += 1

'''
Time complexity: O(N) - N is number of elements in nums
Space complexity: O(1)
'''

'''
Improve points:
-
'''
