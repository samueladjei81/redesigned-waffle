#Ask user to input first number
x = input('choose your first number:')
x = int(x)
#Ask user to input second number
y = input('choose your second number:')
y = int(y)
#compare them and then print a message indicating which one is bigger than the other (or they are both the same) with an appropriate message
if x > y:
    print(x, 'is greter than', y)
elif y > x:
    print(y, 'is greater than', x)
else:
    print(x,'is equal to',y)

