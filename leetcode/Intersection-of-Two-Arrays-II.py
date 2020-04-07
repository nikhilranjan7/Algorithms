from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)

        s = []

        for i in n1:
            if i in n2:
                n1[i] = min(n1[i], n2[i])
                s += [i]*n1[i]

        return s

'''
Time complexity: O(N) - N is the max(len(num1), len(num2))
Space complexity: O(N) #Could be done with one hashed and one whole pass through unhashed list
'''

'''
Improve points:
-
'''
