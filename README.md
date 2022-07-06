# Election-Analysis
## Project Overview
The objective of this project was to complete an audit of election results for a local congressional election in the state of Colorado by completeing the following tasks:
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
  *	Raymon Anthony Doane
-	The candidate results were 
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    -	Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
-	The winner of the election was
    * Diana DeGette, who received 73.8% of the vote and 272,892 votes.
## Challenge Overview
As an extension of the election audit, statistical information about county turnout was requested. The following tasks were assigned: 
1.	Calculate the number of number of voters who participated in the election
2.	Calculate the percentage of votes from each county out of the total count
3.	Identify the county with the highest turnout

## Challenge Summary
The analysis shows that: 
-	The number for votes cast in each county were:
    *	38,855 votes in Jefferson county
    *	306,055 votes in Denver county
    *	24,801 votes in Arapahoe county
-	The percentage of votes out of the total vote count was
    *	10.5% in Jefferson County
    *	82.8% in Denver County
    *	6.7% in Arapahoe county
-	The county with the highest turnout was
    *	Denver with 306,055 votes and 82.8% of the total votes cast
    
The presentedscript provides versatility for future local congressional elections because it has the ability to adapt to a different set of candidates and counties. Rather than hard coding candidate and county names as variables, the script utilizes dynamic lists. The program starts with an empty list for candidates and an empty list for counties. As the program loops through each row of the election data, it checks to see if the candidate name is in the candidate list. If the candidate is not in the list, it adds them to the list. The program then follows the same process for the counties list. This means that any election data formatted with the headers in the same position as those in the provided data (election_data.csv) can be analyzed even if the candidates and counties differ. 

The script could be modified to collect a variety of different information; one example woule be age demographic information. Using a birth date, the program could separate voters into age groups, and output the percentage of voters in each age group that submitted ballots. This information would be useful in allocating resources for outreach to improve voting rates. For example, if younger voters 18 – 25 are significantly less involved than other age groups, voter registration could focus some effort at college campuses, or even sending some high energy advocates to high schools to get high school seniors excited about an upcoming election.  
	
It is possible to use take the election script a step further and modify it to calculate votes for individual topics by adding sections of similar code to the existing structure. Say, for example, a ballot measure in an election is increasing taxes to improve transportation infrastructure by adding more bus lanes. 
 
1. First, a new column would be added to the election results. 
2. The programmer would then initialize the variables including:
   * A list of voting options (bus_lane_options) Since the list is a Boolean, the voting choices will either be true, for people who want new bus lanes, or false for people do not want the bus lanes. 
   * A bus lane dictionary (bus_lane_votes) would also be created to store the votes for each option. 
   * The programmer would then set the value of each option to  in the dictionary to 0 so the code has a numeric value to add to(Bus_lane_votes[bus_lane_options] = 0). 
   * declare a variable to hold the name of the winning result (bus_lane_result =’’) and 
   * set the winning count of votes to 0 (largest_bus_lane_vote  = 0). 

3.The program would then use the existing structure loop through each row of data. 
- If the value is true, 
  * it would add one vote to the dictionary for true (bus_lane_votes[‘True’] +=1) 
  * If the result is not true, it would move on to the next condition. 
- If the result was false
  * it would  add one vote to the “false” results for the (bus_lane_votes[‘False’] +=1), 
4. The program would continue to loop through every row of data

5. Another loop would be utilized to extract the values from the dictionary and determine the winning selection using the following code:
```
For lane_vote in bus_lane_votes 
    If (bus_lane_votes > lrgest_bus_lane_vote): 
    bus_lane_results = lane_vote
```
- This tells the program:
  * initialize a variable to refer to each key in the bus_lane_votes dictionary
  * if the number of votes for the key is the highest value in the dictionary
  * the winning result is the key with the most votes

6. The result would be written into the script, and an f string including plain text concatenated with computer calculated values from the winning varible would be included. This statement would be followed by print(bus_lane_results) to send the results to the terminal, or txt_file.write (bus_lane_results) to send the results to the text file the candidate and county results are being sent to. 

Whatever the ballot measure is, whether it is building a new Publie Library, or creating rules for environmental protection, the previously described process can be adapted to calculate the voting outcome of any proposed idea in any election. 


