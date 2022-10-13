def timeConversion(s):
    # Write your code here
    a = s[0]
    b = s[1]
    c = a+b
    d= s[3]+s[4]
    e= s[6]+s[7]
    if s[8]=="P" and int(c)<12:
        c = int(c)+12
        x =(f"{c}:{d}:{e}")
        print(str(x))
    elif s[8]=="P" and int(c)==12:
        x = (f"{c}:{s[3]+s[4]}:{s[6]+s[7]}")
        print(str(x))
    elif int(c)==12 and s[8]=="A":
        c = "00"
        x = (f"{c}:{s[3]+s[4]}:{s[6]+s[7]}")
        print(str(x))
    else:
        x = (f"{c}:{s[3]+s[4]}:{s[6]+s[7]}")
        print(str(x))
s = input()

result = timeConversion(s)
