ten_things = "Apples Orange Crows Telephone Light Sugar"#this is a string variable

print("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ')# by split function we transform the string to a list and we add (' ') to divise by the (" ")
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn" , "Banana", "Girl", "Boy"]#another list 
              
while len(stuff) != 10:#when the lenght of stuff is to be 10 will stop 
    next_one = more_stuff.pop()# that variable (next_one) has the last thing of more_stuff   :                       
                                       #when pop hasn't a argument will pop or appear the last thing in list and remove it
                                       
    print("Adding:", next_one)#now we use the previous variable 
    
    stuff.append(next_one)#(next_one) is the last thing  in (more_stuff) will append in list of (stuff)
    print(f"There are {len(stuff)} item now")#is will print the lenght of (stuff )    

print("There we go: ",stuff)#print(stuff)

print("Let's do some things with stuff.")

print(stuff[1])#appear the second thing in list
print(stuff[-1])#whoa! fancy    #\print the last thing in list   

print(stuff.pop())#print the latest thing in list and remove it

print(' '.join(stuff))#what cool!     #\(join)is make the list in argument a string again and 
                                      #the (" ") will join in between the things in list 
                                      
print('#'.join(stuff[3:5]))# super stellar!   \ like previous but all list will be string 
                                               \#but in range(3:5) or 3->4 (#) will join in this range 



