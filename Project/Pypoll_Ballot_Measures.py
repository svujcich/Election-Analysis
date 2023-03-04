#add dependencies
import csv
import os

# add a variable to load a file from path
file_to_load = os.path.join('Project', 'Resources', 'votes_with_ballot_measures.csv')
#print (File_to_load)
file_to_save = os.path.join('Project','Results','new_election_results.txt' )

#Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_names = []
county_votes = {}

#track the winning candidate vote and percentages
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_turnout = ""
largest_county_votes = 0

# Create a county list and county votes dictionary.
ballot_measure_options = []
ballot_measure_votes = {}

# create varibles specific to the work week
work_week_options = []
work_week_votes = {}

#make a list of column Names
list_column_names = []


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data) #delimiter=','
    print(reader)
        
    # add names of columns to list 
    for row in reader:
        list_column_names.append(row)
        break    
    #extract list in list
    list_column_names = list_column_names[0]
    # print(list_column_names)

    #get key and value of items in list_column_names
    # print(list(enumerate(list_column_names)))
#     # add ballot measure names to list
    for index, col in enumerate(list_column_names):
        if col == "Ballot ID":
           pass
        elif col == "County":
            pass
        elif col == "Candidate":
            pass
        else:
            ballot_measure_options.append({index: col})
    print(ballot_measure_options)
    
    # read headers
    headers = next(reader)

    # For each row in csv file
    for row in reader:

        #Add to the total vote count
        total_votes = total_votes +1

        # Varibles
        #get the candidate name from each row 
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
         
        # CANDIDATE VOTES
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            #Add the candidate name to candidate list
            candidate_options.append (candidate_name)

            #and begin tracking  that candidate voter count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate count
        candidate_votes[candidate_name] +=1

        # COUNTY VOTES
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_names:

            # 4b: Add the existing county to the list of counties.
            county_names.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1
        

        #BALLOT MEASURES        
        # access index numbers of ballot measure columns
        ballot_measure_indexes = [] 
        for i in ballot_measure_options:
            for j in i:
                # print(j)
                ballot_measure_indexes.append(j)
        # print(ballot_measure_indexes)
            
        #Add to the total vote count
            total_votes = total_votes +1
            
            for i in ballot_measure_indexes:
                
                topic = row[i]
                
                topic_votes = []
                
                if topic not in topic_votes:
                    topic_votes.append(topic)
                    topic_votes[topic] = 0
                topic_votes[topic] += 1
                print("MOMENT OF TRUTH!")
                print(i, topic_votes)
                
            
            
                      
    #     work_week = []
    #     print(i)
    # print(work_week)
            
        # # add work week options to list
        # if work_week not in work_week_options:
        #     work_week_options.append(work_week)
        #     # set the number of votes = 0
        #     work_week_votes[work_week] = 0
        # # add a vote for every occurence
        # work_week_votes[work_week] +=1
        # # print(f'WORK WEEK VOTES{work_week_votes}')

    
# #save the results to our text file
# with open(file_to_save,'w') as txt_file:
#     # print the final vote count (to terminal)
#     election_results = (
#         f'\n Election Results\n'
#         f'---------------------\n'
#         f'Total Votes: {total_votes:,}\n'
#         f'---------------------\n\n'
#         f'County Votes:\n'
#     )
#     print(election_results, end = '')
#     txt_file.write(election_results)

#      # 6a: Write a for loop to get the county from the county dictionary.
#     for county in county_votes:

#         # 6b: Retrieve the county vote count.
#         county_vote = county_votes[county]

#         # 6c: Calculate the percentage of votes for the county.
#         county_percent = int(county_vote)/int(total_votes) *100

#          # 6d: Print the county results to the terminal.
#         county_results = (
#             f'{county}: {county_percent:.1F}% ({county_vote:,})\n'
#         )
#         print(county_results, end="")

#          # 6e: Save the county votes to a text file.
#         txt_file.write(county_results)

#          # 6f: Write an if statement to determine the winning county and get its vote count.
#         if (county_vote > largest_county_votes):
#             largest_county_votes = county_vote
#             largest_county_turnout = county

#     # 7: Print the county with the largest turnout to the terminal.
#     largest_county_turnout = (
#         f'\n'
#         f"-------------------------\n"
#         f"Largest County Turnout: {largest_county_turnout}\n"
#         f"-------------------------\n"
#     )
#     print(largest_county_turnout)

#     # 8: Save the county with the largest turnout to a text file.
#     txt_file.write(largest_county_turnout)

#     # Save the final candidate vote count to the text file.
#     for candidate_name in candidate_votes:

#         # Retrieve vote count and percentage
#         votes = candidate_votes.get(candidate_name)
#         vote_percentage = float(votes) / float(total_votes) * 100
#         candidate_results = (
#             f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#         # Print the winning candidate (to terminal)
#         print(candidate_results)

#         #  Save the candidate results to our text file.
#         txt_file.write(candidate_results)

#         # Determine winning vote count, winning percentage, and candidate.
#         if (votes > winning_count) and (vote_percentage > winning_percentage):
#             winning_count = votes
#             winning_candidate = candidate_name
#             winning_percentage = vote_percentage

#     # Print the winning candidate (to terminal)
#     winning_candidate_summary = (
#         f"-------------------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:,}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"-------------------------\n")
#     print(winning_candidate_summary)
#     # Save the winning candidate's name to the text file
#     txt_file.write(winning_candidate_summary)
    
#     # # add workweek to the results 
#     # for selection in work_week_votes:
#     #     work_week_votes = work_week_votes[work_week]
        
#     #     work_week_percent = int(work_week_votes)/int(total_votes) *100
#     #     work_week_results = (
#     #         if s
#     #     f'{selection}: {work_week_percent:.1F}% {work_week_votes:,})\n'
#     #     )
        
#     #     print(f'{}')
#     #     print(work_week_results, end="")
        
#     #      # 6e: Save the county votes to a text file.
#     #     txt_file.write(work_week_results)
# # #   -----------------------------------------         
# def measures(position):
#     # For each row in csv file
#     for row in reader:       
#         # Extract the work_week data from each row.
#         ballot_measure = row[position]
            
#         # add work week options to list
#         if ballot_measure not in ballot_measure_options:
#             ballot_measure_options.append(ballot_measure)
#             # set the number of votes = 0
#             ballot_measure_votes[ballot_measure] = 0
#         # add a vote for every occurence
#         ballot_measure_votes[ballot_measure] +=1
        
#         # print(ballot_topic)
#         print(ballot_measure)     
# measures(3)       
        
             
# # #   ----------------------------------------- 
# #     #create a list of voting options
# #     options = []
# #     option_votes = {}
# #     # option_votes[options] = 0
# #     option_results = ""
# #     winning_option_vote = 0
    
#     # For each row in csv file
#     # for row in reader:
#     #     ballot_measure = row[3]
#     #     print(ballot_measure)
    
#     # for i in file_to_load:
#     #     print(file_to_load[[i]])
   
   
#     #    # Read the csv and convert it into a list of dictionaries
#     # with open(file_to_load) as election_data:
#     #     reader = csv.reader(election_data) #delimiter=','
#     #     print(reader) 
        
#     #     ballot_measure_options = []
#     #     ballot_measure_votes = {}
#     #     list_column_names = []
    
#     #     # add names of columns to list 
#     # for row in reader:
#     #     list_column_names.append(row)
#     #     break
        