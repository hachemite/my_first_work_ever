from sys import argv

script , input_file = argv
#create a function to display an entire text which reads and prints the input
#file. "f" is just  a variable name for the file
def print_all(f):
    print(f.read())
    # Create a function to go the begeinning of  file # Creates a function 'rewind(f)' which sets the input files current position 
    ## to 0 via the 'seek()' function (this is in bytes i.e the start of the file)
def rewind(f):
    f.seek(0)
# Calls the function 'rewind()' with the parameter 'current_file' which should   #
# reset the files current position to 0, i.e. to the beginning.                  #
# I'm guessing this is needed because we already read/printed the whole          #
# file so the current position is the end of the file.                           #
# UPDATE - commenting out the line below and running the script doesn't print    #
# the lines out, which would suggest the files current position  at this         #
# point in the script is at the end of the file.                                 #
#################################################################################



####################################################
#create a function to print out one line .where 
#line_count is the the line number we want to read
# f is  the name of the file (from above ), and
# readline is a built - in function or method .
def print_a_line(line_count,f):           
    print(line_count,f.readline())
 # # ####################################################################################
# # !  #! NOTE !- readline() reads a single line up to the \n character but leaves the ###
# #\n character at the end of the line, so this automatically advances the file       #####
# #position by 1 line for every time the function is called and leaves a blank       #######
## newline in place. That why there's a line break in the output code.     #####################
## That's how this script is reading, printing and advancing each line in turn.##################
####################################################################################
current_file = open(input_file) # is a variable 

print("First let's print whole file\n")#just a string

print_all(current_file) # you use the function with variable (current_file)---->print(open(input_file).read())

print("Now let's rewind , kind of like a tape.")#just a string

rewind(current_file)# you use the function with variable (current_file) ------> open(input_file).seek(0)
print("Let's print three lines :")#just a string

current_line = 1 # (current line) is (variable) offset a number and his different of the variable (current_file)
print_a_line(current_line, current_file)# when you use (readline) is not (readlines) is so different if use (readline) 
                                     # is print the lines in order if you use it in first time you print the first line   
current_line = current_line + 1 # 1+1
print_a_line(current_line,current_file) #when use (readline )in in second time you print the second line  

current_line = current_line + 1  #2+1
print_a_line(current_line, current_file)#when use (readline )in in third time you print the third line  


#----<>>print(1,open(input_file).readline())

