def beautifulTriplets(d, arr):
    # Write your code here
    count = 0
    for i in arr:
        if (i+d) in arr and (i+d+d)in arr:
            count+=1
    print(count)
    
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

result = beautifulTriplets(d, arr)