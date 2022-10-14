def diagonalDifference(arr):
    # Write your code here
    a = len(arr[0])
    lsum = 0
    rsum = 0
    for i in range(0,a):  
        lsum+=arr[i][i]
    for i in range(0,a):
        rsum+=arr[i][-(i+1)]
    ab_diff = abs(lsum-rsum)
    print(ab_diff)
    
n = int(input().strip())

arr = []

for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
