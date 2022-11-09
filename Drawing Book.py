def pageCount(n, p):
    # Write your code here
    l = []
    r = []
    for i in range(0,n+1,2):
        l.append(i)
    rev_l = l[::-1]
    for j in range(1,n+1,2):
        r.append(j)
    rev_r = r[::-1]
    if p in l:
        a = l.index(p)
        b = rev_l.index(p)
        if a<=b:
            print(a)
        else:
            print(b)
    if p in r:
        c = r.index(p)
        d = rev_r.index(p)
        if n%2==0:
            d = rev_r.index(p)+1
            if c<=d:
                print(c)
            else:
                print(d)
        else:
            if c<=d:
                print(c)
            else:
                print(d)


n = int(input().strip())
p = int(input().strip())
result = pageCount(n, p)
