# Add dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)   

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

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


