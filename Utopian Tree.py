def utopianTree(n):
    # Write your code here
    height = 1
    for i in range(1,n+1):
        if i==1:
            height=2
        elif i%2==0:
            height+=1
        else:
            height = height*2
    print(height)


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    result = utopianTree(n)
