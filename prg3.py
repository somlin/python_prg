def grade_2nd(grades):
#    print (grades)
    min_grade = float(min(grades))
    check_grade =float(max(grades))
#    print(min_grade,check_grade)
    for l in grades:
#        print(l)
        l = float(l)
        if check_grade>l and l>min_grade:
            check_grade = l
    return check_grade

n= int(input())
result=[]
grades = []

while n>0:
    name = input()
    grade = input()
    result.append([grade,name])
    grades.append(float(grade))
    n=n-1
#print(result)

check_grade = grade_2nd(grades)
#print(check_grade)

final = [l for l in result if float(l[0]) == check_grade]
final.sort()
#print(final)
for l in final:
    print(l[1])
    
#print(check_grade)
#result.sort(reverse=True)
#print(result)
#max_grade = result[0][0]
##print(max_grade)
