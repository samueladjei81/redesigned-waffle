def del_line(file_name,term_to_delete):#delete (the name of the file (as will show on line 11), term or string to delete from the list)
    lines =[]
    with open (file_name, mode= 'r') as my_file:
        for i in my_file:
            if not term_to_delete in i:
                lines.append(i)#here is where the reading and deleting happens
    with open(file_name, mode = 'w') as my_file:
        for i in lines:
            my_file.write(i)#this is where the 'writing the whole thing back out' occurs. 

del_line('deleting_files.txt','TLX')
#file name = deleting_files.txt
#term to delete = TLX
