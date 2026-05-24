def write_cars(car_name):#it must take a parameter
    with open('cars.txt', mode = 'w')as my_file:#write this parameter(car_name)
        cars = ['Toyota','Tesla','TLX','Nissan','Range Rover','Lamborghini','p']
        for car in cars:
            my_file.write(car + '\n')
write_cars('cars.txt')#enter the location you want to write into finally...
