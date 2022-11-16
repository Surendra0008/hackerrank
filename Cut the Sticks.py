def cutTheSticks(arr):
    # Write your code 
    b = [len(arr)]
    while len(arr)>0:
        a = min(arr)
        for i in range(len(arr)):
            arr[i]=arr[i]-a
        while 0 in arr:
            arr.remove(0)
        if len(arr)>0:
            b.append(len(arr))
    for j in b:
        print(j)
    
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)
