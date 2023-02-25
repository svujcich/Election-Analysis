# Add dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv") #path has to start at the highest level folder
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources/Practice", "election_analysis.txt")

#initialize votes to 0
total_votes = 0

#initialize candidate options and candidate votes
candidate_options = []
candidate_votes = {}

#Track winning candidate, vote count, and percentage
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:  
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # add to the total vote count
        total_votes += 1

        #get candidates name from each row
        candidate_name = row[2]

        #if candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            #add to candidate_name list
            candidate_options.append(candidate_name)
            #and begin tracking that candidate list
            candidate_votes[candidate_name] = 0
        #add a vote to candidate's count
        candidate_votes[candidate_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #after opening the file, print the final vote count to the terminal
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # after printing the final vote count to the terminal, 
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # 4. Print each candidate's name and percentage of votes to the terminal.
        print(candidate_results)

        #save the candidate results to the text file (ln 47)
        txt_file.write(candidate_results)
        #determine winning vote count,winning percentage, and candidate
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
    #print winning candidate summary results to terminal
    winning_candidate_summary = (
        f'-------------------------------\n'
        f'Winner:{winning_candidate}\n'
        f'Winning Vote Count:{winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------------\n')

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)








#pint(total_votes)
#print(candidate_options)
#print(candidate_votes)



    #Print the file object.
    #Print(election_data)

# Using the open() function with the "w" mode we will write data to the file.
   #txt_file = open(file_to_save, "w")
# Write and read some data to the file.
    #txt_file.write('Counties in the Election')
    #txt_file.write('\n--------------------------------')
    #txt_file.write('\nArapahoe\nDenver\nJefferson')
    
# Close the file
#txt_file.close()


