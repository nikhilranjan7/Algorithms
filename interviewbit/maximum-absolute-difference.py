class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        sumarr_max, sumarr_min = float('-inf'), float('+inf')
        diffarr_max, diffarr_min = float('-inf'), float('+inf')
        for i in range(len(A)):
            sumarr_max = max(sumarr_max, A[i]+i)
            sumarr_min = min(sumarr_min, A[i]+i)

            diffarr_max = max(diffarr_max, A[i]-i)
            diffarr_min = min(diffarr_min, A[i]-i)

        return max(sumarr_max-sumarr_min, diffarr_max-diffarr_min)

'''
Time complexity: O(N) - N is number of elements in A
Space complexity: O(1)
'''

'''
Improve points:
-
'''
