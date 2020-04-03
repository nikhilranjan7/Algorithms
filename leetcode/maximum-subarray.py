class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        i = 0
        maxsum = float('-inf')

        while(i<len(nums)):
            j = i
            currsum = 0
            while(j<len(nums)):
                currsum += nums[j]
                maxsum = max(currsum, maxsum)
                if currsum < 0:
                    i = j
                    break
                else:
                    j += 1

            i += 1

        return maxsum if len(nums) != 1 else nums[0]

'''
Time complexity: O(N) - N is number of elements in nums
Space complexity: O(1)
'''

'''
Improve points:
-
'''
