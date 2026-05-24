#ask the user for a number and store it in a variable
user_number = input('choose a number:')
x = int(user_number)
#if the number is divisible by 3, print the message fizz
if x % 3==0 and x % 5!=0:
    print('fizz')
elif x % 5==0 and x % 3 != 0:
    print('buzz')
if x % 3 ==0 and x % 5==0:
    print('fizz buzz')
else:
    if x % 3 !=0 and x % 5 !=0: 
        print(x)
