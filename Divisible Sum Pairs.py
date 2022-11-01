def divisibleSumPairs(n, k, ar):
    # Write your code here
    l = []
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i<j:
                if (ar[i]+ar[j])%k==0:
                    x = ar[i]
                    y = ar[j]
                    l.append([x,y])
    print(len(l))

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)
