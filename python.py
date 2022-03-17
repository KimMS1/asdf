marks = [90, 25, 67, 45, 80]

number = 0 
for i in marks: 
    number += 1
    if i >= 60:
        print("%d 번 학생은 %d 점 이상이므로 합격입니다." %(number,i))
    else:
        print("%d 번 학생은 %d 점 미만이므로 불합격입니다." %(number,i))