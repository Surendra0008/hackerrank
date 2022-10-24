def camelcase(s):
    # Write your code here
    count = 1
    for i in s:
        if i.isupper()==True:
            count+=1
    print(count)

s = input()

result = camelcase(s)