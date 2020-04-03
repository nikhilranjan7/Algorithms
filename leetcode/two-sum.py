class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()

        i, j = 0, len(nums)-1

        while(i!=j):
            if nums[i][0] + nums[j][0] > target:
                j -= 1
            elif nums[i][0] + nums[j][0] < target:
                i += 1
            else:
                return [nums[i][1],nums[j][1]]

'''
Time complexity: O(N * log N) - N is number of elements in nums
Space complexity: O(N) as one extra element is added with each element in nums
'''

'''
Improve points:
-
'''
