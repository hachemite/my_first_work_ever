from math import *
from random import *

a = randint(1,6)
b = randint(1,11)
l = [-1,-3,-2,-5,-6]
c = choice(l)

d= b**2 - 4*a*c

x1 = -b-sqrt(d)/2*a
x2 = -b+sqrt(d)/2*a
x11 = round(x1,2)
x22 = round(x2,2)




print("""(ta ta ta rata tat)\nHelloo heroda I'm the tester I will evaluate you competence.
For this reason you will choose one of this category :
<>>>the hero thing 
>>> math
>>> animals because you are like him""")

if d < 0:
    print("please don't choose math is trap")

cho = input("choose your test\n>>>>")

if cho == "math":
    print("now solve this problem kid! is quadritic equation ! YEAHHH ):(haha)")
    print("that what nead a =",a,"b =",b,"c =",c)
    de = int(input("first what is delta"))
    if de == d :
        print("good job continu")
        x111 = float(input("now you should now the two solution x1"))
        x222 = float(input("now you should now the two solution x2"))
        
        if x111 == x11 and x222 == x22:
            print("good job you are a hero you can rescue the princess")
        elif x111 == x11 or x222 == x22:
            print("you can continu but I'm not sure you can help the pricess")
        else:
            print("haha get out of here loser")
    else :
        print("you just a donkey hahahahahahahaha")
    


        print(d)
elif cho == "hero":

    he = input("what is hero yes or no" )
    if he == "yes":
        print("goo")
    elif he == "no":
        print("return after to be a hero")
    else :
        print("get out of here I don't kiding chut chut")
        

elif cho == "animal":
    son =input("what is sonic")
    if son == "hedgehog":
        print("bravo you can't continue you are a biologist")

    else :
        print("try again after you die")
else :
    print('I hate the person like you')