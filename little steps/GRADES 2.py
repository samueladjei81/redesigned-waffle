#create a program that asks the user for a mark from 0 to 100 and prints a corresponding grade using the table to the left
grades= ['A*','A','B','C','D','F','N/A'] 

#Devise a test case scheme and test that your program produces the correct output!
score = int(input('please input your score:'))
#match score to grades
if score == 0:
    print(grades[-1])
if score >=1 and score <=39:
    print(grades[-2])
if score >=40 and score <=49:
    print(grades[-3])
if score >=50 and score <=59:
    print(grades[3])
if score >=60 and score <=69:
    print(grades[2])
if score >=70 and score <=79:
    print(grades[1])
if score >=80 and score <=100:
    print(grades[0])
elif score < 0 or score > 100:
    print('invalid')


