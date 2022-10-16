def catAndMouse(x, y, z):
    a =abs(x-z)
    b =abs(y-z)
    if a<b:
        print("Cat A")
    elif a>b:
        print("Cat B")
    else:
        print("Mouse C")
    
q = int(input())

for i in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    result = catAndMouse(x, y, z)
