def repeatedString(s, n):
    # Write your code here
    count = 0
    a = n%len(s)
    b = int((n-a)/len(s))
    c = 0
    for j in s:
        if j=="a":
            c+=1
    d = c*b
    e = ""
    for i in range(a):
        e+=s[i]
    for k in e:
        if k =="a":
            count+=1
    count+=d
    print(count)
s = input()

n = int(input().strip())

result = repeatedString(s, n)
