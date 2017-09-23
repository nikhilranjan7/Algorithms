def one_away(str1, str2):
    # Assume len(str1) is smaller than or equal to len(str2)
    if str1 == str2:
        return True 
    if len(str2) - len(str1) > 1:
        return False
    elif len(str2) - len(str1) == 1:
        s2 = {}
        s1 = {}
        for i in str2:
            s2[i] = 0
        for i in str2:
            s2[i] += 1
        for i in str1:
            s1[i] = 0
        for i in str1:
            s1[i] += 1
        for i in s1:
            if s1[i] != s2[i]:
                return False
        return True
    else:
        differ = 0
        s2 = {}
        s1 = {}
        for i in str2:
            s2[i] = 0
        for i in str2:
            s2[i] += 1
        for i in str1:
            s1[i] = 0
        for i in str1:
            s1[i] += 1
        for i in s2:
            if i not in s1: #O(1)
                differ +=1
            if differ > 1:
                return False
        if differ == 0:
            return True
        
print(one_away("pale","pales"))
        
