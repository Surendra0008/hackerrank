def angryProfessor(k, a):
    # Write your code here
    late_commers=0
    time_commers=0
    for i in a:
        if i>0:
            late_commers+=1
        else:
            time_commers+=1
    if time_commers>=k:
        print("NO")
    else:
        print("YES")
t = int(input().strip())


for I in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)
