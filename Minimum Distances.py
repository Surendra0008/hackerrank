def minimumDistances(a):
    # Write your code here
    b=[]
    d = {}
    for i in range(len(a)):
        d[i]=a[i]
    c = set(a)
    if len(c)==len(a):
        print(-1)
    else:
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i]==a[j]:
                    if abs(i-j)!=0:
                        b.append(abs(i-j))
        print(min(b))
        

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)