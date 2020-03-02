t = int(input())

while(t):

    a, b = map(int, input().split())
    n = int(input())
    wrong = False
    while(n):
        ans = (a + 1 + b)//2
        print(ans, flush=True)
        response = input()
        if response == "TOO_BIG":
            b = ans - 1

        elif response == "TOO_SMALL":
            a = ans + 1

        else:
            wrong = True
            break

        n -= 1
    if wrong == True:
        break

    t -= 1

'''
Time complexity: O(log N) - N is not 'n' but a-b+1
Space complexity: O(1)
'''

'''
Improve points:
-
'''
