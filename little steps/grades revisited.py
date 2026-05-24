#student grades list
student_grades_list = []# we use a list or square brackets here instead of curly or dictionaries because only lists have the attribute append which we would be using later on

#start while loop
while True: #instead of starting with while and a condition, since the first condition is also in the loop, we could start with while True or False to enable us embed the first condition...
    #ask user for name
    name = input('student name : ')

    if name.lower() == 'exit':
        break

    #ask user for assessment mark
    try:# used to try the code for errors. i think try is also used here instead because there was no condition and this was a new variable getting set up in the while loop
        mark = float(input('enter mark(0-100) : '))
    except:#used to help solve the problem when there is an error.
        print('ENTER A VALID NUMBER!!!')
        continue

    if mark < 0 or mark > 100:
        print('please enter mark from 1-100')
        continue
            
    if mark ==0:
        grade = 'N/S'
    elif mark >= 1 and mark <= 39:
        grade = 'F'
    elif mark >= 40 and mark <= 49:
        grade = 'D'
    elif mark >= 50 and mark <= 59:
        grade = 'C'
    elif mark >= 60 and mark <= 69:
        grade = 'B'
    elif mark >= 70 and mark <= 79:
        grade = 'A'
    elif mark >= 80 and mark <= 100:
        grade = 'A*'

    student_record = f"Student name : {name}, Mark : {str(mark)}, Grades : {grade}"
    student_grades_list.append(student_record)

    #print everything in the student record
    #this means take everything in the records one by one so we are going to use the for loop
    for items in student_grades_list:
        print(items)
        


