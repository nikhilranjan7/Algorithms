a = []
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def perm(self, A, i, j):
        if i==j:
            a.append(list(A))
            return
        for k in range(i,j+1):
            A[i], A[k] = A[k], A[i]
            Solution.perm(self, A, i+1, j)
            A[i], A[k] = A[k], A[i]
        return

    def permute(self,A):
        Solution.perm(self, A, 0, len(A)-1)

t = Solution()
t.permute([1,2,3])
print(a)
