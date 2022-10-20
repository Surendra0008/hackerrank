def breakingRecords(scores):
    # Write your code here
    count_min = 0
    count_max = 0
    min = scores[0]
    max = scores[0]
    for i in scores:
        if i<min:
            count_min+=1
            min = i
        if i>max:
            count_max+=1
            max = i
    print(count_max,count_min)

n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)
