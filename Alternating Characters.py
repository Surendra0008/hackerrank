def alternatingCharacters(s):
    # Write your code here
    del_count = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            del_count+=1
    print(del_count)
            
    
q = int(input().strip())
for q_itr in range(q):
    s = input()
    result = alternatingCharacters(s)
