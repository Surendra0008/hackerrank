def permutationEquation(p):
    # Write your code here
    l1 = []
    for i in range(1,len(p)+1):
        l1.append(p.index(i)+1)
    for j in l1:
        l2 = p.index(j)+1
        print(l2)
n = int(input().strip())

p = list(map(int, input().rstrip().split()))

result = permutationEquation(p)
