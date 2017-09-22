def isUnique(string):
    count = {}
    for i in string:
        count[i] = 0
    for i in string:
        count[i] += 1
        if count[i] == 2:
            return False
    return True

print(isUnique(input("Write any string \n")))
