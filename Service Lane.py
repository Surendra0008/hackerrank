def serviceLane(n, cases,width):
    # Write your code here
    for i in cases:
        a = min(i)
        b = max(i)
        print(min(width[a:b+1]))

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
t = int(first_multiple_input[1])
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))
result = serviceLane(n, cases,width)
