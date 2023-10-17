student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights [n] = int(student_heights[n])
num_of_student=0
for students in student_heights:
  num_of_student += 1
sum=0
for height in student_heights:  
  sum+=height  
average=round(sum/num_of_student)
print(average)