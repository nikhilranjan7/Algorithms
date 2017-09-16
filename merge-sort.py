def merge(left, right):
    i,j = 0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i<len(left):
        result.append(left[i])
        i += 1
    while j<len(right):
        result.append(right[j])
        j += 1
    return result

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)

print(mergesort([1,4,3,6,5,1,5,7,3,1,3,5,8,5,2]))
