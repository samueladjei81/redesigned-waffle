def append_file(car_name):
    with open(car_name, mode = 'a')as my_file:
        addition_to_cars = ['\n','Trotro','Bugati','KIA','Veyron']
        for car in addition_to_cars:
            my_file.write(car + '\n')#write these to the old list
append_file('cars_append.txt')#append to this file