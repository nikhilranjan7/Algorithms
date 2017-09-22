def check_permutation(str1, str2):
    a = {}
    if len(str1) != len(str2):
        return False

    for i in str1:
        a[i] = 0
    for j in str2:
        if j not in a:  #O(1)
            return False
        a[j] += 1

    for k in a:
        if a[k] == 2:
            return False

    return True

print(check_permutation('bay', 'aby'))
