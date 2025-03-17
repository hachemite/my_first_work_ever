from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
   
    
    
    try:
        how_much = int(input(">"))
    except:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit(0)
        
    elif how_much ==2004:
        print("Bravo you use a cheat code you can go the place do you want")
        print("press the letter of the place for teleport :\na-start\nb-bear room\nc-cthulhu room")
        while True:
            place = input("now choose: ")
        
            if place == "a":
                print("Here we go to start")
                start()
            elif place =="b":
                print("Here we go to the bear room I think he miss you")
                bear_room2()
            elif place =="c":
                print("Here we go to ctulhu room indeed his anice person")
                cthulhu_room()
            elif place == "d":
                print("d mean dead")
                dead("you want dead Iam wil give you!")
            else :
                print("press again that don't accept")
    
    else:
        dead("You greedy bastard!")

       
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey .")
    print("The fat bear is in front of another door .")
    print("How are you going to move the bear?")
    bear_moved = False
    
    bear_rage = False
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
    elif choice == "I love your story":
        print("now the ctulhu love you but  he ask weard question")
        print("what is my first aperance answer:")
        
        for i in range(0,4):
            date =input("what is date")
            
            if date == "1928":
                print("you are my friend you can go thank for your carring")
                exit(0)
            else:
                print(f'you have {3-i} times')
                
        dead("you don't know anything")
    else :
        cthulhu_room()
#return user to begning of this function
def bear_room2():
    print("you are funny")
    dead("the bear rage and know he eat you")
  
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
        
    elif choice == "left right" :
        print("haaaaaaa you destroy me ahhhh!")
        print("and you escape before the adventure")
        exit(0)
    else:
        dead("You stumble around the room until you starve.")
        

start()     

#function "start " is defined above 
# This is the only function automatically run in this code