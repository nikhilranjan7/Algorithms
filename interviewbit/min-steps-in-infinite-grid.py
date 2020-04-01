class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
        steps_count = 0

        if len(A) == 0:
            return steps_count

        x, y = A[0], B[0]
        i = 1

        while(i<len(A)):
            steps_count += max(abs(A[i]-x), abs((B[i]-y)))
            x, y = A[i], B[i]
            i += 1

        return steps_count


'''
Time complexity: O(N) - N is number of elements in A or B
Space complexity: O(1)
'''

'''
Improve points:
-
'''
