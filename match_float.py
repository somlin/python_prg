#!/usr/bin/python3
import re

num = input().strip()
print(num)
if (bool(re.search(r'^[0-9.,]+$',num))):
    matches = re.split("[,.]+",num)
    print(num,matches)
    if '' in matches:
        matches.remove('')
    print(num,matches)
    if(len(matches)>0):
        for i in matches:
            print(i)

            
#print(matches)
#if(len(matches)>0):
    
##tests = int(input().strip())
##
##
##while tests>0:
##    data = input().strip();
##    print(bool(re.search(r'^[+-]?[0-9]*\.[0-9]+$',data)))
##    ##    if(bool(re.search(r'^[+-]?[0-9]*.[0-9]+$',data))):
####        print("Hello")
####    else:
####        print("Falas")
##    tests=tests-1

#if (bool(re.search(r'^[+-.]?([0-9]+,*)+\.?[0-9]*$',num))):
