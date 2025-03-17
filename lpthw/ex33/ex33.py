i = 0
numbers = []
#creates an empty list (similair to an array in other languages)

#for while-loops.structure is similair to ""def"" , ""if"".and
#""for-loops" , with colon at end of first line .then indent



while i < 6:
    print(f"At the top i is {i}")
#Can also be written as i += 1
#Note: In other languages you can write "i ++ " but
#doesn't work in python
#On  the last loop , the increment raises i to 6 but items
#doesn't gget added to the list or get printed because
#it happens after the print and append but before the 
#loop returns to "while i < 6" .which stops the loop. 
    
    
    numbers.append(i)

    i = i + 1
    print("Numbers now :",numbers)
    print(f"At the bottom  i is {i} ")
    
    
print("The numbers :")

for num in numbers:
    print(num)
        
#The from the study drills

#1.convert this while-loop to a fu,ction that you can call .
#  and replace 6 in the test (i < 6)with a variable

print("converting while-loop to function drill_l")

def drill_l (n):
    i = 0
    numbers1 =[ ]
    while i < n:
        print(f"Item is {i}")
        numbers1.append(i)
        i += 1 
    print(numbers1)
    
#2.Now use this function to rewrite the script to try different numbers.

print("using drill_l with n =3")
drill_l(3)

print("using drill_l with n =8")
drill_l(8)



#3.Add nother wariable to the function arguments that you can pass in
#that lets you change the +1 on line 8 so you can change how much it increment by.

print("Creating function drill_3 to allow variable step size")

def drill_3(n,s):
    i=0
    numbers3 =[]
    while i<n:
        print(f"Item is {i}")
        numbers3.append(i)
        i = i +s 
    print(i)
    print(numbers3)

#4.Rewrite the  script again to use this function to see what effect that has.

print("Using drill_3 with n = 12 and s= 3")
drill_3(12,3)


# 5.Now write it to use for loops and range instead. Do you need the 
#incrementor in the middle anymore ? what happens if you do not get 
# rid of it ?

print("drill_5 uses a for loop and range instead")

def drill_5(n,s):
   
    numbers5 = [i for i in range(0,n,s)]
    #need to specify  starting point of 0 so Python
    #reads the other element correctly
    for i in   numbers5:
        print(f"Item is {i}") 
    print(numbers5)
    
drill_5(14,4)