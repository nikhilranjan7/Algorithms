class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphabet = {}
        output = ''
        for i in range(ord('a'), ord('z')+1):
            alphabet[chr(i)] = min([j.count(chr(i)) for j in A])
            output += chr(i)*alphabet[chr(i)]

        return(list(output))

'''
Time complexity: O(N*M) - N is number of elements in A and M is maximum size of element
Space complexity: O(N)
'''

'''
Improve points:
- Read about space complexity
    Space complexity includes auxiliary space also i.e. the space which is used by algorithm in computation but freed before returning the result. Example list comprehension at Line 6 uses O(N) space
'''
