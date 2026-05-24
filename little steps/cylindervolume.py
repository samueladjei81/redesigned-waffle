#create a code to calculate the volume of a cylinder
#import math and pi
import math
#ask user to input value for radius and height
r = int(input('input radius:'))
h = int(input('input height:'))
#using math, find the area of a cylinder
area_of_cylinder = math.pi*(r**2)*h

#now calculate for area of the cylinder
print('Area of cylinder = %.2f'%area_of_cylinder)