#reading files
def read_names():
    with open('names.txt', mode = 'r')as my_file:
        my_file = my_file.read().splitlines()
        for i in my_file:
            print(i)
read_names()#never forget to call your function
#you might as well remove the def read_names(): and read_names() and the same result would be met...

#writing files
def write_names():
    names = ['Samuel','Felix','Dickson','Gifty','Martha','Lothian']
    with open('names.txt', mode ='w') as my_file:
        my_file = my_file.write()
        for name in names:
            return name
write_names('names.txt')

