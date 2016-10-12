def percentage(details):
    details = list(map(float,details))
    per = float(sum(details))/len(details)
    return per

n= int(input())
result=[]
grades = []
marks = {}
while n>0:
    data = input()
    data = data.split()
    marks[data[0]] = data[1:]
    n=n-1
#print(marks)

name=input()
#print(name, "=>", marks[name])
per = percentage(marks[name])
print("%.2f" % per)
