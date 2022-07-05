#print("Hello World!")

#print("---------------------------") == print('-'*50)
#PRINTING


#print("---------------------------")

#TUPLE == round brackets
counties_tuple = ('Arapahoe','Denver','Jefferson')
#print("County Tuple:")
#print(counties_tuple)
#print("")
#print(counties_tuple[:2])
            #OR
#print(counties_tuple[0:2])


#print('----------------------------')

#LISTS ==square Brackets
counties_list = ['Arapahoe','Denver','Jefferson']

#add to the END of list
#counties_list.append('Longmont')
#print(counties_list)
                #OR
# add to SPECIFIC LOCATION in list
#counties_list.insert(2,'Erie') 
#print(counties_list)

#Replace information
#counties_list[1] = ('Loveland')
#print(counties_list)

#remove from a list
#counties_list.remove('Arapahoe')
#print(counties_list)
                #OR
#POP - remove by index. how does it return value?
#print(counties_list.pop(1))
#print(counties_list)

#range
#Varible refering to index of list; specific to each loop
#common practice uses i
#for county_name in counties_list:
    #print(county_name)
#if the length of the list is unknown
#range of the length because counties list is a string, needs integers
#for i in range(len(counties_list)):
    #print(counties_list[i])

#print('')

#and / or statements
#if 'El Paso' in counties_list or 'Arapahoe' in counties_list:
    #print('El Paso or Arapahoe are in the list of counties.')
#else:
    #print('El Paso and Arapahoe are not in the list of counties.')

# simple commands
#print("County List:")
#print(counties_list)
#print('example ' + 'is successful')

#if counties_list[1] == 'Denver':
    #print(counties_list[1])

#print("---------------------------")

#DICTIONARY == curly brackets
counties_dict = {} #number of voters
counties_dict['Arapahoe'] = 422829
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
counties_dict['Boulder'] = 8675309

#finds how many items are in the list
#print(len(counties_dict))

#prints each dictionary on seperate line
#for county_dict in voting_data:
    #print(county_dict)

#prints the KEY in a dictionary
#for county in counties_dict:
    #print(county)
            #OR
#for county in counties_dict.keys():
    #print(county)
            #OR
#print('')

#prints the VALUE of a dictionary
#keys and values plural
#for voters in counties_dict.values():
    #print(voters)
            #OR
#for county in (counties_dict):
    #print(counties_dict[county])
            #OR
#for county in (counties_dict):
    #print(counties_dict.get(county))

#print the VALUE for just ONE KEY in dictionary
#print(counties_dict['Arapahoe'])
            #OR
#print(counties_dict.get('Boulder'))    

#print('')

#prints KEY-VALUE pairs of a dictionary
#for key,value in counties_dict.items(): #can change "key" and "value" varibles (ex. county, voters)
    #print(key,value)
#for county, voters in counties_dict.items():
    #print(county, ' county has', voters, 'registered_voters')
#print("")
#print(counties_dict.items())



#LISTS OF DICTIONARIES 
voting_data = [{'county':'Arapahoe','registered_voters':422829}, 
                {'county':'Denver', 'registered_voters': 463353}, 
                {'county': 'Jefferson', 'registered_voters': 432438}]

#get a value from the dictionary
#print(voting_data[2]['county'])
                #OR
#print(voting_data[2].get('registered_voters'))

# isolate varibles in lists of dictionaries
    #iterates over list of dictionaries 
    #tells VS code to print one value for each item in the length of the list
    #tells vs code which varible to print the value for.
#for i in range(len(voting_data)):
    #print(voting_data[i]['county'])
                    #OR
#print ALL values for ALL dictionaries in a list of dictionaries
#for county_dict in voting_data: #retrieve each dictionary, defines each dictionary as the varible county_dict
    #for value in county_dict.values():#references each dictionaries and finds all the values
        #print(value)

#REMOVE DICTIONARY from dictionary array
#voting_data.remove({'county':'Arapahoe','registered_voters':422829})
#print(voting_data)
                #OR
#voting_data.pop(1)
#print(voting_data)

#ADD DICTIONARY to dictionary array
#voting_data.insert(2,{'county':'Lyons','registered_voters':522629})
#print(voting_data)
                #OR
#add to dictionary array in SPECIFIC LOCATION
#voting_data.insert(2,{'county':'Lyons','registered_voters':522629})
#print(voting_data)




#DESCISION STATEMENT EXAMPLE
# How many votes did you get?
#my_votes = int(input('How many votes did you get in the election? '))
#  Total votes in the election
#total_votes = int(input('What is the total votes in the election? '))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print('I received ' + str(percentage_votes)+'% of the total votes.')
# int(), float(), str()

# F STRINGS
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#MULTIPLE F STRINGS
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
    #f'You received {candidate_votes:,} number of votes. '
    #f'The total number of votes in the election was {total_votes:,}. '
    #f'You received {candidate_votes / total_votes * 100:.2f}% of the total votes.')
#print(message_to_candidate)
#LIMIT OUTPUT to 2 places AFTER DECIMAL = f'{value:{width}.{precision}}' >> .2F 
#THOUSANDS SEPARATOR = :, inside curly brackets
#for concatenated statements, # print just the key, value pairs. After that works, add an f string 

# more f strings
# print each county and registered voter from the following dictionary
voting_data = [
{"county":"Arapahoe", "registered_voters": 4228293}, 
{"county":"Denver", "registered_voters": 463353}, 
{"county":"Jefferson", "registered_voters": 432438}]
for data in voting_data:
    print(f'{data["county"]} county has {data["registered_voters"]:,} registered voters')



# #DEPENDENCIES
# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)
#datetime classes: date, datetime, time, timedelta, timezone


# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")


print('----------------------------')
#IF STATEMENTS
# subject not in parentheses
# != 'not equal to
counties = ['Arapahoe', 'Denver', 'Jefferson']
#if counties [1] == 'Denver': #because string, in quotes, it is was an int, no quotes
    #print(counties[1])
    

# MEMBERSHIP OPERATORS
#in / not in / and / or / not
counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not the list of counties.")

#not example
#x = 5
#y = 5
#if not(x>y):
    #print('True')
#else:
    #print('False')

#CONJUNCT STATEMENTS
#if "Arapahoe" in counties or "El Paso" in counties:
    #print("Arapahoe or El Paso is in the list of counties.")
#else:
    #print("Arapahoe and El Paso are not in the list of counties.")


#temperature = int(input('What is the temperature outside?'))

# basic if_else statement
#if temperature > 80:
    # print('Turn on the AC.')
#else:
    # print('Open the windows.')



#BASIC LOOPS
# nested if statement
# what is the score??
#score = int(input('What is your test score?'))

#determine the grade
# if score >= 90:
#     print('Good job, you got an A, nerd.')
# else:
#     if score >= 80:
#         print('You got a B. not too shaby!')
#     else:
#         if score >= 70:
#             print('You got a C. You didnt completely fail.')
#         else:
#             if score >= 60:
#                 print('You got a D. Maybe next time stop smoking so much pot and do your homework.')
#             else: 
#                 if score < 60:
#                     print('You failed, Try harder next time')

# # use elif to determine test grade
# score_2 = int(input('What was your test score on the history exam?'))

# if score_2 >= 90:
#     print('You got an A! George Washington yould be proud. keep it up!')
# elif score_2 >= 80:
#     print('You got a B, looks like you learned something!')
# elif score_2 >= 70:
#     print('You got a C. Now did you actually study or did you just get lucky?')
# elif score_2 >= 60:
#     print('you got a D. An unimpressive effort.')
# elif score_2 < 60:
#     print('You failed!')

#WHILE LOOPS = danger zone. condition controlled loops
# x = 0
# while x <=5:
#     print(x)
#     x = x + 1 