def miniMaxSum(arr):
    # Write your code here
    minimum = min(arr)
    maximum = max(arr)
    total = 0
    for i in arr:
     total+= i
    min_sum = total-maximum
    max_sum = total-minimum
    print(min_sum,max_sum)

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
