#A PROGRAM TO CHECK IF SOMEONE IS ELIGIBLE TO VOTE
#ask user for their names:
name = input('Name: ')
#ask user for their age:
age = int(input('Age: '))
#ask user for their country of citizenship
eligible_country = 'UK' or 'Britain'

if age < 18:
    print(name,'You are not yet old enough to vote!')
if age >= 18:
    country_of_citizenship = input('Please input your Country of Citizenship: ')
    if country_of_citizenship == eligible_country:
        print(name,'You are entitled to vote!')
    elif country_of_citizenship != eligible_country:
        print(name,'You are not entitled to vote!')
    

