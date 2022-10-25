def funnyString(s):
    # Write your code here
    s_rev = s[::-1]
    svalues = []
    rev_svalues = []
    for i in s:
        svalues.append(ord(i))
    for j in s_rev:
        rev_svalues.append(ord(j))
    s_differences = []
    srev_differences = []
    for k in range(len(s)-1):
        s_differences.append(abs(svalues[k]-svalues[k+1]))
    for l in range(len(s)-1):
        srev_differences.append(abs(rev_svalues[l]-rev_svalues[l+1]))
    if s_differences==srev_differences:
        print("Funny")
    else:
        print("Not Funny")

q = int(input().strip())

for q_itr in range(q):
    s = input()

    result = funnyString(s)