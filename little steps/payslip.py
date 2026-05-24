#print payslip demonstration
#James Fairbairn 17-01-2020

#create some variables
tax_rate = 0.4
threshold = 11000

#Main program
name = input ('please enter your name:')
salary = int(input('please enter your salary:'))

tax_payable = (salary - threshold) * tax_rate
pay = salary - tax_payable

print('Payslip for:',name.rjust(8,'_'))
print('Salary.....',salary)
print('less tax....',tax_payable)
print('         ','-'*8)
print('Take home..',pay)
