class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        si, ti = len(S)-1, len(T)-1

        while(si > -1 or ti > -1):

            #si stops at non-deleted character from back
            jump = 0
            while(si > -1):
                if S[si] == '#':
                    jump += 1

                else:
                    if jump == 0:
                        break
                    jump -= 1
                si -= 1

            #ti stops at non-deleted character from back
            jump = 0
            while(ti > -1):
                if T[ti] == '#':
                    jump += 1
                else:
                    if jump == 0:
                        break
                    jump -= 1
                ti -= 1

            #check if both si and ti are not empty
            if si < 0 and ti < 0:
                return True
            elif si > -1 and ti < 0:
                return False
            elif si < -1 and ti > 0:
                return False

            #compare if non-deleted chars are equal
            #print(S[si], T[ti])
            if si > -1 and ti > -1 and S[si] != T[ti]:
                return False

            si -= 1
            ti -= 1

        print(si, ti)
        return True


'''
Time complexity: O(N+M) - N and M are number of elements in S and T respectively
Space complexity: O(1)
'''

'''
Improve points:
-
'''
