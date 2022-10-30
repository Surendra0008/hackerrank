def jumpingOnClouds(c, k):
    power = 100
    i = 0
    while True:
        power = power-1-2*c[i]
        i = (i+k)%n
        if i==0:
            break
    print(power)

nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c, k)
