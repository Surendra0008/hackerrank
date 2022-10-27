def pangrams(s):
    # Write your code here
    t = s.lower()
    alphabets = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
    count = 0
    for i in alphabets:
        if i in t:
            count+=1
    if count==26:
        print("pangram")
    else:
        print("not pangram")

s = input()
result = pangrams(s)