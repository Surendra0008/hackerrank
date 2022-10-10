house = input().rstrip().split()
#s is the starting point
s = int(house[0])
#t is the ending point
t = int(house[1]) 
#trees_location takes input of location of apple and orange trees on x-axis
trees_location = input().rstrip().split()
#a is apple tree location
a = int(trees_location[0])
#b is orange tree location
b = int(trees_location[1])
#no_of_fruits takes input of no of apples and no of oranges fallen
no_of_fruits = input().rstrip().split()
#m denotes total no of apples fallen
m = int(no_of_fruits[0])
#n denotes total no of oranges fallen
n = int(no_of_fruits[1])
apples = []
oranges = []
app = input().rstrip().split()
org = input().rstrip().split()
for j in app:
    apples.append(int(j))
for j in org:
    oranges.append(int(j))
apple_f_loc = []
orange_f_loc = []
for i in apples:
    i= i+ a
    apple_f_loc.append(i)
for i in oranges:
    i= i+ b
    orange_f_loc.append(i)
apple_count = 0
orange_count = 0
for i in apple_f_loc:
    if i>= s and i<=t:
        apple_count+=1
    else:
        apple_count=apple_count
for i in orange_f_loc:
    if i>= s and i<=t:
        orange_count+=1
    else:
        orange_count=orange_count
print(apple_count)
print(orange_count)
