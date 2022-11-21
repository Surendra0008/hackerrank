def gameOfThrones(s):
    # Write your code here
    even = 0
    odd = 0
    t = []
    for i in s:
        if s.count(i)%2==0:
            if i not in t:
                even+=1
                t.append(i)
        else:
            if i not in t:
                odd+=1
                t.append(i)
    if odd>1:
        print("NO")
    elif odd>=0 and even==0:
        print("NO")
    else:
        print("YES")
s = input()

result = gameOfThrones(s)
