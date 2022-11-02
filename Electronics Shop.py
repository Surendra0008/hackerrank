def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    sum = []
    for i in keyboards:
        for j in drives:
            if i+j<=b:
                sum.append(i+j)
    if len(sum)==0:
        print(-1)
    else:
        print(max(sum))
    
bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)