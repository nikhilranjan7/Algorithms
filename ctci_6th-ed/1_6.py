def string_compression(s):
  i, j = 1,1
  a = [s[0],1]
  while i<len(s):
    t = s[i]
    if t == s[i-1]:
      a[j] += 1
    else:
      a.append(t)
      a.append(1)
      j += 2
    i += 1
  if len(a)>len(s):
    return s
  return "".join(a) 
  
print(string_compression("aabcccccaaa"))
