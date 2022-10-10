def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeroes = 0
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
             zeroes+=1
    x = len(arr)
    p = positive/int(x)
    n = negative/int(x)
    z = zeroes/int(x)
    print (f"{p:6f}")
    print (f"{n:6f}")
    print (f"{z:6f}")

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = plusMinus(arr)
