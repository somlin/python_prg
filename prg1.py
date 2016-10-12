def check_sides(l,n):
    #print(l,n)
    #l = l
    #print(type(l))
    #print(type(l[1]))
    #a=l[0]
    #b=l[1]
    #c=l[2]
    #lxy= abs(a-b)
    #lxy = abs(l[0]-l[1])
    #lyz = abs(l[2]-l[1])
    #lxz = abs(l[2]-l[0])
    #print(l,lxy,lyz,lxz)
    if l[0]+l[1]+l[2] != n:
        return True
    else:
        return False


x = int(input())
y = int(input())
z = int(input())
n = int(input())
x = [i for i in range(x+1)]
y = [i for i in range(y+1)]
z = [i for i in range(z+1)]
result = [[i,j,k] for i in x for j in y for k in z]
#print(x,y,z)
print(result)
#points = [l for l in result if check_sides(l,n) == True]
points = [l for l in result if l[0]+l[1]+l[2] != n]
print (points)




#hash value
##n = int(input())
##elements = input()
##t = elements.split()
##t = tuple(list(map(int,t)))
##print(t)
##
###print(hash(t))

