def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    addings = 0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    num = 0
    l_case = 0
    u_case = 0
    s_char = 0
    for i in password:
        if i in numbers:
            num+=1
        if i in lower_case:
            l_case+=1
        if i in upper_case:
            u_case+=1
        if i in special_characters:
            s_char+=1
    if l_case==0:
        addings+=1
    if u_case==0:
        addings+=1
    if num==0:
        addings+=1
    if s_char==0:
        addings+=1
    n = n+addings
    if n<6:
        t = 6-n
        addings+=t
    print(addings)
        
n = int(input().strip())

password = input()
answer = minimumNumber(n, password)
