def squares(a, b):
    # Write your code here
    print(floor(sqrt(b))-ceil(sqrt(a))+1)

q = int(input().strip())

for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])
    b = int(first_multiple_input[1])
    result = squares(a, b)
