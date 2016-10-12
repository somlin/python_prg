import re
n= int(input().strip())
#print(n)
binary=[]
reminder = n%2
#print(reminder)
while (n>0):
    reminder = n%2
    n= int(n/2)
#    print(reminder,n)
    binary.insert(0,reminder)
print(binary)
binary = list(map(str,binary))
digits = "".join(list(map(str,binary)))
#print(digits)
matches = re.findall('1+',digits)
#print(matches)
matches.sort(reverse=True)
print(matches)
num = len(matches[0])
print(num)
