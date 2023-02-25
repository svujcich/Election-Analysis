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
	
It is also be possible to create a function to process any boolean value for any ballot measure (measure passes or measure does not pass). This would be achieved by adding a new column with ballot measure results to the csv file, and creating a function with the argument (position) to the script. You could effectively tell the function to identify the voting topic using position argument to return the text in that position in the header row. The function would create a dictionary for the votes, then loop through the data, look at a specific position in each row of data, and target the values in that position. It would track the number of true and false values (for and against votes), using an if statement; if the value is true, add one vote for the measure to pass, and if false, add one vote for blocking the measure. Once the votes have been tallied, the function would use an if statement with a locigal opperator to say if the votes for the ballot measure are greater than the votes against the ballot measure, the measure passes, and if the votes against the measure have more votes, the measure is blocked. Finally, the function would print the winning result to the text file with the other results. 

Adding a function to calculate the results for a boolean ballot measure would enchance this script with a flexible piece of framework tht could be reused for any number of ballot measures, election after election. Whether it is funding a Public Library or proposing measures for environmental protection, calculating the winning decision is as easy as simply calling the function and providing an argument! 
