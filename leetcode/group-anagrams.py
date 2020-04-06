class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            group.setdefault(key, []).append(strs[i])

        return list(group.values())

'''
Time complexity: O(N * K) - N is number of elements in strs, k is max size string present
Space complexity: O(N * K)
'''

'''
Improve points:
-
'''
