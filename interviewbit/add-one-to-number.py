class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        carry = 1

        first_zero = -1
        for i in range(len(A)):
            if A[i] != 0:
                break
            else:
                first_zero = i

        A = A[first_zero+1:]

        for i in range(len(A)-1, -1, -1):
            carry, A[i] = (A[i] + carry)//10, (A[i]+carry)%10

        if carry == 1:
            return [1] + A

        else:
            return A

'''
Time complexity: O(N) - N is number of elements in A
Space complexity: O(1) - Every operation is done inplace
'''

'''
Improve points:
-
'''
