#Ask user for their name
name = input('what is your name?:')
#Ask user for their age
age = input('how old are you?:')
age = int(age)
#country of citizenship
x = 'UK'
y = 'Britain'

#eligibility to vote
if age < 18:
    print(name, 'you are not old enough to vote')
elif age >= 18:
    country_of_citizenship = input('what is your country of citizenship?:')
    if country_of_citizenship == x:
        print(name, 'you are entitled to vote!')
    if country_of_citizenship == y:
        print(name, 'you are entitled to vote!')
    else:
        if age >= 18 and country_of_citizenship != x:  
            if age >= 18 and country_of_citizenship != y:
                print(name, 'you are not entitled to vote')
        
