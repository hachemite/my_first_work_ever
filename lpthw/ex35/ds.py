from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
        how_much = int(choice)

     
        
    if how_much < 50:
        print("Nice , you're not greedy , you win!")
        exit(0)

    else:
        dead("You greedy bastard!You are dead!")

       
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey .")
    print("The fat bear is in front of another door .")
    print("How are you going to move the bear?")
    
    while True :
        choice =  input(">")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
  
        elif choice == "open door" :
            gold_room()

        else:
            print("I got no idea what that mean.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu ")
    print("He, it , whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input('>')
    if "head" in choice:

        dead("Well that was tasty!")

    else :
        cthulhu_room()

        
  
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

