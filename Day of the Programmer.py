def dayOfProgrammer(year):
    # Write your code here
    if year>=1700 and year<=1917:
        if year%4==0:
            print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")
    elif year==1918:
        print(f"26.09.{year}")
    else:
        if year%400==0 or (year%4==0 and year%100!=0):
            print(f"12.09.{year}")    
        else:
            print(f"13.09.{year}")
            
year = int(input().strip())

result = dayOfProgrammer(year)