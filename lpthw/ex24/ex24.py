print("Let's practice everything.") # line with parenthese and double quotes for output a string for user 
print('You\'d need to know \'bout with \\ that do:') # line with parenthese and single quotes for output a string for user but we add  backslash before a quote for veriefied and represent in the string like (') and before backslash to represent (\) 
print("\n newlines \t tabs.")# we add (\n)for newline mean jump to next line and add (\t) for a tab mean escape a four space

poem= """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the neeeds of love
nor comprend passion from intuition 
and requires an explanation
\n\t\twhere there is none.
"""# a variable his name is (poem) is a string with a triple quotes for a liberty in writing extend text
   # as well has newline \n an tab command \t

print("--------------") # just a string with many dash
print(poem)#print the variable
print("--------------")#like 15


five = 10 - 2 + 3 - 6
print(f"This should be five : {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans , jars , crates
    # These are the variable names WHITHIN the function
    #and are known as "local variables"(as opposed
    #to " global variables").They can be different outside 
    # the function (but they don't have to be)
    
start_point = 10000
beans , jars , crates = secret_formula(start_point)
#this calls the function and fills the three variables.
#"beans" is used instead of "jelly_beans" but it doesn't 
#matter. The variables could be called X,Y,Z if you 
#wanted .the function just fills them in with the return
#values in the order that they are listed
######################################################
# remember that this is another way to format a string
print("With a starting point of : {}".format(start_point))
#it's just like with an f"" string 
print(f"We 'd have {beans} beans , {jars} jars ,and {crates} crates.")
#Here we use the variable names as defined above
#and NOT the variable names WITHIN the function
start_point = start_point / 10 
#Reassings start-point with anew value based on the old one 
print("We can also do that this way")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We 'd have {} beans , {} jars ,and {} crates.".format(*formula))
#This version calls on the function and fills in the values 
#directly without creating intermdiate variable outside
#the function