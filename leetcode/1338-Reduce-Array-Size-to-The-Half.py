from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        vals = sorted(Counter(arr).values(), reverse=True) #O(N)

        ans = 0
        new_len = len(arr)

        for i in vals: #O(N)
            ans += 1
            new_len -= i

            if new_len <= len(arr)//2:
                break

        return ans

'''
Time complexity: O(N) - N is number of elements in arr
Space complexity: O(N)
'''

'''
Improve points:
-
'''
