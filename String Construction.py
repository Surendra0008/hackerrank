def stringConstruction(s):
    # Write your code here
    p = ''
    count=0
    for i in s:
        if i not in p:
            p+=i
            count+=1
    print(count)

q = int(input().strip())
for q_itr in range(q):
    s = input()
    result = stringConstruction(s)