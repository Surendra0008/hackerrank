def jumpingOnClouds(c):
    # Write your code here
    steps = 0
    i = 0
    while i<len(c)-1:
        if i+2<len(c) and c[i+2]==0:
            steps+=1
            i+=2
        else:
            steps+=1
            i+=1
    print(steps)

    
n = int(input().strip())
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)
