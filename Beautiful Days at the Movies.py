def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for p in range(i,j+1):
        r = int(str(p)[::-1])
        if (abs(p-r))%k==0:
            count+=1
    print(count)
    
first_multiple_input = input().rstrip().split()

i = int(first_multiple_input[0])

j = int(first_multiple_input[1])

k = int(first_multiple_input[2])

result = beautifulDays(i, j, k)
