# Election-Analysis
## Project Overview
This project focuses on an audit of election results for a local congressional district in the state of Colorado. The following tasks were assigned:
1.	Calculate the total number of votes cast
2.	Get a complete list of candidates who received votes
3.	Calculate the total number of votes each candidate received
4.	Calculate the percentage of votes each candidate won
5.	Determine the winner of the election based on popular vote.
## Resources
-	Data source: election_results.csv
-	Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
- The candidate results were 
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    -	Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was
    * Diana DeGette, who received 73.8% of the vote and 272,892 votes.
    
## Challenge Overview
As an extension of the election audit, statistical information about county turnout was requested. The following tasks were also assigned:
1.	Calculate the number of number of voters who participated in the election
2.	Calculate the percentage of votes from each county out of the total count
3.	Identify the county with the highest turnout

## Challenge Summary
The analysis shows that: 
-	The number of votes cast in each county were:
    *	38,855 votes in Jefferson county
    *	306,055 votes in Denver county
    *	24,801 votes in Arapahoe county
-	The percentage of votes out of the total vote count was
    *	10.5% in Jefferson County
    *	82.8% in Denver County
    *	6.7% in Arapahoe county
-	The county with the highest turnout was
    *	Denver with 306,055 votes and 82.8% of the total votes cast
    
    
    ![election_results_summary](https://user-images.githubusercontent.com/106559768/177671529-6ff24c54-c9c7-4925-9b36-13ebdb964071.jpg)

### Applications
This script provides versatility for future local congressional elections because it has the ability to adapt to a different set of candidates and counties. Rather than hard coding candidate and county names as variables, the script utilizes dynamic lists. The program starts with an empty list for candidates and an empty list for counties. As the program loops through each row of the election data, it checks to see if the candidate name is in the candidate list. If the candidate is not in the list, it adds them to the list. The program then follows the same process for the counties list. This means that any election data formatted with the headers in the same position as those in the provided data (election_data.csv) can be analyzed even if the candidates and counties differ. 

If modified, this script could collect other insightful information; one example would be age demographic information. Using a birth date, the script could be programmed to separate voters into age groups, and output the percentage of voters that submitted ballots. This information would be useful in allocating resources for outreach to improve voting rates. For example, if younger voters 18 – 25 are significantly less involved than other age groups, voter registration campaigns could focus more effort at college campuses, or send some high energy advocates to high schools to get younger participants excited about an upcoming election.  
	
By adding relevant data to the election_results.csv and adding sections of similar code to the existing structure, it is possible to use take the election script a step further and modify it to calculate votes for ion the pyPoll challenge code, the following steps would be followed:
  
  1. Add a new column to the election-results.csv that holds the results for the the ballot measure
  2. Initialize variables 
	  * Create A list of voting options (bus_lane_options[]) 
	   * Create A bus lane dictionary (bus_lane_votes{}) to store the votes for each option (True or False). 
	   * Set the value of each option to  in the dictionary to 0 (bus_lane_votes[bus_lane_options] = 0) so the code has a numeric value to add to
	   * Declare a variable to hold the name of the winning result (bus_lane_result =’’) 
	   * Set the **winning count** of votes to 0 (largest_bus_lane_vote  = 0). 

3. Use the existing structure to loop through each row of data. 
	- If the value is true: 
	  * Add one vote to the dictionary for true (bus_lane_votes[‘True’] +=1) 
	  * If the result is not true, it would move on to the next condition. 
	- If the result is false:
	  * Add one vote to the dictionary for false (bus_lane_votes[‘False’] +=1), 
4. Create aother loop to extract the values from the dictionary and determine the winning selection using the following code:

```
for lane_vote in bus_lane_votes 
    if (bus_lane_votes > largest_bus_lane_vote): 
    bus_lane_result = lane_vote 
```
 - to tell the program:
	 * initialize a variable to refer to each key in the bus_lane_votes dictionary
	 * if the number of votes for the key is the highest value in the dictionary
	 * the winning result is the key with the most votes

5. Format and transcribe the results. Use an f string including plain text concatenated with computer calculated values to provide instructions on what to print. Then use the statement, print(bus_lane_result) to send the results to the terminal, and/or txt_file.write(bus_lane_result) to send the results to the text file the candidate and county results are being sent to. 

Whatever the ballot measure is, whether it is building a new Publie Library, or creating rules for environmental protection, the previously described process can be adapted to calculate the voting outcome of the any proposal.

