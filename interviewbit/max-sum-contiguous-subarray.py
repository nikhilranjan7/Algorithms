class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):

        all_non_pos = True
        for i in A:
            if i > 0:
                all_non_pos = False
        if all_non_pos:
            return max(A)

        maxsum = 0
        i = 0

        while(i<len(A)):
            j = i
            currsum = 0
            while(j<len(A)):
                currsum += A[j]
                maxsum = max(maxsum, currsum)

                if currsum < 0:
                    break

                j += 1

            i = j+1

        return maxsum

'''
Time complexity: O(N) - N is number of elements in A
Space complexity: O(1)
'''

'''
Improve points:
-
'''
