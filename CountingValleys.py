def counting_valleys(steps,path):
    if steps==len(path):
        level=0
        valleycount=0
        for step in path:
            if step=="U":
                level+=1
            if step=="D":
                level-=1
            if level==0 and step=="U":
                valleycount+=1
        return valleycount
    else:
        print("Invalid input")
count=counting_valleys(12,"UUDDDDUUDDUU")
print(count)