#add dependencies
import csv
import os

# add a variable to load a file from path
file_to_load = os.path.join('Project', 'v2', 'Resources','votes_with_ballot_measures.csv')
#print (File_to_load)
file_to_save = os.path.join('Project', 'v2', 'Results','new_election_results.txt' )

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

#track options for 4 day work week 
work_week_options = []
work_week_votes = {}

winning_ww_decision = ""
winning_ww_count = 0
ww_decision = ""
ww_in_favor_percent = 0
ww_against_percent = 0

#track options for HOA Ballot Measure
hoa_options = []
hoa_votes = {}

winning_hoa_decision = ""
winning_hoa_count = 0
hoa_decision = ""
hoa_in_favor_percent = 0
hoa_against_percent = 0


#make a list of column Names
list_column_names = []


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data) #delimiter=','
                         
    # read headers
    headers = next(reader)

    # For each row in csv file
    for row in reader:

        #Add to the total vote count
        total_votes = total_votes +1

        # VARIBLES
        #get the candidate name from each row 
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
        
        work_week = row[3]

        hoa = row[4]
      
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
        
        #WORK WEEK
        if work_week not in work_week_options:
            
            work_week_options.append(work_week)
            
            work_week_votes[work_week] = 0
            
        work_week_votes[work_week] +=1
               
        #HOA
        if hoa not in hoa_options:
            
            hoa_options.append(hoa)
            
            hoa_votes[hoa] = 0
            
        hoa_votes[hoa] +=1
    # print(hoa_votes)

               
#SAVE RESULTS TO TEXT FILE
with open(file_to_save,'w') as txt_file:
    # print the final vote count (to terminal)
    election_results = (
        f'\n ELECTION RESULTS\n'
        f'---------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'---------------------\n\n'
        f'County Votes:\n'
    )
    print(election_results, end = '')
    txt_file.write(election_results)

     # COUNTY RESULTS TO TEXT FILE
     # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:

        # 6b: Retrieve the county vote count.
        county_vote = county_votes[county]

        # 6c: Calculate the percentage of votes for the county.
        county_percent = int(county_vote)/int(total_votes) *100

         # 6d: Print the county results to the terminal.
        county_results = (
            f'{county}: {county_percent:.1F}% ({county_vote:,})\n'
        )
        print(county_results, end="")

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f'\n'
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n"
    )
    print(largest_county_turnout)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_turnout)

    # CANDIDATE TO TEXT FILE
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print the winning candidate (to terminal)
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    
    # WORK WEEK TO TEXT FILE
    #calculate winning decision for four day work week
    for work_week in work_week_votes:

        votes = work_week_votes.get(work_week)
        
        # calculate percentage of votes for passing and blocking 
        if work_week == "True":
            ww_in_favor_percent = (votes/total_votes) * 100
        if work_week == "False":
            ww_against_percent = (votes/total_votes) * 100
        else:
            pass
        
        # calculate winning decision
        if(votes > winning_ww_count):
            winning_ww_count = votes
            winning_ww_decision = work_week
        else:
            pass
        
    # print(winning_ww_count)
    # print(winning_ww_decision)
    # print(ww_in_favor_percent)
    # print(ww_against_percent)
    
    # Translate True/ False into Passes/ Does not Pass
    if winning_ww_decision =="True":
        ww_decision = 'PASSES'
    else:
        ww_decision = 'DOES NOT PASS'
        # print(ww_decision)
        # Print the winning candidate (to terminal)
        
    work_week_summary = (
        
        f"BALLOT MEASURES:\n"
        f"\n"
        f"Four Day Work Week\n"
        f"Decision: {ww_decision}\n"
        f"In Favor: {ww_in_favor_percent:.2f}%\n"
        f"Against {ww_against_percent:.2f}%\n"
        f"\n")
    print(work_week_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(work_week_summary)
        
    # ADD HOA TO TEXT FILE
    #calculate winning decision for four day work week
    for hoa in hoa_votes:

        votes = hoa_votes.get(hoa)
        
        # calculate percentage of votes for passing and blocking 
        if hoa == "True":
            hoa_in_favor_percent = (votes/total_votes) * 100
        if hoa == "False":
            hoa_against_percent = (votes/total_votes) * 100
        else:
            pass
        
        # calculate winning decision
        if(votes > winning_hoa_count):
            winning_hoa_count = votes
            winning_hoa_decision = hoa
        else:
            pass
    
    # Translate True/ False into Passes/ Does not Pass
    if winning_hoa_decision =="True":
        hoa_decision = 'PASSES'
    else:
        hoa_decision = 'DOES NOT PASS'
        # print(ww_decision)
        # Print the winning candidate (to terminal)
        
    hoa_summary = (
        f"Add Home Owner's Association\n"
        f"Decision: {hoa_decision}\n"
        f"In Favor: {hoa_in_favor_percent:.2f}%\n"
        f"Against {hoa_against_percent:.2f}%\n"
        f"-------------------------\n")
    print(hoa_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(hoa_summary) 