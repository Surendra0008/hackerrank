def bonAppetit(bill, k, b):
    # Write your code here
    bill[k] = 0
    sum = 0
    for i in bill:
        sum+=i
    charge = sum/2
    refund = b-charge
    if refund==0:
        print("Bon Appetit")
    else:
        print(int(refund))
# inputs
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)
