def hurdleRace(k, height):
    # Write your code here
    h = max(height)
    doses = h-k
    if doses<=0:
        print(0)
    else:
        print(doses)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)