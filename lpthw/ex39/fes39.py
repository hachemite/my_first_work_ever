# create a mapping of state to abbrevation
regions = {
    'Tanger-Tétouan-Al houcéima' : 'TTH',
    'Oriental' : 'OR',
    'Fés-Méknes': 'FM',
    'Casablanca-Settat' : 'CS',
    'Rabat-Salé-Kénitra' : 'RSK'
}

#create a basic  set of regions and some chefs in them
chefs =  {
    'TTH': 'Tanger-Assilah',
    'OR': 'Wejda-Angad',
    'FM': 'Fés'
}

#add some more chefs
chefs['CS'] = 'Casablanca'
chefs['RSK'] = 'Rabat'

#print out some chefs
print('.'*10)
print('CS region has', chefs['CS'])
print('TTH region has',chefs['TTH'])

#print some regions
print('.'*10)
print("Rabat-Salé-Kénitra's abbrevation is ",regions['Rabat-Salé-Kénitra'])
print("Oriental's abbrevation is ",regions['Oriental'])

#do it by using the state then chefs dict
print('.'*10)
print('Rabat-Salé-Kénitra has ',chefs[regions['Rabat-Salé-Kénitra']])
print("Oriental has ",chefs[regions['Oriental']])

#print every state abbrevation  
print("."*10)
for region,abbrev in list(regions.items()):
    print(f"{region} is abbreviated {abbrev}")
    
#print every city in state
print('-'*10)
for abbrev, chef in list(chefs.items()):
    print(f"{abbrev} has the chef {chef}")
    
#now do both at the same time 
print("-"*10)
for region,abbrev in list(regions.items()):
    print(f"{region} state is abbreviated {abbrev}")
    print(f"and has city {chefs[abbrev]}")

print("-"*10)
#safely get abbreviation by state that might not be there
state =  regions.get('Marrakech-Safi')

if not state:
    print("Sorry, no Marrakech-Safi")
    
#get a city with default value
chef =  chefs.get('MS',"Does Not Exist")
print(f"The city for the 'MS' is : {chef}")