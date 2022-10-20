def migratoryBirds(arr):
    # Write your code here
    a = arr.count(1)
    b = arr.count(2)
    c = arr.count(3)
    d = arr.count(4)
    e = arr.count(5)
    f = [a,b,c,d,e]
    g = f.index(max(f))
    birds_types = [1,2,3,4,5]
    print(b[g])
    
arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)
