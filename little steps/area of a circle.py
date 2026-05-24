#write a code to calculate and output the area of a circle
#the area of a circle includes a constant pi and therefor you need to import math
#import math
import math
#ask user for the radius of the circle
radius = int(input('radius of the circle:'))
area = math.pi*(radius**2)
circumference = math.pi*2*radius
print('area of the circle is:%.2f ' %area)
print('circumference of the circle is:%.2f '%circumference)