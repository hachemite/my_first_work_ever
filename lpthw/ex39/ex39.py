# create a mapping of state to abbrevation
states = {                                                              #|'Oregon' : 'OR' :   'Portland'      |#                     
    'Oregon' : 'OR',                                                    #|                                    |#
    'Florida' : 'FL',                                                   #|'Florida' : 'FL' :  'Jackonsville'  |#                         
    'California': 'CA',                                                 #|                                    |#
    'New York' : 'NY',                                                  #|'California': 'CA' :'San Francisco' |#                      
    'Michigan' : 'MI'                                                   #|                                    |#
}                                                                       #|'New York' : 'NY'  :'New York'      |#              
                                                                        #|                                    |#
#create a basic  set of states and some cities in them                  #|'Michigan' : 'MI'   :'Detroit'      |#                    
cities =  {                                                                                                   
    'CA': 'San Francisco',                                                                             
    'MI': 'Detroit',                                                                                   
    'FL': 'Jackonsville'                                                                               
}                                                                                                      

#add some more cities
cities['NY'] = 'New York'# like append we make a new thing by write the name of dict and in [] we write the key
cities['OR'] = 'Portland'#and after = we write the vale of key
#print out some cities
print('.'*10)
print('NY State has', cities['NY'])# will print  the value of dict cities with [key]
print('OR State has',cities['OR'])

#print some states
print('.'*10)
print("Michigan's abbrevation is ",states['Michigan'])# will print  the value of dict states with [key]
print("Florida's abbrevation is ",states['Florida'])

#do it by using the state then cities dict
print('.'*10)
print('Mighigan has ',cities[states['Michigan']])#will the value of dict states with [key]
print("Florida has ",cities[states['Florida']]) #and after will be abbrevation to use the new key 
                                                #with dict cities to print the value of dict cities with [key]
                                                
                                                
#print every state abbrevation  
print("."*10)
for state,abbrev in list(states.items()):#if we use just states will print just the keys 
                                         #but when use the (items) function it make dict
                                         #like this (key,value) and the list make a 
                                         #list\\\\and we add two variable because the tuple has two value
                                         
    print(f"{state} is abbreviated {abbrev}")#state is the key of the first thing in tuple
                                             #abbrev is the value of the second thing in tuple
    
#print every city in state
print('-'*10)
for abbrev, city in list(cities.items()):#if we use just states will print just the keys 
                                         #but when use the (items) function it make dict
                                         #like this (key,value) and the list make a 
                                         #list\\\\and we add two variable because the tuple has two value
                                         
    print(f"{abbrev} has the city {city}")#state is the key of the first thing in tuple
                                             #abbrev is the value of the second thing in tuple
    
#now do both at the same time 
print("-"*10)
for state,abbrev in list(states.items()): # the same thing with two previous for statement
    print(f"{state} state is abbreviated {abbrev}")#state is the key of the first thing in tuple
                                                    #abbrev is the value of the second thing in tuple
                                             
    print(f"and has city {cities[abbrev]}")#but we use the 'abbrev' like key to use 
                                            #in dict cities to make them value of cities
    

print("-"*10)
#safely get abbreviation by state that might not be there
state =  states.get('Texas')#by get the new variable state get the value of 'states' dict found in argument is 'Texas'
                             #but in dict states we don't have the key 'Texas' 
                             #what make state eqaule nothing or state == None

if not state:#(not state)  it mean it is the 'state' == None or False 
    print("Sorry, no Texas")
    
#get a city with default value
city =  cities.get('TX',"Does Not Exist")#like previous get function but we add another argument 
                                         #mean if  doesn't found the key 'TX' ,will run the second argument
                                         #will get the second string
                                         
print(f"The city for the 'TX' is : {city}")#city ="Does Not Exist" because we don't have the key "TX"