n = int(input())
L = input().split()
L = list(map(int,L))
print(L)
m = max(L)
max2 = min(L)
print(m)
for i in L:
    if i>max2 and i<m:
        max2 = i 
print(max2)

    
