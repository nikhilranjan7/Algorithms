def isSubstring(s, w):
    return w in s
    
def StringRotation(s1, s2):
    if len(s2) > len(s1):
        return False
    i, j = 0,0
    while i<len(s1):
        if s1[i] == s2[j]:
            j += 1
        elif s1[i] != s2[j]:
            j = 0
        i += 1
    a = [s2[k] for k in range(j,len(s2))] #For string splicing is O(N^2)
    return isSubstring(s1,"".join(a))    
    
print(StringRotation("waterbottle","erbottlewat"))
print(StringRotation('foo', 'foofoo'))
