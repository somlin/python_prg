

N = int(input())
for i in range(N):
    print(i,sep='',end='')
#print()
exit

def is_leap(year):
    leap_year = False
    if year%4==0:
        leap_year=True
        if year%100==0:
            if year%400==0:
                leap_year=True
            else:
               leap_year=False
    return (leap_year)

year = int(input())
print(is_leap(year))
