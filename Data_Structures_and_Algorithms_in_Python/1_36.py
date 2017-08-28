a = list(input("Write any string\n"))

k = []

for i in range(len(a)):
    count = 1
    for j in range(i,len(a)):
        if a[i]==a[j] and i!=j:
            count += 1
    k.append((a[i],count))

print(k)
