class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = set(nums)

        maxa = [float('-inf'),float('-inf'),float('-inf')]

        for j in range(3):

            for i in nums:
                maxa[j] = max(i, maxa[j])

            if len(nums) > 0:
                nums.remove(maxa[j])

        if maxa[2] == float('-inf'):
            return maxa[0]

        else:
            return maxa[2]


'''
Time complexity: O(N) - N is number of elements in nums
Space complexity: O(1)
'''

'''
Improve points:
- Solve without removal of elements from set
- Solve without 3 iterations
'''
