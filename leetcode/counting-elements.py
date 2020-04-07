from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:

        count = Counter(arr)

        ans = 0
        for i in count:
            if i+1 in count:
                ans += count[i]

        return ans


'''
Time complexity: O(N) - N is number of elements in arr
Space complexity: O(N)
'''

'''
Improve points:
-
'''
