class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)


        def reverse(i, j):
            if j < 0:
                return

            nonlocal nums
            while(i<j):
                nums[i], nums[j] = nums[j], nums[i]

                i += 1
                j -= 1

        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

'''
Time complexity: O(N) - N is number of elements in nums, 2 complete pass
Space complexity: O(1)
'''

'''
Improve points:
-
'''
