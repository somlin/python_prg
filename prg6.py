#!/usr/bin/python3

s=input().strip()
sub_s= input().strip()

counter= s.findall(sub_s)
print(counter)

##for i in range(0,len(s)):
##    s1=s[i:]
##    print(s1)
##    if sub_s in s1:
##        counter = counter+1
print(counter)
