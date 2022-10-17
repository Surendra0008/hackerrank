import math
def viralAdvertising(n):
    # Write your code here
    likes=0
    p=5
    for i in range(n):
        x=math.floor(p/2)
        p=x*3
        likes+=x
    print(likes)

n = int(input().strip())
result = viralAdvertising(n)