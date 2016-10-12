data= input()
data=data.split()
n=int(data[0])
m=int(data[1])
i=1
while i<=(n-1)/2:
    dash=1
    while dash<=(n-3*i+5):
        print("-",sep="",end="")
        dash=dash+1
    pat=1
    while pat<=(2*i-1):
        print(".|.",sep="",end="")
        pat=pat+1
    dash=1
    while dash<=(n-3*i+5):
        print("-",sep="",end="")
        dash=dash+1
    print()
    i = i+1
dash=1
while dash<=(m-7)/2:
    print("-",sep="",end="")
    dash=dash+1

print("WELCOME",sep="",end="")
dash=1
while dash<=(m-7)/2:
    print("-",sep="",end="")
    dash=dash+1
print()
i=1
while i<=(n-1)/2:
    dash=1
    while dash<=(3*i):
        print("-",sep="",end="")
        dash=dash+1
    pat=1
    while pat<=(n-2*i):
        print(".|.",sep="",end="")
        pat=pat+1
    dash=1
    while dash<=(3*i):
        print("-",sep="",end="")
        dash=dash+1
    print()
    i = i+1
print()
