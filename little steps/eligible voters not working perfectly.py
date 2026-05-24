#Ask user for their name
name = input('what is your name?:')
#Ask user for their age
age = input('how old are you?:')
age = int(age)
#condition where you are not old enough to vote
if age < 18:
    print(name, 'you are not old enough to vote')
#Ask user for their citizenship
    country_of_citizenship = input('what is your citizenship?(if country of citizenship is UK, please enter either UK or Britain):')
#condition that proves your eligibility
elif age >= 18:
    if country_of_citizenship == 'UK' or country_of_citizenship == 'Britain':
        print(name, 'you are entitled to vote!')
    elif country_of_citizenship != 'UK' or country_of_citizenship != 'Britain':
        print (name, 'you are not entitled to vote')
else:
    print(name, 'you are not entitled to vote')
