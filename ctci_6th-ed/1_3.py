def urlify(string):
    string = string.split() #O(N)
    return "%20".join(string) #O(N)

print(urlify(input("Write any string \n")))
