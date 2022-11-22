def pickingNumbers(a):
    # Write your code here
    count = []
    for i in a:
        if i+1 in a:
            count.append(a.count(i)+a.count(i+1))
        else:
            count.append(a.count(i))
    print(max(count))


n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = pickingNumbers(a)
