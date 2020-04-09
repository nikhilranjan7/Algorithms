from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = Counter(s)
        for i in range(len(s)):
            if count_s[s[i]] == 1:
                return i

        return -1

'''
Time complexity: O(N) - N is number of elements in s
Space complexity: O(N)
'''

'''
Improve points:
-
'''
