#create a program which inputs your name , age and weight
name = input('input your name:')
age = int(input('How old are you?:' ))
weight_on_earth = float(input('input your weight:'))

#calculate your age in seconds
#age = years
#age in months ==age/12
#age in days == age/365
#age in hours == age/(365*24)
#age in mins == age/(365*24*60)
#age in seconds == age/(365*24*60*60)
age_in_seconds = age / (365*24*60*60)

#calculate your weight on the moon
#1/6*weight on earth
weight_on_the_moon = weight_on_earth * 1/6

#calculate your weight on Jupiter
#2.4*weight on earth
weight_on_jupiter = weight_on_earth * 2.4

#output your age in seconds
print(name,':','your age in seconds:',age_in_seconds)
#output your weight on the moon
print(name,':','your moon weight:',weight_on_the_moon)
#output your Jupiter weight
print(name,':','your Jupiter weight:',weight_on_jupiter)