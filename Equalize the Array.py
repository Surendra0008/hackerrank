def equalizeArray(arr):
    # Write your code here
    num_count = []
    for i in arr:
        num_count.append(arr.count(i))
    max_count = max(num_count)
    l_arr = len(arr)
    result = l_arr-max_count
    print(result)
    

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = equalizeArray(arr)