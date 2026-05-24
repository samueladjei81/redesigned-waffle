#write a program that prompts the user to input a temperature in celcius
C = int(input('input the temperature: '))
#formula for converting fahrenheit to celcius
F = C * (9/5) + 32
#fix C into F
print(C,'Celcius is %.1f'% F,'degrees Fahrenheit')