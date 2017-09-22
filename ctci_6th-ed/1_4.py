def palindrome_permutation(string):
    string = string.lower()
    string = string.split()
    a = {}
    string = "".join(string)
    for i in string:
        a[i] = 0
    for j in string:
        a[j] += 1
    odd = 0
    if len(string)%2 == 0:
        for k in a:
            if a[k]%2 !=0:
                return False
    else:
        for k in a:
            if a[k]%2!=0:
                odd +=1
            if odd > 2:
                return False

    return True

print(palindrome_permutation("Able was I ere I saw Elba"))
