def findDigits(n):
    # Write your code here
    l = []
    count = 0
    m = str(n)
    for i in m:
        l.append(int(i))
    for k in l:
        try:
            if n%k==0:
                count+=1
        except ZeroDivisionError:
            pass
    print(count)

t = int(input().strip())

for x in range(t):
    n = int(input())

    result = findDigits(n)
