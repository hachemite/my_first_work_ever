print("""You enter a dark room with two doors.
Do you go through door #1 or door #2 #?""")

door = input(">>>>")

if door == "1":
    print("There's a giant bear here eating a cheese cake")
    print("What do you do?")
    print("1.Take the cake .")
    print("2.Scream at the bear.\n you can suicide also if you want")
    
    bear = input(">>>>>")
    
    if bear == "1":
        print("The bear eats your face off<. Good job!")
    elif bear == "2":
        print("The bear eats your legs off . Good job! ")
    elif bear == "suicide"  :
        print(f"Well,doing {bear} is probably better.")
        print("Bear runs away.")
    else:
        print("how you are doing it you are amazing")
  
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina")
    print("1. Bleuberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input(">>>>")
    
    if insanity == "1":
        print("Your body survives powered by a minnnd of jello.")
        print("Good job!")
        
    elif insanity== "2":
        print("'it look good with you but I don't think he can help \a '")
        
    elif insanity == "3":
        input("your last word please")
        print("you die")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
    
else:
    print("shut-fuck-up choose one of them  ,\n \t>>> ({}) yes you are funny ".format(door))