class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        value_dict = {}
        i = 0
        while(i < len(A)):
            j = i
            s = 0
            while(j < len(A)):
                if A[j] < 0:
                    if s in value_dict:
                        if value_dict[s][0] <  j-i+1:
                            value_dict[s][0] = j-i+1
                            value_dict[s][1] = (i, j)
                    else:
                        value_dict[s] = [-1, ()]
                        value_dict[s][0] = j-i+1
                        value_dict[s][1] = (i, j)

                    i = j
                    break
                s += A[j]
                j += 1
                if j == len(A):
                    if s in value_dict:
                        if value_dict[s][0] <  j-i:
                            value_dict[s][0] = j-i
                            value_dict[s][1] = (i, j)
                    else:
                        value_dict[s] = [-1, ()]
                        value_dict[s][0] = j-i
                        value_dict[s][1] = (i, j)
            i += 1

        key = max(value_dict.keys())
        i, j = value_dict[key][1]
        return A[i:j]

'''
Time complexity: O(N) - N is number of elements in A
Space complexity: O(N)
'''

'''
Improve points:
-
'''
