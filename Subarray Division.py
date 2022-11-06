def birthday(s, d, m):
    # Write your code here
    i = 0
    j = m
    count = 0
    while j<=len(s):
        if sum(s[i:j])==d:
            count+=1
        i+=1
        j+=1
    print(count)

n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])
result = birthday(s, d, m)