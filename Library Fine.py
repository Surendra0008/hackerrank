def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine = 0
    if y1>y2:
        print(10000)
    elif y1==y2 and m1>m2:
        a = m1-m2
        b = 500*a
        print(b)
    elif y1==y2 and m1==m2 and d1>d2:
        c = d1-d2
        d = 15*c
        print(d)
    else:
        print(0)
    
first_multiple_input = input().rstrip().split()

d1 = int(first_multiple_input[0])

m1 = int(first_multiple_input[1])

y1 = int(first_multiple_input[2])

second_multiple_input = input().rstrip().split()

d2 = int(second_multiple_input[0])

m2 = int(second_multiple_input[1])

y2 = int(second_multiple_input[2])

result = libraryFine(d1, m1, y1, d2, m2, y2)
