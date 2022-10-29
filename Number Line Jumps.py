def kangaroo(x1, v1, x2, v2):
    # Write your code here
    a = v1
    b = v2
    if x1+v1==x2+v2:
        print("YES")
    else:
        while (x1<=10000 or x2<=10000) and x1+v1!=x2+v2 :
            x1+=1
            v1+=a
            x2+=1
            v2+=b
        if x1+v1==x2+v2:
            print("YES")
        else:
            print("NO") 
        
first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)
