from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
#I added Enter  a nimber
    choice = input(">")
    if "0" in  choice or "1" in choice :
        how_much = int(choice)
    else :
        dead("Man, learn to type a number .")
#function "dead" is defined below
     
        
    if how_much < 50:
        print("Nice , you're not greedy , you win!")
        exit(0)
#exit
#0 is a code for  an error-free exit (ws 2,16,89,etc) 
    else:
        dead("You greedy bastard!You are dead!")
#I added "you are dead"
       
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey .")
    print("The fat bear is in front of another door .")
    print("How are you going to move the bear?")
    bear_moved = False
#bear_moved is a bolean variable
    while True :# all ways the function run if you fault you go to last and you input again choice but you true you go through another function  you escape
        choice =  input(">")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:# that change the value of variable of bear_moved to False to True
            print('the bear has moved from the door.')   #finish the function but we use while for the program work again  
            print("You can go through it now.")#but variable has different value and that make a lot of differences
            bear_moved = True 
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off ")
        elif choice == "open door" and bear_moved:
            gold_room()
#function 'gold-room' was defined above
        else:
            print("I got no idea what that mean.")
#May want to add prompts to give idea
            
def cthulhu_room():
    print("Here you see the great evil Cthulhu ")
    print("He, it , whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input('>')
    
    if "flee" in choice :
#This is looks at the text you entered and if the keyword
#'flee' apears in it anywhere .is does this command
        start()
 #this function defined below 
    elif "head" in choice:
#Check for keyword "head" anywhere in entered text
        dead("Well that was tasty!")
#function "dead" defined below
    else :
        cthulhu_room()
#return user to begning of this function
        
  
def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input('>')
 
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        

start()     

#function "start " is defined above 
# This is the only function automatically run in this code