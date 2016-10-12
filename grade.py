score = input("Please eneter a score between 0.0 and 1.0: ")
score = float(score)
grade = ""
if score >=0.0 and score <=1.0:
    print("score is with in range... calculating grade")
    if score>=0.9:
        grade = 'A'
    elif score>=0.8:
        grade = 'B'
    elif score>=0.7:
        grade = 'C'
    elif score>=0.6:
        grade = 'D'
    else:
        grade = 'F'
    print("Grade:", grade)
else:
    print("Number is not in the range")

