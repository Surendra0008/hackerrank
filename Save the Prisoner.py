def saveThePrisoner(n, m, s):
    # Write your code here
    victim = (m-1+s)%n
    if victim==0:
        print(n)
    else:
        print(victim)
    
t = int(input().strip())

for i in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    result = saveThePrisoner(n, m, s)

