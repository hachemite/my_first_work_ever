from math import sqrt
from random import randint,randrange
from sys import exit
money=0#help to buy item by his quantity
debt = 0#just obstacle if 0 good more than 0 very bad
sword = False#the item who help to kill dragon if he( True)  is false in t he change the start but he change the statement if you buy it
ring = False#the item very important to end story if he True

def bankint():#just a warning for plauer if not return the money
    print("Warning, you must return the money before you end your adventure")
    print("or your destiny will be the same as those of your predecessors")
    town()

def monster():#I want just action in my game by doing fight with dragon for make money or doing other thing like take egg
    global sword # sword and ring in the function not working for this reason we choose global to computer understand is the same variable in the start
    global money
    print("Now the action begin .")
    print("There is the legendry dragon 'Nar Lahab' . ")# just string
    print("The dragon has bunch of baby dragon egg ")
    print("The dragon front of another door it's look like is full of gold and jewels ")
    print("What will you do to overcome this hurdle")

    dragon_move = False# other varible but this is local is working just here

    while True:# to the function loop forever ,I'm using to repeat the action or if you have choice doesn"t exist
        choice = input(">>")
        
        if choice == "take egg":
            dead("The dragon looks at you then burned your face off.")#end
            
        elif choice == "taunt dragon" and not dragon_move:# not mean > drangon_mine == False
            print('the dragon has moved from the door.') 
            print("You can go through it now.")
            dragon_move = True # change the value of the variable 
            
        elif choice == "taunt dragon" and dragon_move:# you should to be both True for the program work / write just dragon_move mean dragon_move == True
            dead("A dragon crushed you with his feet like insects")
            
        elif choice=="open door" and dragon_move:#is trap
            print("This room if full of gold ,how much you take.")
            input(">")
            dead("You greedy bastard!You are dead!,also this is a trap") 
                                                                         
        elif choice=="fight" and sword==False:#like the way of  previous function 
            print("Your fists are weak, it does not hurt a dragon, it is only tickling")
            dead("Indeed, you already die after your head explode with his thunderous laughter")    
        
        elif choice=="fight" and sword==True:
            print("You goin forwad and by the sword irith ou stabbed his belly without resistance.")
            print("From the wound, something mixed with blood came out, what is this?")
            print("Is this a ruby that he swallowed before, is look so precious and ")
            print("I think he cost 10000G")
            print("Now should return to the town , don't worry about the dragon and his baby she cannot die easily.")
            money += 10000# increase the global variable money to 10000
            town()# return to start
        else:#is the sentence if you write a anwser doesn't exist
            print("I got no idea what that mean.")
def bank():#the easy way to get money but has an expensive price is your life \ if you want get money the debt and money increase and if you return money the debt and money decrease


    global money#make local variable to global
    global debt
    print(f"""hello player this is the bank if you want get money
    but you will receive a debt you should pay it by return money
    
    for: get money-->press'a'
    return money -->press'b'    """)
    
    while True:#infinty loop help if is a wrong anwser
       
        cho = input("choose >\t")
        
        
        if cho == 'a' or cho == 'get money':#that simple if because is just increase the debt and money by the quantity money who input the player 
            try:#if the player write a string is make error w should use try and except
                hm_get = int(input("how much-->  "))#how much get
            except:
                print("please I don't understand ,you should put a number")
                bank()#if he wrong he return of the begining  of function bank
                
            money += hm_get #like I said is increase by number  input hm_get cho
            debt += hm_get#the same
            bankint()#function for warning
            
        elif cho == 'b' or cho == 'return money':# is more complex
            if debt==0:#if the player has no debt is cannot return money
                print("You don't have anything to return,please come back again.")
                town()#return to the start
            
            else:# in other case is continue
                try: # we put this for avoid error 
                    hm_re = int(input("how much-->   "))#how much return
                except:
                    print("please I don't understand ,you should put a number")
                    bank()#if he false return to the begining of the function
                    
                if hm_re > money:# we have more here if the player a big number 
                    if money > debt:#first case money bigger than debt is substract the debt in money and make 
                        money -= debt#debt  zero because like you give him all money and give you the rest
                        debt=0
                        
                    else:#that the reverse if money lower mmake money 0 and substract money from debt 
                        debt -=money
                        money = 0
                    bankint()
                    
                else:#if the player give precise number and make that lot easier just subtract the hm_r from money and debt
                    if money> debt:
                        money -= hm_re#we do that for debt don"t make a negative number and this make a big problem
                        debt =0
                    else:
                        money -= hm_re
                        debt -= hm_re
                    bankint()
        
        else:
            print("please precise")# for the program don't stop
            
def merchant():# buying item who help fo to end adventure or doing other stuff 
    #we make the variable global for the function effect in the variable in the start
    global sword
    global ring
    global money

    print("Hello there player this is the merchant  , ")#strings
    print("I think there are two things you may like. ")
    print("Firstly ,the golden ring or 'Turkra',")
    print("by this any women can accept you to marry her.")
    print("Second, the irith sword has a demonic power can kill the most powerful monster.")

    print("Here they are, aren't they awesom. ")
    print("""
    \t ____________________________
    \t|''golden ring''|'''sword '''|
    \t|----------------------------|            
    \t|*****4000G*****|***2000GG***|
    \t|_______________|____________|""")#is just """ for give the liberty to make the table with nice form

   

    while True:#infinty loop to make the else always work if the player if he fault
        cho = input("You want buy something?(yes/no)\n")#yes or no question
        if cho== "no":
            print("If you want something, please come back again")
            town()#imediatly return to the town

        elif cho=="yes":#the begining of new series if function

            while True:# this is  new infinity loop
                cho = input('what do you want the sword or the ring\t')
                
                if cho == "sword":#make sword = True and substract 2000 from money and after return to town()
                    if money >= 2000:
                        print("Now you get the irith sword!")
                        sword = True 
                        money -= 2000
                        town()
                    else:#stop by a message if you not have enough money 
                        print("Sorry sir you don't have enough money!")
                        print("you should return to town and make more money by working!")
                        input()
                        town()
                elif 'ring' in cho :
                    if money >=4000:#make ring = True and substract 4000 from money and after return to town()
                        print("Now you get the irith sword!")
                        ring = True
                        money -= 4000
                        town()
                    else:#stop by a message if you not have enough money
                        print("Sorry sir you don't have enough money!")
                        print("you should return to town and make more money by working!")
                        input()
                        town()                
                else :
                    print("I don't understand please repeat. ")
                    
           
        else :

            print("I don't understand please repeat. ")

def library():# is like manuel or cotent who help you in adventure by give information about the world # this is just a big strings 
    print("Hello player I'm Zina the library lady.")
    print("I can help you to get the knowledge and information about the all places in the town ")#strings
    print("Because you are new I will give you anwser about your question and free trials to read")
    while True:#yes a lot of while loop
        print('I think this list of questions and books , it may interest you. ')

        print("**************************************************************************************************************")
        print('-learn math the hard way')
        print("==============================================================================================================")
        print("-information about bank?")
        print("--------------------------------------------------------------------------------------------------------------")
        print("-school need help!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("-what you need to mary?")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("-merchant")
        print("______________________________________________________________________________________________________________")
        print("-town secret")
        print("##############################################################################################################")
        print("-return town  just write -> town")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////")

        cho = input('\nWhat you need sir , I \' exited to anwser your question .\\\\\\\-->>>\t')

        if cho=='learn math the hard way':
            print("the lady: this book can help you to solve the math question.")
            print('BOOK-->\n              learn math hard way\n')
            input()
            print("\nthe lesson 01: Ordering Numbers Ascending ")
            input()
            print("""Read and write multi-digit integers using the ten basic numbers, number names, and extended formula.
Compare two multi-digit numbers based on the meanings of the numbers everywhere, using the symbols <, = and <
to record the results of comparisons.""")
            input()
            print('\nthe lesson 02: Equation of 1st degree')
            input()
            print("1) What is an equation?")
            input()
            print("""When we want to solve an equation including one unknown variable, as x in the example above, 
we always aim at isolating the unknown variable. 
You can say that we put everything else on the other side of the equal sign. 
It is always a good idea to first isolate the terms including the variable from the constants 
to begin with as we did above by subtracting or adding before dividing or multiplying away the coefficient in front of the variable. 
As long as you do the same thing on both sides of the equal sign you can do whatever you want and in which order you want.""")
            input()
            print('\nthe lesson 03: Equation of 2nd degree')
            input()
            print("""The quadratic equations are simple but you have to learn the different formulas.

Before giving the formulas, we will define what a second degree equation is.

It is an equation of the form ax² + bx + c = 0 (with a non-zero)


To be able to solve such an equation, it is first necessary to calculate the discriminant Δ.

To calculate it, it's easy, just apply this formula:

    Δ = b² - 4ac

We calculate it. Then, depending on the result, we will be able to know the number of solutions that there are, and find them if there are any.

    If Δ <0, nothing could be simpler: there is no solution.

    If Δ = 0, there is only one solution to the equation: it is x = -b / (2a)

    If Δ> 0 there are two solutions which are x1 = (-b-√Δ) / (2a) and x2 = (-b + √Δ) / (2a)


Now it is possible for you to solve a quadratic equation.""")

         
        if cho =="information about bank":
            print("""lady:Recently we heard about the killing of many people in a brutal way, 
and the common thing between them is that they were all happy before they died or had a great time,
but also all of them were lending some money from the bank and they have not returned it yet.
And by that I concluded that the bank owners are brutal killers and eagerly
await to kill their victims if they do not pay the debt, so you should count yourself or return it quickly""")
            


        if cho=="school need help":
            print("lady:Recently it has decreased the level of education in the city where the teachers themselves are unable to solve the issues themselves,\nwhat a shame.")
            
            input()
            print("So please help them, although they will try to show themselves that they are competent, so do not bother, there is a financial reward")
            


        if cho =="what you need to mary":
            print("lady:I think if you offered me the golden ring I would accept your marriage without hesitation")
            input()
            print("But whatever cares, I'm just a 60-year-old divorced woman running a book store T_T")

        if cho == 'merchant':
            print("He is a nice man who sells unique products and without a doubt high quality.")
            print("In my opinion, he is a wonderful , beautiful person,haot and a of course an honest person ...ihm ihm sorry I have overlooked")
            input()
            print("I think he can help you on your adventure and goal, so it is necessary to go to him")



        if cho == 'town secret':
            print("BOOK")
            print("---------------------------------------the secret of town-------------------------------------")
            
            input()
            
            print("""In ancient times, grandparents gathered to stop the bloody war that was A
to start because the invaders approached the city, so they summoned two sets of slogans and legends.
Mythos brought three animals, the snake, the symbol of immortality, the hawk, the symbol of courage and hardness
, and the goat the symbol of hell, or because I have centuries
As for the slogans, I made a bloody ruby
In the end, they put these components in a hole, then put the philosopher's stone, and thus something unknown was born""")
            
            input()
            print("To enter the secret place, it is under the fountain\n")
            print("\n{{{{{{{<Return to town and press 'm' to go to the secret place }}}}}}}}}")
            
            input("")
            print("Lady: is just a story for little kids.")
            
        if cho == "town":
            print("Now you return")
            town()
            exit()
            
        else:
            print("I don't understand you , you can repeat?")
            input()
        
def school():#the way how get money by using your knowledge about math

    print("Hello player, now you are in the school and you can make lots of money by solve exercice")#strings
    print('You have many choices to choose from easy to the the more hard ,and absolutly more hard more money')
    print("""this the choices :
    ---------------------------------------------------------------------------------------------------
    -exercice 1 : make the number in order from the less to great\ the chest is 1000 G --->\t(press'1')

    ---------------------------------------------------------------------------------------------------
    -exercice 2 : solve equaution of first degree \ the chest is 2000G-------------------->\t(press'2')

    ---------------------------------------------------------------------------------------------------
    -exercice3: solve equaution of second degree \ the chest is 3000G--------------------->\t(press'3')

    ---------------------------------------------------------------------------------------------------""")#strings

    global money#make money uselable
    while True:#yes other while loop you know why
        cho = input("Now choose the execice who want")#is ask you a number but is string
        
        if cho == '1':
            l = []# empty list 
            for i in range(0,6):# make the sequence repeat 6 times
                x   = randint(1,100)# every time x get random integer value
                l.append(x)#for every time x have a different is enter/append the list l
            print("after seeing this list you should make the number in order from less to the great")
            print("*********************************************************************************")
            print("This is list the list--->\t",l)
            input("press enter to start order")
            t = []#empty list
            for i in range(1,7) :#make the sequence repeat 6 times
                try:
                    z = int(input(f"write the number {i} and if you sure press enter to continue:\t"))#there you should full the list t
                except:
                    dead("You don't know how write a number")
                t.append(z)# enter the value of x who write in the list t
            print('this th first list ----->:\n',l)
            print('that after your order--->\n',t)
            l.sort()#make number in order from lowest to biggest
            if t == l :# if the t equal l you money increase 1000 and return to the town
                print('your awser is right good job',l)
                print("this your chest 1000G")
                money +=1000
                print('thank you can now return to the town')
                town()
            else:# the penality of stupid is dead 
                print('you have a false anwser this is the right anwser',l,'t\nyou nothing ')
                dead('Idiot what are you doing here ,you west my time')
                
        elif cho =='2':
            print("Now after seeing this equation you should give the anwser")
            a =[2,-3,-4,5,6,-7,-8,9,10,-11] # I make with this list precious for give a good result

            b =[24,27,-28,55,-48,7,64,81,-500,165]

            c = randint(0,100)#random from integer

            z = randint(0,len(a))
            a1 = a[z]
            b1 = b[z]
            x = ((c- b1)/a1)
            fx= round(x,2)#2 number after .
            print(a1,'x','+',b1,'=',c)# present the equaution
            print('this is a:',a1,'\t','this is b:(',b1,')\t','this the result:',c)
            
            
            try :#for avoid error
                fxa = float(input('now give the value of    x='))
            except:
                dead("you don't know how write a number go out of here")
                
        
            if fxa ==fx:#if you right the money increase to 2000
                print("Good job get your chest is ")
                print("now you have 2000G")
                money += 2000
                town()
            else:#not you die
                print("That not your day \v you have a false anwser ")
                print('That right anwser',fx)
                dead("please don't enter if you not ready ")
        
        elif cho =='3':
            print("Now after seeing this equation of second degree you should give the anwser")

            a =[1,1,1,4,-1,1]
            b =[1,3,1,4,2,4]
            c =[-2,2,1,1,-3,0]



            i = randrange(0,len(a))
            a1=a[i]
            b1=b[i]
            c1=c[i]


            delta = b1**2-4*a1*c1

            print(f"{a1}x²+({b1})x+({c1})")
            print('a=',a1,"b=",b1,'c=',c1)



            try :
                an = int(input())
            except:
                dead("You don't know how write a number !")
                
                
            if an == delta:
                
                print('Right,good job ,we continue!')
            else:
                print("From the begining you have a false anwser, get out ")
                town()


            try :
                x1=((-b1)-sqrt(delta))/2*a1
                x2=((-b1)+sqrt(delta))/2*a1
                input("Know you should found the value of x 'press enter to continue'")
            except:
                input("Know you should found the value of x 'press enter to continue'")
              

            #the first part like exercice 2 in school function              
            
            for i in range(3,0,-1):#make the player have 3 tries
                k = i-1 # that just a variable give me the number of try rest
            
           
            
            #in every result of delta is more if statement
            
                if delta==0:#is this occasion 1 result and you get 3000 money
                    try :
                        an = float(input("what x1 equal :"))
                    except:
                        dead("Whaat! before a few second you know how write  a number !")
                            
                    if an==x1:
                        print("Bravo you have the Right anwser now get your chest 3000G")
                        money += 3000
                        town()
                        exit(0)
                        
                    else:
                        print(f"very bad you have {k}tries")
                        
                if delta > 0:##is this occasion 2 result and you get 3000 money
                    
                    print("what x1,x2 equal :")
                    
                    try :
                        an1 = float(input("what x1 equal :"))
                        an2 = float(input("what x2 equal :"))
                    except:
                        dead("You don't know how write a number")
                        
                    z = (an1==x1 or an1==x2)and(an2==x1 or an2==x2)
                    if z == True:
                        print("Bravo you have the Right anwser now get your chest 3000G")
                        money += 3000
                        town()
                        exit(0)
                    else:
                        print(f"very bad you have {k}tries")
                            
                if delta < 0:#that differnt because the resutt not number is string
                    print("what x1,x2 equal :")
                    
                    try:
                        an1 = input("what x1 equal :")
                    except:
                        dead("You don't know how write a nummber")
                        
                    if "impossible" in an1:
                        print("Bravo you have the Right anwser now get your chest 3000G")
                        money += 3000
                        town()
                        exit(0)
                    else:
                        print(f"very bad you have {k} tries")
                           
            dead("very bad your anwser is false but the more important is participation")
                    
                        
        else:
            print('you don\' know write a number')

def dead(why):#dead is dead or the bad end
    print(why,"Good work")#why is variable get change when you write a string in function dead
    print("situation = dead")
    exit(0)#exit mean finish the program and stop

def mary():#the right way to finish the adventure by giving the ring or dying by bank owner
    
    if ring == True:#is like every if statement exercice but is divise for 2 if the first if statement you continu else you return to start 
        print("After I presented to your fiance, the ring, she knew how much you loved her and accepted the marriage,Good end")
    else:
        print("Although you persuaded your fiancée to marry, she refused, saying: Your love for me is not clear and doubtful")
        input()
        town()
    if debt > 0:
        input()
        dead("The last thing you see is the face of your dead wife after she was just at the maxium of her happiness, you know a reason because you broke the promise with the bank owners...")
    else:
        input()
        print("The end,and happy life togheter")
        exit(0)

def town():# the start who can choose the place to go
    global money
    global debt#make the variable global
    print('player , you are in the Town named Feshinton .')
    print("This town is the best choice for buying things but the merchandises is expensive for this reason you should working hard.")
    print("Indeed you subject is marrying for this reason you should a ring and be in good health. ")

    print("--------------------------------------------------------------------------------------------------------------------------")
    print(f"money is ---> {money} , you debt is --->{debt},you have sword {sword},you have ring {ring}")
    print("------------------------------------------------------------------------------------------------------------------------- ")
    print('There are many places for you to choose and')
    print('you can go to the specified location by just writing the letter') 
    print("assigned to the site from this list")

    print("School --->  'a'\nLibrary ---> 'b'\nMerchant ---> 'c'\nBank ---> 'd'\nGo to your fiancée ---> 'e'")
    
    while True :#you can teleport to differnt place by diferent function
        choi = input("now choose:")
        if choi == 'a':
            school()
        elif choi == 'b':
            library()
        elif choi == 'c':
            merchant()
        elif choi == 'd':
            bank()
        elif choi =='m':
            monster()
        elif choi == 'e':
            mary()
        
        else:
            print("You want mary but don't know how write letter that this replusive. ")
        
town()

