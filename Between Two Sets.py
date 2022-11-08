def getTotalX(a, b):
    # Write your code here
    a_factors = []
    b_factors = []
    for i in range(1,max(b)+1):
        for j in a:
            if i%j==0:
                a_factors.append(i)
    for i in range(1,max(b)+1):
        for j in b:
                if j%i==0:
                    b_factors.append(i)
    total_len = len(a+b)
    all_factors = a_factors+b_factors
    common_numbers = []
    for i in all_factors:
        if all_factors.count(i)==total_len:
            if i not in common_numbers:
                common_numbers.append(i)
    print(len(common_numbers))

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

total = getTotalX(a, b)
