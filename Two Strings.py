def twoStrings(s1, s2):
    # Write your code here
    count = 0
    for i in s1:
        if i in s2:
            count+=1
    if count>0:
        print("YES")
    else:
        print("NO")

q = int(input().strip())
for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1, s2)