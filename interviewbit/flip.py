class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        i = 0
        minsum = float('+inf')
        l, r = -1, -1
        arr_map = {'0':-1, '1':1}

        while(i<len(A)):
            j = i
            cursum = 0
            while(j<len(A)):
                cursum += arr_map[A[j]]

                if cursum == 1:
                    i = j + 1
                    break

                if cursum < minsum:
                    minsum = cursum
                    l, r = i, j

                j += 1

            if j == len(A):
                break

        if l == -1:
            return []
        return [l+1, r+1]

'''
Time complexity: O(N) - N is number of elements in A
Space complexity: O(1)
'''

'''
Improve points:
-
'''
