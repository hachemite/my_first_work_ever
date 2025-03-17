from sys import argv  #first I want to tell you this is so complicate really :=( that is arvg is a modulus you can to use the arvg

script, filename = argv # that is make you write variable in the start of program and we use just (script) for forgive the noun of my (ex16) , and filename for 
                                                           #choose a noun for the file we want to create or chose but in this exercice we want create 
                                                           
                                                           
print(f"We' re going to erase {filename}.")#in this place we want just known the noun of file for to be sure
print("If you don't want that, hit CTRL-C (^C).")# I think has any effect I m sure , but if you put (ctrl-c) is a [error]
print("If you do want that, hit RETURN.")# that true but that line has any effect I m sure 

input("?")# is normal if you hit enter to next line

print("Opening the file...")# is just a string give you an information
target = open(filename,'w')# we give the variable the power for (open) is make new file with name who chosen for( filename) or just open the (filename)\\\\ and 'r' is
                                                                                                               #is make the file just for writing
print("Truncating the file. Goodbye!")# is normal is a message for user to get attention of delete all information in file
target.truncate() # in first (target) is open the file chosen or make this file   ////// in second (truncate) it is who make the file delete his information

print("Now I'm going to ask you for three line .")# that another string give the user  a mesage to write 

line1 = input("line 1: ")# is variable (line1) offset by the string who write by the user 
line2 = input("line 2: ")# is the same withe line 20
line3 = input("line 3: ")# is the same withe line 20 , 21

print("I'm going to write these to the file.")# is message to give the user now we write the text who write in file

formated ="{}\n {}\n {}"
target.write(formated.format(line1,line2,line3))# in first (target  ) get the (filename) (the function of open)////the second is the function is (write) it is who input the text in file 

print("And finally,we close it.")#is another message to user for infomated the program finish
target.close() # we know target what do /// close function make the file save it