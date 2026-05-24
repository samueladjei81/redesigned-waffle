#create a program that asks the user for a mark from 0 to 100 and prints a corresponding grade using the table to the left
mark=int(input('what is your score?'))
print('your mark is:',mark)

# corresponding grade
if mark >=int('80') and mark <= int('100'):
    print('your grade is: A*')
if mark >= int('70') and mark <= int('79'):
    print('your grade is: A')
if mark >= int('60') and mark <= int('69'):
    print('your grade is: B')
if mark >= int('50') and mark <= int('59'):
    print('your grade is: C')
if mark >= int('40') and mark <= int('49'):
    print('your grade is: D')
if mark >= int('1') and mark <= int('39'):
    print('your grade is: F')
elif mark == int('0'):
    print('N/S')

    


