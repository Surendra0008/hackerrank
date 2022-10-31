def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    c = []
    d = []
    for i in ar:
        if i not in d:
            c.append(ar.count(i))
            d.append(i)
    for i in c:
        s = i//2
        pairs+=s
    print(pairs)
        
        

n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
