a = 'catdog'
k = []
#Noob solution using six for loops
for i in a:
    k.append(i)
    for j in a:
        if i!=j:
            k.append(i+j)
            for z in a:
                if j!=z and i!=z:
                    k.append(i+j+z)
                    for l in a:
                        if j!=l and i!=l and z!=l:
                            k.append(i+j+z+l)
                            for m in a:
                                if j!=m and i!=m and z!=m and l!=m:
                                    k.append(i+j+z+l+m)
                                    for n in a:
                                        if j!=n and i!=n and z!=n and l!=n and m!=n:
                                            k.append(i+j+z+l+m+n)

print(k)
#TODO Devise a recursive solution
