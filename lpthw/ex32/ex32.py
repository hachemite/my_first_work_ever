the_count = [1,2,3,4]
fruits = ['apple', 'orange' , 'pears' , 'apricots']
change = [1 , 'peenies' , 2 , 'dimes' , 3 , 'quarters']
#In Python these collections of data are called "lists."
#In many other languages they are called "arrays."



#for-loops structure is similair to 'def' and "if".
#with colon at end of first line.then indent

#this first kind of for -loop goes through a list
for number in  the_count :
#The first variable (right after "for") can use 
#any name you like altough ""
    print(f"This is count {number}")
# f function to excute the number variable   

 
#same as above
for fruit in fruits :
#just don't use the same name twice
    print(f"A fruit of type : {fruit}")
#f function to excute  the fruit name variable are the strings
    
#also we can go through mixed list too
#notice we have to use {} since we don't know what's i it    
for i in change:
#"i" is most common variable name for loops
    print(f"I got {i}")
#f function to excute i mixed variable are the strings  

   
#we can also build lists , first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
#Range starts at first number (inclusive) but
#stops at I less than second number (exclusive)
#This is how items in a list are numbered
#But 0 as first number is default  so this can
#also be written as "range(6)"
#Can also specify wheter range goes uo down 
# and size of steps.
    print(f"Adding {i} to the list")
    # append is a function that list understand
    elements.append(i)
# This adds the number to the list one at a line
    
    
#now we can print them out too
for i in elements:
    print(f"Element was: {i}")
    
#And here"s an easier way to do fill in the list in one command
element2 = range(0,6)
for i in element2:
    print(f"element2 item was {i}")